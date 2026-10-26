"""Exact finite verification of anticanonical data of R_[1324,4231].

The rank criterion, Bruhat covers, equivariant tangent characters, and
fixed-point localization use integer arithmetic and rational fractions.
"""
from itertools import permutations, combinations
from fractions import Fraction
from collections import Counter
from math import prod

N = 4
V = (1, 3, 2, 4)
W = (4, 2, 3, 1)
ALL = list(permutations(range(1, N + 1)))

def length(u):
    return sum(u[i] > u[j] for i in range(N) for j in range(i + 1, N))

def bruhat_leq(u, w):
    return all(sum(u[t] >= j for t in range(k)) <= sum(w[t] >= j for t in range(k))
               for k in range(1, N + 1) for j in range(1, N + 1))

def swap(u, i, j):
    q = list(u)
    q[i], q[j] = q[j], q[i]
    return tuple(q)

vertices = sorted((u for u in ALL if bruhat_leq(V, u) and bruhat_leq(u, W)),
                  key=lambda u: (length(u), u))
assert len(vertices) == 16
assert Counter(length(u) for u in vertices) == {1:1, 2:4, 3:6, 4:4, 5:1}

# Independent enumeration of the upper ideal under W by the subword criterion.
word = (1, 2, 3, 2, 1)
def word_product(indices):
    u = (1, 2, 3, 4)
    for k in indices:
        s = word[k]
        u = swap(u, s - 1, s)
    return u
assert word_product(range(5)) == W
subword_elements = {word_product(J) for m in range(6) for J in combinations(range(5), m)}
assert subword_elements == {u for u in ALL if bruhat_leq(u, W)}

# Adjacent fixed points have Bruhat-cover labels epsilon_{u(j)}-epsilon_{u(i)}.
adj = {u: [] for u in vertices}
for u in vertices:
    for i in range(N):
        for j in range(i + 1, N):
            z = swap(u, i, j)
            if z in adj and abs(length(z) - length(u)) == 1:
                alpha = tuple(int(k == u[j] - 1) - int(k == u[i] - 1)
                              for k in range(N))
                adj[u].append((z, alpha))
assert all(len(adj[u]) == 4 for u in vertices)
assert sum(len(a) for a in adj.values()) == 64
assert all(any(back == u and b == tuple(-x for x in a) for back, b in adj[z])
           for u in vertices for z, a in adj[u])

c1 = {u: tuple(sum(a[k] for _, a in adj[u]) for k in range(N)) for u in vertices}
degrees = {}
for u in vertices:
    for z, a in adj[u]:
        key = tuple(sorted((u, z)))
        diff = tuple(c1[u][k] - c1[z][k] for k in range(N))
        d = diff[a.index(1)]
        assert diff == tuple(d * a[k] for k in range(N))
        if key in degrees:
            assert degrees[key] == d
        degrees[key] = d
assert len(degrees) == 32
assert Counter(degrees.values()) == {0:4, 2:24, 4:4}
assert {e for e, d in degrees.items() if d == 0} == {
    ((1,3,4,2),(1,4,3,2)), ((3,1,2,4),(3,2,1,4)),
    ((2,3,4,1),(2,4,3,1)), ((4,1,2,3),(4,2,1,3))
}

def abbv(lam):
    terms = []
    for u in vertices:
        ws = [sum(a[k] * lam[k] for k in range(N)) for _, a in adj[u]]
        assert all(ws)
        terms.append(Fraction(sum(ws)**4, prod(ws)))
    return sum(terms, Fraction())
for cochar in ((0,1,2,3), (0,1,3,7), (-5,1,2,9), (1,4,10,25)):
    assert abbv(cochar) == 320, (cochar, abbv(cochar))
print('VERIFY_OK boolean_interval=16 edges=32 tangent_weights=64')
print('VERIFY_OK anticanonical_degrees=0:4,2:24,4:4 nef_not_ample')
print('VERIFY_OK anticanonical_volume=320 independent_generic_cocharacters=4')
