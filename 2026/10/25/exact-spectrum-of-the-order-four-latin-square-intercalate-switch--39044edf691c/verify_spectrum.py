#!/usr/bin/env python3
"""Exact, dependency-free spectral certificate for four-symbol Latin intercalate flips."""
from collections import Counter, deque
from itertools import combinations, permutations, product
from hashlib import sha256

SYMS = tuple(range(4))
ROWS = tuple(permutations(SYMS))
S = tuple(sorted(T for T in product(ROWS, repeat=4)
                 if all(len({T[r][c] for r in range(4)}) == 4 for c in range(4))))
assert len(S) == 576 and len(set(S)) == 576
idx = {T:i for i,T in enumerate(S)}

# Every 2-by-2 intercalate gives precisely one involutory Latin trade.
A = [set() for T in S]
for k,T in enumerate(S):
    for r,s in combinations(SYMS, 2):
        for c,d in combinations(SYMS, 2):
            if T[r][c] == T[s][d] and T[r][d] == T[s][c]:
                U = [list(row) for row in T]
                U[r][c], U[r][d] = U[r][d], U[r][c]
                U[s][c], U[s][d] = U[s][d], U[s][c]
                j = idx[tuple(map(tuple, U))]
                assert j != k
                A[k].add(j)
assert all(i in A[j] for i in range(576) for j in A[i])
assert Counter(map(len,A)) == {4:432, 12:144}
hi = [i for i in range(576) if len(A[i]) == 12]
lo = [i for i in range(576) if len(A[i]) == 4]
assert all(len(A[j]) == 4 for i in hi for j in A[i])
assert sum(map(len,A))//2 == 1728

# B is 144 by 432, with the high-intercalate squares indexing its rows.
lo_pos = {v:i for i,v in enumerate(lo)}
B = [frozenset(lo_pos[v] for v in A[i]) for i in hi]
assert all(len(row) == 12 for row in B)
G = [[len(B[i] & B[j]) for j in range(144)] for i in range(144)]
assert all(G[i][i] == 12 for i in range(144))
assert all(G[i][j] in (0,2) for i in range(144) for j in range(144) if i != j)
H = [tuple(j for j in range(144) if i != j and G[i][j] == 2) for i in range(144)]
assert all(len(x) == 18 for x in H)
assert all(i in H[j] for i in range(144) for j in H[i])

# Check an annihilating polynomial, not a floating-point diagonalization.
# p(t)=t(t+6)(t+2)(t-6)(t-18).
poly = [1]
for lam in (0, -6, -2, 6, 18):
    nxt = [0]*(len(poly)+1)
    for i,x in enumerate(poly):
        nxt[i] -= lam*x
        nxt[i+1] += x
    poly = nxt
assert poly == [0, 1296, 576, -72, -16, 1]
traces = [0]*5
for column in range(144):
    v = [int(j == column) for j in range(144)]
    acc = [0]*144
    for k in range(6):
        if k <= 4: traces[k] += v[column]
        for j in range(144):
            acc[j] += poly[k]*v[j]
        if k < 5:
            v = [sum(v[z] for z in H[j]) for j in range(144)]
    assert all(x == 0 for x in acc), (column, max(map(abs,acc)))

multiplicity = {-6:15, -2:81, 0:8, 6:39, 18:1}
assert traces == [sum(m*t**k for t,m in multiplicity.items()) for k in range(5)]
assert sum(multiplicity.values()) == 144

# Incidence graph spectrum from BB^T=12I+2H. Positive singular values
# are sqrt(0,8,12,24,48) with respective multiplicities 15,81,8,39,1.
# 318 zero eigenvalues on the full 576 x 576 adjacency matrix.
assert 576 - 2*(81+8+39+1) == 318

# Connectedness follows also from the simple top eigenvalue, but verify
# directly by searching all 576 states.
seen = {0}; q = deque([0]); max_dist = 0
while q:
    i=q.popleft()
    for j in A[i]:
        if j not in seen:
            seen.add(j);q.append(j)
assert len(seen)==576

digest=sha256((';'.join(','.join(map(str,sorted(neigh))) for neigh in A)).encode()).hexdigest()
print('latin_squares=576 high=144 low=432 edges=1728 connected=True')
print('BBT_diagonal=12 BBT_off_diagonal={0,2} halved_degree=18')
print('polynomial_coefficients_low_to_high=',poly)
print('halved_trace_0_to_4=',traces)
print('halved_spectrum=', sorted(multiplicity.items()))
print('flip_adjacency_spectrum: zeros=318; nonzero=±sqrt(8)[81],±sqrt(12)[8],±sqrt(24)[39],±sqrt(48)[1]')
print('lazy_random_walk_spectral_gap=(1-1/sqrt(2))/2')
print('adjacency_sha256=',digest)
print('EXACT_CERTIFICATE_OK')
