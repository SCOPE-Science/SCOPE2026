import math


def run(c=2.0, x0=1.2, sigma0=1.1, rho0=0.4, ratio=0.5, steps=300):
    assert c > 0.0 and 0.0 < abs(x0) < c and sigma0 >= 1.0
    x = x0
    sigma = sigma0
    total_rho = 0.0
    prev_abs = abs(x)
    for k in range(steps):
        rho = rho0 * (ratio ** k)
        total_rho += rho
        beta = rho / (2.0*c*c + rho)

        # Direct scalar minimizer of 0.5*(x-c*t)^2 + rho/4*t^2.
        t = 2.0*c*x / (2.0*c*c + rho)
        assert abs(t) < 1.0
        combo = x - c*t
        assert math.isclose(combo, beta*x, rel_tol=2e-14, abs_tol=2e-14)

        old_x = x
        old_sigma = sigma
        p = -combo / old_sigma
        x = old_x + p
        sigma = old_sigma + old_sigma*p*p

        assert math.isclose(x, old_x*(1.0-beta/old_sigma), rel_tol=2e-14, abs_tol=2e-14)
        assert math.isclose(sigma, old_sigma + beta*beta*old_x*old_x/old_sigma, rel_tol=2e-14, abs_tol=2e-14)
        assert x*old_x > 0.0
        assert abs(x) <= prev_abs
        assert abs(x) < c
        prev_abs = abs(x)

    # Exact infinite geometric rho mass; the omitted tail is negligible here.
    S = rho0/(1.0-ratio)
    movement_bound = abs(x0)*S/(2.0*c*c*sigma0)
    assert abs(x0-x) <= movement_bound + 1e-13
    assert 0.0 < abs(x) < abs(x0)

    # Limit multiplier predicted by rho -> 0.
    lam1_lim = 0.5*(1.0 + x/c)
    lam2_lim = 0.5*(1.0 - x/c)
    assert lam1_lim > 0.0 and lam2_lim > 0.0
    assert abs(lam1_lim-lam2_lim) > 1e-6

    # Parameter remains finite; analytic proof gives a global summable bound.
    sigma_bound = sigma0 + x0*x0*S/(2.0*c*c*sigma0)
    assert sigma <= sigma_bound + 1e-13

    print('VERIFY_OK')
    print(f'x_approx={x:.15g}')
    print(f'sigma_approx={sigma:.15g}')
    print(f'movement={abs(x0-x):.15g}')
    print(f'movement_bound={movement_bound:.15g}')
    print(f'lambda_limit_approx=({lam1_lim:.15g},{lam2_lim:.15g})')


if __name__ == '__main__':
    run()
