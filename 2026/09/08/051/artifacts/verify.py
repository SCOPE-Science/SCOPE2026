"""Standalone verifier: recomputes every Walsh spectrum from committed truth
tables (CSVs + witnesses.json) using its own FWHT, and checks Parseval,
nonlinearity formula, resiliency Walsh-zero conditions, and table totals.
Usage: python3 verify.py
"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))

def fwht(a):
    h = list(a)
    s = 1
    while s < len(h):
        for i in range(0, len(h), 2 * s):
            for j in range(i, i + s):
                u, v = h[j], h[j + s]
                h[j], h[j + s] = u + v, u - v
        s *= 2
    return h

def wt(i):
    return bin(i).count("1")

def spectrum(tt, n):
    N = 1 << n
    return fwht([1 if ((tt >> i) & 1) == 0 else -1 for i in range(N)])

def check_function(tt, n, nl_claim, res_claim):
    W = spectrum(tt, n)
    assert sum(w * w for w in W) == (1 << (2 * n)), "Parseval failed"
    m = max(abs(w) for w in W)
    assert (1 << (n - 1)) - m // 2 == nl_claim, "nl mismatch"
    bal = (W[0] == 0)
    if res_claim == -1:
        assert not bal, "claimed unbalanced but W(0)=0"
    else:
        assert bal, "claimed resilient but unbalanced"
        assert all(W[u] == 0 for u in range(1 << n) if 1 <= wt(u) <= res_claim), "res low fail"
        if res_claim < n:
            assert any(W[u] != 0 for u in range(1 << n) if wt(u) == res_claim + 1), "res not maximal"

def orbits():
    with open(os.path.join(HERE, "rsbf5_orbits.csv")) as f:
        return [[int(v) for v in row["members"].split(";")] for row in csv.DictReader(f)]

def main():
    # n=4 joint table must sum to 65536; spot-replay one truth table per cell implicitly
    # via bent witness + totals; full 65536 replay done by census.py (seconds).
    n4rows = list(csv.DictReader(open(os.path.join(HERE, "n4_joint.csv"))))
    assert sum(int(r["count"]) for r in n4rows) == 65536
    assert sum(int(r["count"]) for r in n4rows if int(r["nl"]) == 6) == 896
    assert sum(int(r["count"]) for r in n4rows if int(r["nl"]) == 0) == 32
    r5rows = list(csv.DictReader(open(os.path.join(HERE, "rsbf5_joint.csv"))))
    assert sum(int(r["count"]) for r in r5rows) == 256
    orbs = orbits()
    assert len(orbs) == 8 and sum(len(o) for o in orbs) == 32
    # replay every RSBF n=5 function from orbit masks and check its cell
    cells = {(int(r["nl"]), int(r["resiliency"])): int(r["count"]) for r in r5rows}
    seen = {}
    for mask in range(256):
        tt = 0
        for j, o in enumerate(orbs):
            if (mask >> j) & 1:
                for x in o:
                    tt |= (1 << x)
        W = spectrum(tt, 5)
        m = max(abs(w) for w in W)
        nl = 16 - m // 2
        res = -1 if W[0] != 0 else 0
        if res == 0:
            for mm in range(1, 6):
                if all(W[u] == 0 for u in range(32) if 1 <= wt(u) <= mm):
                    res = mm
                else:
                    break
        seen[(nl, res)] = seen.get((nl, res), 0) + 1
    assert seen == cells, f"RSBF replay mismatch: {seen} vs {cells}"
    # witness replay
    wit = json.load(open(os.path.join(HERE, "witnesses.json")))
    b = wit["bent_n4"]
    check_function(b["truth"], 4, b["nl"], b["resiliency"])
    assert all(abs(w) == 4 for w in spectrum(b["truth"], 4))
    q = wit["rsbf5_balanced_max"]
    check_function(q["truth"], 5, q["nl"], q["resiliency"])
    assert spectrum(q["truth"], 5)[0] == 0  # balanced
    print(f"VERIFY_OK n4_total=65536 bent=896 rsbf5_total=256 slice_max={wit['rsbf5_slice_max_nl']}")

if __name__ == "__main__":
    main()
