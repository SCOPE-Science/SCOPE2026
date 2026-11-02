#!/usr/bin/env python3
"""Independent exact-arithmetic checks for the four-site midpoint quadratic spline law.
Requires Python 3 and SymPy. Scientific checks are supplementary to the proof.
"""
import random
import sympy as s
E,L,R,x=s.symbols('E L R x',positive=True)
z=s.symbols('z0:6')
k=E+L/2
left=z[0]+z[1]*x+z[2]*x*x
right=z[3]+z[4]*x+z[5]*x*x
y=s.symbols('y0:4')
equations=[left.subs(x,0)-y[0],left.subs(x,E)-y[1],
           right.subs(x,E+L)-y[2],right.subs(x,E+L+R)-y[3],
           left.subs(x,k)-right.subs(x,k),
           s.diff(left-right,x).subs(x,k)]
M,b=s.linear_eq_to_matrix(equations,z)
assert s.factor(M.det()) == E*L*R*(3*E*L+4*E*R+2*L**2+3*L*R)/4
print('Exact interpolation determinant identity: PASS')
phi_left=x-(3*L+4*R)*x*x/(L*(2*L+3*R))
phi_right=(x-L)*(x-L-R)/(2*L+3*R)
assert s.simplify(phi_left.subs(x,L/2)-phi_right.subs(x,L/2))==0
assert s.simplify(s.diff(phi_left-phi_right,x).subs(x,L/2))==0
assert s.simplify(phi_left.subs(x,0))==0
assert s.simplify(s.diff(phi_left,x).subs(x,0)-1)==0
assert s.simplify(phi_right.subs(x,L))==0
assert s.simplify(phi_right.subs(x,L+R))==0
left_peak=L*(2*L+3*R)/(4*(3*L+4*R))
right_trough=R*R/(4*(2*L+3*R))
mid=phi_right.subs(x,L/2)
assert s.simplify(left_peak-mid-L*(L+R)**2/(4*(3*L+4*R)*(2*L+3*R)))==0
r=s.symbols('r',positive=True)
assert s.simplify(((2+3*r)**2-r*r*(3+4*r))+2*(2*r+1)*(r*r-2*r-2))==0
print('Limit spline and exact crossover algebra: PASS')
seed=random.Random(20261027)
for j in range(30):
    e=s.Rational(seed.randint(1,5),seed.randint(8,30))
    ell=s.Rational(seed.randint(1,10),seed.randint(1,6))
    rr=s.Rational(seed.randint(1,10),seed.randint(1,6))
    v=[s.Rational(seed.randint(-6,6),seed.randint(1,5)) for _ in range(4)]
    mapping={E:e,L:ell,R:rr,**dict(zip(y,v))}
    system=M.subs(mapping)
    sol=system.inv()*b.subs(mapping)
    assert system*sol == b.subs(mapping)
    a=s.expand(left.subs(dict(zip(z,sol))).subs(mapping))
    d=s.expand(right.subs(dict(zip(z,sol))).subs(mapping))
    assert a.subs(x,0)==v[0] and a.subs(x,e)==v[1]
    assert d.subs(x,e+ell)==v[2] and d.subs(x,e+ell+rr)==v[3]
    assert a.subs(x,e+ell/2)==d.subs(x,e+ell/2)
    assert s.diff(a-d,x).subs(x,e+ell/2)==0
print('Thirty exact-rational four-data interpolation cases: PASS')
# Actual blowup coefficient for one extremal data vector at fixed L/R,
# comparing fitted polynomial coefficients with limiting shape.
for ell,rr in [(1,1),(1,3),(1,5),(3,2)]:
    target={L:s.Integer(ell),R:s.Integer(rr)}
    phi=[s.Poly(phi_left.subs(target),x),s.Poly(phi_right.subs(target),x)]
    errors=[]
    for inv_e in [40,80,160]:
        e=s.Rational(1,inv_e)
        mapping={E:e,L:s.Integer(ell),R:s.Integer(rr),**dict(zip(y,(0,1,0,0)))}
        sol=M.subs(mapping).inv()*b.subs(mapping)
        p=[s.Poly(s.expand(e*left.subs(dict(zip(z,sol))).subs(mapping)),x),
           s.Poly(s.expand(e*right.subs(dict(zip(z,sol))).subs(mapping)),x)]
        errs=max(abs(float(g)) for a,h in zip(p,phi) for g in (a-h).all_coeffs())
        errors.append(errs)
    assert errors[2]<errors[1]<errors[0]
print('Four families of asymptotic coefficient convergence: PASS')
print('TOTAL: all supplementary checks passed')
