"""Exact symbolic checks for the positive-fitness two-strategy d-player replicator-mutator theorem.

Usage: python scripts/check_threshold.py
Requires sympy (tested with >=1.12).
Finite checks support, but do not replace, the general analytic proof.
"""
from fractions import Fraction
from math import comb
from random import Random
import sympy as s

x=s.symbols('x', real=True)

def game_fitness(m, a, b):
    fa=s.expand(sum(s.Rational(a[k])*comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)))
    fb=s.expand(sum(s.Rational(b[k])*comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)))
    return fa,fb

def drift(m,q,a,b):
    fa,fb=game_fitness(m,a,b)
    direct=(1-q)*x*fa + q*(1-x)*fb-x*(x*fa+(1-x)*fb)
    factor=x*(1-q-x)*fa-(1-x)*(x-q)*fb
    assert s.simplify(direct-factor)==0
    return s.Poly(factor,x),fa,fb

# Check exact odds-ratio derivative and its lower bound polynomial identity.
q=s.symbols('q',positive=True)
G=(1-x)*(x-q)/(x*(1-q-x))
identity=s.cancel(x*(1-x)*s.diff(G,x)/G-q*((1-x)/(x-q)+x/(1-q-x)))
assert identity==0
z=s.symbols('z',real=True)
expr=s.factor((q*((1-x)/(x-q)+x/(1-q-x))-2*q/(1-2*q)).subs(x,z+s.Rational(1,2)))
assert s.simplify(expr- (4*q*z*z*(1-q)/( (1-2*q)*( (s.Rational(1,2)-q)**2-z*z) )))==0, expr
print('Symbolic drift factorization and odds derivative: PASS')

rng=Random(20261026)
checks=0
for m in range(1,7):
    qs=[s.Rational(m,2*(m+1)),(s.Rational(m,2*(m+1))+s.Rational(1,2))/2,s.Rational(1,2)]
    for q0 in qs:
        for rep in range(8):
            a=[rng.randrange(1,50) for _ in range(m+1)]
            b=[rng.randrange(1,50) for _ in range(m+1)]
            p,fa,fb=drift(m,q0,a,b)
            assert p.eval(0)>0 and p.eval(1)<0
            assert p.count_roots(0,1)==1, (m,q0,a,b,p)
            checks+=1
print(f'High-mutation exact Sturm root counts: PASS ({checks} games, m=1..6)')

for m in range(1,7):
    qstar=s.Rational(m,2*(m+1))
    q0=qstar*s.Rational(3,4)
    eps=s.Rational(1,100000)
    a=[eps]*m+[s.Integer(1)]
    b=[s.Integer(1)]+[eps]*m
    p,fa,fb=drift(m,q0,a,b)
    assert s.simplify(p.eval(s.Rational(1,2)))==0
    assert s.diff(p.as_expr(),x).subs(x,s.Rational(1,2))>0
    assert p.count_roots(0,1)==3, (m,q0,p)
    checks+=1
    print(f'd={m+1} below-threshold witness: q={q0}, eps={eps}, roots={p.count_roots(0,1)}')

# Exact explicit small example independent of numerical approximations.
m=2; q0=s.Rational(1,4); eps=s.Rational(1,100)
p,fa,fb=drift(m,q0,[eps,eps,1],[1,eps,eps])
print('d=3 exact positive-payoff witness:',s.factor(p.as_expr()))
assert p.count_roots(0,1)==3
print('All symbolic and rational checks passed.')
