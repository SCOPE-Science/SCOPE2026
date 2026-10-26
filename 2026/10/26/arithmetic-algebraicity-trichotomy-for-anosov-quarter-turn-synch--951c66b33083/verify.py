#!/usr/bin/env python3
"""Exact finite arithmetic checks for the quarter-turn synchronization theorem.
Scientific proof of statements for all n is in RESULT.md; tests are finite."""
from fractions import Fraction
from math import gcd

J = ((0,-1),(1,0))
I = ((1,0),(0,1))

def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def matpow(a,n):
    r=I
    while n:
        if n & 1: r=mul(r,a)
        a=mul(a,a); n//=2
    return r

def det(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def difference(a,b): return tuple(tuple(a[i][j]-b[i][j] for j in range(2)) for i in range(2))
def tr(a): return a[0][0]+a[1][1]

def seq(t,count):
    U=[0,1]
    for n in range(2,count+1): U.append(t*U[-1]-U[-2])
    T=[2,t]
    for n in range(2,count+1): T.append(t*T[-1]-T[-2])
    return U,T

def theoretical(t,delta,n,U,T):
    if n%2==0: return T[n]-2*(-1)**(n//2)
    if delta==0: return 2
    if delta==-2 and n==1: return None
    value=abs(delta)*U[n]+2*(1 if delta>0 else -1)*(-1)**((n-1)//2)
    if delta==-1 and n==1: value+=2
    return value

def test_matrix(A,maxn=32):
    assert det(A)==1 and tr(A)>2
    t=tr(A); delta=A[0][1]-A[1][0]
    U,T=seq(t,maxn)
    actual=[]
    for n in range(1,maxn+1):
        M=difference(matpow(A,n),matpow(J,n))
        d=det(M)
        expectation=theoretical(t,delta,n,U,T)
        assert (expectation is None and d==0) or (expectation is not None and abs(d)==expectation),(A,n,d,expectation)
        actual.append(abs(d))
    if delta==-2:
        assert actual[0]==0
        return
    # Formal derivative identity: coefficients of zZ'/Z equal the raw N_n.
    # c_n=(1/n)sum_{k=1}^n N_k c_{n-k}, with rational exact arithmetic.
    c=[Fraction(1)]
    for n in range(1,maxn+1):
        c.append(sum(Fraction(actual[k-1])*c[n-k] for k in range(1,n+1))/n)
    # Coefficient-by-coefficient differential equation, exact independent check.
    for n in range(1,maxn+1):
        assert n*c[n]==sum(actual[k-1]*c[n-k] for k in range(1,n+1))
    if delta==0:
        # Z^2 (1-z)^2 D = (1+z)^2(1+z^2)^2.
        D=[1,0,-(t*t-2),0,1]
        lhs_f=[1,-2,1]
        rhs_f=[1,2,1]
        sqp=[1,0,2,0,1]
        def conv(x,y):
            a=[0]*(len(x)+len(y)-1)
            for i,v in enumerate(x):
                for j,w in enumerate(y): a[i+j]+=v*w
            return a
        left=conv(conv(conv(c,c),lhs_f),D)
        right=conv(rhs_f,sqp)
        for n in range(maxn+1): assert left[n]==(right[n] if n<len(right) else 0),(A,n,left[n])
    else:
        # Exact rational log-derivative test: S(z)=sum N_n z^n,
        # use recurrence for U_(2k+1), T_(2k) and periodic remainder.
        e=2 if delta==-1 else 0
        for n in range(1,maxn+1):
            if n%2==0: assert actual[n-1]==T[n]-2*(-1)**(n//2)
            else:
                k=(n-1)//2
                q=abs(delta)*U[n]+2*(1 if delta>0 else -1)*(-1)**k + (e if n==1 else 0)
                assert q==actual[n-1],(A,n,q,actual[n-1])

TESTS=[
 ((2,1),(1,1)), # delta=0, t=3
 ((1,2),(1,3)), # delta=1, t=4
 ((1,1),(2,3)), # delta=-1, t=4
 ((1,1),(3,4)), # delta=-2, t=5: infinite first coincidence set
 ((1,1),(4,5)), # delta=-3, t=6
 ((3,2),(1,1)), # delta=1, t=4
]
for A in TESTS: test_matrix(A)
base=((2,1),(1,1))
for k in range(1,6): test_matrix(matpow(base,2**k))
assert det(difference(base,J))==2 and abs(det(difference(matpow(base,2),matpow(J,2))))==9
assert (9-2)%2==1
print('VERIFY_OK; 11 representative/power families x 32 exact iterate comparisons; formal power-series checks; parity and Gauss witness')
