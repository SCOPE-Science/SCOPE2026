from fractions import Fraction as F


def haar_moments(n, s, d):
    assert 2 <= n and 1 <= s <= n and 1 <= d <= n
    eq11_sq = F(d * (d + 2), n * (n + 2))
    eq12_sq = F(d * (n - d), n * (n - 1) * (n + 2))
    c = eq11_sq + (s - 1) * eq12_sq
    theta = F(n, d) * c
    theta_closed = F(d + 2, n + 2) + F((s - 1) * (n - d), (n - 1) * (n + 2))
    assert theta == theta_closed
    return eq11_sq, eq12_sq, c, theta


def source_regime_example():
    n, s, d = 1000, 512, 32
    _, _, _, theta = haar_moments(n, s, d)
    new_rate_constant_over_L = F(2 * n, d) * theta
    source_rate_constant_over_L = F(36 * s, d)
    new_step_times_L = F(1, 1) / theta
    source_step_times_L = F(n, 18 * s)
    assert source_rate_constant_over_L / new_rate_constant_over_L == new_step_times_L / source_step_times_L
    return n, s, d, theta, new_rate_constant_over_L, source_rate_constant_over_L, new_step_times_L, source_step_times_L


def rank_one_sharpness(n, d):
    _, _, eq_q2, theta = haar_moments(n, 1, d)
    eq_q = F(d, n)
    t_star = eq_q / eq_q2
    assert t_star == F(1, 1) / theta
    min_contraction = 1 - eq_q * eq_q / eq_q2
    assert min_contraction == 1 - F(d, n) / theta
    return theta, t_star, min_contraction


if __name__ == '__main__':
    n, s, d, theta, c_new, c_source, a_new, a_source = source_regime_example()
    print(f'example n={n}, s={s}, d={d}')
    print(f'theta = {theta} = {float(theta):.12f}')
    print(f'new stationarity coefficient / L = {c_new} = {float(c_new):.12f}')
    print(f'source Theorem 6 coefficient / L = {c_source} = {float(c_source):.12f}')
    print(f'improvement factor = {c_source / c_new} = {float(c_source / c_new):.12f}')
    print(f'new alpha* L = {a_new} = {float(a_new):.12f}')
    print(f'source alpha L = {a_source} = {float(a_source):.12f}')

    theta1, tstar1, rho1 = rank_one_sharpness(50, 4)
    print('rank-one check n=50, d=4')
    print(f'theta = {theta1}')
    print(f'optimal alpha L = {tstar1}')
    print(f'exact minimum one-step quadratic contraction = {rho1}')

    # Limiting consistency checks.
    for n0 in (2, 5, 20):
        _, _, _, th_full = haar_moments(n0, n0, 1)
        assert th_full == 1
        _, _, _, th_dfull = haar_moments(n0, max(1, n0 // 2), n0)
        assert th_dfull == 1
    print('all exact rational checks passed')
