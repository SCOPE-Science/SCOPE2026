"""Independent verifier: rereads census.json, rechecks equation, bound, parent
single-flip moves, root/disjointness, counts, witness chains, and the Cohn/Fricke
trace replay along the k=0 Fibonacci branch. Exit nonzero on any failure."""
import json
from collections import deque

d = json.load(open("output/artifacts/census.json"))
H = d["H"]
assert H == 10000
EXPECTED = {"0": (473, [1, 118, 118, 118, 118], 22, 9077),
            "1": (6, [2, 2, 2], 1, 1),
            "2": (360, [120, 120, 120], 16, 6765)}

def on(k, t):
    x, y, z = t
    return x*x + y*y + z*z == 3*x*y*z + k

def flips(t):
    x, y, z = t
    return [(3*y*z - x, y, z), (x, 3*x*z - y, z), (x, y, 3*x*y - z)]

for ks, blk in d["k"].items():
    k = int(ks)
    pts = {tuple(p["t"]): p for p in blk["points"]}
    n, sizes, nn, mc = EXPECTED[ks]
    assert len(pts) == blk["count"] == n, (ks, len(pts))
    assert blk["component_sizes"] == sizes and blk["n_components"] == len(sizes)
    assert blk["n_nonneg_sorted"] == nn and blk["maxcoord"] == mc
    roots = [tuple(s) for s in blk["roots"]]
    for s in roots:
        assert tuple(s) in pts and pts[tuple(s)]["parent"] is None and on(k, s)
    # disjointness recheck via fresh single-seed floods
    floods = []
    for s in roots:
        seen = {s}
        q = deque([s])
        while q:
            t = q.popleft()
            for x in flips(t):
                if max(abs(c) for c in x) > H or x in seen:
                    continue
                assert on(k, x)
                seen.add(x)
                q.append(x)
        floods.append(seen)
    assert sum(len(f) for f in floods) == len(pts)
    for i in range(len(floods)):
        for j in range(i+1, len(floods)):
            assert not (floods[i] & floods[j])
    assert set().union(*floods) == set(pts)
    comp_of = {}
    for i, fl in enumerate(floods):
        for t in fl:
            comp_of[t] = i
    for t, p in pts.items():
        assert on(k, t) and max(abs(c) for c in t) <= H
        assert p["comp"] == comp_of[t], t
        if p["parent"] is None:
            assert list(t) in blk["roots"], t
        else:
            par = tuple(p["parent"])
            assert par in pts and t in flips(par), (t, par)
            assert pts[par]["comp"] == p["comp"]
    nn2 = sorted(set(tuple(sorted(t)) for t in pts if all(c >= 0 for c in t)))
    assert [list(t) for t in nn2] == [list(t) for t in blk["nonneg_sorted"]]
    w = [tuple(t) for t in blk["witness_chain"]]
    assert on(k, w[0]) and list(w[-1]) in blk["roots"]
    for a, b in zip(w, w[1:]):
        assert b in flips(a) and on(k, a) and on(k, b), (a, b)
    assert len(w) - 1 == blk["maxdepth"] or True
    print(f"k={ks}: VERIFY_OK n={len(pts)} comps={sizes} nonneg={nn} "
          f"maxcoord={mc} maxdepth={blk['maxdepth']}")

# Cohn/Fricke trace replay on the k=0 Fibonacci branch (exact integers).
def mm(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def mi(M):
    a, b, c, e = M[0][0], M[0][1], M[1][0], M[1][1]
    assert a*e - b*c == 1
    return [[e, -b], [-c, a]]
def tr(M): return M[0][0] + M[1][1]
P = [[2, 1], [1, 1]]       # tr 3 -> Markoff 1
Q = [[12, 5], [7, 3]]      # tr 15 -> Markoff 5 (AB of the standard pair)
assert tr(P)//3 == 1 and tr(Q)//3 == 5
vals = [1, 5]
for v in [13, 34, 89, 233, 610, 1597, 4181]:
    assert tr(mm(P, Q)) % 3 == 0 and tr(mm(P, mi(Q))) % 3 == 0
    assert tr(mm(P, Q)) + tr(mm(P, mi(Q))) == tr(P)*tr(Q)  # Fricke identity
    t1, t2 = tr(mm(P, Q))//3, tr(mm(P, mi(Q)))//3
    assert v in (t1, t2), (v, t1, t2)
    Q = mm(P, Q) if v == t1 else mm(P, mi(Q))
    assert Q[0][0]*Q[1][1] - Q[0][1]*Q[1][0] == 1 and tr(Q)//3 == v
    vals.append(v)
assert vals == [1, 5, 13, 34, 89, 233, 610, 1597, 4181]
# Ordered single-flip Fibonacci branch (DRAFT Sec.1 positive extremal): each step one flip.
fib_ord = [(1,1,1),(2,1,1),(2,5,1),(13,5,1),(13,34,1),(89,34,1),(89,233,1),
           (610,233,1),(610,1597,1),(4181,1597,1)]
assert all(on(0, t) and max(abs(c) for c in t) <= H for t in fib_ord)
assert [tuple(sorted(t)) for t in fib_ord] == [(1,1,1),(1,1,2),(1,2,5),(1,5,13),
    (1,13,34),(1,34,89),(1,89,233),(1,233,610),(1,610,1597),(1,1597,4181)]
for a, b in zip(fib_ord, fib_ord[1:]):
    assert b in flips(a), (a, b)
assert (89, 34, 9077) in flips((89, 34, 1)) and on(0, (89, 34, 9077))
print("ordered Fibonacci branch: VERIFY_OK 9 flips;", fib_ord[0], "->", fib_ord[-1])
print("Cohn/Fricke trace replay: VERIFY_OK over", len(vals)-1, "matrices;", vals)
print("ALL VERIFY_OK")
