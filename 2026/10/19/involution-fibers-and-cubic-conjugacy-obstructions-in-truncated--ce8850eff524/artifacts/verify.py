#!/usr/bin/env python3
"""Finite-field verification of involutive automorphism lift counts for truncated tensor algebras."""
from itertools import product
from math import prod

def inv_mod(A,p):
    n=len(A)
    z=[[int(i==j) for j in range(n)]+list(A[i]) for i in range(n)]
    for k in range(n):
        piv=next((i for i in range(k,n) if z[i][k]%p),None)
        if piv is None:return None
        z[k],z[piv]=z[piv],z[k]
        d=pow(z[k][k],-1,p)
        z[k]=[(v*d)%p for v in z[k]]
        for i in range(n):
            if i==k:continue
            t=z[i][k]
            z[i]=[(x-t*y)%p for x,y in zip(z[i],z[k])]
    return [row[n:] for row in z]

def rank(X,p):
    X=[list(row) for row in X]
    if not X:return 0
    m,n=len(X),len(X[0]); a=0
    for j in range(n):
        i=next((i for i in range(a,m) if X[i][j]%p),None)
        if i is None:continue
        X[a],X[i]=X[i],X[a]
        d=pow(X[a][j],-1,p);X[a]=[(x*d)%p for x in X[a]]
        for k in range(a+1,m):
            c=X[k][j]
            if c:X[k]=[(x-c*y)%p for x,y in zip(X[k],X[a])]
        a+=1
        if a==m:break
    return a

def square(A,p):
    n=len(A)
    return [[sum(A[i][k]*A[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def kernel_dim(A,p):
    # Direct linearization of the quadratic component of phi^2(x)-x.
    n=len(A);c=n*n*n;rowlist=[]
    for i in range(n):
      for j in range(n):
       for v in range(n):
        row=[0]*c
        for s in range(n):
          row[(i*n+j)*n+s] = (row[(i*n+j)*n+s]+A[s][v])%p
        for k in range(n):
         for l in range(n):
          row[(k*n+l)*n+v] = (row[(k*n+l)*n+v]+A[i][k]*A[j][l])%p
        rowlist.append(row)
    return c-rank(rowlist,p)

def matset(n,p):
    for a in product(range(p),repeat=n*n):
      A=[a[i*n:(i+1)*n] for i in range(n)]
      if inv_mod(A,p) is not None:yield A

def enumerate_rank_classes(n,p):
    dd={}
    for A in matset(n,p):
      if any(square(A,p)[i][j] != (i==j) for i in range(n) for j in range(n)):
        continue
      r=rank([[int(i==j)-A[i][j] for j in range(n)] for i in range(n)],p)
      k=kernel_dim(A,p)
      dd[(r,k)]=dd.get((r,k),0)+1
    return dd

def brute_n2(p):
    # Directly compose the images of x,y in 1+V+V tensor V by substitution.
    n=2;total=0; groups={}
    for A in matset(2,p):
     aa=square(A,p)
     if aa != [[1,0],[0,1]]:continue
     count=0
     # B is image coefficients indexed by (word ab, generator c).
     for bs in product(range(p),repeat=8):
      # psi(x_k)=linear A x_k + quadratic B_{ab,k}
      # substitute again, degree >=3 disappears
      ok=True
      for v in range(n):
       for i in range(n):
        for j in range(n):
         val=sum(bs[(i*n+j)*n+s]*A[s][v] for s in range(n))
         val+=sum(A[i][k]*A[j][l]*bs[(k*n+l)*n+v] for k in range(n) for l in range(n))
         if val%p:ok=False;break
        if not ok:break
       if not ok:break
      if ok:count+=1
     k=kernel_dim(A,p)
     assert count==p**k,(p,A,count,k)
     total+=count
     r=rank([[int(i==j)-A[i][j] for j in range(n)] for i in range(n)],p)
     groups[(r,k)]=groups.get((r,k),0)+1
    return total,groups

if __name__=='__main__':
 for p in (2,3):
  total,counts=brute_n2(p)
  print(f'n2_F{p} direct-involutions {total}, profile={counts}')
 for p in (2,3):
  n=3
  profiles=enumerate_rank_classes(n,p)
  count=sum(k_count*p**k for (r,k),k_count in profiles.items())
  print(f'n3_F{p} matrix-nullity verified {count}, profile={profiles}')
 print('VERIFY_OK')

def gf4_mul(a,b):
    t=0
    for i in range(2):
        if (b>>i)&1:t^=a<<i
    if t&8:t^=0b1100 # t^3=t^2+t in F4
    if t&4:t^=0b111 # t^2=t+1
    return t

def gf4_rank(M):
    Z=[list(r) for r in M];m=len(Z);n=len(Z[0]);k=0
    inv=[0,1,3,2]
    for j in range(n):
        i=next((i for i in range(k,m) if Z[i][j]),None)
        if i is None:continue
        Z[k],Z[i]=Z[i],Z[k]
        t=inv[Z[k][j]]
        Z[k]=[gf4_mul(x,t) for x in Z[k]]
        for i in range(m):
            if i==k:continue
            z=Z[i][j]
            if z:Z[i]=[x^gf4_mul(z,y) for x,y in zip(Z[i],Z[k])]
        k+=1
        if k==m:break
    return k

def gf4_test_n2():
    groups={}
    for z in product(range(4),repeat=4):
        A=[z[:2],z[2:]]
        if gf4_mul(z[0],z[3])^gf4_mul(z[1],z[2])==0:continue
        A2=[[gf4_mul(A[i][0],A[0][j])^gf4_mul(A[i][1],A[1][j]) for j in range(2)] for i in range(2)]
        if A2!=[[1,0],[0,1]]:continue
        E=[[int(i==j)^A[i][j] for j in range(2)] for i in range(2)]
        r=gf4_rank(E)
        rows=[]
        for i,j,v in product(range(2),repeat=3):
            row=[]
            for k,l,s in product(range(2),repeat=3):
                x= (A[s][v] if (k,l)==(i,j) else 0)
                if s==v:x^=gf4_mul(A[i][k],A[j][l])
                row.append(x)
            rows.append(row)
        k=8-gf4_rank(rows)
        groups[(r,k)]=groups.get((r,k),0)+1
    expected={(0,8):1,(1,4):15}
    assert groups==expected,(groups,expected)
    assert sum(num*4**k for (r,k),num in groups.items())==69376
    print('n2_F4 matrix-nullity 69376, profile=',groups)

if __name__=='__main__':
    gf4_test_n2()
    print('VERIFY_GF4_OK')
