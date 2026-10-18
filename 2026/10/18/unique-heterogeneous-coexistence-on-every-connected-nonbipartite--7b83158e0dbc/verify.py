"""Reproducible numerical and rational checks for odds-map uniqueness and graph boundaries.
Analytic assertions are proved in RESULT.md, not inferred from sampling.
Run with: python verify.py
"""
from fractions import Fraction as Q
import itertools
import math

COUNT=0

def check(v, desc):
    global COUNT
    assert v, desc
    COUNT+=1

def f(g,z):
    return g*z/(1+(g-1)*z)

def h(t,z):
    return t*z/(1+(t-1)*z)

def apply(W,g,x):
    return [f(g[i],sum(W[i][j]*x[j] for j in range(len(x)))) for i in range(len(x))]

# Explicit positive coexistence equilibrium: W=J/3, gamma=(3,1/2,1/2).
W=[[Q(1,3)]*3 for _ in range(3)]
g=[Q(3),Q(1,2),Q(1,2)]
x=[Q(3,5),Q(1,5),Q(1,5)]
for a,b in zip(apply(W,g,x),x):
    check(a==b,"exact coexistence fixed point")
check(sum(g,Q(0))/3==Q(4,3),"Perron radius at zero")
check(sum((1/a for a in g),Q(0))/3==Q(13,9),"Perron radius at one")

# Connected bipartite graph: reciprocal biases yield a whole continuum.
W2=[[Q(0),Q(1)],[Q(1),Q(0)]]
for b in [Q(1,9),Q(1,5),Q(1,2),Q(3,4),Q(8,9)]:
    z=[h(Q(2),b),b]
    for a,c in zip(apply(W2,[Q(2),Q(1,2)],z),z):
        check(a==c,"bipartite continuum")

# For any r>1, h_r is strictly concave: verify Jensen on a rational grid.
for r in [Q(5,4),Q(2),Q(9,2)]:
    for a,b in itertools.combinations([Q(j,11) for j in range(1,11)],2):
        midpoint=(a+b)/2
        check(h(r,midpoint)>(h(r,a)+h(r,b))/2,"strict Jensen")

# Order barriers on the exact fixed point. These are coordinatewise,
# and capture a crucial step in the deterministic convergence proof.
for r in [Q(1,10),Q(2,5),Q(3,4)]:
    z=[h(r,a) for a in x]
    check(all(p>=q for p,q in zip(apply(W,g,z),z)),"subsolution")
for r in [Q(5,4),Q(3),Q(10)]:
    z=[h(r,a) for a in x]
    check(all(p<=q for p,q in zip(apply(W,g,z),z)),"supersolution")

# From a deliberately asymmetric interior state, iterate both nonlinear
# synchronous and declining-gain expected maps to the known equilibrium.
for start in ([.05,.83,.42],[.99,.02,.01],[.2,.4,.6]):
    z=list(start)
    for _ in range(900):
        z=apply([[float(a) for a in row] for row in W],list(map(float,g)),z)
    check(max(abs(a-b) for a,b in zip(z,map(float,x)))<1e-9,"deterministic convergence")
    z=list(start)
    for step in range(1,17001):
        y=apply([[float(a) for a in row] for row in W],list(map(float,g)),z)
        z=[a+(b-a)/(step+1) for a,b in zip(z,y)]
    check(max(abs(a-b) for a,b in zip(z,map(float,x)))<.035,"diminishing-gain mean drift at finite horizon")
print(f"PASS: {COUNT} rational and numerical assertions")
