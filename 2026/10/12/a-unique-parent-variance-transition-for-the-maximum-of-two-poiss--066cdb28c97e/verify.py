"""Direct finite checks for the Poisson two-sample maximum variance formula.

Uses only Python standard library Decimal. These numerical checks supplement,
but do not replace, the analytic proof of the all-parameter theorem.
"""
from decimal import Decimal, getcontext

getcontext().prec = 72
ONE = Decimal(1)
ZERO = Decimal(0)


def bessel01(lam, terms=150):
    """Series I_0(2*lam), I_1(2*lam)."""
    a, b = ONE, lam
    sa, sb = a, b
    for k in range(1, terms + 1):
        a *= lam * lam / (Decimal(k) * Decimal(k))
        b *= lam * lam / (Decimal(k) * Decimal(k+1))
        sa += a
        sb += b
    return sa, sb


def closed_moments(lam):
    i0, i1 = bessel01(lam)
    e = (-2*lam).exp()
    k = e * i0
    h = lam * e * (i0+i1)
    mu = lam+h
    var = lam + lam*k-h*h
    ratio = h*h/(lam*k)
    return mu, var, ratio


def direct_max_moments(lam, max_k=170):
    """Directly sum F(k)^2-F(k-1)^2, independent of Bessel identity."""
    pk = (-lam).exp()
    cdf = ZERO
    mom1 = mom2 = ZERO
    for k in range(max_k + 1):
        old = cdf
        cdf += pk
        mass = cdf*cdf-old*old
        mom1 += Decimal(k)*mass
        mom2 += Decimal(k*k)*mass
        pk *= lam/Decimal(k+1)
    return mom1, mom2-mom1*mom1, cdf


def bisect_boundary():
    lo, hi = Decimal('1'), Decimal('2')
    for _ in range(130):
        mid = (lo+hi)/2
        ratio = closed_moments(mid)[2]
        if ratio < ONE:
            lo = mid
        else:
            hi = mid
    return lo, hi


def run():
    cases = ['0.01', '0.05', '0.1', '0.2', '0.5', '0.75',
             '1', '1.1', '1.16', '1.17', '1.2', '1.5', '2', '3', '5', '8']
    worst = ZERO
    for s in cases:
        lam = Decimal(s)
        cm, cv, ratio = closed_moments(lam)
        dm, dv, cdf = direct_max_moments(lam)
        e = max(abs(cm-dm), abs(cv-dv))
        worst = max(worst, e)
        assert e < Decimal('1e-42'), (s, e)
        assert abs(cdf-ONE) < Decimal('1e-50'), (s,cdf)
        assert ((cv-lam)>0) == (ratio<ONE), s
        assert cv < cm, s
    lo, hi = bisect_boundary()
    assert Decimal('1.16679740191840365086') < lo < hi < Decimal('1.16679740191840365088')
    assert closed_moments(Decimal('1'))[1] > Decimal('1')
    assert closed_moments(Decimal('2'))[1] < Decimal('2')
    print('VERIFY_OK direct_max_cases=%d max_abs_difference=%s' % (len(cases),worst))
    print('critical_lambda_bracket=[%s,%s]' % (lo, hi))
    print('var_max_lambda1=%s' % closed_moments(Decimal('1'))[1])
    print('var_max_lambda2=%s' % closed_moments(Decimal('2'))[1])


if __name__ == '__main__':
    run()
