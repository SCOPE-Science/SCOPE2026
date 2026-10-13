#!/usr/bin/env python3
"""Exact-rational checker for RK4 heat-step positivity on unit paths and cycles.

Python standard library only. This verifies finite local walk tables and sampled
full matrices; the all-size locality proof is stated in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import factorial, comb


def poly(n, graph, j):
    """Return T[i,j] as degree-four polynomials in the timestep for all i."""
    adj = []
    for i in range(n):
        adj.append([x for x in (i-1, i+1) if 0 <= x < n] if graph == 'P'
                   else [(i-1) % n, (i+1) % n])
    v = [int(i == j) for i in range(n)]
    coeffs = [[F(0) for _ in range(5)] for _ in range(n)]
    for k in range(5):
        for i in range(n):
            coeffs[i][k] = F(v[i], factorial(k))
        v = [sum(v[a] for a in adj[i]) - len(adj[i]) * v[i] for i in range(n)]
    return coeffs


def value(c, h):
    return sum(a * h**k for k, a in enumerate(c))


def bernstein(q, L=F(2,3)):
    """Exact Bernstein coefficients on [0,L]."""
    degree = len(q)-1
    return [sum(q[j] * L**j * F(comb(k,j), comb(degree,j))
                for j in range(k+1)) for k in range(degree+1)]

# Each set is obtained by expanding Q^k and collecting at vertex distances 1, 2;
# the finite list is complete because degree four sees only radius-four walks.
nearest = {
    (F(1),F(-1),F(2,3),F(-1,3)),
    (F(1),F(-3,2),F(3,2),F(-9,8)),
    (F(1),F(-3,2),F(3,2),F(-7,6)),
    (F(1),F(-2),F(5,2),F(-9,4)),
    (F(1),F(-2),F(5,2),F(-55,24)),
    (F(1),F(-2),F(5,2),F(-7,3)),
    (F(1),F(-2),F(8,3),F(-8,3)),
}
distance_two = {
    (F(1,2),F(-2,3),F(13,24)),
    (F(1,2),F(-5,6),F(5,6)),
    (F(1,2),F(-1),F(7,6)),
    (F(1),F(-2),F(7,3)),
    (F(1,2),F(-1),F(29,24)),
}
assert len(nearest) == 7 and len(distance_two) == 5
for q in nearest | distance_two:
    assert all(b > 0 for b in bernstein(q)), (q, bernstein(q))

# Exact thresholds for small exceptional structures. The r polynomial is
# a cubic in h with a unique positive root in each case.
special_roots = {
    ('P',2): (F(3),F(-3),F(2),F(-1)),
    ('P',3): (F(8),F(-12),F(12),F(-9)),
    ('C',3): (F(8),F(-12),F(12),F(-9)),
    ('C',4): (F(3),F(-6),F(8),F(-8)),
    ('C',5): (F(24),F(-48),F(60),F(-55)),
}
fixed_thresholds = {('P',4):F(2,3), ('P',5):F(4,7),
                    ('C',6):F(1,2), ('C',7):F(4,7)}


def cutoff_sign(graph, n, h):
    r = special_roots.get((graph,n))
    if r is not None:
        return value(r,h) >= 0
    t = fixed_thresholds.get((graph,n),F(1,2))
    return h <= t

seen_d1, seen_d2 = set(), set()
checks = 0
for graph, ns in (('P',range(2,31)),('C',range(3,31))):
    for n in ns:
        cols = [poly(n,graph,j) for j in range(n)]
        # Diagonal spectral positivity is proved analytically; evaluate samples.
        for j in range(n):
            assert cols[j][j][0] == 1
        for j in range(n):
            for i in range(j+1,n):
                d = min(i-j,n-(i-j)) if graph == 'C' else i-j
                c = cols[j][i]
                if d == 1:
                    seen_d1.add(tuple(c[1:]))
                if d == 2:
                    seen_d2.add(tuple(c[2:]))
                if d >= 5:
                    assert c == [0]*5
                if d == 4:
                    assert c[:4] == [0]*4 and c[4] > 0
                if d == 3:
                    assert c[:3] == [0]*3 and c[3] > 0
                if d <= 2:
                    assert all(x > 0 for x in bernstein(tuple(c[d:]))), (graph,n,i,j)
        for h in (F(0),F(1,10),F(1,2),F(13,25),F(4,7),F(2,3),
                  F(69,100),F(7,10),F(3,4),F(9,10),F(1),F(3,2),F(2)):
            should = cutoff_sign(graph,n,h)
            actual = all(value(cols[j][i],h) >= 0 for i in range(n) for j in range(n))
            assert actual == should, (graph,n,h,actual,should)
            checks += n*n
assert seen_d1 == nearest, (len(seen_d1),len(nearest),seen_d1^nearest)
assert seen_d2 == distance_two, (len(seen_d2),len(distance_two),seen_d2^distance_two)
print('VERIFY_OK', 'local_nearest_patterns=7', 'local_distance_two_patterns=5',
      'path_cycle_sizes=57', f'exact_matrix_entry_tests={checks}')
