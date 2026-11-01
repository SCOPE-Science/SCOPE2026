"""Exact finite verification of negative type for powers of Hamming graphs.

The universal mathematical argument is in the accompanying proof. This standalone
checker tests distances, q-ary Krawtchouk transforms, and sharp endpoint kernels.
Python standard library only; all tested calculations are integer or rational.
"""
from collections import deque
from fractions import Fraction
from itertools import product
from math import comb

CHECKS = 0


def verify(test, tag):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(tag)


def qkraw(d, q, j, r):
    """Fourier eigenvalue for the weight-r Hamming sphere at support j."""
    return sum((-1) ** a * (q-1) ** (r-a) * comb(j, a) * comb(d-j, r-a)
               for a in range(max(0, r-d+j), min(r, j)+1))


def eig(d, q, k, j, vals=None):
    if vals is None:
        return sum(((r+k-1)//k)*qkraw(d,q,j,r) for r in range(1,d+1))
    return sum(vals[(r+k-1)//k]*qkraw(d,q,j,r) for r in range(1,d+1))


def predicted_admissible(d, q, k):
    return k == 1 or d <= k or (q == 2 and (k == 2 or d == k+1))


# Independent combinatorial q-ary Fourier shell transform.
for d in range(1, 6):
    for q in range(2, 6):
        for j in range(d+1):
            # For one coordinate, summing all nontrivial alphabet symbols
            # against a nontrivial character gives -1; with a trivial
            # character the sum is q-1.
            verify(sum(qkraw(d,q,j,r) for r in range(d+1)) ==
                   (q**d if j == 0 else 0), ('orthogonality',d,q,j))

# All parameter combinations in a broad finite rectangle.
for q in range(2, 7):
    for d in range(1, 11):
        for k in range(1, d+2):
            eigenvalues = [eig(d,q,k,j) for j in range(1,d+1)]
            expected = predicted_admissible(d,q,k)
            verify((max(eigenvalues) <= 0) == expected,
                   ('classification',q,d,k,eigenvalues))

# The critical q-ary graph at d=k+1, q>=3, k>=2.
for q in range(3,8):
    for d in range(3,9):
        k = d-1
        M = (q-1)**(d-2)
        b = Fraction(1,M)
        vals = [0,1,1+b]
        zero = []
        for j in range(1,d+1):
            val = -1 + b * ((-1)**j) * (q-1)**(d-j)
            verify(eig(d,q,k,j,vals) == val,
                   ('q-endpoint Fourier',q,d,j))
            verify(val <= 0, ('q-endpoint sign',q,d,j))
            if val == 0:
                zero.append(j)
        verify(zero == [2], ('q-endpoint singular level',q,d,zero))
        verify(comb(d,2)*(q-1)**2 < q**d-1,
               ('q-endpoint rank',q,d))

# The critical binary graph at d=k+2, k>=3.
for d in range(5,12):
    k = d-2
    M = d-1 if d % 2 else d-3
    b = Fraction(1,M)
    vals = [0,1,1+b]
    zero = []
    for j in range(1,d+1):
        val = -1 + b * ((-1)**j)*(d+1-2*j)
        verify(eig(d,2,k,j,vals) == val,
               ('binary-endpoint Fourier',d,j))
        verify(val <= 0, ('binary-endpoint sign',d,j))
        if val == 0:
            zero.append(j)
    verify(zero == ([d] if d % 2 else [2,d-1]),
           ('binary-endpoint singular levels',d,zero))

# Independently build graph neighbors and BFS, for small complete alphabets.
for q in range(2, 5):
    for d in range(1, 7):
        words = list(product(range(q), repeat=d))
        if len(words) > 256:
            continue
        distances = [sum(x != y for x,y in zip(words[0],u)) for u in words]
        for k in range(1,d+2):
            nbr = [i for i,h in enumerate(distances) if 0 < h <= k]
            adj = [[] for _ in words]
            # Translate adjacency in the additive group (Z/q)^d.
            lookup = {u:i for i,u in enumerate(words)}
            for i,u in enumerate(words):
                adj[i] = [lookup[tuple((u[t]+words[v][t])%q for t in range(d))]
                          for v in nbr]
            dst = [-1]*len(words)
            dst[0] = 0
            todo = deque([0])
            while todo:
                u = todo.popleft()
                for v in adj[u]:
                    if dst[v] < 0:
                        dst[v] = dst[u]+1
                        todo.append(v)
            for i,h in enumerate(distances):
                verify(dst[i] == (h+k-1)//k,
                       ('independent BFS',q,d,k,i))

print('HAMMING_POWER_EXACT_CHECK_OK', CHECKS)
