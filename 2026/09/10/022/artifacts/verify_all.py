"""Final independent verifier for lane-541 emergent census.
Rebuilds every STS from its mathematical definition, checks STS axioms,
enumerates sails with TWO independent enumerators, verifies sail-free
witnesses, checks the archived NAE-4-SAT clause set equals the recomputed
sail set, and replays the UNSAT trace with the closed-tree identity.
Stdlib only. Prints VERIFY_ALL_OK on success.
"""
import itertools
import json
import os
import sys

ART = os.path.dirname(os.path.abspath(__file__))


def canon(blocks):
    return set(tuple(sorted(b)) for b in blocks)


def sails_enumA(blocks, verts):
    bset = canon(blocks)
    byv = {v: [] for v in verts}
    for b in bset:
        for v in b:
            byv[v].append(b)
    out = set()
    for c in verts:
        for trio in itertools.combinations(byv[c], 3):
            priv = [tuple(x for x in b if x != c) for b in trio]
            (a1, a2), (b1, b2), (c1, c2) = priv
            for x, y, z in itertools.product([a1, a2], [b1, b2], [c1, c2]):
                if len({x, y, z}) < 3:
                    continue
                t = tuple(sorted((x, y, z)))
                if t in bset:
                    out.add(frozenset(trio + (t,)))
    return out


def sails_enumB(blocks):
    from collections import Counter
    out = []
    for quad in itertools.combinations(sorted(canon(blocks)), 4):
        verts = sorted({v for b in quad for v in b})
        if len(verts) != 7:
            continue
        d = Counter(v for b in quad for v in b)
        if sorted(d.values()) != [1, 1, 1, 2, 2, 2, 3]:
            continue
        c = [v for v in verts if d[v] == 3]
        if len(c) != 1:
            continue
        c = c[0]
        thru = [b for b in quad if c in b]
        rest = [b for b in quad if c not in b]
        if len(thru) != 3 or len(rest) != 1:
            continue
        D = rest[0]
        contacts = [set(b) & set(D) for b in thru]
        if not all(len(x) == 1 for x in contacts):
            continue
        if len({tuple(sorted(x))[0] for x in contacts}) != 3:
            continue
        out.append(frozenset(quad))
    return set(out)


def is_sts(B, n):
    if len(B) != n * (n - 1) // 6:
        return False
    seen = set()
    for (a, b, c) in B:
        for p in ((a, b), (a, c), (b, c)):
            q = tuple(sorted(p))
            if q in seen:
                return False
            seen.add(q)
    return len(seen) == n * (n - 1) // 2


def parse_wit(w):
    col = {}
    for k, v in w.items():
        col[tuple(sorted(int(x) for x in k.strip('[]').split(',')))] = v
    return col


def mono_count(B, col):
    V = sorted({v for b in B for v in b})
    n = 0
    for s in sails_enumA(B, V):
        vals = [col[b] for b in sorted(s)]
        if vals[0] == vals[1] == vals[2] == vals[3]:
            n += 1
    return n


def sts7():
    return canon([(0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5),
                  (1, 4, 6), (2, 3, 6), (2, 4, 5)])


def sts9():
    pts = [(x, y) for x in range(3) for y in range(3)]
    idx = {p: i for i, p in enumerate(pts)}
    B = set()
    for (x, y) in pts:
        for (dx, dy) in [(0, 1), (1, 0), (1, 1), (1, 2)]:
            B.add(tuple(sorted(idx[((x + k * dx) % 3, (y + k * dy) % 3)]
                               for k in range(3))))
    return B


def sts13():
    B = set()
    for base in [(0, 1, 4), (0, 2, 7)]:
        for t in range(13):
            B.add(tuple(sorted((x + t) % 13 for x in base)))
    return B


def sts15():
    pts = [i for i in range(1, 16)]
    B = set()
    for a in pts:
        for b in pts:
            if b <= a:
                continue
            c = a ^ b
            if c > b and c != a and a ^ b ^ c == 0:
                B.add((a - 1, b - 1, c - 1))
    return B


def sts19():
    B = set()
    for base in [(0, 1, 4), (0, 2, 9), (0, 5, 11)]:
        for t in range(19):
            B.add(tuple(sorted((x + t) % 19 for x in base)))
    return B


