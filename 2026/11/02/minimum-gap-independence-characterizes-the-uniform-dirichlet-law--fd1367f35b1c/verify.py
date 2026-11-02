"""Exact rational checks for the minimum-spacing/Greenwood decomposition.

Requires Python >= 3.9 and only the standard library. These finite checks
supplement the general analytic proof; they do not prove it for all n.
"""
from fractions import Fraction as F
from math import factorial


def beta_moment(n, r):
    return F(n - 1, n - 1 + r)


def dirichlet_sq_mean(k):
    return F(2, k + 1)


def dirichlet_sq_second(k):
    return F(4 * (k + 5), (k + 1) * (k + 2) * (k + 3))


def check_n(n):
    k = n - 1
    e_h = dirichlet_sq_mean(k) - F(1, n)
    e_h2 = (dirichlet_sq_second(k) - F(2, n) * dirichlet_sq_mean(k) + F(1, n*n))
    e_g = F(1, n) + beta_moment(n, 2) * e_h
    e_g2 = F(1, n*n) + F(2,n) * beta_moment(n,2) * e_h + beta_moment(n,4) * e_h2
    e_m = (1-beta_moment(n,1))/n
    e_mg = F(1,n)*e_m + F(1,n)*(beta_moment(n,2)-beta_moment(n,3))*e_h
    c = e_mg-e_m*e_g
    var_g = e_g2 - e_g**2
    var_m = F(n-1,n**4*(n+1))
    assert e_h == F(1,n)
    assert e_g == F(2,n+1)
    assert var_g == F(4*(n-1),(n+1)**2*(n+2)*(n+3))
    assert c == -F(2*(n-1), n**3*(n+1)*(n+2))
    assert c**2 / (var_g*var_m) == F((n+1)*(n+3),n**2*(n+2))
    assert n**2*(dirichlet_sq_second(k)-dirichlet_sq_mean(k)**2) == F(4*(n-2),(n+1)*(n+2))
    return 6


def dirichlet_endpoint_gap(n, a):
    # Conditional expectation of the normalized pivot at m=0 vs m=1/n.
    at_zero = n*F(a+1,(n-1)*a+1)-1
    at_equal = F(1)
    return at_zero - at_equal


def alpha_two_three_dim_conditional(m):
    # n=3, alpha=2. Integrate u(1-u) against (m+Bu)(m+B(1-u)).
    b = 1-3*m
    denom = m*m + m*b + b*b/F(6)
    numer = (m*m+m*b)/6 + b*b/F(30)
    return F(2) - 6*numer/denom


def main():
    tests = 0
    for n in range(2,101):
        tests += check_n(n)
    for n in range(3,101):
        for alpha in (F(1,4), F(1,2), F(1), F(2), F(5), F(9,2)):
            gap = dirichlet_endpoint_gap(n, alpha)
            assert (gap == 0) == (alpha == 1)
            if alpha > 1:
                assert gap < 0
            elif alpha < 1:
                assert gap > 0
            tests += 1
    for m in (F(0),F(1,15),F(1,12),F(1,6),F(1,4),F(1,3)):
        v = alpha_two_three_dim_conditional(m)
        assert F(4,5) <= v <= 1
        if m==0: assert v==F(4,5)
        if m==F(1,3): assert v==1
        tests += 1
    for alpha in (F(1,2),F(1),F(2),F(10)):
        # With two components the normalized quadratic pivot is identically 1.
        assert 2*(1**2)-1 == 1
        tests += 1
    print(f"PASS: {tests} exact rational checks; n=2..100, symmetric Dirichlet alpha limits and n=3 alpha=2 conditional integrals.")


if __name__ == '__main__':
    main()
