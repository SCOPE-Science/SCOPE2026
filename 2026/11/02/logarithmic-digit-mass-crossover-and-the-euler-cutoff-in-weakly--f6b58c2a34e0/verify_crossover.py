"""Reproducible numerical precision checks for the affine countable-branch crossover.

Requirements: Python 3 and mpmath 1.3 or later.
Run: python verify_crossover.py
Analytic asymptotic statements are proved separately; this program tests samples only.
"""
import mpmath as mp
mp.mp.dps = 75


def integral(z, t):
    return -mp.expm1(-z * t) / z if z else t


def continuous_root(t):
    low, high = mp.mpf(-60), mp.mpf(5)
    for _ in range(250):
        mid = (low + high) / 2
        if integral(mid, t) > 1:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def harmonic(N, p):
    if p == 1:
        return mp.digamma(N + 1) + mp.euler
    return mp.zeta(p) - mp.zeta(p, N + 1)


def bisect(fun, low, high, steps=185):
    for _ in range(steps):
        mid = (low + high) / 2
        if fun(mid) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def finite_data(s, t, q=mp.mpf(2)):
    c = s ** q
    N = int(mp.floor(mp.exp(t / s)))
    def pressure(z):
        d = (1 + s * z) / q
        return c ** d * harmonic(N, q * d) - 1
    z = bisect(pressure, mp.mpf(-30), mp.mpf(5))
    d = (1 + s * z) / q
    M = int(mp.floor(mp.exp(t / (2 * s))))
    midpoint_mass = c ** d * harmonic(M, q * d)
    return N, z, midpoint_mass, abs(pressure(z))


def infinite_data(s, q=mp.mpf(2)):
    c = s ** q
    def pressure(z):
        d = (1 + s * z) / q
        return c ** d * mp.zeta(q * d) - 1
    z = bisect(pressure, mp.mpf('0.1'), mp.mpf(3))
    assert abs(pressure(z)) < mp.mpf('1e-45')
    d = (1 + s * z) / q
    L = int(mp.floor(mp.exp(1 / s)))
    cdf = c ** d * harmonic(L, q * d)
    return z, cdf


def run():
    tests = 0
    q = mp.mpf(2)
    for ttext in ['0.5', '1', '2']:
        t = mp.mpf(ttext)
        zstar = continuous_root(t)
        assert abs(integral(zstar, t) - 1) < mp.mpf('1e-45')
        tests += 1
        if t < 1: assert zstar < 0
        elif t == 1: assert abs(zstar) < mp.mpf('1e-40')
        else: assert zstar > 0
        tests += 1
        cdfstar = integral(zstar, t / 2)
        errors = []
        for stext in ['0.05', '0.02', '0.01']:
            s = mp.mpf(stext)
            N,z,cdf,resid = finite_data(s,t,q)
            assert resid < mp.mpf('1e-45')
            assert 0 < cdf < 1
            errors.append(abs(cdf-cdfstar))
            tests += 2
            if t == mp.mpf('0.5'):
                assert z < 0
            elif t == mp.mpf('2'):
                assert z > 0
            tests += 1
        assert errors[2] < errors[1] < errors[0]
        tests += 1
        print('tau=',ttext,'limiting_z=',mp.nstr(zstar,15),
              'limiting_midpoint_mass=',mp.nstr(cdfstar,15),
              'sample_errors=',[mp.nstr(e,7) for e in errors])
    allerr=[]
    for stext in ['0.05','0.02','0.01']:
        s=mp.mpf(stext)
        z,cdf=infinite_data(s,q)
        assert 0 < z < 1
        allerr.append(abs(z-1))
        assert abs(cdf-(1-mp.exp(-1)))<mp.mpf('0.08')
        tests += 2
        print('full s=',stext,'scaled_root=',mp.nstr(z,15),'cdf_at_1=',mp.nstr(cdf,15))
    assert allerr[2] < allerr[1] < allerr[0]
    tests += 1
    # Geometry: intervals with lengths c*n^(-q) and left edge P_n-c*n^(-q).
    for stext in ['0.05','0.01']:
        s=mp.mpf(stext);c=s**2
        prev=mp.mpf(0)
        for n in range(1,30):
            Pn=harmonic(n,q)/mp.zeta(q)
            left=Pn-c*n**(-q)
            assert prev < left < Pn < 1
            assert abs((Pn-left)-c*n**(-q))<mp.mpf('1e-55')
            prev=Pn
            tests += 2
    # Euler-constant cutoff check: H_N = log N + gamma + O(1/N).
    for stext in ['0.05','0.02','0.01']:
        s=mp.mpf(stext)
        N=int(mp.floor(mp.exp(1/s-mp.euler)))
        x=s*harmonic(N,mp.mpf(1))
        assert abs(x-1)<mp.mpf('1e-6')
        tests += 1
    print('PASS:',tests,'sample consistency assertions. No finite tests establish the limit theorem.')

if __name__=='__main__':run()
