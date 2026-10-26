"""Exact checks and independent finite-dimensional examples for a damped pseudomode trimer."""
import sympy as sp

q, k, lam, u, v, y, r, t = sp.symbols('q k lam u v y r t', real=True)
E = sp.symbols('E')
H = sp.Matrix([[0, q, 0], [q, 0, k], [0, k, sp.I*lam]])
char = sp.factor((E*sp.eye(3)-H).det())
assert sp.simplify(char-(E**3-sp.I*lam*E**2-(q**2+k**2)*E+sp.I*lam*q**2)) == 0
P = y**3-y**2+(u+v)*y-u
D = sp.factor(sp.discriminant(P,y))
assert sp.expand(D-(v**2+20*u*v-4*u-8*u**2-4*(u+v)**3)) == 0
U = r**2*(1-2*r)
V = 2*r*(1-r)**2
assert sp.simplify(P.subs({u:U,v:V,y:r})) == 0
assert sp.simplify(sp.diff(P,y).subs({u:U,v:V,y:r})) == 0
assert sp.simplify(sp.diff(D,v).subs({u:U,v:V})+4*r*(3*r-1)**3) == 0
assert sp.simplify(sp.diff(V,r)/sp.diff(U,r)-(1-r)/r) == 0
assert sp.factor(D.subs(u,sp.Rational(1,27))) == -(27*v-8)**2*(108*v+49)/19683
assert sp.expand(U.subs(r,sp.Rational(1,3)+t)) == sp.Rational(1,27)-t*t-2*t**3
assert sp.expand((V-2*U-sp.Rational(2,9)).subs(r,sp.Rational(1,3)+t)) == 6*t**3

for uf in [sp.Rational(1,1000),sp.Rational(1,100),sp.Rational(3,100),sp.Rational(37,1000)]:
    roots = sp.nroots(U-uf, n=40, maxsteps=200)
    positive = sorted(float(sp.re(a)) for a in roots if abs(float(sp.im(a)))<1e-15 and 0<float(sp.re(a))<.5)
    assert len(positive)==2
    lower, upper = [2*rv*(1-rv)**2 for rv in positive]
    assert 0 < lower < upper
    for vv, expected in [(lower/2,-1),(0.5*(lower+upper),1),(upper+0.1,-1)]:
        dd = float(D.subs({u:uf,v:vv}))
        assert dd*expected > 1e-13, (uf,vv,dd,expected)
    print('u=',uf,'lower_v=',round(lower,12),'upper_v=',round(upper,12))

# A second route: complex 3-by-3 eigenvalues at parameters spanning both phases.
import numpy as np
for v0, has_real in [(0.10,True),(0.22,False),(0.40,True)]:
    mat = np.array([[0,.1,0],[.1,0,np.sqrt(v0)],[0,np.sqrt(v0),1j]],complex)
    ev = np.linalg.eigvals(mat)
    real_magnitude = max(abs(float(z.real)) for z in ev)
    assert (real_magnitude>1e-4)==has_real
    assert min(float(z.imag) for z in ev)>0
    print('v=',v0,'max_abs_Re_eig=',format(real_magnitude,'.12g'))

# The tangent-cusp formula has exact coefficient 12 from s_+-s_- ~2 sqrt(delta).
# Check numerical convergence without mistaking it for the analytic argument.
for delta in [1e-4,1e-5,1e-6]:
    u0 = 1/27-delta
    roots = sp.nroots(U-u0, n=35, maxsteps=300)
    positive = sorted(float(sp.re(a)) for a in roots if abs(float(sp.im(a)))<1e-12 and 0<float(sp.re(a))<.5)
    width = (2*positive[1]*(1-positive[1])**2-2*positive[0]*(1-positive[0])**2)
    print('delta=',delta,'width/delta**1.5=',format(width/delta**1.5,'.10f'))
    assert abs(width/delta**1.5-12) < 0.15
print('CHECKS PASSED')
