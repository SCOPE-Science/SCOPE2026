#!/usr/bin/env python3
"""Exact rational verification for uncentered graph-ball maximal averages on a prism.
Run with Python >= 3.9; only the standard library is required.
"""
from fractions import Fraction as Q
from itertools import product, permutations

N = 6
adj = [[False] * N for _ in range(N)]
for h in range(2):
    for j in range(3):
        x, y = 3*h+j, 3*h+(j+1)%3
        adj[x][y] = adj[y][x] = True
for j in range(3):
    adj[j][j+3] = adj[j+3][j] = True
D = [[0 if i == j else (1 if adj[i][j] else 100) for j in range(N)]
     for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
assert max(max(row) for row in D) == 2
balls = []
for v in range(N):
    choices = {tuple(j for j in range(N) if D[c][j] <= r)
               for c in range(N) for r in range(3) if D[c][v] <= r}
    balls.append(sorted(choices, key=lambda x: (len(x), x)))
assert [len(b) for b in balls] == [6] * N
rows12 = [[tuple((12 // len(b)) * (j in b) for j in range(N))
           for b in balls[v]] for v in range(N)]

def positive_definite_integer(M):
    # Symmetric fraction-free elimination: pivot k is the kth leading principal minor.
    A = [row[:] for row in M]
    den = 1
    for k in range(N):
        pivot = A[k][k]
        if pivot <= 0:
            return False
        for i in range(k+1, N):
            for j in range(i, N):
                num = pivot * A[i][j] - A[i][k] * A[k][j]
                assert num % den == 0
                A[i][j] = A[j][i] = num // den
        den = pivot
    return True

def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]

def gram(R):
    return [[sum(row[i] * row[j] for row in R)
             for j in range(N)] for i in range(N)]

def characteristic(M):
    # Faddeev-LeVerrier, exact integer arithmetic.
    B = [[int(i == j) for j in range(N)] for i in range(N)]
    out = [1]
    for k in range(1, N+1):
        B = matmul(M, B)
        trace = sum(B[i][i] for i in range(N))
        assert trace % k == 0
        c = -trace // k
        out.append(c)
        for i in range(N):
            B[i][i] += c
    return out

winners = []
strict = 0
for selection in product(range(6), repeat=6):
    R = [rows12[v][selection[v]] for v in range(N)]
    G = gram(R)
    # 81/50 > ||R/12||_2^2 iff 11664 I - 50 R^T R is positive definite.
    C = [[11664 * (i == j) - 50 * G[i][j] for j in range(N)]
         for i in range(N)]
    if positive_definite_integer(C):
        strict += 1
    else:
        winners.append(selection)
assert strict == 46638 and len(winners) == 18

# Independent strict separation: every centered radius-selection matrix has
# squared spectral norm < 3/2, while the uncentered optimum is > 81/50.
centered_choices = []
for v in range(N):
    centered_choices.append([balls[v].index(tuple(j for j in range(N) if D[v][j] <= r))
                             for r in range(3)])
centered_count = 0
for reduced in product(range(3), repeat=N):
    selection = [centered_choices[v][reduced[v]] for v in range(N)]
    R = [rows12[v][selection[v]] for v in range(N)]
    G = gram(R)
    # (3/2)*144=216; multiplying by 2 gives 432 I - 2 R^T R.
    C = [[432 * (i == j) - 2 * G[i][j] for j in range(N)]
         for i in range(N)]
    assert positive_definite_integer(C)
    centered_count += 1
assert centered_count == 729

# Each exceptional average has denominator 1 or 4; scale by four.
expected = [1, -48, 675, -2868, 4288, -2048, 0]
G0 = None
patterns = []
for sel in winners:
    Bs = [balls[v][sel[v]] for v in range(N)]
    assert all(len(b) in (1, 4) for b in Bs)
    R4 = [[(4 // len(b)) * (j in b) for j in range(N)] for b in Bs]
    G4 = gram(R4)
    assert characteristic(G4) == expected
    if G0 is None:
        G0 = G4
    if all(sel[i] == 1 for i in range(3, 6)):
        assert sorted(sel[:3]) == [0, 0, sel[next(i for i in range(3) if sel[i] != 0)]]
        high = [i for i in range(3) if sel[i] == 0]
        small = next(i for i in range(3) if sel[i] != 0)
        special = next(j for j in range(3, 6) if j in Bs[small])
        assert len(high) == 2 and sel[small] in (1, 2, 3)
    else:
        assert all(sel[i] == 4 for i in range(3))
        high = [i for i in range(3, 6) if sel[i] == 0]
        small = next(i for i in range(3, 6) if sel[i] != 0)
        special = next(j for j in range(3) if j in Bs[small])
        assert len(high) == 2 and sel[small] in (2, 3, 4)
    pat = ['c'] * N
    for v in high: pat[v] = 'H'
    pat[small] = 'a'
    pat[special] = 'b'
    assert pat.count('H') == 2 and pat.count('a') == 1 and pat.count('b') == 1
    # The exceptional Gram is a coordinate permutation of the reference Gram.
    refpat = ['H', 'H', 'a', 'b', 'c', 'c']
    assert any(all(pat[i] == refpat[pi[i]] for i in range(N)) and
               all(G4[i][j] == G0[pi[i]][pi[j]] for i in range(N) for j in range(N))
               for pi in permutations(range(N)))
    patterns.append(tuple(pat))
assert len(set(patterns)) == 18
paired_to_small = sum(p.index('a') % 3 == p.index('b') % 3 for p in patterns)
assert paired_to_small == 6 and len(patterns) - paired_to_small == 12

# Isolate the only root of q above the rational cutoff 81/50.
def q(x):
    return 64*x**3 - 124*x**2 + 33*x - 2
lo, hi = Q(163356,100000), Q(163357,100000)
assert Q(81,50) < lo < hi < 2
assert q(lo) < 0 < q(hi)
# q''(x)>0 and q'(81/50)>0 for x>=81/50.
assert 384 * Q(81,50)-248 > 0
assert 192*Q(81,50)**2 - 248*Q(81,50) + 33 > 0
# The remaining two real roots of q lie in (0,1/10) and (1/5,1/4).
assert q(Q(0)) < 0 < q(Q(1,10))
assert q(Q(1,5)) > 0 > q(Q(1,4))

# Exact rational interval arithmetic verifies strict active-ball choices.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def divp(x,y):
    assert x[0]>0 and y[0]>0
    return (x[0]/y[1],x[1]/y[0])
def mult(x, n):
    assert n>=0
    return (x[0]*n,x[1]*n)
ONE = (Q(1),Q(1))
a = (1-Q(1)/lo, 1-Q(1)/hi)
x = add((Q(2),Q(2)),a)
b = divp(x,(8*lo-1,8*hi-1))
c = divp(x,(16*lo-1,16*hi-1))
lookup = {'H':ONE,'a':a,'b':b,'c':c}
active = 0
for sel, pat in zip(winners,patterns):
    f = [lookup[k] for k in pat]
    for v in range(N):
        means = []
        for ball in balls[v]:
            total = (Q(0),Q(0))
            for j in ball:
                total = add(total, f[j])
            means.append((total[0]/len(ball),total[1]/len(ball)))
        chosen = means[sel[v]]
        assert all(chosen[0]>means[k][1] for k in range(6) if k != sel[v])
        active += 5
assert active == 540

# The canonical vector (1,1,a,b,c,c) is an eigenvector of A^T A
# with eigenvalue the root of q. The equations reduce to:
#   d=(2+a+b)/4, e=(2+a+c)/4,
#   d=2*lambda*b, e=4*lambda*c,
#   (d+e)/2=lambda-1 iff q(lambda)=0.
# Since Gram entries are nonnegative and the vector positive, Perron-Frobenius
# gives the simple dominant eigenvalue. Coordinate permutations transfer it.
print('CERTIFICATE_OK selections=46656 strict=46638 exceptional=18')
print('CERTIFICATE_OK characteristic=[1,-48,675,-2868,4288,-2048,0]')
print('CERTIFICATE_OK active_competitor_inequalities=540 rays=18 orbit_types=6+12')
print('CERTIFICATE_OK centered_strict_lt_3/2=729 uncentered_gt_81/50')
