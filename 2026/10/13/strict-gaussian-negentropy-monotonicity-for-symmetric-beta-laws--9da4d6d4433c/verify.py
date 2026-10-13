"""Numerical cross-checks for Gaussian negentropy of symmetric beta laws.

Requires Python 3.9+ and mpmath >= 1.3. The mathematical proof is analytic;
these finite checks are diagnostics and not certificates for all shape parameters.
"""
import mpmath as mp

mp.mp.dps = 75


def entropy(a):
    return mp.log(mp.beta(a, a)) - 2 * (a - 1) * (mp.digamma(a) - mp.digamma(2 * a))


def negentropy(a):
    variance = 1 / (4 * (2 * a + 1))
    return mp.log(2 * mp.pi * mp.e * variance) / 2 - entropy(a)


def derivative(a):
    return -1 / (2 * a + 1) + (a - 1) * (
        mp.polygamma(1, a) - mp.polygamma(1, a + mp.mpf('0.5'))
    )


def gaussian_divergence(a, mean, variance):
    beta_variance = 1 / (4 * (2 * a + 1))
    return (mp.log(2 * mp.pi * variance) +
            (beta_variance + (mp.mpf('0.5') - mean) ** 2) / variance) / 2 - entropy(a)


def run():
    shape_values = [mp.mpf(s) for s in (
        '0.05', '0.1', '0.2', '0.5', '0.75', '1', '1.01', '1.5',
        '2', '3', '5', '10', '25', '100', '1000'
    )]
    assert all(negentropy(a) > 0 for a in shape_values)
    assert all(negentropy(shape_values[i]) > negentropy(shape_values[i + 1])
               for i in range(len(shape_values) - 1))
    for a in shape_values:
        assert derivative(a) < 0
        assert mp.fabs(derivative(a) - mp.diff(negentropy, a)) < mp.mpf('1e-60')
        v = 1 / (4 * (2 * a + 1))
        assert mp.fabs(gaussian_divergence(a, mp.mpf('0.5'), v) - negentropy(a)) < mp.mpf('1e-65')
        for mean, variance in [(mp.mpf('0.45'), v), (mp.mpf('0.5'), 2*v), (mp.mpf('0.5'), v/2)]:
            assert gaussian_divergence(a, mean, variance) > negentropy(a)

    for a in [mp.mpf(2), mp.mpf(3), mp.mpf(8), mp.mpf(100)]:
        delta = mp.polygamma(1, a) - mp.polygamma(1, a + mp.mpf('0.5'))
        assert 0 < delta < 2 / (2 * a - mp.mpf('0.5')) ** 2
        assert (2 * a - mp.mpf('0.5')) ** 2 - 2*(a-1)*(2*a+1) == mp.mpf(9)/4

    # Check the asymptotic coefficients without treating finite values as proof.
    for a in [mp.mpf(100), mp.mpf(1000), mp.mpf(10000)]:
        assert abs(a*a*negentropy(a)-mp.mpf(3)/16) < mp.mpf(1)/(10*a*a)
        assert abs(a*a*a*derivative(a)+mp.mpf(3)/8) < mp.mpf(1)/(10*a*a)

    for n in [1,3,5,19,199,1999]:
        m = mp.mpf(n+1)/2
        # The median in an odd uniform sample is Beta(m,m).
        variance = mp.mpf(1)/(4*(n+2))
        assert mp.fabs(negentropy(m) - gaussian_divergence(m, mp.mpf('0.5'), variance)) < mp.mpf('1e-65')
    print('PASS: 15 shape values; derivatives, optimum, positivity;'
          ' 4 trigamma bounds; 3 rate checks; 6 odd-sample identities.')
    print('Example J(1):', mp.nstr(negentropy(mp.mpf(1)), 18))
    print('At a=1000, a^2 J(a):', mp.nstr(1000000*negentropy(mp.mpf(1000)), 18))


if __name__ == '__main__':
    run()
