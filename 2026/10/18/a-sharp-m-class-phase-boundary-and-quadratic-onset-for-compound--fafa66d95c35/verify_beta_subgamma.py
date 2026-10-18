"""Reproduce exact rational moment identities and numerical scale comparisons.

Uses the Python standard library only. Exact rational checks test the algebra;
they do not replace the analytic proof of the infinite-parameter theorem.
"""
from fractions import Fraction as Q
from math import factorial, isfinite


def rising(x, n):
    ans = Q(1)
    for j in range(n):
        ans *= x + j
    return ans


def moment(n, a, b):
    return 2 * rising(a, n) / ((n + 1) * (n + 2) * rising(b, n))


def series_mgf(t, a, b, terms=250):
    """MGF for R = B Y, B~Beta(1,2), Y~Beta(a,b-a)."""
    out, coeff, power = 1.0, 1.0, 1.0
    aa, bb = float(a), float(b)
    for n in range(1, terms):
        coeff *= (aa+n-1)/((bb+n-1)*(n+2))
        power *= t
        inc = coeff*power
        out += inc
        if abs(inc) < 1.e-16*max(1.0, out) and n > 12:
            break
    return out


def psi(t, a, b):
    mgf = series_mgf(t, a, b)
    return (1-1/mgf)/t


def run():
    count = 0
    alphas = [Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(3,2),Q(3)]
    betas = [Q(1,10),Q(1),Q(5),Q(10),Q(20),Q(50),Q(200)]
    for alpha in alphas:
        a = alpha+2
        for beta in betas:
            b = a+beta
            m = a/(3*b)
            for n in range(0, 16):
                an = moment(n,a,b)/factorial(n)
                an1 = moment(n+1,a,b)/factorial(n+1)
                assert an1/an == (a+n)/((b+n)*(n+3)); count += 1
                if n >= 1:
                    sign = (an1/an-m) * (b+n)*(n+3)*3*b/n
                    assert sign == b*(3-a)-a*(n+3); count += 1
            m2=moment(2,a,b)
            deriv=m2/2-m*m
            assert deriv == a*(b*(3-a)-4*a)/(36*b*b*(b+1)); count+=1
            favorable = alpha >= 1 or beta <= a*(a+1)/(1-alpha)
            assert (deriv <= 0) == favorable; count += 1
            for n in range(1,20):
                an=moment(n,a,b)/factorial(n)
                if favorable:
                    assert an <= m**n; count += 1
    # Sharp transition equality and algebraic critical constants.
    for alpha in [Q(1,10),Q(1,4),Q(1,2),Q(3,4)]:
        a=alpha+2
        beta0=a*(a+1)/(1-alpha)
        b=a+beta0
        m=a/(3*b)
        A=moment(2,a,b)/2-m*m
        B=moment(3,a,b)/6-m*moment(2,a,b)+m**3
        assert A==0; count+=1
        assert B==-(a-3)**4/(8640*(a+3)); count+=1
        # Derivative of A(b) at the critical b, exact quotient derivative.
        A1=(a-3)**4/(1728*a*(a+1))
        onset_t=-A1/(2*B)
        onset_c=-A1*A1/(4*B)
        assert onset_t==5*(a+3)/(2*a*(a+1)); count+=1
        assert onset_c==5*(3-a)**4*(a+3)/(6912*a*a*(a+1)**2); count+=1
        # At the boundary the scale function strictly falls below its origin limit.
        for t in (.1,.5,1.,2.,4.,8.,16.):
            assert psi(t,a,b)<float(m)+1e-12; count+=1
    # Independent numerical corroboration: over threshold a positive t improves m.
    for alpha in (Q(1,10),Q(1,4),Q(1,2)):
        a=alpha+2
        beta0=a*(a+1)/(1-alpha)
        for delta in (Q(1),Q(5),Q(30)):
            b=a+beta0+delta
            m=float(a/(3*b))
            assert any(psi(k/10,a,b)>m+1e-8 for k in range(1,201)); count+=1
    # Direct double-moment identity for canonical factorization, independent of intensity.
    for alpha in alphas:
        a=alpha+2
        for beta in betas:
            b=a+beta
            for n in range(0,8):
                # Moment of size-biased jump divided by E[J^2], times Beta(1,2).
                eb=Q(2, (n+1)*(n+2))
                jump_ratio=rising(a,n)/rising(b,n)
                assert moment(n,a,b)==eb*jump_ratio; count+=1
    print(f"PASS: {count} exact rational / numerical consistency assertions")

if __name__=='__main__':
    run()
