"""Numerical checks for the singular-edge shifted-grid variance formulas.

Requires mpmath and scipy. The proof in RESULT.md is independent of this code.
Run: python verify.py
"""
from math import gamma, pi, sin
import mpmath as mp
from scipy.integrate import quad
from scipy.special import zeta as hurwitz_zeta


def constants(alpha):
    a = float(alpha)
    c = 2 * gamma(1-a)**2 * (2*pi)**(2*a-2) * hurwitz_zeta(2-2*a,1)
    return c, c*sin(pi*a/2)**2


def grid(m,a,u):
    return m**(a-1)*sum((j+u)**(-a) for j in range(m))


mp.mp.dps = 38
for a in [mp.mpf('0.25'), mp.mpf('0.40')]:
    c, anti_c = constants(a)
    def z(u):
        return mp.zeta(a,u)
    cuts=[mp.mpf('0'),mp.mpf('.001'),mp.mpf('.1'),mp.mpf('.5'),mp.mpf('.9'),mp.mpf('.999'),mp.mpf('1')]
    c_direct=mp.quad(lambda u:z(u)**2,cuts)
    anti_direct=mp.quad(lambda u:((z(u)+z(1-u))/2)**2,cuts)
    assert abs(float(c_direct)/c-1)<2e-6, (a,c_direct,c)
    assert abs(float(anti_direct)/anti_c-1)<2e-6, (a,anti_direct,anti_c)
    m=40
    af=float(a)
    mean=1/(1-af)
    v_antithetic=quad(lambda u:((grid(m,af,u)+grid(m,af,1-u))/2-mean)**2,
                       0,1,epsabs=1e-9,limit=500)[0]
    scaled=v_antithetic*m**(2-2*af)
    assert abs(scaled/anti_c-1)<0.005,(a,scaled,anti_c)
    assert 0<2*sin(pi*af/2)**2<1

# Exact local singular exponent is the moment threshold for every finite m.
for a in [0.25,0.40,0.65]:
    for m in [1,3,7]:
        v1=grid(m,a,1e-10)*(1e-10)**a
        v2=grid(m,a,1e-12)*(1e-12)**a
        target=m**(a-1)
        assert abs(v1/target-1)<0.02 and abs(v2/target-1)<0.02

print('VERIFY_OK: hurwitz_parseval=4, paired_grid_asymptotics=2, local_moments=9')
