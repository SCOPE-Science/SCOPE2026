#!/usr/bin/env python3
"""Reproduce the higher-support census for the displayed ternary LCD code."""
from collections import Counter
from itertools import combinations, product

# Rows of the generator displayed in An--Hong--Kim--Lim, Proposition 4.1.
G = (
(1,0,0,0,0,2,2,0,0,0,1,1,0,2,1,1,1,2,2,1,2,1,0,2,0),
(0,1,0,0,0,0,0,2,2,2,1,0,0,1,1,2,1,1,1,1,1,2,1,2,1),
(0,0,1,0,0,2,1,2,2,0,2,0,2,2,2,0,0,2,1,1,2,0,2,0,0),
(0,0,0,1,0,2,0,2,1,1,1,2,2,2,0,1,1,0,1,0,0,2,1,0,0),
(0,0,0,0,1,1,1,1,0,2,1,1,2,0,0,1,0,1,1,1,2,1,2,2,2),
)
Q, K, N = 3, 5, 25
assert len(G) == K and all(len(r) == N for r in G)
COLUMNS = tuple(tuple(G[i][j] for i in range(K)) for j in range(N))


def rank(rows):
    A = [list(v) for v in rows]
    if not A:
        return 0
    r, k = 0, len(A[0])
    for j in range(k):
        pivot = next((s for s in range(r, len(A)) if A[s][j] % Q), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        factor = pow(A[r][j] % Q, -1, Q)
        A[r] = [(factor*x) % Q for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][j] % Q:
                coeff = A[i][j] % Q
                A[i] = [(a-coeff*b) % Q for a,b in zip(A[i], A[r])]
        r += 1
        if r == len(A):
            break
    return r


def spaces(d):
    """Enumerate every d-space of F_3^5 by its unique RREF matrix."""
    for piv in combinations(range(K), d):
        slots = [(i,j) for i,p in enumerate(piv)
                 for j in range(p+1, K) if j not in piv]
        for vals in product(range(Q), repeat=len(slots)):
            rows = [[int(j==p) for j in range(K)] for p in piv]
            for (i,j),value in zip(slots,vals):
                rows[i][j] = value
            yield rows


def dot(a,b):
    return sum(x*y for x,y in zip(a,b)) % Q


def zeros(rows):
    return tuple(j+1 for j,p in enumerate(COLUMNS)
                 if all(dot(row,p)==0 for row in rows))


def codeword(a):
    return tuple(dot(a,p) for p in COLUMNS)


def normalize(a):
    t = next(z for z in a if z)
    return tuple((v*pow(t,-1,Q)) % Q for v in a)


assert rank(G)==K
GRAM = [[sum(G[i][h]*G[j][h] for h in range(N))%Q
         for j in range(K)] for i in range(K)]
assert rank(GRAM)==K  # Euclidean LCD
assert len(set(normalize(p) for p in COLUMNS)) == N
weights = Counter(sum(v!=0 for v in codeword(a))
                  for a in product(range(Q),repeat=K))
assert dict(weights)=={0:1,14:22,15:56,16:62,17:32,18:20,
                      19:24,20:12,21:4,22:4,23:6}
expected = {
1:{14:11,15:28,16:31,17:16,18:10,19:12,20:6,21:2,22:2,23:3},
2:{19:6,20:87,21:291,22:326,23:216,24:205,25:79},
3:{22:15,23:255,24:445,25:495},
4:{24:25,25:96},
5:{25:1},
}
expected_total = {1:121,2:1210,3:1210,4:121,5:1}
actual={}
minimal_2_zeros=[]
for r in range(1,K+1):
    census=Counter()
    for U in spaces(r):
        missing = zeros(U)
        support=N-len(missing)
        census[support]+=1
        if r==2 and support==19:
            minimal_2_zeros.append(missing)
            # The four projective nonzero words in a ternary two-space.
            a,b=U
            four=[tuple((s*a[i]+t*b[i])%Q for i in range(K))
                  for s,t in ((1,0),(0,1),(1,1),(1,2))]
            assert sorted(sum(c!=0 for c in codeword(v)) for v in four)==[14,14,14,15]
    actual[r]=dict(sorted(census.items()))
    assert actual[r]==expected[r], (r,actual[r])
    assert sum(census.values())==expected_total[r]

expected_minimal={
(3,8,14,20,23,24),
(2,4,12,16,22,24),
(2,11,12,20,21,22),
(2,17,19,20,21,23),
(2,6,12,15,22,23),
(2,5,18,20,21,25),
}
assert set(minimal_2_zeros)==expected_minimal
# A second census: dual projective planes are annihilators of two-spaces.
# Counting column points inside every vector 3-space does not enumerate the
# primal two-spaces, and must yield the same 6/87/... projective-plane profile.
geometric = Counter(sum(rank([*W,list(p)])==3 for p in COLUMNS)
                    for W in spaces(3))
assert dict(sorted(geometric.items()))=={0:79,1:205,2:216,3:326,4:291,5:87,6:6}
maximal_planes={tuple(j+1 for j,p in enumerate(COLUMNS)
                      if rank([*W,list(p)])==3)
                for W in spaces(3)
                if sum(rank([*W,list(p)])==3 for p in COLUMNS)==6}
assert maximal_planes==expected_minimal
assert Counter(len(set(a)&set(b)) for a,b in combinations(maximal_planes,2))=={1:7,2:2,3:6}
frequency=Counter(i for plane in maximal_planes for i in plane)
assert frequency[2]==5 and sum(t==5 for t in frequency.values())==1
# The sharp universal second-weight inequality: every occupied coordinate
# contributes to exactly three of the four projective nonzero words.
assert (4*14+2)//3 == 19
assert min(actual[2])==19
print('ORDINARY_WEIGHTS',dict(sorted(weights.items())))
print('HIGHER_SUPPORT_COUNTS',actual)
print('MINIMUM_TWO_SPACES',sorted(maximal_planes))
print('DUAL_THREE_SPACE_PLANE_COUNTS',dict(sorted(geometric.items())))
print('GENERALIZED_WEIGHTS',[min(actual[r]) for r in range(1,K+1)])
print('VERIFY_OK')
