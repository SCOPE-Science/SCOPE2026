#!/usr/bin/env python3
"""Independent numerical checks for an affine projector on spherical shells.

Requires Python 3 and mpmath >=1.2.  These checks support but do not
replace the analytic proof for every dimension and hole radius.
"""
import mpmath as mp

mp.mp.dps = 48

def kappa(d, r):
    r = mp.mpf(r)
    return (d + 2) * (1 - r**d) / (1 - r**(d+2))

def ball_excess(d, s):
    s = mp.mpf(s)
    if s <= 1:
        return mp.mpf(0)
    q = mp.mpf(d + 1)/2
    x = 1 - 1/s**2
    c = mp.gamma(mp.mpf(d)/2 + 1)/(mp.sqrt(mp.pi)*mp.gamma(q))
    return c*(s*x**q/(d+1) - mp.betainc(q, mp.mpf('0.5'), 0, x)/2)

def formula(d,r):
    rr = mp.mpf(r)
    if rr == 1:
        return 1 + 2*sphere_excess(d,d)
    k = kappa(d,rr)
    return 1 + 2*(ball_excess(d,k)-rr**d*ball_excess(d,k*rr))/(1-rr**d)

def sphere_excess(d,s):
    s = mp.mpf(s)
    if s <= 1:
        return mp.mpf(0)
    c = mp.gamma(mp.mpf(d)/2)/(mp.sqrt(mp.pi)*mp.gamma(mp.mpf(d-1)/2))
    b = mp.acos(1/s)
    return c * mp.quad(lambda a: (s*mp.cos(a)-1)*mp.sin(a)**(d-2), [0,b])

def direct(d,r):
    rr=mp.mpf(r)
    k=kappa(d,rr)
    cut=1/k
    integrand=lambda s: d*s**(d-1)*sphere_excess(d,k*s)/(1-rr**d)
    if cut>=1:
        return mp.mpf(1)
    return 1+2*mp.quad(integrand,[max(rr,cut),1])

checks=0
for d in (2,3,4,5,6):
    for r in ('0','0.15','0.5','0.81'):
        a=formula(d,r)
        b=direct(d,r)
        assert abs(a-b)<mp.mpf('3e-34'), (d,r,a,b)
        checks+=1
    grid=[formula(d,r) for r in ('0','0.15','0.5','0.81','1')]
    assert all(x>y for x,y in zip(grid,grid[1:]))
    checks+=4
for d in (3,4,5,6,9):
    assert (abs(formula(d,1)-formula(d-2,0))<mp.mpf('3e-37')) if d>3 else (abs(formula(d,1)-(mp.mpf(5)/3))<mp.mpf('3e-37'))
    checks+=1
assert abs(formula(3,0)-mp.mpf(253)/125)<mp.mpf('1e-38'); checks+=1
assert abs(formula(2,1)-(mp.mpf(1)/3+2*mp.sqrt(3)/mp.pi))<mp.mpf('1e-38'); checks+=1
for d in (2,3,4,6):
    beta_coeff=mp.betainc(mp.mpf(d+1)/2,mp.mpf('0.5'),0,1-1/mp.mpf(d+2)**2,regularized=True)
    r=mp.mpf('0.0001')
    ratio=(formula(d,0)-formula(d,r))/r**d
    assert abs(ratio-beta_coeff) < mp.mpf('0.000002'),(d,ratio,beta_coeff)
    checks+=1
print(f'VERIFY_OK: {checks} high-precision formula, direct-integration, monotonicity, shell/ball, and small-hole checks')
