#!/usr/bin/env python3
"""Finite corroborations for coordinate-matching sections of generic determinant.
Only standard Python; all arithmetic is exact over prime fields.
"""
from itertools import product
from random import Random

def rank(a,p):
    m=[row[:] for row in a]; n=len(m); r=0
    for j in range(n):
        piv=next((i for i in range(r,n) if m[i][j]%p),None)
        if piv is None: continue
        m[r],m[piv]=m[piv],m[r]
        inv=pow(m[r][j]%p,-1,p)
        m[r]=[(v*inv)%p for v in m[r]]
        for i in range(r+1,n):
            v=m[i][j]%p
            if v: m[i]=[(x-v*y)%p for x,y in zip(m[i],m[r])]
        r+=1
        if r==n:break
    return r

def det(a,p):
    n=len(a); b=[row[:] for row in a]; z=1
    for j in range(n):
        t=next((i for i in range(j,n) if b[i][j]%p),None)
        if t is None:return 0
        if t!=j:b[t],b[j]=b[j],b[t];z=-z
        v=b[j][j]%p; z=(z*v)%p; inv=pow(v,-1,p)
        for i in range(j+1,n):
            c=b[i][j]*inv%p
            if c:
                for l in range(j+1,n):b[i][l]=(b[i][l]-c*b[j][l])%p
    return z%p

def is_sing(a,k,p):
    n=len(a)
    if det(a,p):return False
    for i in range(n):
        for j in range(n):
            if i==j and i<k:continue
            sub=[[a[s][t] for t in range(n) if t!=j] for s in range(n) if s!=i]
            if det(sub,p):return False
    return True

def expected(a,k,p):
    n=len(a)
    return rank(a,p)<=n-2 or any(
        all(a[i][j]%p==0 and a[j][i]%p==0 for j in range(n)) for i in range(k))

def run():
    tests=0; singular=0
    for n in (3,4):
      for k in range(1,n+1):
        free=[(i,j) for i in range(n) for j in range(n) if not(i==j and i<k)]
        if n==4 or n==3:
          num=1<<len(free)
          for bits in range(num):
            a=[[0]*n for _ in range(n)]
            for h,(i,j) in enumerate(free):a[i][j]=(bits>>h)&1
            lhs=is_sing(a,k,2);rhs=expected(a,k,2)
            assert lhs==rhs,(n,k,bits,lhs,rhs,a)
            tests+=1;singular+=int(lhs)
          print('exhaustive_GFp',p:=2,'n',n,'k',k,'entries',num)
    rng=Random(23019)
    for p in (3,5,7):
      for n in (4,5,6):
        for k in (1,n//2,n):
          for _ in range(140):
            a=[[rng.randrange(p) if not(i==j and i<k) else 0 for j in range(n)] for i in range(n)]
            lhs=is_sing(a,k,p);rhs=expected(a,k,p)
            assert lhs==rhs,(p,n,k,lhs,rhs,a)
            tests+=1;singular+=int(lhs)
          print('random_GFp',p,'n',n,'k',k,'cases',140)
    print('VERIFY_OK: tests',tests,'singular',singular)
if __name__=='__main__':run()
