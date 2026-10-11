"""Reproducible quadrature diagnostics for a cubic global-center occupation law.
Uses Python's standard library.  Numerical checks are diagnostics, not infinite proofs.
"""
from math import expm1, pi, sin, sqrt


def simpson(f, a, b, n=24000):
    assert n > 0 and n % 2 == 0
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(a + j * h)
    return total * h / 3


def period(L):
    if not L > 0:
        raise ValueError("L must be positive")
    def integrand(theta):
        s = sin(theta)
        if s == 0:
            return 1.
        return sqrt(L) * s / sqrt(expm1(L * s * s))
    return 4 * simpson(integrand, 0., pi / 2)


def moment(p, L, kappa=1.):
    if p < 0 or L <= 0 or kappa <= 0:
        raise ValueError("requires p>=0, L>0, kappa>0")
    T = period(L)
    def integrand(theta):
        s = sin(theta)
        if s == 0.:
            return 1 / sqrt(L) if p == 0. else 0.
        return s * expm1(L * s * s) ** ((p - 1) / 2)
    return (4 * sqrt(L) / (T * kappa**(p/2))) * simpson(integrand, 0., pi / 2)


def main():
    vals = [period(L) for L in (0.001, 1., 4., 12., 40.)]
    assert all(vals[j] > vals[j+1] > 0 for j in range(len(vals)-1))
    assert abs(vals[0] - 2*pi) < 0.001
    assert abs(moment(0,4.) - 1) < 2e-9
    assert abs(moment(1,4.) - 4*sqrt(4)/period(4.)) < 2e-9
    L=80.
    p_half=moment(0.5,L)
    p1=moment(1,L)
    p2=moment(2,L)
    assert abs(p_half / (sqrt(2)) - 1) < 0.025
    assert abs((p1/L)/(2/pi)-1) < 0.025
    A=sqrt(expm1(L))
    asym2=A*sqrt(2*L/pi)
    assert abs(p2/asym2-1) < 0.1
    print('CHECK_OK')
    print('T(L):',[(L,round(T,9)) for L,T in zip((0.001,1.,4.,12.,40.),vals)])
    print('L=80: T*sqrt(L)=',round(period(80)*sqrt(80),9),' target 2*pi=',round(2*pi,9))
    print('L=80: m_0.5=',round(p_half,9),' target sqrt(2)=',round(sqrt(2),9))
    print('L=80: m_1/L=',round(p1/L,9),' target 2/pi=',round(2/pi,9))
    print('L=80: m_2/pred=',round(p2/asym2,9))

if __name__ == '__main__':
    main()
