#!/usr/bin/env python3
"""Symbolic and numerical checks for a four-patch corridor-ranking theorem.
Dependencies: Python 3.10+, sympy, numpy. This checker corroborates, but does not replace, the written proof.
"""
from fractions import Fraction
import itertools
import math
import random
import sympy as sp
import numpy as np

x, a, b, c, alpha, beta, t = sp.symbols('x a b c alpha beta t', positive=True, real=True)
A = sp.Matrix([[0,a,t*alpha,0],[a,0,b,0],[t*alpha,b,0,c],[0,0,c,0]])
B = sp.Matrix([[0,a,0,0],[a,0,b,t*beta],[0,b,0,c],[0,t*beta,c,0]])
pa = x**4-(a*a+b*b+c*c+t*t*alpha*alpha)*x*x-2*a*b*alpha*t*x+a*a*c*c
pb = x**4-(a*a+b*b+c*c+t*t*beta*beta)*x*x-2*b*c*beta*t*x+a*a*c*c
checks=0
for mat, pol in ((A,pa),(B,pb)):
    cp=mat.charpoly()
    assert sp.expand(cp.as_expr().subs(cp.gen,x)-pol)==0
    checks+=1
assert sp.expand(pa-pb+t*x*((alpha*alpha-beta*beta)*t*x+2*b*(a*alpha-c*beta)))==0
checks+=1

# Independently evaluate the exact determinant at rational parameters, not using charpoly.
def determinant_four(M):
    ans=Fraction(0)
    for q in itertools.permutations(range(4)):
        inv=sum(q[i]>q[j] for i in range(4) for j in range(i+1,4))
        term=Fraction(-1 if inv%2 else 1)
        for i in range(4):term*=M[i][q[i]]
        ans+=term
    return ans

def mat_value(aa,bb,cc,al,be,tt,option):
    M=[[Fraction(0) for j in range(4)] for i in range(4)]
    edges=[(0,1,aa),(1,2,bb),(2,3,cc)]+([(0,2,al*tt)] if option=='A' else [(1,3,be*tt)])
    for i,j,z in edges:M[i][j]=M[j][i]=z
    return M

def p_eval(xx,aa,bb,cc,al,be,tt,option):
    w=(al if option=='A' else be)
    cross=aa if option=='A' else cc
    return xx**4-(aa**2+bb**2+cc**2+(tt*w)**2)*xx**2-2*bb*cross*w*tt*xx+aa**2*cc**2

def eigvals(aa,bb,cc,al,be,tt,option):
    M=mat_value(aa,bb,cc,al,be,tt,option)
    return np.linalg.eigvalsh(np.array(M,dtype=float))[-1]

rng=random.Random(1904)
for k in range(850):
    aa,bb,cc,al,be,tt=[Fraction(rng.randint(1,12),rng.randint(1,9)) for j in range(6)]
    xx=Fraction(rng.randint(1,30),rng.randint(1,14))
    for option in ('A','B'):
        M=mat_value(aa,bb,cc,al,be,tt,option)
        N=[[xx*(i==j)-M[i][j] for j in range(4)] for i in range(4)]
        assert determinant_four(N)==p_eval(xx,aa,bb,cc,al,be,tt,option)
        checks+=1
    ra=eigvals(aa,bb,cc,al,be,tt,'A');rb=eigvals(aa,bb,cc,al,be,tt,'B')
    predicted=(al**2-be**2)*tt*rb+2*bb*(aa*al-cc*be)
    if abs(predicted)>1e-8 and abs(ra-rb)>1e-8:
        assert (ra>rb)==(predicted>0)
        checks+=1

# Exact algebraic crossover example: a=b=1,c=3,alpha=2,beta=1.
u=(sp.Integer(66)-10*sp.sqrt(37))/123
T=sp.sqrt(u)
K=sp.Rational(2,3)
assert 0 < float(T) < 2/9
checks+=1
r=K/T
assert sp.simplify(pb.subs({a:1,b:1,c:3,alpha:2,beta:1,t:T,x:r}))==0
checks+=1
# At r>max(a,c)=3 this is the unique largest positive root by interlacing.
for tt,expected in [(sp.Rational(1,10),-1),(sp.Rational(1,2),1)]:
    ra=eigvals(Fraction(1),Fraction(1),Fraction(3),Fraction(2),Fraction(1),Fraction(tt),'A')
    rb=eigvals(Fraction(1),Fraction(1),Fraction(3),Fraction(2),Fraction(1),Fraction(tt),'B')
    assert (ra-rb)*expected>0
    checks+=1

# Signed parameter regimes including both directions of reversal and all-tie equality.
examples=[(1,1,3,2,1),(3,1,1,1,2),(2,1,1,3,2),(2,1,2,1,1),(1,2,1,1,1)]
for aa,bb,cc,al,be in examples:
    for tt in (Fraction(1,100),Fraction(1,5),Fraction(1),Fraction(7)):
        ra=eigvals(aa,bb,cc,al,be,tt,'A');rb=eigvals(aa,bb,cc,al,be,tt,'B')
        sign=(al*al-be*be)*tt*rb+2*bb*(aa*al-cc*be)
        if abs(float(sign))>1e-8:
            assert (ra>rb)==(sign>0)
            checks+=1
        else:
            assert abs(ra-rb)<1e-8
            checks+=1
print(f'PASS: {checks} symbolic, exact-rational, and numeric checks')
print('Example t* =',sp.N(T,16),'and common capacity =',sp.N(r,16))
