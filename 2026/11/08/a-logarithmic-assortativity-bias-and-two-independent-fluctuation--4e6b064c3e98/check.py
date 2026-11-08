#!/usr/bin/env python3
"""Exact finite-state diagnostics for a two-community uniform-attachment model.

Uses Python standard library only; no asymptotic assertion is inferred from tests.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

checks=0

def eq(actual, expected, what=''):
    global checks
    checks += 1
    assert actual == expected, f'{what}: {actual} != {expected}'

def prob(q, N, S):
    A=(N+S)//2; B=(N-S)//2
    pa=q*B/((1-q)*A+q*B)
    pb=q*A/((1-q)*B+q*A)
    return pa,pb

def f(q, y):
    a=1-2*q
    return q*(1+a*y*y)/(1-a*a*y*y)

for q in [F(1,5),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(4,5)]:
    a=1-2*q
    b=2*q*(1-q)*a
    for N in range(2, 31):
        for A in range(1,N):
            S=2*A-N
            y=F(S,N)
            pa,pb=prob(q,N,S)
            eq((pa+pb)/2, f(q,y),'conditional mean')
            eq(f(q,y)-q, b*y*y/(1-a*a*y*y),'exact bias')
            eq((pa-pb)/2, -2*q*(1-q)*y/(1-a*a*y*y),'cross bracket')
            eq(pa, q*(1-y)/(1+a*y),'incoming A')
            eq(pb, q*(1+y)/(1-a*y),'incoming B')

# Distribution of the count of cross-community edges and A-minus-B balance.
for q in [F(1,4),F(1,2),F(3,4)]:
    a=1-2*q
    b=2*q*(1-q)*a
    states={(0,0):F(1)} # (S, C), initial two vertices opposite types
    expected_compensator=F(0)
    expected_T=F(0)
    for t in range(1,13):
        N=t+1 # pre-addition population 2+(t-1)
        total=sum(states.values(),F(0))
        eq(total,F(1),'total probability')
        pt=F(0)
        it=F(0)
        nxt={}
        for (S,C),mass in states.items():
            y=F(S,N)
            pa,pb=prob(q,N,S)
            pt+=mass*f(q,y)
            it+=mass*y*y/(1-a*a*y*y)
            for sgn,p in [(1,pa),(-1,pb)]:
                for cross in [0,1]:
                    prob_cross=p if cross else 1-p
                    key=(S+sgn,C+cross)
                    nxt[key]=nxt.get(key,F(0))+mass*F(1,2)*prob_cross
        expected_compensator+=pt
        expected_T+=it
        states=nxt
        meanC=sum((F(C)*v for (S,C),v in states.items()),F(0))
        eq(meanC, expected_compensator, 'Doob expectation exact')
        eq(meanC-F(t)*q, b*expected_T,'bias identity')

# Quadratic imbalance additive functional T_n for simple symmetric random walk.
for n in range(2,13):
    paths=[]
    for signs in product((-1,1),repeat=n-1):
        S=0; T=F(0)
        for j in range(n):
            T+=F(S*S,(j+2)**2)
            if j<n-1:S+=signs[j]
        paths.append(T)
    ET=sum(paths,F(0))/len(paths)
    VT=sum((z-ET)**2 for z in paths)/len(paths)
    expected=sum((F(j,(j+2)**2) for j in range(n)),F(0))
    var_formula=sum((F(2*j*(j-1),(j+2)**4) for j in range(n)),F(0))
    var_formula+=sum((F(4*i*(i-1),(i+2)**2*(j+2)**2) for i in range(n) for j in range(i+1,n)),F(0))
    eq(ET,expected,'quadratic functional expectation')
    eq(VT,var_formula,'quadratic functional covariance')

# Check the exact finite simple walk square covariance for many pairs.
for i in range(0,11):
    for j in range(i,12):
        vals=[]
        for signs in product((-1,1),repeat=j):
            S=0; Si=0
            for k,sgn in enumerate(signs,1):
                S+=sgn
                if k==i:Si=S
            if i==0:Si=0
            vals.append((Si*Si,S*S))
        avgxy=sum((F(x*y) for x,y in vals),F(0))/len(vals)
        ex=sum((F(x) for x,y in vals),F(0))/len(vals)
        ey=sum((F(y) for x,y in vals),F(0))/len(vals)
        eq(avgxy-ex*ey, F(2*i*(i-1)), 'simple walk square covariance')

print(f'PASS {checks} exact-rational assertions')
