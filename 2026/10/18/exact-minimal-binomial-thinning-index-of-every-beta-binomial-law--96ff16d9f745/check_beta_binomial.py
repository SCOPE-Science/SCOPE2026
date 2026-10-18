"""Exact-rational checks of finite beta-binomial inverse thinning coefficients.

The mathematical theorem for all real positive shapes and all sample sizes
rests on the analytic beta-Stein induction, not on these finite checks.
Run: python3 check_beta_binomial.py
"""
from fractions import Fraction
from math import comb


def rising(x, n):
    result = Fraction(1)
    for i in range(n):
        result *= x + i
    return result


def moment(a, b, k):
    return rising(a, k) / rising(a+b, k)


def inverse_coefficients(n, a, b, scale):
    output = []
    for k in range(n+1):
        m = n-k
        expected = sum(
            (-1)**j * comb(m, j) * scale**(m-j) * moment(a,b,k+j)
            for j in range(m+1)
        )
        output.append(comb(n,k) * expected / (scale**n))
    return output


def run():
    shapes = [Fraction(1,3), Fraction(1,2), Fraction(1), Fraction(2),
              Fraction(5,2), Fraction(3)]
    cases = 0
    for n in range(1,9):
        for a in shapes:
            for b in shapes:
                rho = (a+n-1)/(a+b+n-1)
                q = inverse_coefficients(n,a,b,rho)
                assert all(v>=0 for v in q), (n,a,b,rho,q)
                assert sum(q) == 1
                assert q[n-1] == 0, (n,a,b,q)
                smaller = rho * Fraction(99,100)
                q_smaller = inverse_coefficients(n,a,b,smaller)
                assert q_smaller[n-1] < 0, (n,a,b,smaller)
                p = [comb(n,k)*rising(a,k)*rising(b,n-k)/rising(a+b,n)
                     for k in range(n+1)]
                for k in range(n+1):
                    reconstructed = sum(q[j]*comb(j,k)*rho**k*(1-rho)**(j-k)
                                        for j in range(k,n+1))
                    assert p[k] == reconstructed, (n,a,b,k)
                cases += 1
    print(f"PASS: {cases} exact-rational shape/sample instances, "
          "nonnegative inverse coefficients, sharp negative boundary, "
          "and full thinning reconstruction")


if __name__ == '__main__':
    run()
