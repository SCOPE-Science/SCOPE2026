"""Murnaghan padded-triple census: cores |.|<=4, n=6..10. Kronecker via class inner product."""
import json, math
from fractions import Fraction
from functools import lru_cache

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None: max_part = n
    for f in range(min(max_part, n), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest

CORES = [p for k in range(0, 5) for p in partitions(k)]
print(f"#cores = {len(CORES)}")

T = {}
with open("chartables.json") as f:
    raw = json.load(f)
for ns, v in raw.items():
    n = int(ns)
    parts = [tuple(p) for p in v["parts"]]
    idx = {p: i for i, p in enumerate(parts)}
    T[n] = {"parts": parts, "idx": idx, "T": v["T"], "z": v["z"]}

def pad(core, n):
    w = sum(core)
    first = n - w
    if core and first < core[0]:
        return None
    return (first,) + tuple(core)

def kron(n, a, b, c):
    d = T[n]; ia, ib, ic = d["idx"][a], d["idx"][b], d["idx"][c]
    s = Fraction(0)
    for j in range(len(d["parts"])):
        s += Fraction(d["T"][ia][j] * d["T"][ib][j] * d["T"][ic][j], d["z"][j])
    assert s.denominator == 1 and s >= 0, (n, a, b, c, s)
    return int(s)

# ---- global verification per n: pointwise character-product identity + dim identity
for n in range(6, 11):
    d = T[n]; P = len(d["parts"])
    dims = {p: d["T"][d["idx"][p]][d["idx"][tuple([1]*n)]] for p in d["parts"]}
    # dim identity for every ordered pair (also exercises all kronecker numbers)
    for a in d["parts"]:
        for b in d["parts"]:
            tot = sum(kron(n, a, b, c) * dims[c] for c in d["parts"])
            assert tot == dims[a] * dims[b], (n, a, b)
    # symmetry spot + full symmetry on subset
    assert kron(n, (n,), (n,), (n,)) == 1
    print(f"n={n}: dim-identity OK over all {P}x{P} pairs; g((n)^3)=1", flush=True)

# ---- padded census
NS = list(range(6, 11))
valid = {n: [c for c in CORES if pad(c, n) is not None] for n in NS}
for n in NS:
    print(f"n={n}: {len(valid[n])} valid cores")

recs = {}   # (a,b,c) -> {traj:{n:g}, ns:[...], stab, gbar, status}
for a in CORES:
    for b in CORES:
        for c in CORES:
            ns = [n for n in NS if pad(a, n) is not None and pad(b, n) is not None and pad(c, n) is not None]
            if not ns:
                continue
            traj = {n: kron(n, pad(a, n), pad(b, n), pad(c, n)) for n in ns}
            g10 = traj[10] if 10 in traj else None
            # stab: first n0 with all subsequent (in-window) equal to g10 value... define via suffix-constancy
            stab, status = None, None
            # find first n0 s.t. traj constant on [n0..max(ns)]
            for n0 in ns:
                vals = [traj[m] for m in ns if m >= n0]
                if len(set(vals)) == 1:
                    stab = n0
                    break
            assert stab is not None
            gbar = traj[ns[-1]]
            if ns[-1] < 10:
                status = "window-truncated"
            elif traj[9] != traj[10] or (len(ns) >= 2 and any(traj[ns[i]] != traj[ns[i+1]] for i in range(len(ns)-1)) and stab == 10):
                status = "increasing-at-10"
            else:
                status = "stabilized-in-window"
            recs[(a, b, c)] = {"ns": ns, "traj": traj, "stab": stab, "gbar": gbar, "status": status}

print(f"#reduced triples with >=1 valid n: {len(recs)}")
full = {k: v for k, v in recs.items() if v["ns"] == NS}
print(f"#triples valid at all n=6..10: {len(full)}")

from collections import Counter
stabhist = Counter(v["stab"] for v in recs.values() if v["status"] == "stabilized-in-window")
print("stab histogram (stabilized):", dict(sorted(stabhist.items())))
ninc = sum(1 for v in recs.values() if v["status"] == "increasing-at-10")
print("increasing-at-10:", ninc)
ntr = sum(1 for v in recs.values() if v["status"] == "window-truncated")
print("window-truncated:", ntr)

# stabilized counts by n: triples with stab<=n
for n in NS:
    cnt = sum(1 for v in recs.values() if v["stab"] <= n)
    print(f"stab<={n}: {cnt}")

# maximal-delay: full-trajectory strictly increasing
strict = {k: v for k, v in full.items() if all(v["traj"][n] < v["traj"][n+1] for n in range(6, 10))}
print(f"strictly increasing full trajectories: {len(strict)}")
for k in sorted(strict, key=lambda k: (strict[k]["traj"][10], k)):
    v = strict[k]
    print([list(x) for x in k], [v["traj"][n] for n in NS])

with open("census_raw.json", "w") as f:
    json.dump({"recs": [{"a": list(k[0]), "b": list(k[1]), "c": list(k[2]), **{kk: (vv if kk != "traj" else {str(n): g for n, g in vv.items()}) for kk, vv in v.items()}} for k, v in recs.items()]}, f)
print("saved census_raw.json")
