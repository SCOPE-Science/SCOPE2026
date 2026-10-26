"""Reproduce numerical checks of low-band asymptotics for a harmonic delta lattice.

Requires Python 3 and mpmath. Numerical checks are not the proof of the
all-fixed-index asymptotic theorem.
"""
import mpmath as mp

mp.mp.dps = 155


def dirichlet_shift(n, radius):
    """Root of a parity-reduced, finite-interval Dirichlet determinant."""
    a = mp.mpf(radius)
    s = n % 2
    m = (n - s) // 2
    b = mp.mpf(s) + mp.mpf('0.5')
    z = a * a
    initial = 2 ** (n + 2) * a ** (2 * n + 1) * mp.exp(-z) / (mp.factorial(n) * mp.sqrt(mp.pi))
    det = lambda shift: mp.hyp1f1(-m - shift / 4, b, z)
    d = mp.findroot(det, (mp.mpf('0.75') * initial, mp.mpf('1.25') * initial))
    assert d > 0
    assert abs(det(d)) < mp.mpf('1e-65')
    return d


def parity_function(x, energy, parity):
    x = mp.mpf(x)
    e = mp.mpf(energy)
    if parity == 0:
        return mp.exp(-x * x / 2) * mp.hyp1f1(-e / 4, mp.mpf('0.5'), x * x)
    return x * mp.exp(-x * x / 2) * mp.hyp1f1((2 - e) / 4, mp.mpf('1.5'), x * x)


def bandwidth_asymptotic(n, a):
    a = mp.mpf(a)
    c = 2 ** (n + 2) / (mp.factorial(n) * mp.sqrt(mp.pi))
    leading = c * a ** (2 * n + 1) * mp.exp(-a * a)
    two_term = leading * (1 - mp.mpf((n + 1) ** 2) / (2 * a * a))
    return leading, two_term


def run():
    count = 0
    print('n, a, exact_width, exact_over_leading, scaled_second_order_residual')
    for a in (6, 8, 10):
        shifts = [dirichlet_shift(n, a) for n in range(5)]
        for n in range(5):
            width = shifts[n] - (shifts[n - 1] if n else 0)
            assert width > 0
            leading, refined = bandwidth_asymptotic(n, a)
            assert abs(width - refined) < abs(width - leading)
            count += 2
            z = mp.mpf(a) ** 2
            residual = ((width / leading) - 1 + (n + 1) ** 2 / (2 * z)) * z ** 2
            print(n, a, mp.nstr(width, 14), mp.nstr(width / leading, 14), mp.nstr(residual, 10), sep=', ')
        # Exact shifted Dirichlet/Robin endpoint identity, sampled at high precision.
        for n in range(5):
            energy = 2 + 2 * n + shifts[n]
            switched_parity = (n + 1) % 2
            robin = mp.diff(lambda x: parity_function(x, energy, switched_parity), a) + a * parity_function(a, energy, switched_parity)
            assert abs(robin) < mp.mpf('1e-45')
            count += 1
    # Duplication-formula constant that joins even/odd Kummer sectors.
    for n in range(16):
        m, s = divmod(n, 2)
        b = mp.mpf(s) + mp.mpf('0.5')
        lhs = 4 / (mp.factorial(m) * mp.gamma(m + b))
        rhs = 2 ** (n + 2) / (mp.factorial(n) * mp.sqrt(mp.pi))
        assert mp.almosteq(lhs, rhs)
        count += 1
    print('PASS:', count, 'exact-identity and asymptotic-consistency assertions')


if __name__ == '__main__':
    run()
