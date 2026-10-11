#!/usr/bin/env python3
import sympy as s

t=s.symbols("t", real=True)
pi=s.pi
q5=s.sqrt(5)
tau=(3-q5)/2
r0=(3*q5-5)/2

v=[s.Matrix([s.cos(j*pi/5),s.sin(j*pi/5)]) for j in range(10)]
u=[s.Matrix([s.cos(pi/10+j*pi/5),s.sin(pi/10+j*pi/5)]) for j in range(10)]
c=s.cos(pi/10)
d=(1-t)*v[0]+t*v[1]
n=s.Matrix([-d[1],d[0]])

def active_intersection(j):
    A=s.Matrix.vstack(u[3].T,u[j].T)
    b=s.Matrix([c,c-u[j].dot(d)])
    return s.simplify(A.inv()*b)

x1=active_intersection(1)
x2=active_intersection(2)

# Exact objective-normal decompositions.
coef1=s.Matrix.hstack(u[3],u[1]).inv()*n
coef2=s.Matrix.hstack(u[3],u[2]).inv()*n
target1=s.Matrix([
    ((3-q5)*t+q5-1)/2,
    (q5-1)*(1-t)/2
])
target2=s.Matrix([t,1-t])
for got,want in list(zip(coef1,target1))+list(zip(coef2,target2)):
    assert s.diff(got-want,t,2).equals(0)
    for a in (s.Integer(0),s.Rational(1,2)):
        assert float(abs(s.N((got-want).subs(t,a),100))) < 1e-90

def residuals(x):
    return (
        [c-u[j].dot(x) for j in range(10)]
        + [c-u[j].dot(x+d) for j in range(10)]
    )

# Every residual is affine in t.  Endpoint nonnegativity therefore certifies
# feasibility on the full interval.
for x,ends in ((x1,(s.Integer(0),tau)),(x2,(tau,s.Rational(1,2)))):
    for res in residuals(x):
        assert s.diff(res,t,2).equals(0)
        for a in ends:
            val=float(s.N(res.subs(t,a),100))
            assert val > -1e-80

den=n.dot(v[3])
raw1=s.cancel(n.dot(x1)/den)
raw2=s.cancel(n.dot(x2)/den)
r1=r0+(11-5*q5)*t/2+(q5-2)*t**2
r2=1-(q5-1)*t*(1-t)/2

# Replay the trigonometric reductions at more points than the rational
# degree permits; these are regression checks, not the proof of the
# continuum formula stated in RESULT.md.
for raw,closed in ((raw1,r1),(raw2,r2)):
    for a in (s.Rational(0),s.Rational(1,7),tau,s.Rational(2,5),s.Rational(1,2)):
        assert float(abs(s.N((raw-closed).subs(t,a),100))) < 1e-80

assert s.simplify(r1.subs(t,0)-r0)==0
assert s.simplify(r1.subs(t,tau)-r0)==0
assert s.simplify(r2.subs(t,tau)-r0)==0
assert s.simplify(s.diff(r1,t,2)-2*(q5-2))==0
assert q5-2>0
assert s.simplify(s.diff(r2,t) - (q5-1)*(2*t-1)/2)==0
assert float(s.N(s.diff(r2,t).subs(t,tau),50)) < 0
assert float(s.N(s.diff(r2,t).subs(t,s.Rational(49,100)),50)) < 0

m=s.simplify(1-r0)
assert m==(7-3*q5)/2
print("VERIFY_OK")
print("tau =",s.N(tau,30))
print("max_ratio =",s.N(r0,30))
print("M_curvature =",s.N(m,30))
