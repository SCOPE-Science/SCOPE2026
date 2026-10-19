#!/usr/bin/env python3
"""Exact symbolic cross-checks for a complementary switched-temperature OU model.

Requires Python 3.10+ and SymPy. Proof is in RESULT.md. No stochastic simulation
is used to infer claims about continuous parameter domains.
"""
import sympy as sp
from functools import lru_cache

k,g,D,d,t=sp.symbols('k gamma D delta t',positive=True)
checks=0

def check(a,b=0):
    global checks
    assert sp.simplify(a-b)==0, 'symbolic identity failed: '+str(sp.factor(a-b))
    checks+=1

@lru_cache(None)
def M(p,q,eta=0):
    """Stationary E[S^eta X^(2p) Y^(2q)] from the coupled generator."""
    if p+q==0:
        return sp.Integer(1) if eta==0 else sp.Integer(0)
    rhs=sp.Integer(0)
    if p:
        rhs+=2*p*(2*p-1)*(D*M(p-1,q,eta)+d*M(p-1,q,1-eta))
    if q:
        rhs+=2*q*(2*q-1)*(D*M(p,q-1,eta)-d*M(p,q-1,1-eta))
    return sp.factor(rhs/(2*k*(p+q)+2*g*eta))

for p,q in [(1,0),(0,1),(2,0),(0,2),(1,1),(3,0),(4,0)]:
    check(M(p,q)-M(q,p)) if p!=q else check(M(p,q),M(p,q))
check(M(1,0),D/k)
check(M(2,0),3*D**2/k**2+3*d**2/(k*(k+g)))
check(M(1,1),D**2/k**2-d**2/(k*(k+g)))
check(M(0,2),M(2,0))

# All projection fourth cumulants, checked as a polynomial in cos^2(theta).
x=sp.symbols('x',real=True)
proj4=x*x*M(2,0)+6*x*(1-x)*M(1,1)+(1-x)**2*M(0,2)
check(proj4-3*(D/k)**2,3*d*d*(2*x-1)**2/(k*(k+g)))
# (X+Y)/sqrt2 and (X-Y)/sqrt2 each have strictly Gaussian one-time moments.
check(proj4.subs(x,sp.Rational(1,2)),3*(D/k)**2)

# First four even moments through degree eight, via generator rather than Beta law.
m2,m4,m6,m8=(M(j,0) for j in (1,2,3,4))
check(m6-15*m4*m2+30*m2**3)
check(m8-28*m6*m2-35*m4**2+420*m4*m2**2-630*m2**4,
      -630*d**4/(k*(k+g)**2*(3*k+g)))

# Independent Beta mixture moments, as a separate representation.
nu=g/(2*k)
q2=1/(2*nu+1)
q4=3/((2*nu+1)*(2*nu+3))
check(q2,k/(k+g))
check(q4,3*k*k/((k+g)*(3*k+g)))
check(3*d*d*q2/k**2,3*d*d/(k*(k+g)))
check(105*d**4*(q4-3*q2*q2)/k**4,-630*d**4/(k*(k+g)**2*(3*k+g)))

# Lag solution independent of the degree-8 generator calculation.
F=(k*sp.exp(-2*g*t)-g*sp.exp(-2*k*t))/(k*(k+g)*(k-g))
check(F.subs(t,0),1/(k*(k+g)))
check(sp.diff(F,t).subs(t,0))
check(sp.diff(F,t,2).subs(t,0),-4*g/(k+g))
check(sp.diff(F,t,2).subs(t,0)/F.subs(t,0),-4*k*g)
check(sp.limit(F,g,k),sp.exp(-2*k*t)*(1/(2*k*k)+t/k))
# Q= k*Z, E[Q_t Q_0]=k^2 F(t).
G=k*k*F
B=k/(k+g)*sp.exp(-2*g*t)
check(sp.diff(B,t)+2*g*B)
check(sp.diff(G,t)+2*k*G-2*k*B)
check(G.subs(t,0),k/(k+g))
check(B.subs(t,0),k/(k+g))

# Invert the observable A(t) = -delta^2 F(t); the sign of delta is invisible.
A=-d*d*F
check(-sp.diff(A,t,2).subs(t,0)/(4*k*A.subs(t,0)),g)
check(-k*(k+g)*A.subs(t,0),d*d)

# Explicit parameter witnesses, not used as global proofs.
for kv,gv in [(1,1),(1,3),(2,1),(3,2),(5,7)]:
    ff=sp.limit(F.subs(k,kv),g,gv) if kv==gv else F.subs({k:kv,g:gv})
    assert float(ff.subs(t,sp.Rational(1,3)))>0
    checks+=1

print(f'PASS: {checks} exact symbolic and rational assertions')
