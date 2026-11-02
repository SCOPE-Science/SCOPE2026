#!/usr/bin/env python3
"""Finite exact tests of adjacency-graph identities; no infinite certification."""
from fractions import Fraction
from itertools import product
from math import factorial, gamma, isclose, pi

CHECKS=0

def check(condition, explanation):
    global CHECKS
    assert condition, explanation
    CHECKS += 1

def counts(word):
    arcs={(a,b) for a,b in zip(word,word[1:]) if a!=b}
    edges={tuple(sorted(e)) for e in arcs}
    mutual=sum((a,b) in arcs and (b,a) in arcs for a,b in edges)
    single=sum(((a,b) in arcs)+((b,a) in arcs)==1 for a,b in edges)
    return len(arcs),len(edges),mutual,single

def no_ordered(n,a,b):
    f=[Fraction(1),Fraction(1)]
    for j in range(2,n+1):
        f.append(f[-1]-a*b*f[-2])
    return f[n]

def no_unordered(n,a,b):
    if n<=1: return Fraction(1)
    x,y,z=a,b,1-a-b
    for _ in range(1,n):
        x,y,z=a*(x+z),b*(y+z),(1-a-b)*(x+y+z)
    return x+y+z

def exact_expected(n,probs):
    val=[Fraction(0)]*4
    for word in product(range(len(probs)),repeat=n):
        weight=Fraction(1)
        for a in word: weight*=probs[a]
        v=counts(word)
        for j in range(4): val[j]+=weight*v[j]
        check(v[0]==2*v[2]+v[3] and v[1]==v[2]+v[3], 'combinatorial identities')
    return val

def automata_expected(n,probs):
    D=sum((1-no_ordered(n,a,b) for i,a in enumerate(probs) for j,b in enumerate(probs) if i!=j),Fraction(0))
    U=sum((1-no_unordered(n,a,b) for i,a in enumerate(probs) for j,b in enumerate(probs) if i<j),Fraction(0))
    return [D,U,D-U,2*U-D]

for probs in [tuple(map(Fraction,[Fraction(1,2),Fraction(1,3),Fraction(1,6)])),
              (Fraction(1,2),Fraction(1,2)),
              (Fraction(1,4),Fraction(1,4),Fraction(1,2))]:
    for n in range(1,8):
        actual=exact_expected(n,probs)
        pred=automata_expected(n,probs)
        for a,b in zip(actual,pred):check(a==b,('pattern automata',n,probs,a,b))

for N in range(1,120):
    number_divisors=sum(N%i==0 for i in range(1,N+1))
    number_factorizations=sum(i*j==N for i in range(1,N+1) for j in range(1,N//i+1))
    check(number_divisors==number_factorizations,'Dirichlet divisor representation')

for s in (1.4,1.7,2.0,2.5,3.0):
    g=1/s
    for a in (.5,1.0,2.0):
        # Logarithmic quadrature, whose truncation is small for s>1.
        from math import exp, expm1
        N=20000
        left,right=-30.0,40.0
        dt=(right-left)/N
        integral=0.0
        for j in range(N):
            t=left+(j+.5)*dt
            u=exp(t)
            integral+=-expm1(-a*u**(-s))*u*dt
        exact=a**g*gamma(1-g)
        check(abs(integral-exact)<1.e-4,('integral numerical check',s,a,integral,exact))

print(f'PASS {CHECKS} finite exact and supplementary numerical assertions')
