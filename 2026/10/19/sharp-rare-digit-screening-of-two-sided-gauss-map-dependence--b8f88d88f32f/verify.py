"""Reproducibility checks for sharp rare-digit screening in the Gauss map.

Requires: sympy, mpmath.  Executes finite exact identities and high-precision
independent checks; the accompanying proof supplies the infinite argument.
"""
import sympy as sp
import mpmath as mp

u, v, z, k = sp.symbols('u v z k', real=True)
s = u + v
# Euler--Maclaurin expansion of the tail through terms sufficient for z^2.
tail = (z/(1+s*z) + z**2/(2*(1+s*z)**2)
        + z**3/(6*(1+s*z)**3))
lnorm = sp.log(1+z)
ratio = lnorm * (1+u*z)*(1+v*z) * tail / z**2
expansion = sp.series(ratio, z, 0, 3).removeO().expand()
assert sp.simplify(expansion - 1 - z**2*(u-sp.Rational(1,2))*(v-sp.Rational(1,2))) == 0

p = 1/(k*(k+1))
mu = (1/k + 1/(k+1) - 1)/2
part = (1/(4*(k+1)) + 3/(4*(k+1)**2) - 1/(4*(k+1)**3)
        - 1/(4*k) - 1/(4*k**2) + 1/(4*k**3))
assert sp.simplify(p*mu**2 - part) == 0
S = sp.pi**2/12-sp.Rational(3,4)
assert sp.simplify(sp.Rational(1,2)*S**2 - (sp.pi**2-9)**2/288) == 0
assert sp.simplify(sp.Rational(1,2)*(sp.Rational(1,4))**2 - sp.Rational(1,32)) == 0

# Independent exact-rectangle quadrature, using the telescoped Gamma product
# for U,V in (1/2,1). This quadrant realizes the sign of the limiting copula.
mp.mp.dps = 70
for n_int in (10, 30, 100, 400):
    n = mp.mpf(n_int)
    L = mp.log1p(1/n)
    pp = mp.log((n+1)/(n+mp.mpf('0.5')))/L
    joint = (mp.loggamma(n+1)+mp.loggamma(n+2)
             -2*mp.loggamma(n+mp.mpf('1.5')))/L
    delta = joint-pp**2
    assert delta > 0
    observed = n*n*(2*delta)
    assert abs(observed-mp.mpf(1)/32) < mp.mpf('0.004')

print('VERIFY_OK')
