"""Reproduce algebraic and numerical checks for priced one-way three-state cycles.

Run: python check.py (Python >=3.9; requires numpy and sympy).
Numerical sampling is not used to certify the global theorem.
"""
from fractions import Fraction
import itertools
import math
import random
import numpy as np
import sympy as sp


def rate_gap(rate):
    s = sum(rate)
    t = rate[0]*rate[1]+rate[1]*rate[2]+rate[2]*rate[0]
    return (s - math.sqrt(max(s*s-4*t, 0.0))) / 2.0


def optimal_gap(price, budget=1.0):
    a,b,c = price
    d=math.sqrt(max(a*a+b*b+c*c-a*b-a*c-b*c,0))
    return 3*budget/(2*(a+b+c-d))


def allocation(price,budget=1.0):
    idx=sorted(range(3),key=lambda i:price[i])
    a,b,c=[price[i] for i in idx]
    if abs(a-b)<1e-13:
        if abs(b-c)<1e-13:
            ans=[budget/(3*a)]*3
        else:
            ans=[budget/(2*a),budget/(2*a),0.0]
        return [ans[idx.index(i)] for i in range(3)]
    lam=2*optimal_gap([a,b,c])
    r=(lam*(a+b)-2)/(1-lam*a)
    scale=math.sqrt(budget/(a*(1+r)**2+b+c*r*r))
    vals=[(scale*(1+r))**2,scale**2,(scale*r)**2]
    return [vals[idx.index(i)] for i in range(3)]


def run():
    counter=0
    cases=[(1,1,1),(1,1,2),(2,2,5),(1,2,2),(1,2,3),(1,3,5),
           (0.01,1,1),(0.5,1,1),(3,1,2),(20,3,1),(0.2,0.21,5)]
    gen=random.Random(100629)
    for _ in range(400):
        cases.append(tuple(math.exp(gen.uniform(-5,5)) for _ in range(3)))
    for price in cases:
        budget=gen.uniform(.5,5)
        x=allocation(price,budget)
        assert min(x)>=-1e-10
        assert abs(sum(p*r for p,r in zip(price,x))-budget)<2e-9*budget
        assert abs(sum(x)/2-optimal_gap(price,budget))<2e-9*max(1,budget)
        delta=sum(x)**2-4*(x[0]*x[1]+x[1]*x[2]+x[2]*x[0])
        assert delta<1e-9*max(1,sum(x)**2)
        if max(price)-min(price)>1e-12:
            assert abs(delta)<1e-9*max(1,sum(x)**2)
        counter+=3
        for _ in range(120):
            z=np.array([gen.expovariate(1) for _ in range(3)])
            z=z*budget/np.dot(z,price)
            assert rate_gap(z) <= optimal_gap(price,budget)+2e-10*max(1,budget)
            counter+=1
    # Exact generalized-eigenvalue certificate for a finite grid of rational prices.
    a,b,c,L=sp.symbols('a b c L')
    P=sp.Matrix([[a+b,a],[a,a+c]])
    H=sp.Matrix([[2,1],[1,2]])
    assert sp.simplify((H-L*P).det() - ((a*b+a*c+b*c)*L**2-2*(a+b+c)*L+3)) == 0
    counter+=1
    for x,y,z in itertools.product(range(1,8),repeat=3):
        ps=sorted([sp.Rational(x),sp.Rational(y),sp.Rational(z)])
        s=sum(ps); d=sp.sqrt(sum(t*t for t in ps)-sum(ps[i]*ps[j] for i in range(3) for j in range(i+1,3)))
        lm=sp.simplify(3/(s-d))
        assert sp.simplify((H-L*P).det().subs({a:ps[0],b:ps[1],c:ps[2],L:lm}))==0
        counter+=1
    # Direct eigenvalue replay for rational and random positive rate triples.
    for _ in range(3000):
        x,y,z=(gen.uniform(.001,3) for _ in range(3))
        Q=np.array([[-x,x,0],[0,-y,y],[z,0,-z]])
        roots=sorted(np.linalg.eigvals(Q),key=lambda t:abs(t))
        computed=-max(roots[1].real,roots[2].real)
        assert abs(computed-rate_gap([x,y,z])) < 2e-10
        counter+=1
    # Budget-one equal-price sample triangles have constant optimum 1/2.
    for _ in range(500):
        u,v,w=(gen.uniform(.1,1) for _ in range(3))
        # Create a triangle from edge-length coordinates.
        u=v+w if _%3==0 else min(u,v+w)
        # Enforce the remaining two triangle inequalities.
        if v>u+w or w>u+v:
            continue
        total=u*u+v*v+w*w
        assert abs(sum([u*u/total,v*v/total,w*w/total])/2-.5)<1e-12
        assert abs(rate_gap([u*u/total,v*v/total,w*w/total])-.5)<2e-7
        counter+=1
    print('PASS',counter,'assertion checks')
if __name__ == '__main__':run()
