"""Exact Fourier checks for rank-exponential kernels on finite-field matrix spaces.

Run with Python 3 and standard library only. The analytic theorem does not
rely on exhaustive finite-field computations.
"""
from fractions import Fraction
from math import prod


def qbinom(n,k,q):
    if not 0 <= k <= n: return 0
    num = prod(q**(n-i)-1 for i in range(k))
    den = prod(q**(k-i)-1 for i in range(k))
    return num // den


def coefficient(q,m,n,s,t):
    return sum(qbinom(n-s,j-s,q)*q**(m*(n-j))*t**(n-j)*
               prod(1-q**i*t for i in range(j))
               for j in range(s,n+1))


def binary_rank(encoded,m,n):
    basis = [0]*n
    rank = 0
    for row in range(m):
        x = (encoded >> (row*n)) & ((1<<n)-1)
        while x:
            pivot=x.bit_length()-1
            if basis[pivot]: x ^= basis[pivot]
            else:
                basis[pivot]=x
                rank+=1
                break
    return rank


def binary_fourier(q,m,n,B,t):
    assert q==2
    v=Fraction(0)
    for X in range(1<<(m*n)):
        sign = -1 if (B & X).bit_count()%2 else 1
        v+=sign*t**binary_rank(X,m,n)
    return v


def prime_rank(flat,m,n,p):
    a=[[flat[i*n+j]%p for j in range(n)] for i in range(m)]
    row=0
    for col in range(n):
        pivot=next((i for i in range(row,m) if a[i][col]),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        inv=pow(a[row][col],-1,p)
        a[row]=[(x*inv)%p for x in a[row]]
        for i in range(m):
            if i!=row:
                d=a[i][col]
                a[i]=[(u-d*v)%p for u,v in zip(a[i],a[row])]
        row+=1
        if row==m:break
    return row


def ternary_fourier(m,n,B,t):
    assert m==n==2
    totals=[Fraction(0)]*3
    for code in range(3**(m*n)):
        X=[]; y=code
        for _ in range(m*n):
            X.append(y%3);y//=3
        phase=sum(b*x for b,x in zip(B,X))%3
        totals[phase]+=t**prime_rank(X,m,n,3)
    assert totals[1]==totals[2]
    return totals[0]-totals[1]


def verify():
    count=0
    for m,n in ((2,2),(3,2),(3,3)):
        for t in (Fraction(0),Fraction(1,8),Fraction(1,4),Fraction(1,2),Fraction(3,5),Fraction(1)):
            for B in range(1<<(m*n)):
                s=binary_rank(B,m,n)
                a=coefficient(2,m,n,s,t)
                b=binary_fourier(2,m,n,B,t)
                assert a==b, (m,n,s,t,a,b)
                count+=1
    for t in (Fraction(0),Fraction(1,5),Fraction(1,3),Fraction(2,3),Fraction(1)):
        for code in range(3**4):
            B=[];y=code
            for _ in range(4):B.append(y%3);y//=3
            a=coefficient(3,2,2,prime_rank(B,2,2,3),t)
            b=ternary_fourier(2,2,B,t)
            assert a==b,(t,B,a,b)
            count+=1
    assert coefficient(2,3,3,3,Fraction(3,10))<0
    assert coefficient(2,3,3,2,Fraction(3,5))<0
    assert coefficient(2,3,3,1,Fraction(1,2))>0
    assert coefficient(2,3,3,2,Fraction(1,2))==0
    for q in (2,3,4,5):
        for n in (2,3,4,5):
            m=n+1
            for k in range(n):
                t=Fraction(1,q**k)
                for s in range(n+1):
                    z=coefficient(q,m,n,s,t)
                    assert (z>0) == (s<=k), (q,m,n,s,k,z)
    print('PASS: exact binary and ternary character sums:',count)
    print('PASS: separated admissible points and forbidden intervals')
    print('PASS: boundary Fourier supports for four field sizes')

if __name__=='__main__': verify()
