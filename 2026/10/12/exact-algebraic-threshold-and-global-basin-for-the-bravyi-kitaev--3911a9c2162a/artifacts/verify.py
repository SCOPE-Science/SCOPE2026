import sympy as sp

r,y,z = sp.symbols('r y z', positive=True, real=True)
eps = (1-r)/2
f = (1-15*r**7+15*r**8-r**15)/(2*(1+15*r**8))
Q = y**6+y**5+y**4-14*y**3+y**2+y+1
q = z**3+z**2-2*z-16

want = r*(1-r**2)*Q.subs(y,r**2)/(2*(1+15*r**8))
assert sp.factor((f-eps)-want) == 0
assert sp.expand(y**3*q.subs(z,y+1/y)-Q) == 0
assert q.subs(z,2) == -8
assert sp.factor(sp.diff(q,z)) == 3*z**2+2*z-2

roots = sp.nroots(q, n=60, maxsteps=100)
real_roots = [sp.re(a) for a in roots if abs(float(sp.im(a))) < 1e-40]
assert len(real_roots) == 1
zs = real_roots[0]
assert 2 < zs < 3
ys = (zs-sp.sqrt(zs**2-4))/2
rs = sp.sqrt(ys)
es = (1-rs)/2

# Direct numerical fixed-point replay at high precision.
f_eps = sp.lambdify(r, f, 'mpmath')
import mpmath as mp
mp.mp.dps = 50
rr = mp.mpf(str(sp.N(rs,55)))
ee = mp.mpf(str(sp.N(es,55)))
assert abs(f_eps(rr)-ee) < mp.mpf('1e-45')

# Basin-side sign checks are supplementary to the analytic monotonicity proof.
def fmap(e):
    R=1-2*e
    return (1-15*R**7+15*R**8-R**15)/(2*(1+15*R**8))
for a in [mp.mpf('0.001'), mp.mpf('0.05'), ee-mp.mpf('1e-10')]:
    assert fmap(a) < a
for a in [ee+mp.mpf('1e-10'), mp.mpf('0.2'), mp.mpf('0.49')]:
    assert fmap(a) > a

print('VERIFY_OK')
print('z_star='+mp.nstr(mp.mpf(str(sp.N(zs,55))),50))
print('y_star='+mp.nstr(mp.mpf(str(sp.N(ys,55))),50))
print('epsilon_star='+mp.nstr(ee,50))
