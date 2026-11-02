"""Exact reproducibility checks for cycle cumulants of random Cayley-tree overlaps.

Uses only the Python standard library. Finite checks supplement analytic proofs.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
from heapq import heapify, heappush, heappop

checks = 0

def check(lhs, rhs, name):
    global checks
    assert lhs == rhs, (name, lhs, rhs)
    checks += 1

def prufer_tree(n, word):
    degrees=[1]*n
    for v in word: degrees[v] += 1
    leaves=[i for i in range(n) if degrees[i]==1]
    heapify(leaves)
    edges=[]
    for v in word:
        u=heappop(leaves)
        edges.append((min(u,v),max(u,v)))
        degrees[u]-=1
        degrees[v]-=1
        if degrees[v]==1: heappush(leaves,v)
    u,v=leaves
    edges.append((min(u,v),max(u,v)))
    return frozenset(edges)

def all_trees(n):
    return list(prufer_tree(n, word) for word in product(range(n),repeat=n-2))

def mean(n): return F(2*(n-1),n)

def cycle_cumulant(n, ell):
    return F(n-1,n**ell) + F(n*(n-3),2)*F(2*(n-1),n*n)**ell

def matrix_product(X,Y):
    m=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(m)) for j in range(m)] for i in range(m)]

def matrix_trace(M): return sum(M[i][i] for i in range(len(M)))

for n in range(3,9):
    edges=list(combinations(range(n),2))
    m=len(edges)
    M=[]
    for e in edges:
        row=[]
        for f in edges:
            row.append(2*n if e==f else 3 if set(e)&set(f) else 4)
        M.append(row)
    Mpower=[row.copy() for row in M]
    check(sum(M[i][i] for i in range(m)), m*2*n, f'trace(K) n={n}')
    for ell in range(2,6):
        Mpower=matrix_product(Mpower,M)
        direct=F(matrix_trace(Mpower), n**(2*ell))
        spec=mean(n)**ell + F(n-1,n**ell) + F(n*(n-3),2)*F(2*(n-1),n*n)**ell
        check(direct,spec,f'spectral trace n={n} ell={ell}')
        check(direct-mean(n)**ell,cycle_cumulant(n,ell),f'cycle cumulant n={n} ell={ell}')

for n in (3,4):
    trees=all_trees(n)
    check(len(trees),n**(n-2),f'Cayley count {n}')
    # Check every tree appears precisely once in the Prufer enumeration.
    check(len(set(trees)),len(trees),f'Prufer injectivity {n}')
    mu=mean(n)
    count=len(trees)
    cyc3=F(0)
    forest3=F(0)
    centered3=F(0)
    for A,B,C in product(trees, repeat=3):
        AB=len(A & B); BC=len(B & C); CA=len(C & A)
        cyc3 += AB*BC*CA
        forest3 += AB*BC
        centered3 += (AB-mu)*(BC-mu)*(CA-mu)
    denom=count**3
    check(cyc3/denom,mu**3+cycle_cumulant(n,3),f'triangle exact moment {n}')
    check(forest3/denom,mu**2,f'forest path exact product {n}')
    check(centered3/denom,cycle_cumulant(n,3),f'triangle centered mixed cumulant {n}')
    cyc4=F(0)
    cent4=F(0)
    for A,B,C,D in product(trees, repeat=4):
        xs=[len(A & B),len(B & C),len(C & D),len(D & A)]
        p=1
        q=F(1)
        for x in xs:
            p *= x
            q *= x-mu
        cyc4 += p
        cent4 += q
    denom4=count**4
    check(cyc4/denom4,mu**4+cycle_cumulant(n,4),f'four-cycle exact moment {n}')
    check(cent4/denom4,cycle_cumulant(n,4),f'four-cycle centered cumulant {n}')

# The triangle formula has first asymptotic term 4/n: test its exact remainder.
for n in (3,4,5,10,25,100,1000):
    tri=cycle_cumulant(n,3)
    check(tri>0,True,f'positive triangle cumulant {n}')
    # Explicit polynomial form of the second eigenvalue contribution.
    check(tri,F(n-1,n**3)+F(4*(n-3)*(n-1)**3,n**5),f'triangle polynomial {n}')
print(f'VERIFY_OK {checks} exact assertions; all Prufer trees through 4 vertices tested')
