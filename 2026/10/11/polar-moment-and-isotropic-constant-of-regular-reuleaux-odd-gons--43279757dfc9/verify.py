#!/usr/bin/env python3
import math
import mpmath as mp
import sympy as sp

t = sp.symbols("t", positive=True)
R = 1/(2*sp.cos(t))
N = sp.pi/(2*t)

Asec = t
Atri = sp.sin(t)*sp.cos(t)
I2sec = t/2
I2tri = Atri*(2+sp.cos(2*t))/6
Ixsec = 2*sp.sin(t)/3
Ixtri = Atri*(2*sp.cos(t))/3

Jseg = sp.simplify(
    R**2*(Asec-Atri)
    + (I2sec-I2tri)
    - 2*R*(Ixsec-Ixtri)
)
Jpoly1 = R**4*sp.sin(4*t)*(2+sp.cos(4*t))/12
Jsum = sp.trigsimp(N*(Jpoly1+Jseg))

Jclosed = (
    sp.pi*(3+sp.tan(t)**2)/8
    - N*sp.tan(t)*(11+sp.tan(t)**2)/16
)
assert sp.simplify(sp.trigsimp(Jsum-Jclosed)) == 0

Apoly1 = R**2*sp.sin(4*t)/2
Aseg = Asec-Atri
Asum = sp.trigsimp(N*(Apoly1+Aseg))
Aclosed = sp.pi/2-N*sp.tan(t)/2
assert sp.simplify(sp.trigsimp(Asum-Aclosed)) == 0

L2 = sp.simplify(Jclosed/(2*Aclosed**2))
x = sp.symbols("x", positive=True)
Jseries = sp.series(Jclosed.subs(t,sp.pi*x/2),x,0,6).removeO()
Aseries = sp.series(Aclosed.subs(t,sp.pi*x/2),x,0,6).removeO()
L2series = sp.series(L2.subs(t,sp.pi*x/2),x,0,6).removeO()

assert sp.simplify(
    Jseries
    - (sp.pi/32-sp.pi**3*x**2/192+sp.pi**5*x**4/2560)
) == 0
assert sp.simplify(
    Aseries
    - (sp.pi/4-sp.pi**3*x**2/48-sp.pi**5*x**4/480)
) == 0
assert sp.simplify(
    L2series
    - (1/(4*sp.pi)+sp.pi**3*x**4/180)
) == 0

mp.mp.dps = 50
worst = mp.mpf("0")
for n in [3,5,7,9,11,21,41]:
    tt = mp.pi/(2*n)
    rr = 1/(2*mp.cos(tt))
    def rho(th):
        return -rr*mp.cos(th)+mp.sqrt(1-rr**2*mp.sin(th)**2)
    radial_J = n/4*mp.quad(lambda th: rho(th)**4, [-2*tt, 2*tt])
    uu = mp.tan(tt)
    closed_J = (2*mp.pi*(3+uu**2)-n*uu*(11+uu**2))/16
    err = abs(radial_J-closed_J)
    worst = max(worst,err)
    assert err < mp.mpf("1e-40")

print("VERIFY_OK")
print("symbolic_segment_decomposition = passed")
print("symbolic_area_identity = passed")
print("symbolic_covariance_and_series = passed")
print("radial_checks_n = 3,5,7,9,11,21,41")
print("max_radial_error =", mp.nstr(worst, 8))
