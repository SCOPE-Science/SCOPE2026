#!/usr/bin/env python3
"""Exact reproducible certificate for the two-token Petersen critical group.
Python 3 standard library only. Run: python3 verify.py.
"""
from collections import Counter, deque
from itertools import combinations
from math import prod

EXPECTED = [2] * 8 + [4] * 2 + [28, 1596, 38304] + [191520] * 3
EXPECTED_DET = 49253533675382566432014336000
EXPECTED_FACT = {2: 36, 3: 9, 5: 3, 7: 6, 19: 5}
EXPECTED_ELEMS = {
    2: {0: 28, 1: 8, 2: 4, 5: 4},
    3: {0: 39, 1: 1, 2: 4},
    5: {0: 41, 1: 3},
    7: {0: 38, 1: 6},
    19: {0: 39, 1: 5},
}

def graph():
    # Vertex i is the i-th lexicographically ordered pair from {0,...,4}.
    V = list(combinations(range(5), 2))
    G = {(i,j) for i in range(10) for j in range(i+1,10)
         if set(V[i]).isdisjoint(V[j])}
    assert len(G) == 15
    assert all(sum((min(i,j),max(i,j)) in G for j in range(10)) == 3 for i in range(10))
    configs = list(combinations(range(10), 2))
    nbr = {v: [] for v in range(10)}
    for u,v in G:
        nbr[u].append(v)
        nbr[v].append(u)
    location = {c:i for i,c in enumerate(configs)}
    n=len(configs)
    L=[[0]*n for _ in range(n)]
    for i,(u,v) in enumerate(configs):
        for token,occupied in ((u,v),(v,u)):
            for w in nbr[token]:
                if w == occupied: continue
                j=location[tuple(sorted((w,occupied)))]
                if i<j:
                    L[i][j]=L[j][i]=-1
                    L[i][i]+=1
                    L[j][j]+=1
    assert sum(L[i][i] for i in range(n))//2 == 120
    assert Counter(L[i][i] for i in range(n)) == {4:15, 6:30}
    assert all(sum(row)==0 for row in L)
    seen={0};q=deque([0])
    while q:
        v=q.popleft()
        for u in range(n):
            if L[v][u]==-1 and u not in seen:
                seen.add(u);q.append(u)
    assert len(seen)==45
    return L

def bareiss_det(matrix):
    # Exact fraction-free integer determinant; independent of p-adic diagonalization.
    a=[row[:] for row in matrix]
    n=len(a)
    sign=1;prev=1
    for k in range(n-1):
        if not a[k][k]:
            t=next((i for i in range(k+1,n) if a[i][k]), None)
            assert t is not None
            a[k],a[t]=a[t],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def valuation(v,p,limit):
    if v==0:return limit
    e=0
    while e<limit and v%p==0:
        v//=p;e+=1
    return e

def local_smith_p(matrix,p,E):
    # Integral elementary operations modulo p**(E+1).
    # These identify the p-primary Smith valuations exactly because E=v_p(det).
    modulus=p**(E+1)
    a=[[z%modulus for z in row] for row in matrix]
    n=len(a);diag=[]
    for k in range(n):
        minimum=E+1;where=None
        for i in range(k,n):
            for j in range(k,n):
                v=valuation(a[i][j],p,E+1)
                if v<minimum:minimum=v;where=(i,j)
                if minimum==0:break
            if minimum==0:break
        assert where is not None
        u,v=where
        a[k],a[u]=a[u],a[k]
        for row in a: row[k],row[v]=row[v],row[k]
        step=p**minimum
        quotient=modulus//step
        unit=a[k][k]//step
        assert unit%p
        unit_inv=pow(unit,-1,quotient)
        # Clear below by elementary integer row operations.
        for i in range(k+1,n):
            assert a[i][k]%step==0
            coef=(a[i][k]//step*unit_inv)%quotient
            for j in range(k,n):
                a[i][j]=(a[i][j]-coef*a[k][j])%modulus
            assert a[i][k]==0
        # Clear right by elementary integer column operations.
        for j in range(k+1,n):
            assert a[k][j]%step==0
            coef=(a[k][j]//step*unit_inv)%quotient
            for i in range(k,n):
                a[i][j]=(a[i][j]-coef*a[i][k])%modulus
            assert a[k][j]==0
        diag.append(minimum)
    assert diag==sorted(diag)
    assert sum(diag)==E
    return diag

def exact_charpoly(A):
    # Coefficients via Newton identities and exact traces of matrix powers.
    n=len(A)
    power=[[int(i==j) for j in range(n)] for i in range(n)]
    traces=[]
    for exponent in range(1,n+1):
        nxt=[[0]*n for _ in range(n)]
        for i in range(n):
            out=nxt[i]
            for k,v in enumerate(power[i]):
                if v:
                    for j,w in enumerate(A[k]):
                        if w:out[j]+=v*w
        power=nxt
        traces.append(sum(power[i][i] for i in range(n)))
    coefs=[1]
    for j in range(1,n+1):
        numerator=-sum(coefs[j-i]*traces[i-1] for i in range(1,j+1))
        assert numerator%j==0
        coefs.append(numerator//j)
    return coefs

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def predicted_charpoly():
    # Ascending coefficient ordering.
    pol=[1]
    for q,exponent in [([0,1],1),([-7,1],6),([-6,1],6),([-5,1],4),
                       ([-3,1],5),([-2,1],5),([32,-13,1],4),([38,-13,1],5)]:
        for _ in range(exponent):pol=multiply(pol,q)
    assert len(pol)==46
    return list(reversed(pol))

def verify():
    L=graph();reduced=[row[:-1] for row in L[:-1]]
    determinant=bareiss_det(reduced)
    assert determinant==EXPECTED_DET
    actual_charpoly=exact_charpoly(L)
    assert actual_charpoly==predicted_charpoly()
    # Spectrum's nonzero root product divided by number of vertices is tau.
    assert abs(actual_charpoly[-2])==45*determinant
    ds={}
    for p,E in EXPECTED_FACT.items():
        ds[p]=local_smith_p(reduced,p,E)
        assert dict(Counter(ds[p]))==EXPECTED_ELEMS[p]
    inv=[prod(p**ds[p][j] for p in ds) for j in range(44)]
    assert inv==[1]*28+EXPECTED
    assert all(inv[j+1]%inv[j]==0 for j in range(43))
    assert prod(inv)==determinant
    # Two distinct exact identities: determinant and p-adic elementary divisors.
    print('VERIFY_OK; 45 states; 120 transitions; critical order',determinant)
    print('nonunit Smith factors:', ' '.join(map(str,EXPECTED)))

if __name__=='__main__':verify()
