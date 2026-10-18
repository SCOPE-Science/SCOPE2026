#!/usr/bin/env python3
"""Reproduce symbolic identities and independently evaluate finite noisy-leader designs."""
import sympy as sp

m, k = sp.symbols('m k', positive=True)

def reduced_trace(M, K, a):
    b = 3 - a
    SA=(M-a)/sp.Integer(3)+a/(3+K)
    SB=(3-b)/M+b/(M+K)
    TA=(M-a)/sp.Integer(9)+a/(3+K)**2
    TB=(3-b)/M**2+b/(M+K)**2
    return SA+SB+(SB*TA+SA*TB)/(1-SA*SB)

F=[sp.factor(reduced_trace(m,k,a)) for a in range(4)]
D01=(k*k*(m-7)-30*k-m*(m*m-m+6))/(3*(k+m)*((2*m+1)*k+9*m))
D03=-(m-3)*((m-6)*k*(k+m+3)+3*m*m)/(9*m*(k+3)*(k+m))
P=(6*k**3+k*k*(m**3-8*m*m+30*m+18)+k*(m**4-2*m**3-6*m*m+72*m)+3*m*m*(m*m-2*m+3))
D02=-2*P/(3*m*(k+3)*(k+m)*(k*m+4*k+9*m))
for lhs, rhs in [(F[0]-F[1],D01),(F[0]-F[2],D02),(F[0]-F[3],D03)]:
    assert sp.cancel(lhs-rhs)==0

# Each coefficient in P(m,k), after substituting m=y+3, is strictly positive.
y=sp.symbols('y',nonnegative=True)
for c in sp.Poly(P.subs(m,y+3),k).all_coeffs():
    assert all(v>=0 for v in sp.Poly(c,y).all_coeffs())

def exact_matrix_trace(M,K,a):
    n=M+3
    X=sp.zeros(n)
    for i in range(M):
        for j in range(M,n):
            X[i,i]+=1; X[j,j]+=1; X[i,j]-=1; X[j,i]-=1
    for v in list(range(a))+list(range(M,M+3-a)):
        X[v,v]+=K
    return sp.trace(X.inv())

samples=[sp.Rational(1,10),sp.Rational(1,2),sp.Integer(1),sp.Integer(2),sp.Integer(3),sp.Integer(5),sp.Integer(10),sp.Integer(20),sp.Integer(50),sp.Integer(200)]
checks=3+4
for M in range(3,13):
    for K in samples:
        vals=[sp.factor(reduced_trace(sp.Integer(M),K,a)) for a in range(4)]
        # Verify regime using algebraic threshold sign, no floating point.
        if M==3: expected={0,3}
        elif M in (4,5):
            Q=(M-6)*K*(K+M+3)+3*M*M
            expected=({0} if Q>0 else {3} if Q<0 else {0,3})
        elif M in (6,7): expected={0}
        else:
            N=(M-7)*K*K-30*K-M*(M*M-M+6)
            expected=({0} if N<0 else {1} if N>0 else {0,1})
        actual={i for i in range(4) if vals[i]==min(vals)}
        assert actual==expected,(M,K,actual,expected,vals)
        checks+=1
for M in range(3,9):
    for K in [sp.Rational(1,2),sp.Integer(2),sp.Integer(10)]:
        for a in range(4):
            assert sp.factor(exact_matrix_trace(M,K,a)-reduced_trace(sp.Integer(M),K,a))==0
            checks+=1
# Exact threshold tie at m=4,5 and m=8,10 tested algebraically without radicals.
for M in (4,5):
    X=sp.symbols('X',positive=True)
    q=(M-6)*X*(X+M+3)+3*M*M
    assert sp.rem(sp.together(F[0]-F[3]).as_numer_denom()[0].subs({m:M,k:X}),q,X)==0
    checks+=1
for M in (8,10):
    X=sp.symbols('X',positive=True)
    q=(M-7)*X*X-30*X-M*(M*M-M+6)
    assert sp.rem(sp.together(F[0]-F[1]).as_numer_denom()[0].subs({m:M,k:X}),q,X)==0
    checks+=1
print('PASS',checks,'exact symbolic and rational assertions')
