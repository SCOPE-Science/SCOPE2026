"""Checks for Gaussian-tree edge-crossing versus squared-amplitude covariance.

The all-tree theorem is proved analytically in RESULT.md.  These checks are
finite, reproducible corroborations, not a replacement for that proof.
Standard Python library only; run with `python3 verify.py`.
"""
from fractions import Fraction as F
from math import acos, erf, exp, pi, sqrt
import random

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

# Exact rational algebra for the three-variable Gaussian identity.
rs = [F(-4,5), F(-3,5), F(-1,3), F(0), F(1,4), F(2,3), F(4,5)]
bs = [F(-3,4), F(-1,2), F(0), F(1,3), F(2,3)]
for r in rs:
    for a in bs:
        for b in bs:
            alpha = (a-r*b)/(1-r*r)
            beta = (b-r*a)/(1-r*r)
            left = -(1-r*r)*(r*(alpha*alpha+beta*beta)+2*alpha*beta)
            right = r*(a*a+b*b)-2*a*b
            check(left == right, 'Gaussian-regression algebra')

# Independent numerical conditional-normal integration of the fundamental
# sign-change/squared-coordinate moments.
def integrate_simpson(f, hi=10.0, steps=12000):
    h = hi / steps
    accum = f(0.0)+f(hi)
    for j in range(1, steps):
        accum += (4 if j % 2 else 2)*f(j*h)
    return accum*h/3

def phi(x):
    return exp(-x*x/2)/sqrt(2*pi)

def Phi(x):
    return (1+erf(x/sqrt(2)))/2

for r in [-.9,-.7,-.35,-.1,0,.1,.35,.7,.9]:
    a = r/sqrt(1-r*r)
    p = integrate_simpson(lambda x: 2*phi(x)*Phi(-a*x))
    cross_second = integrate_simpson(lambda x: 2*x*x*phi(x)*Phi(-a*x))
    check(abs(p-acos(r)/pi)<2e-9, 'Gaussian sign probability integration')
    check(abs(cross_second-(acos(r)-r*sqrt(1-r*r))/pi)<2e-9,
          'Gaussian sign-square moment integration')

# Exact rational positive-correlation counterexample outside a Markov path.
r,a,b=F(1,2),F(4,5),F(1,10)
determinant=1+2*r*a*b-r*r-a*a-b*b
numerator=r*(a*a+b*b)-2*a*b
check(determinant==F(9,50) and numerator==F(33,200), 'non-tree sign boundary')

# Two independently organized sums for homogeneous Gaussian chains.
for r in rs:
    for n in range(2,26):
        direct = sum(r**(2*min(abs(t-s),abs(t-s-1)))
                     for s in range(1,n) for t in range(1,n+1))
        collapsed = 2*sum((n-1-h)*r**(2*h) for h in range(n-1))
        check(direct==collapsed, 'Gaussian-chain geometric collapse')

# Tree path-product verification in a non-path branching example.
parents=[-1,0,0,1,1,2,5]
edge_corr=[None,F(1,2),F(-2,5),F(3,5),F(-3,4),F(1,3),F(2,3)]
ancestors=[]
for v in range(len(parents)):
    a=[v]
    while parents[a[-1]]>=0:a.append(parents[a[-1]])
    ancestors.append(a)

def path_edges(u,v):
    common=next(z for z in ancestors[u] if z in ancestors[v])
    out=[]
    for z in ancestors[u]:
        if z==common:break
        out.append(z)
    for z in ancestors[v]:
        if z==common:break
        out.append(z)
    return out

def covariance(u,v):
    prod=F(1)
    for z in path_edges(u,v):prod*=edge_corr[z]
    return prod

for child in range(1,len(parents)):
    parent=parents[child];r=edge_corr[child]
    for vertex in range(len(parents)):
        # Choose the endpoint of this edge closest in the tree to vertex.
        du=len(path_edges(vertex,parent));dv=len(path_edges(vertex,child))
        endpoint=parent if du<dv else child
        eta=covariance(vertex,endpoint)
        a=covariance(vertex,parent);b=covariance(vertex,child)
        numerator=r*(a*a+b*b)-2*a*b
        check(numerator==-r*(1-r*r)*eta*eta, 'tree Markov path identity')

# Seeded independent simulation of one representative Gaussian tree.
# Uses a simple generation recurrence, never the analytical covariance formula.
seed=10273117
rng=random.Random(seed)
N=250000
means_i=[0.0]*(len(parents)-1)
means_q=[0.0]*len(parents)
cross=[[0.0]*len(parents) for _ in range(len(parents)-1)]
cross2=[[0.0]*len(parents) for _ in range(len(parents)-1)]
for _ in range(N):
    x=[0.0]*len(parents)
    x[0]=rng.gauss(0,1)
    for child in range(1,len(parents)):
        r=float(edge_corr[child]);x[child]=r*x[parents[child]]+sqrt(1-r*r)*rng.gauss(0,1)
    i=[float(x[parents[c]]*x[c]<0) for c in range(1,len(parents))]
    q=[v*v for v in x]
    for e in range(len(i)):
        means_i[e]+=i[e]
        for v in range(len(q)):
            p=i[e]*q[v];cross[e][v]+=p;cross2[e][v]+=p*p
    for v in range(len(q)):means_q[v]+=q[v]
for e in range(len(parents)-1):
    child=e+1;r=float(edge_corr[child])
    for v in range(len(parents)):
        du=len(path_edges(v,parents[child]));dv=len(path_edges(v,child))
        nearest=parents[child] if du<dv else child
        eta=float(covariance(v,nearest))
        expected=-r*sqrt(1-r*r)*eta*eta/pi
        actual=cross[e][v]/N-(means_i[e]/N)*(means_q[v]/N)
        # Conservative empirical tolerance for a diagnostic, not certification.
        sd=sqrt(max(0.0,cross2[e][v]/N-(cross[e][v]/N)**2))/sqrt(N)
        check(abs(actual-expected) < 9*sd + .009, 'tree simulation cross-covariance')

print(f'PASS: {checks} finite checks (exact rational, Gaussian quadrature, branching tree, seeded simulation).')
