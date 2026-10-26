#!/usr/bin/env python3
"""Independent numerical checks for the stated integer-power secant ambiguity formulas."""
import sympy as sp
import mpmath as mp
mp.mp.dps = 38
T, u = sp.symbols('T u', positive=True, real=True)
f = sp.sin(u*T)/sp.sinh(T)
max_abs_integral_error = mp.mpf(0)
max_scaled_zero_error = mp.mpf(0)
for m in range(1, 5):
    if m > 1:
        f = sp.diff(f, T)/sp.sinh(T)
    P = sp.lambdify((T,u), f, 'mpmath')
    n = m-1
    small_T=mp.mpf('0.05')
    for j in (1,2):
        y0=mp.besseljzero(n+mp.mpf('0.5'),j)
        if m==1:
            y=y0
        else:
            F=lambda y: (-1)**n*small_T**(2*n+1)*P(small_T,y/small_T)
            y=mp.findroot(F,(y0-mp.mpf('0.02'),y0+mp.mpf('0.02')))
        assert abs(y-y0)<mp.mpf('0.002')
        max_scaled_zero_error=max(max_scaled_zero_error,abs(y-y0))
    if m <= 3:
        tau=mp.mpf('0.7');k=mp.mpf('4.3');v=k/2
        closed=2**m*mp.pi*(-1)**n/mp.factorial(n)/mp.sinh(mp.pi*v)*P(tau,v)
        integral=mp.quad(lambda t: mp.sech(t+tau/2)**m*mp.sech(t-tau/2)**m*mp.cos(k*t),[-mp.inf,0,mp.inf])
        err=abs(closed-integral)
        max_abs_integral_error=max(err,max_abs_integral_error)
        assert err<mp.mpf('1e-30')
assert 0<mp.tanh(mp.mpf('0.7'))/mp.mpf('0.7')<1
print('PASS: integer powers 1..4, two Bessel roots each, direct integral m=1..3')
print('max difference in rescaled roots at T=0.05:',mp.nstr(max_scaled_zero_error,12))
print('max absolute integral-vs-closed-form error:',mp.nstr(max_abs_integral_error,12))
