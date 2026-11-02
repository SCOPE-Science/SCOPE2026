"""Reproduce the exact polynomial identities used in the Zak-zero theorem.

Run: python checker.py
Requires: sympy >= 1.10. The symbolic assertions are identities over Q(q,x,z).
"""
import sympy as sp

q, x, z, u = sp.symbols('q x z u')
y = q / x
F = x/(1-q*z) - x**2/(1-q**2*z) - y/(z-q) + y**2/(z-q**2)
D = (1-q*z)*(1-q**2*z)*(z-q)*(z-q**2)
N = (x**3*((1-x)+q*(x-q)*z)*(z-q)*(z-q**2)
     - q*((x-q)*z+q**2*(1-x))*(1-q*z)*(1-q**2*z))
assert sp.cancel(x**2 * F * D - N) == 0

coeff = sp.Poly(N, z).all_coeffs()
a3, a2, a1, a0 = coeff
obstruction = q**2*x*(x**2-q)*(q-1)**3*(q**2+q+1)*(x**4+(1+2*q+q**2)*x**2+q**2)
assert sp.factor(a3*(a1-a3)-a0*a2+a0**2-obstruction) == 0
assert sp.factor(a3-q*(x-q)**2*(q**2+q*x+x**2)) == 0
assert sp.factor(a0+q**3*(x-1)**2*(x**2+x+1)) == 0

at_plus_one = (x-q)*(x**2-q)*(q-1)**3*(q+1)*(x-1)
at_minus_one = -(x-q)*(q+1)*(q**2+1)*(x-1)*(q**2+q*x**2+2*q*x+q+x**2)
assert sp.factor(N.subs(z,1)-at_plus_one) == 0
assert sp.factor(N.subs(z,-1)-at_minus_one) == 0

boundary = q*(q-1)**2*(q**2+q+1)*z*(z-1)*(z+1)
assert sp.factor(N.subs(x,1)-boundary) == 0

middle = (u**3*(u-1)**2*(u**2+u+1)*(z-1)
          *(u**3*(z**2+1)+(u**6+u**4+2*u**3+u**2+1)*z))
assert sp.factor(N.subs({q:u**2,x:u})-middle) == 0

# Check a representative finite collection against the absolutely convergent Zak series.
import mpmath as mp
mp.mp.dps = 40
for beta, t, xi in [(mp.mpf('0.3'),mp.mpf('0.19'),mp.mpf('0.37')),
                    (mp.mpf('1.0'),mp.mpf('0.23'),mp.mpf('0.29')),
                    (mp.mpf('1.7'),mp.mpf('0.45'),mp.mpf('0.63'))]:
    qq=mp.exp(-2*mp.pi*beta); xx=qq**xi; yy=qq**(1-xi); zz=mp.exp(2*mp.pi*1j*t)
    ff = xx/(1-qq*zz)-xx**2/(1-qq**2*zz)-yy/(zz-qq)+yy**2/(zz-qq**2)
    spectral = -1j*mp.pi*beta*mp.exp(2*mp.pi*1j*t*xi)*ff/3
    def g(v):
        return v/((v*v+1)*(v*v+4))
    direct = mp.fsum(g((t-m)/beta)*mp.exp(2*mp.pi*1j*m*xi) for m in range(-700,701))
    assert abs(direct-spectral) < mp.mpf('3e-8')
print('PASS: all symbolic identities and sample Poisson checks')
