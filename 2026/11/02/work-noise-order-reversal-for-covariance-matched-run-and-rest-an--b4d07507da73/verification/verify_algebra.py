"""Exact algebraic certificates for matched active-force work-noise comparison.
Requires Python 3 and SymPy. Prints PASS or raises on an incorrect identity.
"""
import sympy as s
k,g,v,x=s.symbols('k g v x', positive=True, finite=True)
q=s.sqrt(2)
mu=g*v*v/(2*(k+g))
EXU=v*v/(2*(k+g))
EX2=v*v/(2*k*(k+g))
Phi3=lambda u: u*u/(2*(k+g)) - k*x*u/(k+g)
Phi2=lambda u: -k*x*u/(k+g)
for u in [-v,s.Integer(0),v]:
    L=(-k*x+u)*s.diff(Phi3(u),x)
    if u==0:
        L+=g*s.Rational(1,2)*(Phi3(v)-Phi3(0))+g*s.Rational(1,2)*(Phi3(-v)-Phi3(0))
    else:
        L+=g*(Phi3(s.Integer(0))-Phi3(u))
    assert s.simplify(L-(mu-(u*u-k*u*x)))==0
for u in [-v/q,v/q]:
    L=(-k*x+u)*s.diff(Phi2(u),x)+g*s.Rational(1,2)*(Phi2(-u)-Phi2(u))
    assert s.simplify(L-(mu-(u*u-k*u*x)))==0
cQ=1/(2*(k+g));cP=-k/(k+g)
V3=s.factor(g*(cQ**2*v**4+2*cQ*cP*v**2*EXU+cP**2*v**2*EX2))
V2=s.factor(2*g*cP**2*(v**2/2)*EX2)
assert s.simplify(V3-g*v**4/(4*(k+g)**2))==0
assert s.simplify(V2-g*k*v**4/(2*(k+g)**3))==0
assert s.simplify(V3/V2-(k+g)/(2*k))==0
assert s.simplify(s.diff(V3,g)-v**4*(k-g)/(4*(k+g)**3))==0
assert s.simplify(s.diff(V2,g)-k*v**4*(k-2*g)/(2*(k+g)**4))==0
print('PASS: 3-state and 2-state generator Poisson identities; exact quadratic brackets; variance ratio and two maxima')
