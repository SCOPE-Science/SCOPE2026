#!/usr/bin/env python3
"""Finite-field checks of the Heisenberg retraction orbit formula.

Only finite tests; the general theorem is established by the accompanying proof.
Run: python3 verify_retracts.py
"""
from collections import Counter, deque
from itertools import combinations, product
from math import prod

def rank_mod(M, q):
    a=[list(row) for row in M]
    if not a: return 0
    nr,nc=len(a),len(a[0]);r=0
    for c in range(nc):
        k=next((i for i in range(r,nr) if a[i][c]%q),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        z=pow(a[r][c]%q,-1,q)
        a[r]=[v*z%q for v in a[r]]
        for i in range(nr):
            if i!=r and a[i][c]%q:
                z=a[i][c]
                a[i]=[(v-z*w)%q for v,w in zip(a[i],a[r])]
        r+=1
        if r==nr:break
    return r

def rref_subspaces(n,r,q):
    for piv in combinations(range(n),r):
        pairs=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
        for vs in product(range(q),repeat=len(pairs)):
            rows=[[int(j==p) for j in range(n)] for p in piv]
            for (i,j),v in zip(pairs,vs):rows[i][j]=v
            yield rows

def omega(u,v,m,q):
    return sum(u[i]*v[m+i]-u[m+i]*v[i] for i in range(m))%q

def test_complements(m,q):
    n=2*m; classes=Counter()
    for r in range(m+1):
        for W in rref_subspaces(n,r,q):
            if any(omega(x,y,m,q) for x in W for y in W):continue
            piv=[next(j for j,v in enumerate(x) if v) for x in W]
            K0=[[int(a==j) for a in range(n)] for j in range(n) if j not in piv]
            for coeffs in product(range(q), repeat=r*(n-r)):
                K=[[ (x[a]+sum(coeffs[j*r+i]*W[i][a] for i in range(r)))%q
                    for a in range(n)] for j,x in enumerate(K0)]
                rk=rank_mod([[omega(x,y,m,q) for y in K] for x in K],q)
                classes[(r,(rk-2*(m-r))//2)]+=q**r
    return classes

def matmul2(A,B):
    return tuple(__import__('functools').reduce(lambda a,b:a^b,
                  (B[j] for j in range(len(A)) if (v>>j)&1),0) for v in A)

def rowmul2(v,A):
    z=0
    for j,x in enumerate(A):
        if v>>j&1:z^=x
    return z

def mv2(A,x):
    return sum((row&x).bit_count()%2<<i for i,row in enumerate(A))

def omega2(u,v,m=2):
    ans=0
    for i in range(m):ans^=((u>>i&1)&(v>>(m+i)&1))^((v>>i&1)&(u>>(m+i)&1))
    return ans

def matrix_rank2(rows,n):
    piv={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p not in piv:
                piv[p]=v;break
            v^=piv[p]
    return len(piv)

def kernel_basis2(A):
    out=[]
    for v in range(1,1<<len(A)):
        if mv2(A,v)==0 and matrix_rank2(out+[v],len(A))>len(out):out.append(v)
    return out

def mat_rank2(A):return matrix_rank2(A,len(A))

def invariants2(A):
    r=mat_rank2(A)
    K=kernel_basis2(A)
    alt=[]
    for u in K:
        alt.append(sum(omega2(u,v)<<j for j,v in enumerate(K)))
    return (r,(mat_rank2(alt)-2*(2-r))//2)

def transvection2(u,n=4):
    cols=[(1<<j)^(u if omega2(1<<j,u) else 0) for j in range(n)]
    return tuple(sum(((c>>i)&1)<<j for j,c in enumerate(cols)) for i in range(n))

def test_full_orbits_2():
    n=4;identity=tuple(1<<i for i in range(n))
    projections={}
    for rows in product(range(1<<n), repeat=n):
        if matmul2(rows,rows)!=rows:continue
        cols=[sum(((rows[i]>>j)&1)<<i for i in range(n)) for j in range(n)]
        if any(omega2(x,y) for x in cols for y in cols):continue
        for f in range(1<<n):
            if rowmul2(f,rows)==f:
                projections[(rows,f)]=invariants2(rows)
    predicted=Counter({(0,0):1,(1,0):240,(2,0):480,(2,1):480})
    got=Counter(projections.values())
    assert got==predicted,(got,predicted)
    matrices=[transvection2(u) for u in range(1,1<<n)]
    rem=set(projections)
    orbit_sizes=[]
    while rem:
        seed=rem.pop();queue=deque([seed]);sz=1;old=projections[seed]
        while queue:
            A,f=queue.popleft()
            for P in matrices:
                x=(matmul2(matmul2(P,A),P), rowmul2(f,P))
                if x in rem:
                    assert projections[x]==old
                    rem.remove(x);queue.append(x);sz+=1
            for j in range(n):
                x=(A,f^rowmul2(1<<j,A))
                if x in rem:
                    assert projections[x]==old
                    rem.remove(x);queue.append(x);sz+=1
        orbit_sizes.append((old,sz))
    assert Counter(orbit_sizes)==Counter({((0,0),1):1,((1,0),240):1,((2,0),480):1,((2,1),480):1}),orbit_sizes
    assert len(projections)==1201
    return sorted(orbit_sizes)

if __name__=='__main__':
    for m,q,exp in [(1,2,{(0,0):1,(1,0):12}),
                     (2,2,{(0,0):1,(1,0):240,(2,0):480,(2,1):480}),
                     (2,3,{(0,0):1,(1,0):3240,(2,0):9720,(2,1):19440})]:
        got=test_complements(m,q)
        assert got==Counter(exp),(m,q,got)
        print('COMPLEMENTS_OK',m,q,dict(sorted(got.items())))
    got=test_full_orbits_2()
    print('CONJUGATION_ORBITS_OK',got)
    print('VERIFY_OK')
