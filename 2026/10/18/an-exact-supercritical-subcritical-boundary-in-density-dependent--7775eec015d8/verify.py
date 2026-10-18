#!/usr/bin/env python3
"""Exact symbolic checks for a quadratic two-population Hopf criticality formula.

Dependency: sympy>=1.12. All identities use exact symbolic arithmetic.
"""
import sympy as s

U, V = s.symbols('U V', real=True)
D, w = s.symbols('D w', positive=True, real=True)
B = (1 + w*w)/D
v = (w*V-U)/B
u = U
# Translation of the ecological flow at its unit coexistence equilibrium.
F = s.expand(-u-B*v-u*u-B*u*v-B*v*v-B*u*v*v)
H = s.expand(D*u+v+D*u*v-v*v*v)
# The rotating Cartesian coordinates are U=u, V=(u+Bv)/w.
Fp = s.expand(F+w*V)
Gp = s.expand((F+B*H)/w-w*U)
at0 = {U: s.Integer(0), V: s.Integer(0)}
def diff(expr, a, b):
    return s.diff(expr, U, a, V, b).subs(at0)
# Poincare--Lyapunov radial cubic coefficient for U'=-w V+Fp,
# V'=w U+Gp. Terms Fp,Gp have degree >=2.
L = (
    diff(Fp,3,0)+diff(Fp,1,2)+diff(Gp,2,1)+diff(Gp,0,3)
)/16 + (
    diff(Fp,1,1)*(diff(Fp,2,0)+diff(Fp,0,2))
    -diff(Gp,1,1)*(diff(Gp,2,0)+diff(Gp,0,2))
    -diff(Fp,2,0)*diff(Gp,2,0)
    +diff(Fp,0,2)*diff(Gp,0,2)
)/(16*w)
expected = -D*(B*(D+2)-3)/(8*B*w*w)
assert s.simplify(s.cancel(L-expected)) == 0
# Independent calculation from the multilinear-eigenvector formula.
q = s.Matrix([1,(-1-s.I*w)/B]);
p0 = s.Matrix([1,(1-s.I*w)/D])
inner = (s.conjugate(p0).T*q)[0]
p = p0/s.conjugate(inner)
A = s.Matrix([[-1,-B],[D,1]])
assert s.simplify(A*q-s.I*w*q)==s.zeros(2,1)
assert s.simplify(A.T*p+s.I*w*p)==s.zeros(2,1)
assert s.simplify((s.conjugate(p).T*q)[0]-1)==0
xy = s.symbols('x y',real=True)
x,y=xy
f0=x*(1+B*y-B*y*y-x)
g0=y*(D*x+3*y-y*y-(D+2))
field=s.Matrix([f0,g0]); origin={x:1,y:1}
def BL(a,b):
    return s.Matrix([sum(s.diff(field[i],xy[j],xy[k]).subs(origin)*a[j]*b[k]
                         for j in range(2) for k in range(2)) for i in range(2)])
def CL(a,b,c):
    return s.Matrix([sum(s.diff(field[i],xy[j],xy[k],xy[l]).subs(origin)*a[j]*b[k]*c[l]
                         for j in range(2) for k in range(2) for l in range(2)) for i in range(2)])
qc=s.conjugate(q)
G21=(s.conjugate(p).T*(CL(q,q,qc)
        -2*BL(q,A.inv()*BL(q,qc))
        +BL(qc,(2*s.I*w*s.eye(2)-A).inv()*BL(q,q))))[0]
# In Cartesian coordinates radius R=2|z|; hence L=Re(G21)/8.
assert s.simplify(s.cancel(s.re(G21)/8-expected))==0
for b,d,want in [ (s.Integer(1),s.Integer(2),-s.Rational(1,4)),
                  (s.Rational(2,5),s.Integer(5),s.Rational(5,16)) ]:
    wval=s.sqrt(b*d-1)
    got=s.simplify(expected.subs({D:d,w:wval}))
    assert got == want, (b,d,got,want)
    assert b*d == 2
for d,b in [ (s.Rational(3,2),s.Rational(1,1)),
             (s.Integer(3),s.Rational(3,5)),
             (s.Integer(6),s.Rational(3,8)) ]:
    assert b*d>1
    assert (b*(d+2)-3>0)==(d==s.Rational(3,2))
# Audit the entire unfolding, not only its critical Taylor jet.
mu=s.symbols('mu',real=True)
a2=D-(s.Rational(1,2)+mu)**2
c2=s.Rational(3,2)+mu
x0,y0=s.symbols('x0 y0',real=True)
ff=x0*(1+B/s.Integer(4)-B*(y0-s.Rational(1,2))**2-x0)
gg=y0*(-a2-(y0-c2)**2+D*x0)
assert s.simplify(ff.subs({x0:1,y0:1}))==0
assert s.simplify(gg.subs({x0:1,y0:1}))==0
uu,vv=s.symbols('uu vv',real=True)
assert s.simplify(s.expand(ff.subs({x0:1+uu,y0:1+vv})) -(-uu-B*vv-uu**2-B*uu*vv-B*vv**2-B*uu*vv**2))==0
assert s.simplify(s.expand(gg.subs({x0:1+uu,y0:1+vv})) -(D*uu+(1+2*mu)*vv+D*uu*vv+2*mu*vv**2-vv**3))==0

print('Exact Cartesian and complex Hopf coefficients agree.')
print('Both opposite-criticality examples share the spectrum +/-i.')
print('All exact symbolic checks passed.')
