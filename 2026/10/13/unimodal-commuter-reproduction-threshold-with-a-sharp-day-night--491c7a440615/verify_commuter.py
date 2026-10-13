"""Reproduce symbolic identities and finite checks for the two-city commuter threshold.

Requires Python 3 and SymPy. This is a check of explicit algebra, not an
exhaustive or independent verification of the analytic global argument.
"""
import sympy as s

p, a, b, r, z = s.symbols('p a b r z', real=True)
q = 1-a
H = s.Matrix([
    [a+q/(1+r*p), q*s.sqrt(r)*p/(1+r*p)],
    [q*s.sqrt(r)*p/(1+r*p), b*(1-q*p)+q*r*p*p/(1+r*p)]
])
Q = ((z-1)*(z-b) +
     (r*(z-a)*(z-b)+b*q*(z-1))*p -
     r*q*(1-b)*(z-a)*p*p)
assert s.simplify((1+r*p)*(z*z-z*s.trace(H)+H.det())-Q) == 0
assert s.simplify(s.diff(Q,p,2) + 2*r*q*(1-b)*(z-a)) == 0
assert s.simplify(s.diff(Q,p).subs({z:1,p:0}) - r*q*(1-b)) == 0
assert s.factor(s.diff(Q,z).subs({z:1,p:0})) == 1-b

Qbench = s.factor(Q.subs({r:1,b:s.Rational(1,2)}))
zend = (2+a+s.sqrt(5*a*a-8*a+4))/4
assert s.simplify(Qbench.subs({p:1,z:zend})) == 0
assert s.simplify(s.diff(Qbench,p).subs({p:1,z:zend}) -
                  (1-a)*(3*a-2)/4) == 0
assert s.simplify(s.resultant(Qbench.subs(a,0),
                            s.diff(Qbench,p).subs(a,0), z) + (p**4-10*p*p+1)/8) == 0
pstar = s.sqrt(3)-s.sqrt(2)
zstar = (s.sqrt(6)+s.sqrt(3)-s.sqrt(2)-1)/2
assert s.simplify(Qbench.subs({a:0,p:pstar,z:zstar})) == 0
assert s.simplify(s.diff(Qbench,p).subs({a:0,p:pstar,z:zstar})) == 0
assert 0 < float(pstar) < 1
assert s.simplify(Qbench.subs({a:0,p:s.Rational(1,3)}) -
                  (12*z*z-14*z+3)/9) == 0
z13 = (7+s.sqrt(13))/12
assert s.simplify(Qbench.subs({a:0,p:s.Rational(1,3),z:z13})) == 0
assert (11*z13/10 < 1) == True
thresholds = [(79-s.sqrt(2281))/220,(79+s.sqrt(2281))/220]
for x in thresholds:
    assert s.simplify(Qbench.subs({a:0,p:x,z:s.Rational(10,11)})) == 0
assert 0 < float(thresholds[0]) < float(pstar) < float(thresholds[1]) < 1

# Positivity and denominator checks at six sample parameter points only.
for aa, bb, rr in [
    (s.Rational(1,10),s.Rational(1,3),s.Rational(1,2)),
    (s.Rational(1,2),s.Rational(9,10),s.Rational(1,100)),
    (s.Rational(7,10),s.Rational(1,2),s.Integer(1)),
    (s.Integer(0),s.Rational(1,2),s.Integer(1)),
    (s.Rational(9,10),s.Rational(1,10),s.Integer(1)),
    (s.Rational(1,5),s.Rational(4,5),s.Integer(2)),
]:
    hh=H.subs({a:aa,b:bb,r:rr})
    f=s.lambdify(p,hh,'numpy')
    import numpy as np
    grid=np.linspace(0.0,1.0,2001)
    vals=np.array([max(np.linalg.eigvalsh(f(t))) for t in grid])
    diffs=np.diff(vals)
    signs=[int(np.sign(v)) for v in diffs if abs(v)>1.e-11]
    assert all(x<=y for x,y in zip(signs,signs[1:])),(aa,bb,rr)
print('VERIFY_OK')
print('p_star(0)=',s.N(pstar,16))
print('normalized_lam_star(0)=',s.N(zstar,16))
print('two_R0_equal_1_fractions=',[str(s.N(t,16)) for t in thresholds])
