"""Exact independent checks for the threshold-exceedance/convex-spacing theorem.
Scientific reproducibility only; no external services required.
"""
from fractions import Fraction as Q
from math import comb, factorial, exp, sqrt


def moment(m, power):
    return Q(factorial(power) * factorial(m - 1), factorial(m + power - 1))


def direct_tail_first(m, power, t):
    # Independently integrate x^power (m-1)(1-x)^(m-2) over [t,1].
    return (m - 1) * sum(
        Q((-1)**k * comb(m - 2, k), power + k + 1)
        * (1 - t**(power + k + 1))
        for k in range(m - 1)
    )


def direct_tail_other(m, power, t):
    # Integrate E[X_2^power | X_1=s] over the beta density of X_1.
    return moment(m, power) * (1 - t)**(m + power - 1)


def direct_covariance(m, power, t):
    p = (1 - t)**(m - 1)
    mixed = m * (direct_tail_first(m, power, t)
                 + (m - 1) * direct_tail_other(m, power, t))
    return mixed - m * p * (m * moment(m, power))


def shifted_covariance(m, power, t):
    # Condition on X_1>t by independent affine-simplex-volume reasoning.
    h = sum(comb(power, j) * t**(power-j) * (1-t)**j * moment(m, j)
            for j in range(power+1))
    h += (m-1) * (1-t)**power * moment(m, power)
    return m * (1-t)**(m-1) * (h - m * moment(m, power))


def quadratic_closed(m, t):
    return Q(m-1, m+1)*t*(1-t)**(m-1)*((m+2)*t-2)


def var_q(m):
    return Q(4*(m-1), (m+1)**2*(m+2)*(m+3))


def var_k(m, t):
    p = (1-t)**(m-1)
    q = max(Q(0),1-2*t)**(m-1)
    return m*p*(1-p)+m*(m-1)*(q-p*p)


def corr(m, t):
    # Float expressions avoid giant exact powers in the large-m diagnostic.
    t = float(t)
    p=(1-t)**(m-1)
    q=max(0.,1-2*t)**(m-1)
    vk=m*p*(1-p)+m*(m-1)*(q-p*p)
    vq=4*(m-1)/((m+1)**2*(m+2)*(m+3))
    cv=(m-1)/(m+1)*t*(1-t)**(m-1)*((m+2)*t-2)
    return cv/sqrt(vk*vq)


def lim_corr(c):
    return c*(c-2)/(2*sqrt(exp(c)-1-c*c))


def run():
    tests = 0
    for m in range(2,14):
        for j in range(1,16):
            t = Q(j,16)
            for degree in range(2,7):
                a=direct_covariance(m,degree,t)
                b=shifted_covariance(m,degree,t)
                assert a==b, (m,degree,t,a,b)
                tests += 1
                if degree == 2:
                    assert a == quadratic_closed(m,t), (m,t,a)
                    tests += 1
                    root=Q(2,m+2)
                    assert (a>0)-(a<0) == (t>root)-(t<root), (m,t,a)
                    tests += 1
            assert var_k(m,t)>=0 and (var_k(m,t)==0)==(m==2 and t==Q(1,2)), (m,t)
            tests += 1
        # Fourth-moment derivation: E[sum(X_i^2)^2].
        second = m*moment(m,4) + m*(m-1)*Q(4, m*(m+1)*(m+2)*(m+3))
        assert second - (m*moment(m,2))**2 == var_q(m)
        tests += 1
    for c in (0.5,1,1.5,2,3,4,6):
        approximate=corr(100000,c/100000)
        target=lim_corr(c)
        assert abs(approximate-target)<0.0003,(c,approximate,target)
        tests += 1
    print('PASS', tests, 'independent exact-rational and asymptotic checks')
    for c in (0.5,1,2,3,4):
        print('limit correlation at c=',c,':',f'{lim_corr(c):.10f}')

if __name__=='__main__':run()
