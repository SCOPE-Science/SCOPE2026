"""Symbolic identities and event-driven stochastic checks for the two-boundary finite-speed absorption allocation theorem.

Dependencies: Python 3, sympy.
Run: python check.py
"""
import math
import random
import sympy as sp

x, xi, ql, qr, Q, P = sp.symbols('x xi ql qr Q P', positive=True)
# Units: corridor [-1,1], speed one, velocity-flip rate xi.
cm, km = sp.symbols('cm km')
H1 = cm - x
S1 = km + xi*cm*2*x - xi*x*x

def boundary(S, H):
    return [sp.expand(ql*S.subs(x,-1)-(2-ql)*H.subs(x,-1)),
            sp.expand(qr*S.subs(x,1)+(2-qr)*H.subs(x,1))]

sol1 = sp.solve(boundary(S1,H1),(cm,km),simplify=False)
S1 = sp.factor(S1.subs(sol1))
H1 = sp.factor(H1.subs(sol1))
F = (P*(2*xi**2-3*xi+1)+Q*(3*xi-2)+4)/(Q+(2*xi-1)*P)
assert sp.factor(S1.subs(x,0)-F.subs({Q:ql+qr,P:ql*qr}))==0
assert sp.factor(sp.diff(F,P)-((1-2*xi)*(4-Q+2*Q*xi))/(Q+(2*xi-1)*P)**2)==0
assert sp.factor(F.subs(xi,sp.Rational(1,2))-(8-Q)/(2*Q))==0
# Original published telegraph first-passage formula: Angelani, arXiv:1601.04845, eq. (36).
# In his convention the reorientation rate alpha=2*xi and eps=q/(2-q).
el=ql/(2-ql); er=qr/(2-qr); alpha=2*xi
Tangel=sp.Rational(1,2)*(2*(2+el*er*alpha**2)+3*alpha*(el+er))/(el+er+2*el*er*alpha)
assert sp.factor(Tangel-S1.subs(x,0))==0
# Recursion for second raw moment: H2'=-2*S1, S2'=2*xi*H2-2*H1.
c2,k2=sp.symbols('c2 k2')
H2=c2+sp.integrate(-2*S1,(x,0,x))
S2=k2+sp.integrate(2*xi*H2-2*H1,(x,0,x))
sol2=sp.solve(boundary(S2,H2),(c2,k2),simplify=False)
H2=sp.factor(H2.subs(sol2));S2=sp.factor(S2.subs(sol2))
assert sp.factor(sp.diff(H2,x)+2*S1)==0
assert sp.factor(sp.diff(S2,x)-2*xi*H2+2*H1)==0
assert all(sp.factor(v)==0 for v in boundary(S2,H2))
critical=sp.Rational(1,2)
variance=sp.factor((S2.subs(x,0)-S1.subs(x,0)**2).subs(xi,critical))
variance_explicit=(96-32*(ql+qr)-11*(ql+qr)**2+32*ql*qr)/(6*(ql+qr)**2)
assert sp.factor(variance-variance_explicit)==0
# Classical symmetric-boundary published second moment (Angelani eq. 67).
q=sp.symbols('q',positive=True)
eps=q/(2-q)
Tcrit=(8-2*q)/(4*q)
raw2=sp.factor((S2.subs(x,0)).subs({xi:critical,ql:q,qr:q}))
assert sp.factor(raw2-(sp.Rational(5,3)*Tcrit**2+sp.Rational(1,3)/eps**2-1))==0
# The variance grows strictly with the product P at the critical rate.
assert sp.factor(sp.diff((96-32*Q-11*Q**2+32*P)/(6*Q**2),P)-sp.Rational(16,3)/Q**2)==0
# Separate event-driven Monte Carlo: velocities flip at rate xi,
# encounter at boundary is absorbing with probability q, otherwise reflected.
def simulate_one(rng, rate, left, right):
    position=0.; orientation=1 if rng.random()<.5 else -1
    elapsed=0.
    for _ in range(100000):
        distance=(1-position) if orientation>0 else (1+position)
        boundary_time=distance
        flip_time=rng.expovariate(rate) if rate>0 else float('inf')
        if flip_time<boundary_time:
            elapsed+=flip_time;position+=orientation*flip_time; orientation=-orientation
        else:
            elapsed+=boundary_time;position=float(orientation)
            if rng.random()<(right if orientation>0 else left):return elapsed
            orientation=-orientation
    raise RuntimeError('unexpected number of events')

r=random.Random(640193)
for rate,left,right in [(.0,1.,0.),(.2,.2,.8),(.5,.2,.8),(.5,.5,.5),(.9,.2,.8),(2.,.7,.9)]:
    n=14000
    obs=[simulate_one(r,rate,left,right) for _ in range(n)]
    mean=sum(obs)/n
    predicted=float(F.subs({xi:rate,Q:left+right,P:left*right}))
    # Six-sigma-style loose tolerance to avoid brittle random verification.
    if rate==.5:
        var_pred=(96-32*(left+right)-11*(left+right)**2+32*left*right)/(6*(left+right)**2)
        assert abs(mean-predicted)<8*math.sqrt(var_pred/n)+.04
        samplevar=sum((w-mean)**2 for w in obs)/n
        assert abs(samplevar-var_pred)<1.1
    else:
        samplevar=sum((w-mean)**2 for w in obs)/n
        assert abs(mean-predicted)<8*math.sqrt(samplevar/n)+.04
# Separate finite-parameter objective comparisons for the exact optimizer.
for rho in (0,.02,.3,.49,.5,.51,1,5):
 for total in (.01,.35,1.,1.2,1.7,1.99):
  low=max(0,total-1);high=total/2
  opt=low if rho<.5 else high
  ref=float(F.subs({xi:rho,Q:total,P:opt*(total-opt)}))
  for j in range(21):
   left=low+(min(total,1)-low)*j/20
   value=float(F.subs({xi:rho,Q:total,P:left*(total-left)}))
   assert value+1.e-9>=ref
print('PASS: symbolic first-/second-moment equations, source agreement, critical variance,')
print('      84,000 event-driven trajectories and 1,008 allocation comparisons.')
