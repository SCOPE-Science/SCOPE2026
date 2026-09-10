"""Verify the elementary counting refutation of the [1/30,1/8] triangle-density interval.

Checks (exact integer arithmetic, stdlib only):
1. STS(7) and STS(9): loose-triangle count T == n(n-1)(n-3)/6 exactly,
   and h <= T.
2. Random greedy linear 3-graphs: exact h <= T <= (4/3)*sum_v C(d(v),2),
   edge/degree linear bounds, and t(H) <= U'(n) with
   U'(n) = 120(n-1)/((n-2)(n-3)(n-4)(n-5)).
3. Exact rational checks: U'(n+1)/U'(n) = n(n-5)/(n-1)^2 < 1 (monotone to 0),
   U'(19) = 9/238 > 1/30, U'(n) < 1/30 for all n >= 20 by base + induction
   step (n-1)/(n-5) >= n/(n-1), and U'(n) < 1/8 for all n >= 15.
"""
import itertools
import math
import random
from fractions import Fraction


def count_triangles(edges):
    """Number of unordered edge-triples pairwise meeting in 3 distinct singletons."""
    T = 0
    for a, b, c in itertools.combinations(edges, 3):
        ab, bc, ac = a & b, b & c, a & c
        if len(ab) == 1 and len(bc) == 1 and len(ac) == 1 and len(ab | bc | ac) == 3:
            assert len(a | b | c) == 6
            T += 1
    return T


def triangle_density(edges, n):
    """t(H): fraction of 6-sets whose induced subhypergraph contains a loose triangle."""
    verts = range(n)
    eset = list(edges)
    hit = 0
    total = 0
    for S in itertools.combinations(verts, 6):
        total += 1
        S = set(S)
        sub = [e for e in eset if e <= S]
        found = False
        for a, b, c in itertools.combinations(sub, 3):
            ab, bc, ac = a & b, b & c, a & c
            if len(ab) == 1 and len(bc) == 1 and len(ac) == 1 and len(ab | bc | ac) == 3:
                found = True
                break
        if found:
            hit += 1
    return hit, total


def degrees(edges, n):
    d = [0] * n
    for e in edges:
        for v in e:
            d[v] += 1
    return d


def is_linear(edges):
    seen = set()
    for e in edges:
        for p in itertools.combinations(sorted(e), 2):
            if p in seen:
                return False
            seen.add(p)
    return True


def Up(n):
    """Exact rational bound U'(n) = 120(n-1)/((n-2)(n-3)(n-4)(n-5))."""
    return Fraction(120 * (n - 1), (n - 2) * (n - 3) * (n - 4) * (n - 5))


def U(n):
    return float(Up(n))


# ---- Steiner triple systems (exact enumeration checks) ----
fano = [{0,1,2},{0,3,4},{0,5,6},{1,3,5},{1,4,6},{2,3,6},{2,4,5}]
assert is_linear(fano)
T7 = count_triangles(fano)
assert T7 == 28, T7
h7, c7 = triangle_density(fano, 7)
print(f"STS(7): T={T7} (=28 predicted), 6-sets hit={h7}/{c7}, t={h7/c7:.4f}, U(7)={U(7):.4f}")

pts9 = [(x, y) for x in range(3) for y in range(3)]
idx = {p: i for i, p in enumerate(pts9)}
dirs = [(1,0),(0,1),(1,1),(1,2)]
sts9 = []
for d in dirs:
    for p in pts9:
        line = frozenset(idx[((p[0]+k*d[0])%3, (p[1]+k*d[1])%3)] for k in range(3))
        sts9.append(set(line))
sts9 = [set(s) for s in {frozenset(s) for s in sts9}]
assert len(sts9) == 12, len(sts9)
assert is_linear(sts9)
T9 = count_triangles(sts9)
assert T9 == 72, T9
h9, c9 = triangle_density(sts9, 9)
print(f"STS(9): T={T9} (=72 predicted), 6-sets hit={h9}/{c9}, t={h9/c9:.4f}, U(9)={U(9):.4f}")
assert h9 <= T9  # each hit 6-set needs a spanning triangle; t*C(n,6) <= T

# ---- random greedy linear 3-graphs ----
random.seed(612)
for n in (8, 10, 12):
    triples = list(itertools.combinations(range(n), 3))
    random.shuffle(triples)
    used, edges = set(), []
    for t in triples:
        ps = list(itertools.combinations(t, 2))
        if all(p not in used for p in ps):
            edges.append(set(t))
            used.update(ps)
    assert is_linear(edges)
    assert len(edges) <= n*(n-1)//6
    d = degrees(edges, n)
    assert all(x <= (n-1)//2 for x in d)
    T = count_triangles(edges)
    cap = sum(x*(x-1)//2 for x in d)
    assert T * 3 <= 4 * cap, (T, cap)  # T <= (4/3) sum C(d,2), exact integers
    h, c = triangle_density(edges, n)
    assert h <= T, (h, T)
    t = h / c
    assert t <= U(n) + 1e-12, (t, U(n))
    print(f"n={n}: e={len(edges)}, T={T}, 4/3*sumC(d,2)={4*cap/3:.2f}, "
          f"t={t:.4f} <= U(n)={U(n):.4f} OK")

# ---- U'(n) kills the 1/30 leg (exact rationals) ----
for n in (10, 13, 14, 15, 19, 20, 21, 100):
    u = Up(n)
    print(f"U'({n}) = {u} ~= {float(u):.6f}  (< 1/30: {u < Fraction(1,30)}, < 1/8: {u < Fraction(1,8)})")
assert Up(19) == Fraction(9, 238) and Up(19) > Fraction(1, 30)
# exact monotonicity on a wide window via closed ratio
assert all(Up(n + 1) / Up(n) == Fraction(n * (n - 5), (n - 1) ** 2) < 1
           for n in range(6, 2000))
# threshold: base n=20 (68400 < 73440) + induction step
# (n-1)/(n-5) >= n/(n-1)  <=>  3n+1 >= 0
assert 3600 * 19 < 18 * 17 * 16 * 15
assert all(Fraction(n - 1, n - 5) >= Fraction(n, n - 1) for n in range(20, 2000))
assert all(Up(n) < Fraction(1, 30) for n in range(20, 2000))
assert Up(15) < Fraction(1, 8)  # 1/8 leg vacuous from n=15 on
print("ALL CHECKS PASSED")
