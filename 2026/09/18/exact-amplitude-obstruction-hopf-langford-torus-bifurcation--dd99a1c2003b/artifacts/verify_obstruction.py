from math import pi, isclose


def weighted_divergence(s, alpha, mu, gamma):
    D = (1.0 + 2.0 * gamma) * mu - 2.0 * gamma * alpha
    return D * s ** (gamma - 1.0)


def first_integral_derivative(s, z, c, gamma):
    # On the neutral surface alpha=(1+2 gamma)c, mu=2 gamma c.
    alpha = (1.0 + 2.0 * gamma) * c
    mu = 2.0 * gamma * c
    ds = 2.0 * s * (mu - alpha + z)
    dz = mu * z - gamma * (s + z * z)

    Hs = gamma * s ** (gamma - 1.0) * ((z - c) ** 2 - c * c) + gamma * s ** gamma
    Hz = 2.0 * s ** gamma * (z - c)
    return Hs * ds + Hz * dz


def source_curve_check():
    # Admissible source-theorem coefficients alpha1=gamma0=omega=1,
    # alpha2=gamma1=mu2=0.
    alpha1 = gamma0 = omega = 1.0
    muhat0 = 2.0 / 3.0
    condition3 = (muhat0 - alpha1) * (alpha1 * gamma0 - (gamma0 + 1.0) * muhat0)
    condition4 = (
        4.0 * alpha1**2 * gamma0 * (gamma0 + 2.0)
        - 4.0 * alpha1 * (gamma0 + 2.0) * (2.0 * gamma0 + 1.0) * muhat0
        + (2.0 * gamma0 + 3.0) ** 2 * muhat0**2
    )
    paper_muhat1 = (8.0 * pi * pi - 2.0) / 27.0
    exact_muhat1 = 0.0
    return condition3, condition4, paper_muhat1, exact_muhat1


def example2_check(eps=1e-3):
    alpha = eps + 0.01 * eps**2
    beta = 0.1 + 4.43 * eps + 0.04 * eps**2
    gamma = -1.0 - eps + 0.04 * eps**2
    mu = 3.99317 * eps + 0.04 * eps**2
    z_star = alpha - mu
    s_star = z_star * (mu / gamma - z_star)
    trace = (1.0 + 2.0 * gamma) * mu - 2.0 * gamma * alpha
    determinant = 2.0 * gamma * s_star
    return alpha, beta, gamma, mu, s_star, trace, determinant


if __name__ == "__main__":
    # Direct checks of the neutral first integral at several positive points.
    for s, z, c, g in [
        (0.7, 0.2, 0.3, 0.6),
        (1.4, -0.5, 0.2, 1.0),
        (0.3, 0.8, 0.1, 2.5),
    ]:
        val = first_integral_derivative(s, z, c, g)
        assert abs(val) < 1e-12, val

    c3, c4, paper_m1, exact_m1 = source_curve_check()
    assert c3 > 0.0 and c4 < 0.0
    assert paper_m1 > 2.8 and isclose(exact_m1, 0.0)

    alpha, beta, gamma, mu, s_star, trace, det = example2_check()
    assert gamma < 0.0
    assert s_star > 0.0
    assert det < 0.0

    print(f"admissible_test_condition3={c3:.12g}")
    print(f"admissible_test_condition4={c4:.12g}")
    print(f"paper_muhat1={paper_m1:.12g}")
    print(f"exact_neutral_muhat1={exact_m1:.12g}")
    print(f"example2_gamma={gamma:.12g}")
    print(f"example2_s_star={s_star:.12g}")
    print(f"example2_trace={trace:.12g}")
    print(f"example2_determinant={det:.12g}")
