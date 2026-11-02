"""Algebraic and numerical checks for a symmetric three-normal mixture.

This finite checker accompanies, but is not a substitute for, the exact analytic proof.
"""
import math
import random
import sympy as sp
import mpmath as mp

checks = 0

def check(condition, explanation):
    global checks
    assert condition, explanation
    checks += 1

# Exact derivatives in the auxiliary variable u=k cosh(z), with k>0.
u, k, b = sp.symbols('u k b', positive=True)
q = (u + k**2)/(1 + u)**2
check(sp.factor(sp.diff(q, u) - (1-u-2*k**2)/(1+u)**3) == 0,
      'exact derivative of posterior-variance profile')
check(sp.simplify(q.subs(u, k) - k/(1+k)) == 0,
      'center curvature')
check(sp.simplify(q.subs(u, 1-2*k**2) - 1/(4*(1-k**2))) == 0,
      'interior maximizing curvature')
check(sp.simplify(k/(1+k)-1/(4*(1-k**2))).subs(k,sp.Rational(1,2))==0,
      'continuity at the curvature bifurcation')

mp.mp.dps = 50
rcrit = mp.exp(mp.mpf('1.5'))/2

def Q(k):
    return k/(1+k) if k>=mp.mpf('0.5') else 1/(4*(1-k*k))

def B(r):
    r=mp.mpf(r)
    if r <= rcrit:
        return 4+mp.lambertw(-4*r*r*mp.exp(-4),0).real
    return 1-2*mp.lambertw(-mp.exp(mp.mpf('0.5'))/(2*r),0).real

for r in ['0.000001','0.01','0.1','0.5','1','2',str(rcrit),'2.5','5','20','100','1000000']:
    bb=B(r)
    kk=mp.mpf(r)*mp.exp(-bb/2)
    check(mp.fabs(bb*Q(kk)-1)<mp.mpf('1e-43'),f'boundary curvature for r={r}')
    check(bb>1 and bb<4, f'root range {r}')
    if mp.mpf(r)<rcrit:
        check(bb>3 and kk<mp.mpf('.5'), f'outer curvature branch {r}')
    elif mp.mpf(r)>rcrit:
        check(bb<3 and kk>mp.mpf('.5'), f'central curvature branch {r}')
    for shift in ['-0.0002','-0.000001','0.000001','0.0002']:
        btest=bb+mp.mpf(shift)
        curv=btest*Q(mp.mpf(r)*mp.exp(-btest/2))
        check((curv<1) if mp.mpf(shift)<0 else (curv>1),f'local root transition r={r}, shift={shift}')

check(mp.fabs(B(1)-mp.mpf('3.9206903948728864'))<mp.mpf('5e-16'), 'weight (1/4,1/2,1/4) numerical threshold')
check(mp.fabs(B(2)-mp.mpf('3.532109317947512'))<mp.mpf('5e-15'), 'equal-component threshold')
check(mp.fabs(B(rcrit)-3)<mp.mpf('1e-46'), 'triple phase endpoint')

# Numerically check exact curvature supremum against a finite grid;
# this probes the formula but does not prove global maximization.
rng=random.Random(20261026)
for j in range(180):
    r=mp.mpf(math.exp(rng.uniform(-3,3)))
    btest=mp.mpf(math.exp(rng.uniform(-2,2)))
    kk=r*mp.exp(-btest/2)
    analytic=-1+btest*Q(kk)
    max_grid=-mp.inf
    zstar=mp.mpf(0) if kk>=mp.mpf('0.5') else mp.acosh((1-2*kk*kk)/kk)
    sample_z=[mp.mpf(i)*mp.mpf('0.04') for i in range(401)]+[zstar]
    for z in sample_z:
        uz=kk*mp.cosh(z)
        val=-1+btest*(uz+kk*kk)/(1+uz)**2
        if val>max_grid:max_grid=val
    check(mp.fabs(max_grid-analytic)<mp.mpf('1e-43'),f'supremum attained at derived stationary point j={j}')

# The strict unimodality witness at r=1, b=4.
check(mp.exp(2)>mp.mpf(23)/6, 'unimodality coefficient strict inequality')
for zraw in [0.0001,0.1,0.3,1,2,3,5,10,20,50]:
    zz=mp.mpf(zraw)
    h=4*mp.sinh(zz)/zz-mp.cosh(zz)
    check(h<=mp.mpf(23)/6,'global modal auxiliary bound numerically')
check(4*Q(mp.exp(-2))>1,'unimodal witness is not log-concave')

print(f'PASS: {checks} exact-symbolic and numerical assertions')
print('r_critical =',mp.nstr(rcrit,35))
print('B(1) =',mp.nstr(B(1),35))
print('B(2) =',mp.nstr(B(2),35))
print('Witness r=1, b=4: unique mode at zero, positive maximal log curvature =',mp.nstr(-1+4*Q(mp.exp(-2)),30))
