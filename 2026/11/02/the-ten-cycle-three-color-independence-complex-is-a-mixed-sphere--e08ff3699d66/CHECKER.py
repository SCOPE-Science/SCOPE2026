#!/usr/bin/env python3
"""Reproduce the face-poset matching and integral Morse boundary for Ind(C10 x K3).
Pure Python 3 standard library; no external packages, downloads, or stored data.
"""
from collections import Counter, deque
from functools import lru_cache

N, Q = 10, 3
V = N*Q
adj = [0]*V
for i in range(N):
    for a in range(Q):
        v = Q*i+a
        for j in ((i-1) % N, (i+1) % N):
            for b in range(Q):
                if a != b:
                    adj[v] |= 1 << (Q*j+b)

# Every independent subset is counted exactly once by the vertex-extension recursion.
faces = {0}
for v in range(V):
    bit = 1 << v
    faces.update({f | bit for f in faces if not (f & adj[v])})
faces.remove(0)
assert len(faces) == 216257
fvector = Counter(f.bit_count()-1 for f in faces)
assert [fvector[i] for i in range(15)] == [
    30,375,2560,10545,27456,46385,52080,40245,
    22460,9594,3330,955,210,30,2
]

# Lexicographic pivot matching: all available sigma < sigma + {v} are paired.
# At fixed v no two such pairs intersect; hence iteration order is irrelevant.
remaining = set(faces)
matched = {}
for v in range(V):
    bit = 1 << v
    for sigma in tuple(remaining):
        tau = sigma | bit
        if not (sigma & bit) and tau in remaining:
            assert sigma in remaining
            matched[sigma] = tau
            remaining.remove(sigma)
            remaining.remove(tau)
assert len(matched) == 108121
assert len(remaining) == 15
critical = {d:sorted(f for f in remaining if f.bit_count()-1==d) for d in (0,5,6)}
assert [len(critical[d]) for d in (0,5,6)] == [1,8,6]
assert sum(1 for f in remaining if f.bit_count()-1 not in (0,5,6)) == 0
assert critical[5] == [6303768,6303784,6311960,6311976,10498072,10498088,10506264,10506280]
assert critical[6] == [153166112,153239696,306221344,306331720,612405392,612442184]

# Check Forman acyclicity in the COMPLETE directed Hasse graph.
# Every unmatched cover is oriented down, and every matched cover up.
indegree = {f:0 for f in faces}
out = {}
edge_count = 0
for tau in faces:
    if tau.bit_count() == 1:
        continue
    bits = tau
    while bits:
        bit = bits & -bits
        bits -= bit
        sigma = tau ^ bit
        if matched.get(sigma) == tau:
            source,target = sigma,tau
        else:
            source,target = tau,sigma
        out.setdefault(source,[]).append(target)
        indegree[target] += 1
        edge_count += 1
assert edge_count == 1502070
queue = deque(f for f,d in indegree.items() if d == 0)
visited = 0
while queue:
    f = queue.pop()
    visited += 1
    for g in out.get(f,()):
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
assert visited == len(faces), (visited,len(faces))
del out, indegree, queue

# Signed integral Morse boundary between critical dimensions 6 and 5.
upper = {tau:sigma for sigma,tau in matched.items()}
unit = {f:tuple(int(i == j) for j in range(8))
        for i,f in enumerate(critical[5])}
zero = (0,)*8

@lru_cache(None)
def project(sigma):
    assert sigma.bit_count() == 6
    if sigma in unit:
        return unit[sigma]
    if sigma in upper:  # Matched as the upper face of a 4-5 pair.
        return zero
    assert sigma in matched
    tau = matched[sigma]
    assert tau.bit_count() == 7
    accum = [0]*8
    pivot_sign = None
    bits = tau
    pos = 0
    while bits:
        bit = bits & -bits
        bits -= bit
        rho = tau ^ bit
        sign = 1 if pos % 2 == 0 else -1
        if rho == sigma:
            pivot_sign = sign
        else:
            z = project(rho)
            for i in range(8):
                accum[i] += sign*z[i]
        pos += 1
    assert pivot_sign in (1,-1)
    return tuple(-pivot_sign*x for x in accum)

M = [[0]*6 for _ in range(8)]
for column,tau in enumerate(critical[6]):
    bits=tau
    pos=0
    while bits:
        bit = bits & -bits
        bits -= bit
        z = project(tau ^ bit)
        sign=1 if pos%2==0 else -1
        for row in range(8):
            M[row][column] += sign*z[row]
        pos += 1
expected = [
    [0,0,0,0,0,0],
    [-1,0,0,0,0,1],
    [0,0,1,-1,0,0],
    [1,0,-1,0,0,0],
    [0,1,0,0,-1,0],
    [0,0,0,0,1,-1],
    [0,-1,0,1,0,0],
    [0,0,0,0,0,0],
]
assert M == expected, M

# The six active rows/columns form a cyclic graph's oriented incidence matrix:
# column sums zero, each column contains exactly one 1 and one -1, and
# rows 1..6 are all connected by those six columns. Rank is exactly 5.
assert all(sum(M[row][col] for row in range(8)) == 0 for col in range(6))
assert all(sorted(M[row][col] for row in range(8) if M[row][col]) == [-1,1]
           for col in range(6))
seen = {1}
changed = True
while changed:
    changed = False
    for col in range(6):
        ends = {row for row in range(8) if M[row][col]}
        if ends & seen and not ends <= seen:
            seen |= ends
            changed = True
assert seen == set(range(1,7))

# Exact Bareiss determinant of a displayed 5x5 minor, rows 1..5/cols 0..4.
def determinant(A):
    A = [list(row) for row in A]
    n = len(A)
    den = 1
    sign = 1
    for k in range(n-1):
        if A[k][k] == 0:
            r = next((r for r in range(k+1,n) if A[r][k]),None)
            assert r is not None
            A[k],A[r] = A[r],A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = A[i][j]*pivot - A[i][k]*A[k][j]
                assert num % den == 0
                A[i][j] = num//den
            A[i][k] = 0
        den = pivot
    return sign*A[-1][-1]
assert determinant([row[:5] for row in M[1:6]]) == 1

# The upper bound 5 on the rank comes from row sum zero. The minor
# equals 1, so all five nonzero Smith factors are units over Z.
# Morse CW has only a point, eight 5-cells and six 6-cells. Consequently
# H5=Z^3, H6=Z; attaching maps S5 -> wedge S5 are classified by Z^8.
print('C10K3_INTEGRAL_MORSE_HOMOTOPY_OK')
print('face_vector=',[fvector[i] for i in range(15)])
print('faces=',len(faces),'matches=',len(matched),'Hasse_edges=',edge_count,
      'critical=(1 in dim0,8 in dim5,6 in dim6)')
print('Morse_boundary_rows=',M)
print('integral_boundary_rank=5; unimodular_minor=1; H5=Z^3; H6=Z')
