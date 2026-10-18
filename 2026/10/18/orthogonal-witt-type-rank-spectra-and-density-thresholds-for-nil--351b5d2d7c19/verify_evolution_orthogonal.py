#!/usr/bin/env python3
"""Independent finite-field checks for rank census of one-dimensional-square algebras."""
from itertools import combinations,product
from math import prod
from fractions import Fraction

def hist_formula(q,n,eps=None):
    m=n//2
    if n%2: w=m; order=2*q**(m*m)*prod(q**(2*i)-1 for i in range(1,m+1))*(q-1)//2
    else: w=m if eps==1 else m-1; order=2*q**(m*(m-1))*(q**m-eps)*prod(q**(2*i)-1 for i in range(1,m))*(q-1)
    counts={n+1:q**n*order}
    for r in range(w+1):
        num=Fraction(1,1)
        for j in range(r):
            if n%2: num*=Fraction(q**(2*(m-j))-1, q**(j+1)-1)
            else: num*=Fraction((q**(m-j-1)+eps)*(q**(m-j)-eps),q**(j+1)-1)
        assert num.denominator==1
        maps=prod(q**n-q**i for i in range(r))
        k=int(num)*maps
        counts[r]=counts.get(r,0)+k*q**r
        counts[r+1]=counts.get(r+1,0)+k*(q**n-q**r)
    return {r:c for r,c in sorted(counts.items()) if c}

def rank(A,q):
    A=[list(row) for row in A]
    if not A:return 0
    i=0
    for j in range(len(A[0])):
        k=next((k for k in range(i,len(A)) if A[k][j]%q),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i]
        inv=pow(A[i][j],-1,q)
        A[i]=[(x*inv)%q for x in A[i]]
        for h in range(len(A)):
            if h==i:continue
            c=A[h][j]
            A[h]=[(x-c*y)%q for x,y in zip(A[h],A[i])]
        i+=1
        if i==len(A):break
    return i

def signed_type(q,diag):
    n=len(diag)
    if n%2:return None
    det=prod(diag)%q
    x=((-1)**(n//2)*det)%q
    return 1 if pow(x,(q-1)//2,q)==1 else -1

def exhaustive_endomorphisms(q,diag):
    n=len(diag); counts={}; n_qualifying=0
    for elems in product(range(q),repeat=n*n):
        A=[elems[i*n:(i+1)*n] for i in range(n)]
        Gram=[[sum(A[k][i]*diag[k]*A[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]
        lam=Gram[0][0]*pow(diag[0],-1,q)%q
        if any(Gram[i][j] != (lam*diag[i] if i==j else 0)%q for i in range(n) for j in range(n)):continue
        n_qualifying+=1
        for f in product(range(q),repeat=n):
            M=[list(row)+[0] for row in A]+[list(f)+[lam]]
            r=rank(M,q)
            counts[r]=counts.get(r,0)+1
    want=hist_formula(q,n,signed_type(q,diag))
    assert counts==want,(q,diag,counts,want)
    return n_qualifying,sum(counts.values()),want

def isotropic_rref(q,diag,r):
    n=len(diag);total=0
    for pivs in combinations(range(n),r):
        free=[(i,j) for i in range(r) for j in range(pivs[i]+1,n) if j not in pivs]
        for vals in product(range(q),repeat=len(free)):
            U=[[0]*n for _ in range(r)]
            for i,j in enumerate(pivs):U[i][j]=1
            for (i,j),v in zip(free,vals): U[i][j]=v
            if all(sum(U[i][k]*diag[k]*U[j][k] for k in range(n))%q==0 for i in range(r) for j in range(r)):
                total+=1
    return total

def formula_subspaces(q,n,r,eps):
 m=n//2
 t=Fraction(1)
 for i in range(r):
  if n%2: t*=Fraction(q**(2*(m-i))-1,q**(i+1)-1)
  else:t*=Fraction((q**(m-i-1)+eps)*(q**(m-i)-eps),q**(i+1)-1)
 assert t.denominator==1
 return int(t)

if __name__=='__main__':
    for q,diag in [(3,[1,1]),(3,[1,2]),(5,[1,1]),(5,[1,2]),(3,[1,1,1])]:
        a,b,p=exhaustive_endomorphisms(q,diag)
        print('DIRECT',q,diag,'qualifying T',a,'total endomorphisms',b,'ranks',p)
    for q,diag in [(3,[1,1,1,1]),(3,[1,1,1,2]),(5,[1,1,1,1]),(5,[1,1,1,2]),(3,[1,1,1,1,1])]:
        n=len(diag); ep=signed_type(q,diag);w=n//2 if n%2 or ep==1 else n//2-1
        for r in range(w+1):
            obs=isotropic_rref(q,diag,r)
            exp=formula_subspaces(q,n,r,ep)
            assert obs==exp,(q,diag,r,obs,exp)
        print('ISOTROPIC',q,diag,'all dimensions through',w,'ok')
    print('VERIFY_OK_ORTHOGONAL_EVOLUTION_RANK_SPECTRA')
