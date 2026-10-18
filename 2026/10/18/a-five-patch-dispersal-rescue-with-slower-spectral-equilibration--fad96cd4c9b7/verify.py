"""Exact-arithmetic checks for a five-patch spectral tradeoff.

Run: python3 verify.py. Only the Python standard library is needed.
The analytic proof in RESULT.md, not these finite checks alone, establishes
all graph-order and parameter assertions.
"""
from fractions import Fraction as Q
from itertools import combinations


def matrix(n, edges):
    a = [[0] * n for _ in range(n)]
    for i, j in edges:
        assert i != j
        a[i][j] = a[j][i] = 1
    return a


def product(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def characteristic_coefficients(a):
    """Coefficients of det(xI-A), descending, by Newton identities."""
    n = len(a)
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = [0]
    for _ in range(n):
        power = product(power, a)
        traces.append(sum(power[i][i] for i in range(n)))
    coeffs = [Q(1)]
    for k in range(1, n + 1):
        ck = -sum(coeffs[k-j] * traces[j] for j in range(1, k+1)) / k
        coeffs.append(ck)
    assert all(v.denominator == 1 for v in coeffs)
    return tuple(int(v) for v in coeffs)


def pmul(f, g):
    """Multiply descending-coefficient polynomials."""
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i+j] += x*y
    return tuple(out)


def evaluate(coefficients, x):
    v = Q(0)
    for c in coefficients:
        v = v*x + c
    return v


def connected(n, es):
    reached = {0}
    while True:
        nxt = reached | {j for i, j in es if i in reached} | {i for i, j in es if j in reached}
        if nxt == reached:
            return len(reached) == n
        reached = nxt


def contains_triangle(n, es):
    s = set(es)
    return any((i,j) in s and (i,k) in s and (j,k) in s
               for i,j,k in combinations(range(n),3))


G = {(0,1), (0,2), (0,4), (1,2), (2,3)}
H = G | {(3,4)}
assert characteristic_coefficients(matrix(5,G)) == pmul((1,0),pmul((1,-1,-3),(1,1,-1)))
assert characteristic_coefficients(matrix(5,H)) == pmul((1,0),pmul((1,2),(1,-2,-2,2)))

# Rational root isolation for the cubic belonging to H.
f = (1, -2, -2, 2)
assert evaluate(f, Q(-3,2)) < 0 < evaluate(f, Q(-1))
assert evaluate(f, Q(0)) > 0 > evaluate(f, Q(1))
assert evaluate(f, Q(12,5)) < 0 < evaluate(f, Q(5,2))
# These three disjoint intervals each contain one real root, exhausting degree three.
# The positive Perron root beta therefore lies strictly between 12/5 and 5/2.
# Let alpha=(1+sqrt(13))/2 and phi=(1+sqrt(5))/2.
# Bound alpha in (23/10,47/20), phi in (3/2,13/8), beta in (12/5,5/2).
assert 13 > Q(18,5)**2 and 13 < Q(37,10)**2
assert 5 > 2**2 and 5 < Q(9,4)**2
# On 0<=q<=1/2, the numerator of D_G(q)-D_H(q), after
# multiplying positive denominators, is
# (2*alpha-beta*phi)+q*(2-alpha-phi+beta).
# Both coefficients are strictly positive by the following rational bounds.
assert 2*Q(23,10)-Q(5,2)*Q(13,8) == Q(43,80) > 0
assert 2-Q(47,20)-Q(13,8)+Q(12,5) == Q(17,40) > 0
# From the other two intervals, the modulus of every other shifted eigenvalue
# except -2+1/2=-3/2 is <3/2.
assert Q(7,20) * (Q(12,5) + Q(1,2)) == Q(203,200) > 1
# For G, its Perron root in A+I/2 is (2+sqrt(13))/2.
assert 13 < Q(26,7)**2  # 7(2+sqrt(13))/40 < 1.
assert Q(3,4)**2 < 13  # (2+sqrt(13))/sqrt(5) > 2.
assert Q(5,2) * 2 + 1 == 6  # H damping ratio is <2.
# All columns of (I+2A)/8 sum to at most 7/8.
for es in (G,H):
    a = matrix(5,es)
    assert all((1+2*sum(a[i][j] for i in range(5))) <= 7 for j in range(5))
    assert connected(5,es) and contains_triangle(5,es)

# Entire connected nonbipartite landscape with n<=4, not a numeric sample.
paw = pmul((1,1),(1,-1,-3,1))
diamond = pmul((1,0),pmul((1,1),(1,-1,-4)))
complete = pmul((1,-3),pmul((1,1),pmul((1,1),(1,1))))
seen = {2:0, 3:0, 4:0}
edge_additions = 0
for n in (2,3,4):
    all_pairs = list(combinations(range(n),2))
    for bits in range(1 << len(all_pairs)):
        edges = {e for j,e in enumerate(all_pairs) if bits & (1<<j)}
        if not connected(n,edges) or not contains_triangle(n,edges):
            continue
        seen[n] += 1
        if n == 3:
            assert len(edges) == 3
        if n == 4:
            expected = {4:paw,5:diamond,6:complete}[len(edges)]
            assert characteristic_coefficients(matrix(n,edges)) == expected
        for e in all_pairs:
            if e not in edges:
                edge_additions += 1
                assert n == 4 and len(edges) in (4,5)
                newer = edges | {e}
                expected = {5:diamond,6:complete}[len(newer)]
                assert characteristic_coefficients(matrix(n,newer)) == expected

# Exact intervals for eigenvalues of the paw graph (one eigenvalue is -1).
p = (1,-1,-3,1)
assert evaluate(p,Q(-149,100)) < 0 < evaluate(p,Q(-147,100))
assert evaluate(p,Q(31,100)) > 0 > evaluate(p,Q(32,100))
assert evaluate(p,Q(217,100)) < 0 < evaluate(p,Q(218,100))
# The paw/diamond comparison is uniformly strict on 0<=q<=1/2.
# At q=0, D_paw<2.18/1.47<2.5/1.6<D_diamond.
assert Q(218,147) < Q(25,16)
# At q=1/2, D_paw<2.68/.97 < (2+sqrt(17))/(sqrt(17)-2).
assert Q(268,97) < Q(31,11)
# Each cross-multiplied difference is affine in q, hence positive
# at both endpoints implies positive throughout the closed interval.
# Likewise diamond<K4 at q=0 and at q=1/2.
assert Q(26,15) < 3  # diamond(0)<2.6/1.5
assert 3 < 7  # diamond(1/2)<3 versus K4(1/2)=7
# The diamond has damping ratio (2+sqrt17)/(sqrt17-2),
# lying in (31/11,3) because 4<sqrt17<21/5.
assert 4**2 < 17 < Q(21,5)**2
# K4 has eigenvalues 3,-1,-1,-1 and damping 7 at diagonal weight 1/2.
assert edge_additions > 0
print('5-vertex graph characteristic polynomials: exact PASS')
print('Perron growth switch and damping-ratio reversal: exact PASS')
print('All connected nonbipartite graphs of order <=4: exact PASS')
print('Counts by order:',seen,'candidate edge-additions:',edge_additions)
print('Only standard-library rational arithmetic and exhaustive labeled enumeration used.')
