"""Reproduce the algebraic phase-boundary and finite-matrix checks.

Requirements: Python 3, sympy, numpy, scipy.  Run: python VERIFY.py
The symbolic equalities verify identities for symbolic parameters; the
finite matrix tests are corroboration, not proofs for all graph sizes.
"""
from math import sqrt
import numpy as np
import sympy as s
from scipy.optimize import minimize_scalar, brentq

checks=0
p,q,B,t,a=s.symbols('p q B t a', positive=True)
b=(B-p*a)/(t*q)
D=(q+a)*(p+b)-p*q
F=(q+a)**(p-1)*(p+b)**(q-1)*D
phi=(p-1)/(q+a)-p*(q-1)/(t*q*(p+b))+s.diff(D,a)/D
Q=p*q*q*t*t+q*(B*(p+1)-p*q)*t+B*(B-q*q)
R=p*p*(B+q)*t-(B*B+B*p*(q+1)+p*p*q)
assert s.cancel(phi.subs(a,0)-p*Q/(B*q*(B+p*q*t)))==0;checks+=1
assert s.cancel(phi.subs(a,B/p)-R/(B*t*(B+p*q)))==0;checks+=1
assert s.simplify(Q.subs(t,1)-B*(B+q*(p+1-q)))==0;checks+=1
assert s.simplify(R.subs(t,1)-B*(p*(p-q-1)-B))==0;checks+=1
phi_fun=s.lambdify((p,q,B,t,a),phi,'numpy')

def phases(ip,iq,bv,tv):
    hi=(bv*bv+bv*ip*(iq+1)+ip*ip*iq)/(ip*ip*(bv+iq))
    if bv<iq*iq:
        A=ip*iq*iq; C=bv*(bv-iq*iq)
        mid=iq*(bv*(ip+1)-ip*iq)
        lo=(-mid+sqrt(mid*mid-4*A*C))/(2*A)
    else: lo=0.0
    assert 0<=lo<hi
    if tv<=lo: return 0.,lo,hi
    if tv>=hi: return bv/ip,lo,hi
    return brentq(lambda av:phi_fun(ip,iq,bv,tv,av),0.,bv/ip,xtol=1e-13),lo,hi

for ip in range(1,8):
 for iq in range(1,ip+1):
  for bv in (0.08,0.5,1.,2.,4.,10.,50.):
   for tv in (0.03,0.2,0.5,0.9,1.,1.4,3.,10.):
    astar,lo,hi=phases(ip,iq,bv,tv);checks+=1
    bstar=(bv-ip*astar)/(tv*iq)
    assert astar >= -1e-10 and bstar >= -1e-10;checks+=1
    def det_formula(av):
        be=(bv-ip*av)/(tv*iq)
        return (iq+av)**(ip-1)*(ip+be)**(iq-1)*((iq+av)*(ip+be)-ip*iq)
    z=minimize_scalar(lambda av:-np.log(det_formula(av)),bounds=(0.,bv/ip),method='bounded',options={'xatol':1e-13})
    assert abs(z.x-astar)<2e-5,(ip,iq,bv,tv,z.x,astar);checks+=1
    assert det_formula(astar) >= det_formula(0.)-1e-7 and det_formula(astar)>=det_formula(bv/ip)-1e-7;checks+=1
    if checks%37<4:
        # Build the graph Laplacian independently, then add the diagonal gains.
        L=np.zeros((ip+iq,ip+iq),dtype=float)
        for u in range(ip):
            for v in range(ip,ip+iq):
                L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
        M=L+np.diag([astar]*ip+[bstar]*iq)
        assert np.isclose(np.linalg.det(M),det_formula(astar),rtol=2e-8,atol=2e-7);checks+=1
        assert np.linalg.eigvalsh(M).min()>0;checks+=1

# Independent *exact* determinant checks at rational gains, including boundaries.
for ip in range(1,6):
 for iq in range(1,ip+1):
  for av,be in [(s.Rational(1,3),s.Rational(2,5)),(s.Rational(0),s.Rational(2,5)),(s.Rational(2,3),s.Rational(0))]:
   L=s.zeros(ip+iq)
   for u in range(ip):
    for v in range(ip,ip+iq):
     L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
   for u in range(ip):L[u,u]+=av
   for v in range(ip,ip+iq):L[v,v]+=be
   exact=(iq+av)**(ip-1)*(ip+be)**(iq-1)*((iq+av)*(ip+be)-ip*iq)
   assert L.det()==exact;checks+=1

# Special exact instance: four vertices versus two, total budget one.
assert s.simplify(Q.subs({p:4,q:2,B:1})-(16*t*t-6*t-3))==0;checks+=1
assert s.simplify((B*B+B*p*(q+1)+p*p*q)/(p*p*(B+q))).subs({p:4,q:2,B:1})==s.Rational(15,16);checks+=1
assert abs((3+sqrt(57))/16 - 0.6593646522044219)<1e-12;checks+=1
print('PASS:',checks,'symbolic, matrix, and finite optimization checks')
