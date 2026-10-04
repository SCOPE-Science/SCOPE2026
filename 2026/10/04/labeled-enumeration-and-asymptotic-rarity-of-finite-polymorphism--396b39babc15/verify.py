#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import factorial, exp

N=10

def add(a,b):
    return [a[i]+b[i] for i in range(N+1)]

def mul(a,b):
    c=[Fraction(0) for _ in range(N+1)]
    for i,ai in enumerate(a):
        if not ai: continue
        for j,bj in enumerate(b[:N+1-i]):
            if bj: c[i+j]+=ai*bj
    return c

def exp_series(a):
    assert a[0]==0
    b=[Fraction(0) for _ in range(N+1)]
    b[0]=1
    for n in range(1,N+1):
        b[n]=sum(Fraction(k)*a[k]*b[n-k] for k in range(1,n+1))/n
    return b

def reciprocal_one_minus(d):
    assert d[0]==0
    q=[Fraction(0) for _ in range(N+1)]
    q[0]=1
    for n in range(1,N+1):
        q[n]=sum(d[k]*q[n-k] for k in range(1,n+1))
    return q

def shift_x(a):
    return [Fraction(0)]+a[:N]

z=[Fraction(0) for _ in range(N+1)]; z[1]=1
T=[z]
for h in range(1,N):
    e=exp_series(T[-1]); e[0]-=1
    T.append(shift_x(e))
P=[Fraction(1) for _ in range(N+1)]  # 1/(1-z)
H=P[:]
F={}
for h in range(1,N):
    D=shift_x(exp_series(T[h-1]))
    F[h]=reciprocal_one_minus(D)
    H=[H[i]+F[h][i]-P[i] for i in range(N+1)]

formula=[int(H[n]*factorial(n)) for n in range(1,N+1)]
expected=[1,4,27,232,2285,25716,324583,4571904,71321769,1225291780]
assert formula==expected, (formula, expected)

def source_height(f):
    n=len(f)
    indeg=[0]*n
    for y in f: indeg[y]+=1
    src=[i for i,d in enumerate(indeg) if d==0]
    if not src:
        return 0
    heights=[]
    for s in src:
        seen={}
        x=s; t=0
        while x not in seen:
            seen[x]=t
            x=f[x]; t+=1
        heights.append(seen[x])
    return heights[0] if len(set(heights))==1 else -1

brute=[]
by_height=[]
for n in range(1,8):
    c=0; bh={}
    for f in product(range(n), repeat=n):
        h=source_height(f)
        if h>=0:
            c+=1; bh[h]=bh.get(h,0)+1
    brute.append(c); by_height.append(bh)
assert brute==expected[:7], (brute,expected[:7])

# Match the height-stratified EGF against brute force.
for n,bh in enumerate(by_height, start=1):
    assert bh.get(0,0)==factorial(n)
    for h in range(1,n):
        coeff=int((F[h][n]-P[n])*factorial(n))
        assert coeff==bh.get(h,0), (n,h,coeff,bh.get(h,0))

# Numerical constants used only to check the explicit analytic inequalities in the proof.
r=0.58
b1=r*(exp(r)-1)
q=r*exp(b1)
assert b1<r and q<1
rho=0.5671432904097839
assert abs(rho*exp(rho)-1)<1e-15

print('FORMULA_COUNTS', formula)
print('BRUTE_COUNTS', brute)
print('HEIGHT_ROWS', by_height)
print('DOMINANCE_CHECK', {'r':r,'b1':b1,'q':q,'rho':rho})
print('VERIFY_OK')
