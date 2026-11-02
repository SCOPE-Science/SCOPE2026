#!/usr/bin/env python3
"""Exact finite checks for the Legendre--Cartier genus-five theorem.
This file supports finite verification only; the all-prime result has a symbolic proof.
Requires only Python's standard library.
"""
from math import comb


def trim(v):
    v=list(v)
    while len(v)>1 and v[-1]==0:v.pop()
    return v


def mulx(v,c,p):
    return [0]+[(c*u)%p for u in v]


def add(u,v,p):
    return trim([( (u[i] if i<len(u) else 0)+(v[i] if i<len(v) else 0))%p for i in range(max(len(u),len(v)))])


def negmul(u,c,p):
    return [(-c*x)%p for x in u]


def legendre_poly(p,n):
    h=pow(2,-1,p)
    a,b=[1],[0,h]
    if n==0:return a
    if n==1:return b
    for j in range(1,n):
        d=pow(j+1,-1,p)
        w=add(mulx(b,(2*j+1)*h,p), negmul(a,j,p),p)
        w=trim([(z*d)%p for z in w]);a,b=b,w
    return b


def coef_poly(p,j):
    m=(p-1)//2
    c=[0]*(j+1)
    for u in range(j//2+1):
        z=j-2*u
        if u+z<=m:
            c[z]=comb(m,u)*comb(m-u,z)%p
    return trim(c)


def evalpoly(a,v,p):
    out=0
    for z in v[::-1]:out=(out*a+z)%p
    return out


def divrem(a,b,p):
    a=trim(a);b=trim(b)
    assert b!=[0]
    b0=pow(b[-1],-1,p)
    while len(a)>=len(b) and a!=[0]:
        lead=a[-1]*b0%p
        offset=len(a)-len(b)
        for i,c in enumerate(b): a[offset+i]=(a[offset+i]-lead*c)%p
        a=trim(a)
    return a


def gcd(a,b,p):
    while b!=[0]:a,b=b,divrem(a,b,p)
    if a==[0]:return [0]
    q=pow(a[-1],-1,p)
    return trim([(q*x)%p for x in a])


def rank(M,p):
    M=[row[:] for row in M]
    rows=len(M);cols=len(M[0]);k=0
    for j in range(cols):
        t=next((t for t in range(k,rows) if M[t][j]%p),None)
        if t is None:continue
        M[k],M[t]=M[t],M[k]
        d=pow(M[k][j],-1,p)
        M[k]=[u*d%p for u in M[k]]
        for i in range(rows):
            if i!=k and M[i][j]:
                c=M[i][j]
                M[i]=[(M[i][l]-c*M[k][l])%p for l in range(cols)]
        k+=1
        if k==rows:break
    return k


def determinant(M,p):
    A=[row[:] for row in M]
    result=1
    for j in range(len(A)):
        t=next((i for i in range(j,len(A)) if A[i][j]%p),None)
        if t is None:return 0
        if t!=j:A[j],A[t]=A[t],A[j];result=-result
        pivot=A[j][j];result=result*pivot%p
        inv=pow(pivot,-1,p)
        for i in range(j+1,len(A)):
            u=A[i][j]*inv%p
            for k in range(j,len(A)):
                A[i][k]=(A[i][k]-u*A[j][k])%p
    return result%p


def matmul(U,V,p):
    n=len(U)
    return [[sum(U[i][j]*V[j][k] for j in range(n))%p for k in range(n)] for i in range(n)]


def isprime(n):
    return n>1 and all(n%d for d in range(2,int(n**.5)+1))


def degrees(p):
    if p%6==1:
        r=(p-1)//6
        return [r,2*r,3*r]
    r=(p+1)//6
    return [r-1,2*r-1,3*r-1]


def verify(p):
    m=(p-1)//2
    dd=degrees(p)
    polys=[legendre_poly(p,d) for d in dd]
    for d,P in zip(dd,polys):
        assert len(P)==d+1
        Q=coef_poly(p,d)
        assert Q==trim([(-x if d%2 else x)%p for x in P]),(p,d,Q,P)
        der=trim([i*P[i]%p for i in range(1,len(P))]) if len(P)>1 else [0]
        assert gcd(P,der,p)==[1],(p,d,'not squarefree')
        assert evalpoly(2,P,p)==1 and evalpoly(-2,P,p)==(p-1 if d%2 else 1)
    # Complete raw Hasse-Witt matrix in every smooth F_p-parameter;
    # since the coefficients belong to F_p, the Frobenius-twist of H is H.
    for A in range(p):
        if A in (2,p-2):continue
        H=[[0]*5 for _ in range(5)]
        for i in range(1,6):
            for j in range(1,6):
                e=p*i-j
                if e>=0 and e%6==0:
                    H[i-1][j-1]=evalpoly(A,coef_poly(p,e//6),p)
        stable=H
        for _ in range(4):stable=matmul(stable,H,p)
        expected=sum(w*(evalpoly(A,P,p)!=0) for w,P in zip((2,2,1),polys))
        assert rank(H,p)==expected==rank(stable,p),(p,A,rank(H,p),rank(stable,p),expected)
        vals=[evalpoly(A,Q,p) for Q in polys]
        direct=(((-1)**dd[2])*vals[0]**2*vals[1]**2*vals[2])%p
        assert determinant(H,p)==direct,(p,A,'determinant',determinant(H,p),direct)
    return polys


def main():
    primes=[p for p in range(5,200) if isprime(p)]
    for p in primes:verify(p)
    for p,target in [(13,[0,0,0]),(19,[0,1,0])]:
        P=verify(p)
        g=[len(gcd(P[0],P[1],p))-1,len(gcd(P[0],P[2],p))-1,len(gcd(P[1],P[2],p))-1]
        assert g==target,(p,g)
        print('EXACT_OVERLAPS',p,'degrees=',degrees(p),'pairwise_gcd_degrees=',g)
    print('VERIFY_OK',len(primes),'prime characteristics and all smooth prime-field parameters')

if __name__=='__main__':main()
