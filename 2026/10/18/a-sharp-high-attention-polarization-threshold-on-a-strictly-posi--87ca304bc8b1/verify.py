"""Self-contained numerical cross-checks for a two-block saturating influence equation.

The mathematical conclusion is proved analytically in RESULT.md; finite precision
checks here are a reproducibility aid, not a substitute for that proof.
"""
import math


def bisect(f, lo, hi, iterations=160):
    flo, fhi = f(lo), f(hi)
    assert flo * fhi < 0.0, (lo, hi, flo, fhi)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if f(mid) * flo > 0:
            lo, flo = mid, f(mid)
        else:
            hi, fhi = mid, f(mid)
    return (lo + hi) / 2


def parameters(a, b, gamma=1.0, d=1.0):
    assert 0 < b < a <= 1 and gamma > 0 and d > 0
    lm = gamma * (a-b) / 2.0
    lp = gamma * (a+b) / 2.0
    ratio = lp / lm
    zc = bisect(lambda z: math.sinh(2*z)/(2*z)-ratio, 1e-5, 10.0)
    uc = d * zc / (lm * math.tanh(zc))
    return lm, lp, zc, uc


def polar_eigenvalues(u, lm, lp, d=1.0):
    z = bisect(lambda zz: d*zz/lm - u*math.tanh(zz), 1e-5, 20.0)
    q = 1.0 / math.cosh(z)**2
    return z, -d+u*lp*q, -d+u*lm*q


def main():
    lm, lp, zc, uc = parameters(1.0, 1.0/3.0)
    assert abs(lm-1/3) < 1e-12
    assert abs(lp-2/3) < 1e-12
    assert abs(zc-1.0886594924826534) < 1e-11
    assert abs(uc-4.100987229929905) < 1e-11
    print('critical z=',format(zc,'.14f'),'critical u=',format(uc,'.14f'))
    for u in (3.1, 4.0, 4.5, 7.0):
        z, lsum, ldiff = polar_eigenvalues(u,lm,lp)
        assert ldiff < 0
        assert (lsum > 0) == (u < uc)
        # Check equilibrium equation explicitly in two complementary blocks.
        s=z/lm
        f1=-s+u*math.tanh(lm*s)
        f2=s+u*math.tanh(-lm*s)
        assert abs(f1)+abs(f2) < 1e-11
        print('u=',u,'z=',format(z,'.10f'),'sum eigenvalue=',format(lsum,'.10f'),
              'difference eigenvalue=',format(ldiff,'.10f'))
    # Verify the exact critical identity, independent of rounded u.
    eigsumcrit=-1+uc*lp/(math.cosh(zc)**2)
    eigdiffcrit=-1+uc*lm/(math.cosh(zc)**2)
    assert abs(eigsumcrit) < 1e-12
    assert abs(eigdiffcrit+0.5) < 1e-12
    print('All reproducibility checks passed.')


if __name__ == '__main__':
    main()
