from fractions import Fraction

def beta_moment(n, q):
    # Y ~ Beta(n-1, 2): E[Y^q] = (n-1)_q/(n+1)_q.
    out = Fraction(1)
    for j in range(q):
        out *= Fraction(n - 1 + j, n + 1 + j)
    return out

def check(max_n=250):
    checks = 0
    for n in range(2, max_n + 1):
        p = n - 2
        c = Fraction((n + 1) * (n + 2), 12 * n * (n - 1))

        # Conditional normalized sample variance with endpoints 0 and 1.
        e_sum_sq = Fraction(1) + Fraction(p, 3)
        e_square_sum = Fraction(p, 12) + Fraction(n * n, 4)
        c_direct = (e_sum_sq - e_square_sum / n) / (n - 1)
        assert c_direct == c
        checks += 1

        m1, m2, m3, m4 = [beta_moment(n, q) for q in range(1, 5)]
        assert m1 == Fraction(n - 1, n + 1)
        assert m2 == Fraction(n * (n - 1), (n + 1) * (n + 2))
        assert m3 == Fraction(n * (n - 1), (n + 2) * (n + 3))
        assert m4 == Fraction(n * (n - 1), (n + 3) * (n + 4))
        checks += 4

        # Set interval length ell=1; scale powers can then be restored analytically.
        assert c * m2 == Fraction(1, 12)
        checks += 1

        var_r = m2 - m1 * m1
        assert var_r == Fraction(2 * (n - 1), (n + 1)**2 * (n + 2))
        checks += 1

        mu4 = Fraction(1, 80)
        sig2 = Fraction(1, 12)
        var_s2 = Fraction(1, n) * (mu4 - Fraction(n - 3, n - 1) * sig2 * sig2)
        assert var_s2 == Fraction(2 * n + 3, 360 * n * (n - 1))
        checks += 1

        cov = c * (m3 - m1 * m2)
        assert cov == Fraction(1, 3 * (n + 1) * (n + 3))
        checks += 1

        corr2 = cov * cov / (var_r * var_s2)
        assert corr2 == Fraction(20 * n * (n + 2), (n + 3)**2 * (2 * n + 3))
        checks += 1

        var_hat = c * c * (m4 - m2 * m2)
        assert var_hat == Fraction(2*n*n + 6*n + 1, 36*n*(n-1)*(n+3)*(n+4))
        checks += 1

        ratio = var_hat / var_s2
        assert ratio == Fraction(10 * (2*n*n + 6*n + 1), (n+3)*(n+4)*(2*n+3))
        checks += 1

        deficit = Fraction(1) - ratio
        assert deficit == Fraction((n-2)*(2*n*n+n-13), (n+3)*(n+4)*(2*n+3))
        assert (deficit == 0) if n == 2 else (deficit > 0)
        checks += 2

    print('VERIFY_OK')
    print(f'max_n={max_n}')
    print(f'exact_checks={checks}')

if __name__ == '__main__':
    check()
