"""Reproducible checks for an ideal symmetric binary-source microlensing model.

Uses only the Python standard library. Run: python verify.py
"""

from fractions import Fraction as F
from math import hypot, isclose, sqrt
from random import Random


def magnification(u):
    return (u * u + 2) / (u * sqrt(u * u + 4))


def flux(t, b, s):
    return (magnification(hypot(b, t - s)) + magnification(hypot(b, t + s))) / 2


def kernel(z, b):
    q = (z * z + b * b) * (z * z + b * b + 4)
    return z / q ** 1.5


def derivative(t, b, s):
    return 4 * (kernel(s - t, b) - kernel(s + t, b))


def critical(b):
    B = b * b
    return sqrt((sqrt(9 * B * B + 36 * B + 16) - 2 * B - 4) / 5)


def bisect(fun, lo, hi, n=90):
    v0 = fun(lo)
    assert v0 * fun(hi) <= 0
    for _ in range(n):
        mid = (lo + hi) / 2
        if fun(mid) * v0 > 0:
            lo, v0 = mid, fun(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def rational_checks():
    # Verify exact rational derivative and symmetry identities at 199 test values.
    for q in range(2, 201):
        y = F(q + 3, 2)
        L = y**3 - 3*y + 2
        dL = 3*y**2 - 3
        N = y**4 - 3*y**2 + 1
        dN = 4*y**3 - 6*y
        dA = (dN * L - 2*N*dL) / L**3
        PA = y**5 + y**4 - 2*y**3 - 6*y**2 - 3*y + 3
        assert dA == -2*PA / ((y-1)**5 * (y+2)**3)
        dD = (L - y*dL) / L**2
        assert dD == -2*(y*y+y+1) / ((y-1)**3 * (y+2)**2)
        z=y-2
        assert PA == z**5+11*z**4+46*z**3+86*z**2+61*z+5
        assert PA > 0
    return 199


def numerical_checks():
    r = Random(532817)
    checked = 0
    splits = 0
    for _ in range(1200):
        b = 10 ** r.uniform(-1.3, 1.3)
        s0 = critical(b)
        assert b/sqrt(5) < s0 < b/sqrt(2)
        factor = r.choice((.55,.75,.9,.98,1.02,1.2,1.6,2.5,4))
        s = factor*s0
        assert isclose(derivative(0,b,s), 0, abs_tol=1e-13)
        assert derivative(s,b,s) < 0
        g0 = flux(0,b,s)
        if s < s0:
            # There must be no positive root; scan densely in (0,s).
            for j in range(1,151):
                t=s*j/151
                assert derivative(t,b,s) < 0
                assert flux(t,b,s) < g0
                checked += 1
        else:
            # The unique positive root lies in (0,s), and is a strict global maximum.
            left=s*1e-5
            while derivative(left,b,s)<=0:
                left/=10
                assert left > 1e-13*s
            t=bisect(lambda v:derivative(v,b,s),left,s)
            assert 0<t<s
            assert derivative(t*.98,b,s)>0
            assert derivative((t+s)/2,b,s)<0
            assert flux(t,b,s)>g0
            assert flux(-t,b,s)==flux(t,b,s)
            for j in range(1,151):
                v=s*j/151
                if v < t*.97: assert derivative(v,b,s)>0
                elif v > t*1.03: assert derivative(v,b,s)<0
                checked += 1
            splits+=1
    return checked,splits


def benchmark_and_onset():
    b=1.0
    s0=critical(b)
    assert isclose(s0,sqrt((sqrt(61)-6)/5), rel_tol=1e-13)
    assert isclose(2*s0,1.203411708737007,abs_tol=1e-12)
    s=.8
    t=bisect(lambda x:derivative(x,b,s), .1, s)
    assert abs(t-.630876026959269)<1e-11
    assert abs(flux(t,b,s)-1.2104081209755768)<1e-11
    assert abs(flux(0,b,s)-1.1968505057115397)<1e-11
    D=2*b*b+4
    c=18*s0*(5*s0*s0+D)/(5*s0*s0+7*D)
    for eps in (1e-4,5e-5,1e-5):
        s=s0+eps
        t=bisect(lambda x:derivative(x,b,s),sqrt(c*eps)*0.5,s)
        assert abs(t*t/(c*eps)-1)<.002
    return s0,t,c


if __name__=='__main__':
    exact=rational_checks()
    checks,splits=numerical_checks()
    crit,t,c=benchmark_and_onset()
    print(f'PASS: {exact} rational derivative confirmations; {checks} sampled light-curve derivatives; {splits} split-mode parameter sets.')
    print(f'PASS: b=1 critical half-spacing {crit:.15f}; post-split test peak {t:.9f}; onset coefficient {c:.12f}.')
    print('Note: finite checks supplement, and do not replace, the analytic proof.')
