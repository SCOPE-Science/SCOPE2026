"""Reproduce finite Gaussian-conditioning and interpolation identities.

Uses exact rational sympy arithmetic. Finite tests supplement the analytical
proof; they do not certify the infinite-dimensional convergence statement.
"""
from fractions import Fraction
from itertools import combinations
import math
import random
import sympy as sp

checks = 0

def test(condition, description):
    global checks
    assert condition, description
    checks += 1

def blocks(n, edges):
    endpoints = [0] + [i for i in range(1,n) if i not in edges] + [n]
    return [(endpoints[j], endpoints[j+1]) for j in range(len(endpoints)-1)]

def interp_weights(t, n, endpoints):
    u = sp.Rational(t)
    for k in range(len(endpoints)-1):
        a, b = sp.Rational(endpoints[k],n), sp.Rational(endpoints[k+1],n)
        if a <= u <= b:
            if a == b: continue
            v=(u-a)/(b-a)
            return {a:1-v,b:v}
    raise AssertionError('not covered')

def interp_cov(s,t,n,endpoints):
    ws = interp_weights(s,n,endpoints)
    wt = interp_weights(t,n,endpoints)
    return sum(a*b*min(x,y) for x,a in ws.items() for y,b in wt.items())

def bridge_cov(s,t,n):
    s,t=sp.Rational(s),sp.Rational(t)
    for k in range(n):
        a,b=sp.Rational(k,n),sp.Rational(k+1,n)
        if a<=s<=b and a<=t<=b:
            return min(s,t)-a-(s-a)*(t-a)/(b-a)
    return sp.Rational(0)

def via_projection(s,t,n,edges):
    # Conditioning observations L_i = W_{(i+1)/n}-2W_{i/n}+W_{(i-1)/n}.
    s,t=sp.Rational(s),sp.Rational(t)
    def observation_cov(x,i):
        a,b,c=[sp.Rational(v,n) for v in (i-1,i,i+1)]
        return min(x,c)-2*min(x,b)+min(x,a)
    if not edges:return min(s,t)
    I=sorted(edges)
    v=sp.Matrix([observation_cov(s,i) for i in I])
    w=sp.Matrix([observation_cov(t,i) for i in I])
    m=sp.Matrix([[observation_cov(sp.Rational(j+1,n),i)-2*observation_cov(sp.Rational(j,n),i)+observation_cov(sp.Rational(j-1,n),i) for j in I] for i in I])
    return sp.factor(min(s,t)-(v.T*m.inv()*w)[0])

for n in range(2,9):
    # Full enumeration of all observation edge subsets for these finite n.
    for mask in range(1<<(n-1)):
        edges={i+1 for i in range(n-1) if mask&(1<<i)}
        pieces=blocks(n,edges)
        ep=[0]+[b for _,b in pieces]
        test(pieces[0][0]==0 and pieces[-1][1]==n and all(pieces[k][1]==pieces[k+1][0] for k in range(len(pieces)-1)),'partition')
        test(len(ep)==n-len(edges)+1,'rank of constraints')
        for x in range(n+1):
            for y in range(n+1):
                t,s=sp.Rational(x,n),sp.Rational(y,n)
                actual=via_projection(s,t,n,edges) if n<=5 else None
                proposed=interp_cov(s,t,n,ep)
                if actual is not None:
                    test(actual==proposed, 'node Schur complement mismatch')
                if edges==set():
                    test(proposed==min(s,t),'no constraints')
                if len(edges)==n-1:
                    test(proposed==s*t,'all constraints')

# Direct continuous-time Schur complement at half-grid points, including bridge residual.
for n in range(2,7):
    for mask in range(1<<(n-1)):
        edges={i+1 for i in range(n-1) if mask&(1<<i)}
        ep=[0]+[b for _,b in blocks(n,edges)]
        for i in range(2*n+1):
            for j in range(i,2*n+1):
                s,t=sp.Rational(i,2*n),sp.Rational(j,2*n)
                actual=via_projection(s,t,n,edges)
                expected=interp_cov(s,t,n,ep)+bridge_cov(s,t,n)
                test(actual==expected,'continuous-time Schur complement mismatch')

# Closed-set examples: midpoint covariance on a fixed macroscopic gap.
for a,b in [(sp.Rational(0),sp.Rational(1)),(sp.Rational(1,4),sp.Rational(3,4)),(sp.Rational(1,3),sp.Rational(2,3))]:
    m=(a+b)/2
    q=(m-a)*(b-m)/(b-a)  # Brownian bridge midpoint variance
    test(q==sp.Rational(b-a,4),'mid-gap conditional variance removal')

# Deterministic exact controls: full constraints collapse to tB1; no constraints gives Wiener.
for n in [3,5,12]:
    e=set(range(1,n))
    ep=[0,n]
    for i in range(n+1):
        test(interp_cov(sp.Rational(i,n),sp.Rational(i,n),n,ep)==sp.Rational(i*i,n*n),'rank-one limit')

print('PASS: %d exact assertions; node Schur complements and off-grid Brownian bridge decomposition.'%checks)
