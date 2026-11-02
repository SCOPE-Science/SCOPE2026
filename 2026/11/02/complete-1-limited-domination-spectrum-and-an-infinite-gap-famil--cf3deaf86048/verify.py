#!/usr/bin/env python3
"""Exact standalone checks for the size enumerator of 1-limited dominating sets on cycle prisms.
Python 3, standard library only.  Full mathematical proof and scope are in RESULT.md.
"""
from collections import defaultdict
from itertools import product
from math import comb

P = [(a,b) for a in range(4) for b in range(4)]

def ok(a,b,c):
    for r in (0,1):
        y = (b >> r) & 1
        nbrs = ((a >> r)&1) + ((c >> r)&1) + ((b >> (1-r))&1)
        if nbrs < 1+y:
            return False
    return True

EDGES = {(a,b): [(b,c) for c in range(4) if ok(a,b,c)] for a,b in P}
CORE = [(0,0),(0,3),(1,1),(1,3),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]

# Bivariate integer polynomial: exponent pair (t,z) -> coefficient.
def plus(p,q):
    a = dict(p)
    for k,v in q.items():
        a[k] = a.get(k,0)+v
        if not a[k]: del a[k]
    return a

def neg(p): return {e:-v for e,v in p.items()}

def mul(p,q):
    d=defaultdict(int)
    for (i,j),a in p.items():
        for (k,l),b in q.items(): d[(i+k,j+l)] += a*b
    return {e:v for e,v in d.items() if v}

ONE = {(0,0):1}

# Exact Leibniz determinant by subset dynamic programming, including permutation signs.
def determinant(A):
    n=len(A)
    D={0:ONE}
    for i in range(n):
        N={}
        for mask,poly in D.items():
            for j in range(n):
                if mask >> j & 1 or not A[i][j]:continue
                inversions = (mask>>(j+1)).bit_count()
                candidate=mul(poly,A[i][j])
                if inversions&1:candidate=neg(candidate)
                key=mask|1<<j
                N[key]=plus(N.get(key,{}),candidate)
        D=N
    return D[(1<<n)-1]

# Determinant of I-tM on recurrent states; acyclic states do not affect closed walks.
A=[]
for a,b in CORE:
    row=[]
    for c,d in CORE:
        entry=dict(ONE) if (a,b)==(c,d) else {}
        if (c,d) in EDGES[(a,b)]: entry=plus(entry,{(1,b.bit_count()):-1})
        row.append(entry)
    A.append(row)
left=determinant(A)
f1={(0,0):1,(1,1):-1}
f2={(0,0):1,(1,1):-1,(2,3):1}
# Q=1 - t z^2 - t^2 z^3 - (2z^4+z^5)t^3 - (z^4+z^5+z^6)t^4 - t^5 z^6
f3={(0,0):1,(1,2):-1,(2,3):-1,(3,4):-2,(3,5):-1,
    (4,4):-1,(4,5):-1,(4,6):-1,(5,6):-1}
right=mul(mul(f1,f2),f3)
assert left==right,(left,right)

# Transfer by cyclic words, polynomial in the number of selected vertices.
def transfer_counts(n):
    out=defaultdict(int)
    for init in CORE:
        dp={(init,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (ab,k),count in dp.items():
                a,b=ab
                for bc in EDGES[ab]:
                    if bc in CORE:nxt[(bc,k+b.bit_count())]+=count
            dp=nxt
        for (ab,k),count in dp.items():
            if ab==init:out[k]+=count
    return dict(out)

# Independent direct graph-based check, not using local transfer validity.
def brute_counts(n):
    ans=defaultdict(int)
    # selected bit position = 2*i + r
    for mask in range(1<<(2*n)):
        good=True
        for i in range(n):
            for r in (0,1):
                v=2*i+r
                chosen = mask>>v&1
                neigh=((mask>>(2*((i-1)%n)+r))&1)+((mask>>(2*((i+1)%n)+r))&1)+((mask>>(2*i+1-r))&1)
                if neigh < 1 + chosen:
                    good=False;break
            if not good:break
        if good:ans[mask.bit_count()]+=1
    return dict(ans)

exhaustive=0
for n in range(3,9):
    a=brute_counts(n)
    b=transfer_counts(n)
    assert a==b,(n,a,b)
    exhaustive+=1<<(2*n)

for n in range(3,41):
    d=transfer_counts(n)
    assert min(d)==n,(n,d)
    assert d[n]==2+(4 if n%4==0 else 0)
    assert d.get(n+1,0)==(n if n%2 else 0)
    if n%2==0:
        expected=n*(7*n-14+2*(-1)**(n//2))//4
    else:
        expected=n*(3*n-6-(-1)**((n-1)//2))//2
    assert d[n+2]==expected,(n,d[n+2],expected)
    assert d[2*n]==1 and d[2*n-1]==2*n
print('VERIFY_OK determinant_monomials=%d exhaustive_assignments=%d n=3..8 min_nearmin_profiles=3..40' % (len(left),exhaustive))
