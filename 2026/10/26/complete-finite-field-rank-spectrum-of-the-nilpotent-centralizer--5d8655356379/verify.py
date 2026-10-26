#!/usr/bin/env python3
"""Independently enumerate nilpotent centralizers and compare rank polynomials.
Run: python3 verify.py . No external packages required.
"""
from collections import Counter
from itertools import product


def add(a,b,q):
    return (a^b) if q == 4 else (a+b)%q

def mul(a,b,q):
    if q!=4: return a*b%q
    z=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1): z^=1<<(i+j)
    if z&8: z^=0b1110  # x^3=x*(x^2+x+1)+x^2+x
    if z&4: z^=0b111   # x^2=x+1
    return z

def inverse(a,q):
    return next(x for x in range(1,q) if mul(x,a,q)==1)

def rank(M,q):
    A=[row[:] for row in M]; nr=len(A);nc=len(A[0]);r=0
    for col in range(nc):
        pivot=next((k for k in range(r,nr) if A[k][col]),None)
        if pivot is None:continue
        A[pivot],A[r]=A[r],A[pivot]
        z=inverse(A[r][col],q)
        for j in range(col,nc):A[r][j]=mul(A[r][j],z,q)
        for k in range(nr):
            if k!=r and A[k][col]:
                factor=A[k][col]
                for j in range(col,nc):
                    y=mul(factor,A[r][j],q)
                    A[k][j]=add(A[k][j],y,q) if q==4 else (A[k][j]-y)%q
        r+=1
        if r==nr:break
    return r

def mat(m,a,b,c,d):
    N=2*m-1;A=[[0]*N for _ in range(N)]
    # Domain: R/(t^m) ⊕ R/(t^(m-1)); multiplication by t on both.
    for j in range(m):
        for k,v in enumerate(a):
            if j+1+k<m:A[j+1+k][j]=v
        for k,v in enumerate(c):
            if j+k<m-1:A[m+j+k][j]=v
    for j in range(m-1):
        for k,v in enumerate(b):
            if j+1+k<m:A[j+1+k][m+j]=v
        for k,v in enumerate(d):
            if j+1+k<m-1:A[m+j+1+k][m+j]=v
    return A

def matrix_mult(A,B,q):
    n=len(A);C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    C[i][j]=add(C[i][j],mul(A[i][k],B[k][j],q),q)
    return C

def H(l,q):
    C=Counter({0:1})
    for r in range(1,l):C[r]=(q-1)*q**(r-1)
    return C

def shift_scale(P,shift,factor):
    return Counter({r+shift:c*factor for r,c in P.items()})

def poly_add(*args):
    v=Counter()
    for P in args:v.update(P)
    return v

def formulas(l,q):
    G=Counter({0:1})
    for k in range(1,l):
        G=poly_add(G,
            Counter({2*k:(q*q-1)*(q*q-q)*q**(4*(k-1))}),
            shift_scale(H(k,q),k,(q-1)*(q+1)**2*q**(3*(k-1))))
    F=poly_add(G,
        Counter({2*l:q*(q-1)**2*q**(4*(l-1))}),
        shift_scale(H(l,q),l,(2*q*q-q-1)*q**(3*(l-1))))
    return F

def check(m,q):
    h=m-1;counts=Counter();total=0
    J=[[0]*(2*m-1) for _ in range(2*m-1)]
    for j in range(m-1): J[j+1][j]=1
    for j in range(m-2): J[m+j+1][m+j]=1
    for coeffs in product(range(q),repeat=4*m-5):
        a=coeffs[:h]
        b=coeffs[h:2*h]
        c=coeffs[2*h:3*h]
        d=coeffs[3*h:]
        A=mat(m,a,b,c,d)
        r=rank(A,q);counts[r]+=1;total+=1
        assert (r==2*m-2)==bool(b[0] and c[0])
        if total<=5 or (m<=3 and q==2):
            assert matrix_mult(A,J,q)==matrix_mult(J,A,q)
            power=A
            for _ in range(2*m-1):power=matrix_mult(power,A,q)
            assert not any(any(row) for row in power)
    expected=formulas(h,q)
    assert counts==expected,(m,q,counts,expected)
    assert total==q**(4*m-5)
    assert counts[2*m-2]==(q-1)**2*q**(4*m-7)
    print('OK',m,q,total,sorted(counts.items()))

if __name__=='__main__':
    for m,q in [(2,2),(3,2),(4,2),(3,3),(2,4),(3,4)]:check(m,q)
    print('VERIFY_OK_CONSECUTIVE_JORDAN_RANK_SPECTRUM')
