#!/usr/bin/env python3
"""Independent exact-rational finite checks for Hamming graph cut/cycle projections.

Usage: python check_hamming.py
Requires only the Python 3 standard library. Finite tests are illustrative;
the analytic proof in RESULT.md covers all stated dimensions and alphabets.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb

def solve(A, b):
    n = len(A)
    T = [[F(x) for x in row] + [F(b[i])] for i, row in enumerate(A)]
    for k in range(n):
        p = next(i for i in range(k, n) if T[i][k])
        T[k], T[p] = T[p], T[k]
        v = T[k][k]
        for j in range(k, n+1): T[k][j] /= v
        for i in range(k+1, n):
            w = T[i][k]
            if not w: continue
            for j in range(k, n+1): T[i][j] -= w*T[k][j]
    x = [F(0) for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = T[i][n]-sum(T[i][j]*x[j] for j in range(i+1, n))
    return x

def hamming(d,q):
    V = list(product(range(q),repeat=d)); pos={v:i for i,v in enumerate(V)}
    E=[]
    for v in V:
        for axis in range(d):
            for color in range(v[axis]+1,q):
                w=list(v);w[axis]=color;E.append((pos[v],pos[tuple(w)]))
    return V,E

def direct_column(d,q):
    vertices, edges = hamming(d,q)
    n=len(vertices)
    L=[[0]*n for _ in range(n)]
    for u,v in edges:
        L[u][u]+=1; L[v][v]+=1; L[u][v]-=1;L[v][u]-=1
    base=vertices.index((0,)*d)
    targ=vertices.index((1,)+(0,)*(d-1))
    rhs=[int(i==base)-int(i==targ) for i in range(n)]
    anchor=n-1
    remain=[i for i in range(n) if i!=anchor]
    sol=solve([[L[i][j] for j in remain] for i in remain],[rhs[i] for i in remain])
    pot=[F(0)]*n
    for i,x in zip(remain,sol): pot[i]=x
    grad=[pot[u]-pot[v] for u,v in edges]
    e=edges.index((base,targ))
    diag=grad[e]
    assert diag>=0
    cut_norm=sum(abs(x) for x in grad)
    cycle_norm=sum(abs(x-F(int(i==e))) for i,x in enumerate(grad))
    return cut_norm, cycle_norm,diag

def closed(d,q):
    a=F((d+1)*(q-1),q)
    diag=F(2,d*(q-1))*(1-F(1,q**d))
    return a,1+a-2*diag,diag

def radial_exact(r,q):
    # integrate the polynomial A^(r-k) B^k on [0,1] exactly
    from math import comb
    ans=[]
    for k in range(r+1):
        a=r-k
        poly=[F(0) for _ in range(r+1)]
        for i in range(a+1):
            for j in range(k+1):
                poly[i+j] += F(comb(a,i)*((q-1)**i)*comb(k,j)*((-1)**j))
        ans.append(sum(z/F(i+1) for i,z in enumerate(poly))/q**(r+1))
    return ans

def run():
    total=0
    for d,q in [(1,2),(1,3),(1,5),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3)]:
        a=direct_column(d,q); b=closed(d,q)
        assert a==b,(d,q,a,b)
        assert a[0]==F((d+1)*(q-1),q)
        total+=4
        print(f'H({d},{q}): cut={a[0]}, cycle={a[1]}, Qdiag={a[2]} — exact match')
    for d in range(2,9):
        for q in range(2,9):
            r=d-1
            f=radial_exact(r,q)
            assert all(x>0 for x in f)
            assert all(f[i]>f[i+1] for i in range(r))
            assert sum(comb(r,k)*(q-1)**k*f[k] for k in range(r+1))==F(1,q)
            assert sum(comb(r-1,k)*(q-1)**k*(f[k]-f[k+1]) for k in range(r))==F(1,2*q)
            assert 2*f[0]==closed(d,q)[2]
            total+=5
    print(f'PASS: {total} exact-rational identities and independently solved graph cases')

if __name__=='__main__':run()
