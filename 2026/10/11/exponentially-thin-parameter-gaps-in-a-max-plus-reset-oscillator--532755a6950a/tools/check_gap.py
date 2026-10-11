"""Finite consistency checks for the max-plus reset-gap theorem.

Requires sympy and mpmath. The universal asymptotic is proved analytically,
not by the finite tests performed here.
"""
import mpmath as mp
import sympy as sp

q = sp.symbols('q')
x, y = sp.Integer(1), sp.Integer(1)
for k in range(1, 13):
    x, y = sp.expand(q*x+y), sp.expand(1-q*x)
    assert sp.Poly(x, q).get_domain() == sp.ZZ

mp.mp.dps = 85

def h(n, R):
    theta = mp.acos(mp.sqrt(R)/2)
    return 1+R**(mp.mpf(n+1)/2)*mp.sin(n*theta)/mp.sin(theta)

# Recurrence and trigonometric solution agree away from the nearby roots.
for R in [mp.mpf(3)/2,mp.mpf(9)/4,mp.mpf(11)/4]:
    a,b = mp.mpf(1),mp.mpf(1)
    for j in range(1, 11):
        a,b = R*a+b,1-R*a
        assert abs(a-h(j,R)) < mp.mpf('1e-65')

for n in [7,8,9,10,12,15,18,24]:
    theta = mp.pi/n
    center = 4*mp.cos(theta)**2
    derivative = n*(2*mp.cos(theta))**n/(4*mp.sin(theta)**2)
    step = 1/derivative
    upper = mp.findroot(lambda R:h(n,R), (center-2*step,center-step/2))
    lower = mp.findroot(lambda R:h(n,R)-1/R, (center-step,center-step/4))
    assert center-3*step < upper < lower < center
    assert abs(h(n,upper)) < mp.mpf('1e-60')
    assert abs(h(n,lower)-1/lower) < mp.mpf('1e-60')
    for root in [upper, lower]:
        assert all(h(j,root)>0 for j in range(1,n))
    gap = lower-upper
    leading = mp.tan(theta)**2/(n*(2*mp.cos(theta))**n)
    assert 1 < gap/leading < mp.mpf('1.01')
    if n in [7,9,12,18]:
        print('n',n,'gap',mp.nstr(gap,20),
              'sharp_scale',mp.nstr(leading,20),
              'ratio',mp.nstr(gap/leading,12))
print('RESET_GAP_CHECK_OK')
