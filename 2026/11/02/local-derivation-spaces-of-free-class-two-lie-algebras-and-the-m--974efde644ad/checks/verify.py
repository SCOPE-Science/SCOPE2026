#!/usr/bin/env python3
"""Finite-field reproducibility checks for local derivations of a free class-two Lie algebra.
Only prime fields in these tests; the mathematical proof covers arbitrary fields.
"""
from itertools import combinations,product

def pivots(rows,p):
    d={}
    for row in rows:
        a=[x%p for x in row]
        for col,v in sorted(d.items()):
            if a[col]:
                k=a[col]
                a=[(x-k*y)%p for x,y in zip(a,v)]
        for col,k in enumerate(a):
            if k:
                iv=pow(k,-1,p)
                d[col]=[(x*iv)%p for x in a]
                break
    return d

def rank(rows,p): return len(pivots(rows,p))

def orthogonal(rows,width,p):
    d=pivots(rows,p)
    free=[j for j in range(width) if j not in d]
    for t in free:
        v=[0]*width;v[t]=1
        for j in sorted(d,reverse=True):
            v[j]=-sum(d[j][k]*v[k] for k in range(j+1,width))%p
        yield v

def data(n,p):
    pairs=list(combinations(range(n),2));m=len(pairs)
    pos={b:i for i,b in enumerate(pairs)}
    images=[]
    for a in range(n):
      for b in range(n):
        mat=[[0]*m for _ in range(m)]
        for j,(u,v) in enumerate(pairs):
          if b==u and a!=v:
            t=tuple(sorted((a,v)))
            mat[pos[t]][j]=(mat[pos[t]][j]+(1 if a<v else -1))%p
          if b==v and a!=u:
            t=tuple(sorted((u,a)))
            mat[pos[t]][j]=(mat[pos[t]][j]+(1 if u<a else -1))%p
        images.append(mat)
    return pairs,images

def matvec(mat,x,p):
    return [sum(a*b for a,b in zip(row,x))%p for row in mat]

def addvec(x,y,p):return [(a+b)%p for a,b in zip(x,y)]

def local_dim(n,p):
    pairs,images=data(n,p); m=len(pairs)
    constraints=[]
    for z in product(range(p),repeat=m):
      if not any(z): continue
      ev=[matvec(M,z,p) for M in images]
      for y in orthogonal(ev,m,p):
        constraints.append([y[i]*z[j]%p for i in range(m) for j in range(m)])
    dim=m*m-rank(constraints,p)
    imrank=rank([[v for row in M for v in row] for M in images],p)
    return dim,imrank,len(constraints)

def direct_local(n,p):
    pairs,images=data(n,p);m=len(pairs)
    P=[[ (7*i+3*j+1)%p for j in range(n)] for i in range(n)]
    Q=[[ (5*i+j+1)%p for j in range(n)] for i in range(m)]
    A=[[ (2*i+3*j+1)%p for j in range(n)] for i in range(n)]
    rho=[[sum(A[a][b]*images[a*n+b][i][j] for a in range(n) for b in range(n))%p for j in range(m)] for i in range(m)]
    R=[[ (rho[i][j]+(1 if p==2 and i==j else 0))%p for j in range(m)] for i in range(m)]
    ordinary=[]
    for idx,M in enumerate(images):
        a=idx//n; b=idx%n
        ordinary.append(lambda v,z,M=M,a=a,b=b:([v[b] if i==a else 0 for i in range(n)]+matvec(M,z,p)))
    for i in range(m):
      for j in range(n):
        ordinary.append(lambda v,z,i=i,j=j:([0]*n+[v[j] if t==i else 0 for t in range(m)]))
    for x in product(range(p),repeat=n+m):
        v=x[:n];z=x[n:]
        candidate=matvec(P,v,p)+addvec(matvec(Q,v,p),matvec(R,z,p),p)
        ev=[f(v,z) for f in ordinary]
        if rank(ev+[candidate],p)!=rank(ev,p):
            raise AssertionError((n,p,'locality_failed',x,candidate))
    return p**(n+m)

if __name__=='__main__':
    cases=[(3,2,9,8),(4,2,16,15),(5,2,25,24),(3,3,9,9),(4,3,16,16),(3,5,9,9)]
    for n,p,goal,imgoal in cases:
        loc,im,checks=local_dim(n,p)
        assert (loc,im)==(goal,imgoal),(n,p,loc,im,goal,imgoal)
        print('tangent-reflexivity',n,p,'dim',loc,'induced',im,'witness checks',checks)
    for n,p in [(3,2),(4,2),(3,3)]:
        count=direct_local(n,p)
        print('full pointwise local-derivation tests',n,p,count)
    print('FREE_CLASS2_LOCAL_DERIVATIONS_OK')
