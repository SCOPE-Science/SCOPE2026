"""Finite direct checks plus a finite-interpolation exact determinant proof.

Requires only Python 3 standard library. Run: python verify_prism.py
"""
from collections import Counter
from math import comb


def transition(a,b,c):
    return all(((b >> j)&1) == (((a >> j)&1)+((c >> j)&1)+((b >> (1-j))&1) == 2) for j in (0,1))


def raw_matrix(z):
    return [[z**b.bit_count() if b==j//4 and transition(a,b,j%4) else 0
             for j in range(16)] for a in range(4) for b in range(4)]


def determinant(A):
    A=[list(row) for row in A]
    n=len(A);sign=1;den=1
    for k in range(n-1):
        if not A[k][k]:
            pivot=next((i for i in range(k+1,n) if A[i][k]),None)
            if pivot is None:return 0
            A[k],A[pivot]=A[pivot],A[k];sign=-sign
        q=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*q-A[i][k]*A[k][j]
                assert numerator%den==0
                A[i][j]=numerator//den
            A[i][k]=0
        den=q
    return sign*A[-1][-1]


def formula(n):
    ans=Counter({0:1,n:2})
    for j in range(1,n//4+1):
        ans[4*j]+=n*comb(n-3*j,j)//(n-3*j)
    if n%4==0:ans[3*n//2]+=4
    return ans


def direct_count(n):
    ans=Counter()
    for bits in range(1<<(2*n)):
        good=True
        for i in range(n):
            for j in (0,1):
                v=2*i+j
                degree=((bits>>(2*((i-1)%n)+j))&1)+((bits>>(2*((i+1)%n)+j))&1)+((bits>>(2*i+1-j))&1)
                if ((bits>>v)&1)!=(degree==2):good=False;break
            if not good:break
        if good:ans[bits.bit_count()]+=1
    return ans


def run():
    # Complete finite-grid polynomial identity: det(I-tM(z)) has degree
    # at most 16 in t and 32 in z. Equality at 17 by 33 distinct grid
    # points is therefore a rigorous certificate of polynomial identity.
    checks=0
    for z in range(33):
        M=raw_matrix(z)
        for t in range(17):
            A=[[(int(i==j)-t*M[i][j]) for j in range(16)] for i in range(16)]
            lhs=determinant(A)
            rhs=(1-t*z)**2*(1-z**6*t**4)*(1-t-z**4*t**4)
            assert lhs==rhs,(z,t,lhs,rhs)
            checks+=1
    print('FORMAL_DETERMINANT_CERTIFICATE',checks,'evaluation points')
    profiles=0
    for n in range(3,10):
        observed=direct_count(n)
        assert observed==formula(n),(n,observed,formula(n))
        profiles+=(1<<(2*n))
    print('DIRECT_EQUILIBRIUM_CHECK',profiles,'profiles n=3..9')
    for n in (3,4,5,6,7,8,9,10,12,16,20):
        print('n',n,'producers polynomial',sorted(formula(n).items()),'total',sum(formula(n).values()))

if __name__=='__main__':run()
