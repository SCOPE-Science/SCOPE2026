"""Numerical cross-checks for logarithmic-phase radial Bergman moments.

Requires mpmath. The universal assertions rest on the accompanying analytic proof.
"""
import mpmath as mp

mp.mp.dps = 45


def beta_moment(n, a, tau):
    a, tau = mp.mpf(str(a)), mp.mpf(str(tau))
    fun = lambda t: (t**n * (1-t)**(a-1) *
                     mp.exp(1j * (-mp.log(1-t))**tau))
    return mp.quad(fun, [0, mp.mpf('0.5'), mp.mpf('0.9'),
                        mp.mpf('0.99'), mp.mpf('1')]) / mp.beta(n+1, a)


def contour_to_gamma_ratio(L, tau, a):
    """Ratio of deformed large-n gamma integral to its predicted factor.

    We integrate along the ray through the lower quadrant after factoring
    out the constant complex rotation and linear Mellin oscillation.
    """
    L, tau, a = map(lambda s: mp.mpf(str(s)), (L, tau, a))
    kappa = tau * L**(tau-1)
    theta = mp.atan(kappa/a)
    rot = mp.exp(-1j*theta)

    def integrand(u):
        if u == 0:
            return mp.mpc(0)
        z = kappa*u*rot
        remainder = (L-mp.log(z))**tau-L**tau+kappa*mp.log(z)
        return u**(a-1)*mp.exp(-kappa*u*rot-1j*kappa*mp.log(u)
                               +1j*remainder)

    cuts = [0, mp.mpf('0.1'), mp.mpf('0.4'), mp.mpf('0.7'), 1,
            mp.mpf('1.3'), mp.mpf('1.7'), mp.mpf('2.4'),
            mp.mpf('3.5'), 5, 8, 12, 20, 40]
    integral = mp.quad(integrand, cuts)
    return (integral*mp.exp(-1j*a*theta-1j*kappa*mp.log(kappa)
                            -kappa*theta)*kappa**a / mp.gamma(a-1j*kappa))


def run():
    checks = 0
    for a in ['0.7', '1', '2.5']:
        aa = mp.mpf(a)
        for n in [0, 3, 15]:
            direct = beta_moment(n, a, '1')
            expected = mp.beta(n+1, aa-1j)/mp.beta(n+1, aa)
            err = abs(direct-expected)
            assert err < mp.mpf('1e-26'), (a, n, err)
            checks += 1

    # Verify the subcritical gamma-law approximation in an accessible range.
    for a in ['1', '2']:
        for L in [40, 80]:
            tau = mp.mpf('0.6')
            phase = lambda x: mp.exp(1j*(L-mp.log(x))**tau)
            # On [0,40] the phase is real for either L.
            value = mp.quad(lambda x: x**(mp.mpf(a)-1)*mp.exp(-x)*phase(x),
                            [0, mp.mpf('0.1'), 1, 3, 10, 40]) / mp.gamma(a)
            assert abs(value/mp.exp(1j*L**tau)-1) < mp.mpf('0.11'), (a, L)
            checks += 1

    # Ratios need only move toward 1 as L increases; convergence is slow
    # when tau approaches 2. These are consistency checks, not a proof.
    for a, tau in [('1', '1.3'), ('2', '1.5')]:
        z_small = contour_to_gamma_ratio(100, tau, a)
        z_big = contour_to_gamma_ratio(500, tau, a)
        d_small, d_big = abs(z_small-1), abs(z_big-1)
        assert d_big < d_small and d_big < mp.mpf('0.30'), (
            a, tau, d_small, d_big)
        checks += 2
        print('MELLIN_RATIO', a, tau, 'L=100', mp.nstr(z_small, 14),
              'L=500', mp.nstr(z_big, 14), flush=True)

    print('VERIFY_OK', checks, 'beta identities, subcritical phase, and complex-contour gamma ratios')


if __name__ == '__main__':
    run()
