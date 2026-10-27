"""Reproducibility checks for a mixed-polarity three-stage exponential pulse.

Requires Python 3.11+, mpmath and sympy. These numerical checks supplement
but do not replace the analytic argument in RESULT.md.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 55


def pulse(t, a, b):
    rate = a + b
    if t < 0:
        return mp.exp(b*t)/rate**2
    return mp.exp(-a*t)*(1+rate*t)/rate**2


def direct_ambiguity(T, w, a, b):
    # Angular Doppler variable equals 2*w; frequency in cycles equals w/pi.
    kernel = lambda t: (pulse(t+T/2, a, b)*pulse(t-T/2, a, b)
                        *mp.exp(-2j*w*t))
    return mp.quad(kernel, [-mp.inf, -T/2, T/2, mp.inf])


def explicit_ambiguity(T, w, a, b):
    u = a + 1j*w
    v = b - 1j*w
    d = u*u - v*v
    numerator = 2*u**3*mp.exp(-v*T) - v*(T*u*d + 3*u*u - v*v)*mp.exp(-u*T)
    return numerator / (4*u**3*v*d*d)


def zero_equation(T, w, a, b):
    u = a+1j*w
    v = b-1j*w
    d = u*u-v*v
    rhs = v*(T*u*d+3*u*u-v*v)/(2*u**3)
    return mp.exp((u-v)*T)-rhs


def limiting_delay(a, b):
    d=a-b
    assert d>0
    lam=a+b
    h=d/lam
    return -mp.lambertw(-h*mp.exp(-h), -1)/d-1/lam


def assert_small(x, threshold, msg):
    if not abs(x) < threshold:
        raise AssertionError(f'{msg}: {mp.nstr(x, 12)}')


# Exact symbolic algebra for the convolution kernel and large-frequency series.
u,v,T = sp.symbols('u v T')
c2 = 2*(u*sp.exp(-v*T)-v*sp.exp(-u*T))/(u*u-v*v)
c3_via_derivative = (c2-u*sp.diff(c2,u))/u
c3_closed = 2*(2*u**3*sp.exp(-v*T)
    -v*(T*u*(u*u-v*v)+3*u*u-v*v)*sp.exp(-u*T))/(u*(u*u-v*v)**2)
assert sp.simplify(c3_via_derivative-c3_closed)==0
print('PASS symbolic convolution identity')

a,b,z = sp.symbols('a b z', positive=True, real=True)
U=a+sp.I/z
V=b-sp.I/z
R = V*(T*U*(U*U-V*V)+3*U*U-V*V)/(2*U**3)
lam=a+b
series = (-(1+lam*T)-sp.I*3*lam**2*T*z/2
          +lam**2*((4*a+b)*T-3)*z*z/2)
assert sp.simplify(sp.series(R-series,z,0,3).removeO())==0
print('PASS symbolic high-frequency expansion')

for a_val,b_val in [(mp.mpf('1'),mp.mpf('.5')),
                    (mp.mpf('2'),mp.mpf('1')),
                    (mp.mpf('1'),mp.mpf('1.2'))]:
    for T_val,w_val in [('0.3','0.2'),('1.8','1.2'),('3','2.4')]:
        t=mp.mpf(T_val);w=mp.mpf(w_val)
        difference=(direct_ambiguity(t,w,a_val,b_val)
                    -explicit_ambiguity(t,w,a_val,b_val))
        assert_small(difference,mp.mpf('1e-24'),'quadrature vs formula')
print('PASS nine independent split-integral ambiguity comparisons')

for a_val,b_val in [(mp.mpf('1'),mp.mpf('.5')),
                    (mp.mpf('2'),mp.mpf('1')),
                    (mp.mpf('1'),mp.mpf('.8'))]:
    d=a_val-b_val;lam=a_val+b_val
    Tstar=limiting_delay(a_val,b_val)
    assert Tstar>0
    assert_small(mp.exp(d*Tstar)-1-lam*Tstar,mp.mpf('1e-43'), 'limiting delay equation')
    Dprime=d*mp.exp(d*Tstar)-lam
    assert Dprime>0
    print('case rates',mp.nstr(a_val,3),mp.nstr(b_val,3),
          'limiting delay',mp.nstr(Tstar,15))
    for n in ([8,25,70] if b_val/a_val <= mp.mpf(".5") else [70,130,250]):
        wguess=(n+mp.mpf('.5'))*mp.pi/Tstar
        root=mp.findroot(lambda tt,ww:
                  (mp.re(zero_equation(tt,ww,a_val,b_val)),
                   mp.im(zero_equation(tt,ww,a_val,b_val))),
                  (Tstar,wguess),tol=mp.mpf('1e-42'),maxsteps=80)
        tt,ww=root
        assert tt>0 and ww>0
        assert_small(zero_equation(tt,ww,a_val,b_val),mp.mpf('1e-42'),'complex root equation')
        assert_small(explicit_ambiguity(tt,ww,a_val,b_val),mp.mpf('1e-40'),'ambiguity at root')
        if n>=25:
            assert abs(tt-Tstar)*n*n < 1e4
            assert abs(ww-wguess)*n < 1e4
        print('  n',n,'T',mp.nstr(tt,16),
              'Doppler',mp.nstr(ww/mp.pi,16),
              'frequency-spacing-error',mp.nstr(ww-wguess,7))
print('PASS nine high-precision positive real delay-Doppler roots')
print('All reproducibility checks passed; these are not infinite certificates.')
