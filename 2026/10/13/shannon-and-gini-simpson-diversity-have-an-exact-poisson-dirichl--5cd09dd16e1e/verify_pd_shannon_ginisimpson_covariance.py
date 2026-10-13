#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 70

def rising(x, t):
    return mp.gamma(x + t) / mp.gamma(x)

def mixed_power(alpha, theta, u, v):
    return (
        rising(1-alpha, u+v-1)
        + (theta+alpha) * rising(1-alpha, u-1) * rising(1-alpha, v-1)
    ) / rising(theta+1, u+v-1)

def beta_moment(a, b, p=0, q=0):
    return mp.beta(a+p, b+q) / mp.beta(a, b)

def beta_moment_logx(a, b, p=0, q=0):
    m = beta_moment(a, b, p, q)
    return m * (mp.digamma(a+p) - mp.digamma(a+b+p+q))

def beta_moment_log1mx(a, b, p=0, q=0):
    m = beta_moment(a, b, p, q)
    return m * (mp.digamma(b+q) - mp.digamma(a+b+p+q))

def means(alpha, theta):
    es2 = (1-alpha) / (theta+1)
    eh = mp.digamma(theta+1) - mp.digamma(1-alpha)
    return es2, eh

def es2h_by_gamma_derivative(alpha, theta):
    return -mp.diff(lambda v: mixed_power(alpha, theta, 2, v), 1)

def es2h_by_beta(alpha, theta):
    a1 = 1-alpha
    b1 = theta+alpha
    a2 = 1-alpha
    b2 = theta+2*alpha

    # Same-index contribution: -E[V1^2 log V1].
    same = -beta_moment_logx(a1, b1, p=2, q=0)

    # Ordered distinct-index contribution:
    # -E[V1(1-V1){log(1-V1)+log V2}].
    v1_weight = beta_moment(a1, b1, p=1, q=1)
    log_1mv1_weight = beta_moment_log1mx(a1, b1, p=1, q=1)
    elog_v2 = mp.digamma(a2) - mp.digamma(a2+b2)
    distinct = -(log_1mv1_weight + v1_weight * elog_v2)
    return same + distinct

def cov_dh_closed(alpha, theta):
    return (theta+alpha) / ((theta+1)**2 * (theta+2))

def var_d_closed(alpha, theta):
    return (
        2*(1-alpha)*(theta+alpha)
        / ((theta+1)**2*(theta+2)*(theta+3))
    )

def var_h_closed(alpha, theta):
    return (
        (theta+alpha) / ((theta+1)**2*(1-alpha))
        + (1-alpha)/(theta+1) * mp.polygamma(1, 2-alpha)
        - mp.polygamma(1, theta+2)
    )

def corr_closed(alpha, theta):
    cov = cov_dh_closed(alpha, theta)
    return cov / mp.sqrt(var_d_closed(alpha, theta) * var_h_closed(alpha, theta))

def corr_limit(alpha):
    c = (1-alpha)*mp.polygamma(1, 1-alpha) - 1
    return 1 / mp.sqrt(2*(1-alpha)*c)

def check_close(x, y, tol=mp.mpf("1e-45")):
    scale = max(mp.mpf(1), abs(x), abs(y))
    assert abs(x-y) <= tol*scale, (x, y, abs(x-y))

def run():
    alphas = [
        mp.mpf("0"),
        mp.mpf("0.1"),
        mp.mpf("0.3"),
        mp.mpf("0.5"),
        mp.mpf("0.75"),
        mp.mpf("0.9"),
    ]
    theta_grid = {
        mp.mpf("0"): [mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("5"), mp.mpf("20")],
        mp.mpf("0.1"): [mp.mpf("0.0"), mp.mpf("0.2"), mp.mpf("1"), mp.mpf("5"), mp.mpf("20")],
        mp.mpf("0.3"): [mp.mpf("0.0"), mp.mpf("0.2"), mp.mpf("1"), mp.mpf("5"), mp.mpf("20")],
        mp.mpf("0.5"): [mp.mpf("0.0"), mp.mpf("0.2"), mp.mpf("1"), mp.mpf("5"), mp.mpf("20")],
        mp.mpf("0.75"): [mp.mpf("0.0"), mp.mpf("0.2"), mp.mpf("1"), mp.mpf("5"), mp.mpf("20")],
        mp.mpf("0.9"): [mp.mpf("0.0"), mp.mpf("0.2"), mp.mpf("1"), mp.mpf("5"), mp.mpf("20")],
    }

    mixed_checks = 0
    covariance_checks = 0
    variance_checks = 0
    correlation_checks = 0

    for alpha in alphas:
        for theta in theta_grid[alpha]:
            if theta <= -alpha:
                continue

            es2, eh = means(alpha, theta)
            m1 = es2h_by_gamma_derivative(alpha, theta)
            m2 = es2h_by_beta(alpha, theta)
            check_close(m1, m2, mp.mpf("2e-44"))
            mixed_checks += 1

            cov_s2_h_1 = m1 - es2*eh
            cov_s2_h_2 = m2 - es2*eh
            target = -cov_dh_closed(alpha, theta)
            check_close(cov_s2_h_1, target, mp.mpf("2e-44"))
            check_close(cov_s2_h_2, target, mp.mpf("2e-44"))
            covariance_checks += 2

            m22 = mixed_power(alpha, theta, 2, 2)
            vard_from_mixed = m22 - es2**2
            check_close(vard_from_mixed, var_d_closed(alpha, theta), mp.mpf("2e-44"))
            assert var_d_closed(alpha, theta) > 0
            assert var_h_closed(alpha, theta) > 0
            variance_checks += 3

            rho = corr_closed(alpha, theta)
            assert 0 < rho < 1
            correlation_checks += 1

    asymptotic_checks = 0
    for alpha in [mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.8"), mp.mpf("0.95")]:
        target = corr_limit(alpha)
        rho = corr_closed(alpha, mp.mpf("1000000"))
        assert abs(rho-target) < mp.mpf("2e-5")
        asymptotic_checks += 1

    dp_target = 1/mp.sqrt(2*(mp.pi**2/6-1))
    check_close(corr_limit(mp.mpf("0")), dp_target, mp.mpf("1e-50"))

    print(
        "VERIFY_OK "
        f"mixed_checks={mixed_checks} "
        f"covariance_checks={covariance_checks} "
        f"variance_checks={variance_checks} "
        f"correlation_checks={correlation_checks} "
        f"asymptotic_checks={asymptotic_checks} "
        f"dirichlet_limit={mp.nstr(dp_target, 16)}"
    )

if __name__ == "__main__":
    run()
