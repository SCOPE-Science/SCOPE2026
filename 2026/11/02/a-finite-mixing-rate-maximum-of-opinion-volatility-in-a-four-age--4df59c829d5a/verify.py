"""Exact stationary-moment checks for a four-node stochastic-gossip chain.

Run with Python 3 and SymPy: python verify.py
The identities themselves are proved in RESULT.md; these checks are independent
substitutions and generator reconstructions, not an empirical proof.
"""
from itertools import product
import sympy as sp

x,y=sp.symbols('x y')
a,m,t=sp.symbols('a m t',positive=True)

# Only the receiver updates. Each listed directed link has an independent
# Poisson clock with the indicated rate.
events=[
 (a,((1-t)*x,y)),
 (a,(x,(1-t)*y+t)),
 (m,((1-t)*x+t*y,y)),
 (m,(x,(1-t)*y+t*x))]

monomials=[x,y,x*x,x*y,y*y]
unknowns=sp.symbols('EX EY EX2 EXY EY2')
moment_map={(0,0):sp.Integer(1),(1,0):unknowns[0],(0,1):unknowns[1],
            (2,0):unknowns[2],(1,1):unknowns[3],(0,2):unknowns[4]}

def expected(poly):
    p=sp.Poly(sp.expand(poly),x,y)
    return sp.expand(sum(c*moment_map[powers] for powers,c in p.terms()))

def generator(f):
    return sp.expand(sum(rate*(f.subs({x:newx,y:newy}, simultaneous=True)-f)
              for rate,(newx,newy) in events))

eqs=[expected(generator(f)) for f in monomials]
T=sp.Matrix([[eq.diff(z) for z in unknowns] for eq in eqs])
constant=sp.Matrix([eq.subs(dict.fromkeys(unknowns,0)) for eq in eqs])
assert sp.simplify(T.det())!=0

# Symbolically verify the claimed variance formula and its derivative.
u=sp.symbols('u',positive=True)
V=t*u*(1+u)**2/((1+2*u)**2*((2-t)+(4-3*t)*u))
Q=(2-t)*(1+u)-4*(1-t)*u**2
assert sp.factor(sp.diff(V,u)-t*(1+u)*Q/((1+2*u)**3*((2-t)+(4-3*t)*u)**2))==0
assert sp.simplify(sp.limit(V,u,sp.oo)-t/(4*(4-3*t)))==0

checks=0
for aa,tt,mm in product([sp.Rational(1,2),1,3],
                         [sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5),1],
                         [0,sp.Rational(1,7),sp.Rational(3,2),5]):
    substitution={a:aa,t:tt,m:mm}
    A=T.subs(substitution)
    b=-constant.subs(substitution)
    values=A.inv()*b
    ex,ey,ex2,exy,ey2=values
    predicted=sp.cancel(V.subs({t:tt,u:sp.Rational(mm,aa)}))
    assert sp.cancel(ex2-ex*ex-predicted)==0,substitution
    assert sp.cancel(ey2-ey*ey-predicted)==0,substitution
    assert sp.cancel(ex-sp.Rational(mm,aa+2*mm))==0,substitution
    assert sp.cancel(ey-sp.Rational(aa+mm,aa+2*mm))==0,substitution
    # The 2x2 stationary covariance is positive semidefinite.
    cov=sp.simplify(exy-ex*ey)
    assert predicted>=0 and sp.simplify(predicted**2-cov**2)>=0
    checks+=1

for tt in [sp.Rational(1,10),sp.Rational(1,2),sp.Rational(9,10)]:
    root=((2-tt)+sp.sqrt((2-tt)*(18-17*tt)))/(8*(1-tt))
    assert sp.simplify(Q.subs({t:tt,u:root}))==0
    assert root>0
    assert sp.N(V.subs({t:tt,u:root}))>sp.N(tt/(4*(4-3*tt)))

# A fully symbolic alternative basis recovers the same second moments.
z,d=sp.symbols('z d')
zd_events=[(rate, (sp.expand((nx+ny)/2-sp.Rational(1,2)).subs({x:z-d+sp.Rational(1,2),y:z+d+sp.Rational(1,2)},simultaneous=True),
                    sp.expand((ny-nx)/2).subs({x:z-d+sp.Rational(1,2),y:z+d+sp.Rational(1,2)},simultaneous=True)))
           for rate,(nx,ny) in events]
mean_d=a/(2*(a+2*m))
Lambda=a*(2-t)+m*(4-3*t)
mean_z2=m*t*(a+m)/(2*(a+2*m)*Lambda)
mean_d2=a*(a*(2-t)+m*t)/(4*(a+2*m)*Lambda)
for f in (d,z,z*z,z*d,d*d):
    drift=sum(rate*(f.subs({z:nz,d:nd},simultaneous=True)-f)
              for rate,(nz,nd) in zd_events)
    p=sp.Poly(sp.expand(drift),z,d)
    E={(0,0):1,(1,0):0,(0,1):mean_d,(2,0):mean_z2,
       (1,1):0,(0,2):mean_d2}
    assert sp.cancel(sum(coeff*E[powers] for powers,coeff in p.terms()))==0

print('PASS: symbolic derivative, stationary z/d identities, and',checks,
      'independent exact-rational generator reconstructions.')