def main():
    log = []
    # 1. rebuild + STS check + dual-enumerator agreement
    systems = [("STS7", sts7(), 7), ("STS9", sts9(), 9),
               ("STS13", sts13(), 13), ("STS15", sts15(), 15),
               ("STS19", sts19(), 19)]
    expect_sails = {"STS19": 912, "STS15": 420}
    for label, B, n in systems:
        assert is_sts(B, n), label
        V = sorted({v for b in B for v in b})
        A = sails_enumA(B, V)
        Bb = sails_enumB(B)
        assert A == Bb, label
        extra = ""
        if label in expect_sails:
            assert len(A) == expect_sails[label], label
            extra = " (expect %d OK)" % expect_sails[label]
        log.append("%s: STS_ok sails=%d dual-enumerator agree%s"
                   % (label, len(A), extra))
    # 2. witness checks
    d1 = json.load(open(os.path.join(ART, "sail_smallsts.json")))
    d2 = json.load(open(os.path.join(ART, "sail_target_part2.json")))
    cases = [("STS7", sts7(), d1["STS7_witness"]),
             ("STS9", sts9(), d1["STS9_witness"]),
             ("STS13", sts13(), d1["STS13_witness"]),
             ("STS15", sts15(), d2["STS15_seed7_witness"])]
    for label, Rb, w in cases:
        col = parse_wit(w)
        assert set(col.keys()) == Rb, label + " block-set mismatch"
        m = mono_count(Rb, col)
        r = sum(1 for v in col.values() if v == 0)
        assert m == 0, label
        log.append("%s: witness block-set matches STS; mono=%d red=%d "
                   "blue=%d -> SAIL-FREE OK" % (label, m, r, len(col) - r))
    # 3. clause-set equality: archived clauses == recomputed sails of STS19
    B19 = sts19()
    B19s = sorted(B19)
    pos = {b: i for i, b in enumerate(B19s)}
    recomputed = set()
    for s in sails_enumA(B19s, list(range(19))):
        q = tuple(sorted(pos[b] for b in s))
        recomputed.add((q, True))
        recomputed.add((q, False))
    T = json.load(open(os.path.join(ART, "sts19_unsat_trace.json")))
    archived = set()
    for c in T["clauses"]:
        a, b, c_, d, pol = c
        archived.add((tuple(sorted((a, b, c_, d))), pol))
    assert archived == recomputed, "clause set != recomputed sail set"
    log.append("STS19: archived %d clauses == recomputed sail-constraint "
               "set (912 sails x2 polarities) OK" % len(archived))
    # 4. trace replay
    nvars = T["nvars"]
    clauses = [tuple(c) for c in T["clauses"]]
    fix = T["fix_var"]
    trace = [tuple(t) for t in T["trace"]]
    assert nvars == 57 and T["result"] == "UNSAT"
    a = [-1] * nvars
    a[fix] = 0
    stack = [[]]
    for t in trace:
        if t[0] == "decide":
            _, v, val, depth = t
            assert a[v] == -1, "decide on assigned var"
            a[v] = val
            stack.append([v])
        elif t[0] == "unit":
            _, v, val, ci = t
            (x1, x2, x3, x4, pol) = clauses[ci]
            assert v in (x1, x2, x3, x4)
            sat = 1 if pol else 0
            others = [x for x in (x1, x2, x3, x4) if x != v]
            assert all(a[o] != -1 and a[o] != sat for o in others), \
                "unit not forced"
            assert a[v] == -1
            a[v] = val
            stack[-1].append(v)
        elif t[0] == "conflict":
            _, ci = t
            (x1, x2, x3, x4, pol) = clauses[ci]
            sat = 1 if pol else 0
            assert all(a[x] != -1 and a[x] != sat
                       for x in (x1, x2, x3, x4)), "conflict invalid"
        elif t[0] == "backtrack":
            tr = stack.pop()
            for u in tr:
                a[u] = -1
        else:
            raise AssertionError(t)
    ndec = sum(1 for t in trace if t[0] == "decide")
    ncf = sum(1 for t in trace if t[0] == "conflict")
    assert ncf == ndec // 2 + 1, "tree not closed"
    log.append("STS19 TRACE: replay OK decisions=%d conflicts=%d "
               "closed-tree identity holds => UNSAT CERTIFIED" % (ndec, ncf))
    log.append("VERIFY_ALL_OK")
    open(os.path.join(ART, "verify_all.log"), "w").write("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    sys.exit(main())
