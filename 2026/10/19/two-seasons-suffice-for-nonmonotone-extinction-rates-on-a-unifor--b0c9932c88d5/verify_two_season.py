#!/usr/bin/env python3
"""Exact rational certificate for two-season directed-cycle Floquet inequalities.
Requires only the Python 3 standard library.
"""
from fractions import Fraction as F
from math import factorial

N = 80
A = [[11,0,0,6],[6,10,0,0],[0,6,12,0],[0,0,6,2]]
B = [[8,0,0,6],[6,0,0,0],[0,6,7,0],[0,0,6,9]]
I = [[F(int(i==j)) for j in range(4)] for i in range(4)]
J = [[F(1) for _ in range(4)] for _ in range(4)]
def matmul(X,Y):
    return [[sum((X[i][k]*Y[k][j] for k in range(4)),F(0)) for j in range(4)] for i in range(4)]
def plus(X,Y):
    return [[X[i][j]+Y[i][j] for j in range(4)] for i in range(4)]
def scale(X,c):
    return [[c*X[i][j] for j in range(4)] for i in range(4)]
def mv(X,v):
    return [sum((X[i][j]*v[j] for j in range(4)),F(0)) for i in range(4)]
def exp_bounds(G,h):
    X=scale(G,h)
    r=max(sum(row) for row in X)
    assert r<N+2
    P=I
    term=I
    for k in range(1,N+1):
        term=scale(matmul(term,X),F(1,k))
        P=plus(P,term)
    eps=r**(N+1)/factorial(N+1)/(1-r/F(N+2))
    return P,plus(P,scale(J,eps))
def collatz(T,q):
    h=T/2
    LA,UA=exp_bounds(A,h)
    LB,UB=exp_bounds(B,h)
    lower=matmul(LB,LA)
    upper=matmul(UB,UA)
    return min(z/F(v) for z,v in zip(mv(lower,q),q)), max(z/F(v) for z,v in zip(mv(upper,q),q))

T0=F(2,5);T1=F(8,5);T2=F(16,5)
lo0,hi0=collatz(T0,[31163,14916,23238,30684])
lo1,hi1=collatz(T1,[36440,17177,17764,28619])
lo2,hi2=collatz(T2,[36320,17105,17882,28692])
assert hi0 < 263, 'Small-period upper bound failed'
assert lo1 > 7500000000, 'Medium-period lower bound failed'
assert hi2 < 55000000000000000000, 'Large-period upper bound failed'
assert F(7500000000) > F(263)**4
assert F(7500000000)**2 > F(55000000000000000000)
# Prove that all three displayed population growth exponents are strictly negative.
for T,hi,threshold in [
    (T0,hi0,F(263)),
    (T1,hi1,F(8000000000)),
    (T2,hi2,F(55000000000000000000)),
]:
    assert hi < threshold
    assert sum(((16*T)**k/F(factorial(k)) for k in range(81)),F(0)) > threshold
print('CERTIFIED exact rational matrix-exponential and Perron inequalities')
for name,lo,hi in [('T=2/5',lo0,hi0),('T=8/5',lo1,hi1),('T=16/5',lo2,hi2)]:
    print(name,'spectral enclosure approximate',f'{float(lo):.9g}',f'{float(hi):.9g}')
print('rho(H(2/5))<263, rho(H(8/5))>7500000000, rho(H(16/5))<55000000000000000000')
print('Hence lambda(2/5)<lambda(8/5)>lambda(16/5), and all three exponents are negative.')
