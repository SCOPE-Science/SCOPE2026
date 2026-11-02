#!/usr/bin/env python3
"""Exact polynomial identity and sample arithmetic checks for fifth-layer m-ary partitions.

Uses only Python's standard library. The all-integer conclusion is proved in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial

def trim(v):
    v=list(v)
    while v and v[-1]==0: v.pop()
    return tuple(v)

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def scale(a,c): return trim([F(c)*x for x in a])
def neg(a): return scale(a,-1)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    if not a or not b: return ()
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return trim(z)

def prod(*items):
    v=(F(1),)
    for item in items: v=mul(v,item)
    return v

ONE=(F(1),); M=(F(0),F(1))
def varnum_factor(t):
    # n*m+t; polynomial in n with coefficients in Q[m]
    return {0:(F(t),),1:M}

def binom_mn(J):
    # P(n,m)=binom(m*n+J-1,J) as n-polynomial with m-polynomial coefficients
    z={0:ONE}
    for t in range(J):
        w={}
        for i,c in z.items():
            w[i]=add(w.get(i,()),scale(c,t))
            w[i+1]=add(w.get(i+1,()),mul(c,M))
        z=w
    return {i:scale(p,F(1,factorial(J))) for i,p in z.items()}

def shifted_binomial(i):
    # Coefficients of binom(n+i-1,i) as a polynomial in n
    z=[F(1)]
    for t in range(i):
        w=[F(0)]*(len(z)+1)
        for j,c in enumerate(z): w[j]+=t*c;w[j+1]+=c
        z=w
    return [x/factorial(i) for x in z]

def transformed_h(J):
    z=binom_mn(J)
    a={}
    for i in range(J,0,-1):
        leading=z.get(i,())
        ci=scale(leading,factorial(i))
        a[i]=ci
        B=shifted_binomial(i)
        for j,b in enumerate(B): z[j]=sub(z.get(j,()),scale(ci,b))
    assert all(not p for p in z.values()),('polynomial remainder',z)
    return a

a={0:ONE}
for level in range(1,5):
    b={}
    for j,coefficient in a.items():
        for i,alpha in transformed_h(j+1).items():
            b[i]=add(b.get(i,()),mul(coefficient,alpha))
    a=b
    assert max(a)==level

# Exact coefficient polynomials in the basis h_j=q/(1-q)^(j+1).
claim={
 1:scale(prod(M, M, M, M,sub(M,ONE),add(M,ONE),add(sub(sub(prod(M,M,M,M),scale(prod(M,M,M),2)),M),scale(ONE,3))),F(-1,24)),
 2:scale(prod(M,M,M,M,M,sub(M,ONE),add(add(add(add(scale(prod(M,M,M,M),7),prod(M,M,M)),scale(prod(M,M),-4)),scale(M,-7)),scale(ONE,-3))),F(1,12)),
 3:scale(prod(M,M,M,M,M,M,M,sub(M,ONE),add(add(scale(prod(M,M),3),scale(M,2)),ONE)),F(-1,2)),
 4:prod(M,M,M,M,M,M,M,M,M,M)
}
assert a==claim,(a,claim)

# Unimodular first-four-coefficient matrix: content in the h-basis is exact.
from itertools import permutations
from math import comb, gcd
matrix=[[comb(n+j-1,j) for j in range(1,5)] for n in range(1,5)]
D=0
for permutation in permutations(range(4)):
    inversions=sum(permutation[i]>permutation[j] for i in range(4) for j in range(i+1,4))
    term=(-1)**inversions
    for i,j in enumerate(permutation):term*=matrix[i][j]
    D+=term
assert D==1

def peval(poly,n): return sum(c*n**i for i,c in enumerate(poly))
def qmul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): z[i+j]+=u*v
    return z

c={j:peval(p,3) for j,p in a.items()}
assert c=={1:-729,2:21627,3:-74358,4:59049},c
# H4 numerator: q * sum_j c_j(1-q)^(4-j) / (1-q)^5.
pol=[0]*4
for j,v in c.items():
    t=[1]
    for k in range(4-j):t=qmul(t,[1,-1])
    for k,x in enumerate(t):pol[k]+=v*x
assert pol==[243*23,243*137,243*80,243*3],pol

def bary(m,end):
    b=[0]*(end+1);b[0]=1
    for n in range(1,end+1): b[n]=b[n-1]+(b[n//m] if n%m==0 else 0)
    return b

for p in [3,5,7,11]:
    D=p**5; B=bary(p,8*D)
    content=0
    for j in range(1,5):
        assert peval(a[j],p).denominator==1
        content=gcd(content,int(peval(a[j],p)))
    assert content==(243 if p==3 else p**4)
    for n in range(1,9):
        rhs=0
        for j in range(1,5):
            P=peval(a[j],p)
            assert P.denominator==1
            for k in range(1,n+1):
                from math import comb
                rhs+=int(P)*comb(k+j-1,j)*B[n-k]
        assert rhs==B[D*n-1],(p,n,rhs,B[D*n-1])
        if p==3:
            assert rhs%243==0
            if n==1:assert rhs//243==23
            if n==2:assert rhs//243==275
        else:
            assert rhs%(p**4)==0
            convolution=sum((n-k)*B[k] for k in range(n))
            assert (rhs//p**4 -pow(8,-1,p)*convolution)%p==0
            if n==1: assert rhs%(p**5)!=0
print('VERIFY_OK')
