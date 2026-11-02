"""Reproduce the exact two-by-two split-flow formulas and check asymptotic endpoint geometry.
The universal assertion is proved analytically in RESULT.md; finite checks are corroboration.
"""
from math import cos, sin, exp, sqrt, pi, log, isclose


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(2)) for i in range(2)]


def epsilon_for_phase(h, phase):
    z = (h / phase) ** 2
    return z / (2 * (sqrt(1 + z) + 1))


def endpoints(h, r, epsilon):
    p = sqrt(epsilon / (1 + epsilon))
    theta = h / (2 * sqrt(epsilon * (1 + epsilon)))
    c, s = cos(theta), sin(theta)
    q = exp(-r * h / epsilon)
    conservative = [[c, -p * s], [s / p, c]]
    dissipative = [[1., 0.], [0., q]]
    direct = multiply(multiply(conservative, dissipative), conservative)
    analytic = [[c*c-q*s*s, -p*(1+q)*c*s],
                [(1+q)*c*s/p, q*c*c-s*s]]
    for i in range(2):
        for j in range(2):
            assert isclose(direct[i][j], analytic[i][j], rel_tol=1e-11, abs_tol=1e-11)
    x_split = matvec(direct, [1., 1/r])
    discriminant = r*r*(1+epsilon)**2 - 4*epsilon*(1+epsilon)
    assert discriminant > 0
    root = sqrt(discriminant)
    ls = -2 / (r * (1 + epsilon) + root)
    lf = (-r*(1+epsilon)-root)/(2*epsilon*(1+epsilon))
    du0 = -1/(r*(1+epsilon))
    fast_weight = (du0-ls)/(lf-ls)
    slow_weight = 1-fast_weight
    u_true = slow_weight*exp(ls*h)+fast_weight*exp(lf*h)
    v_true = -(1+epsilon)*(ls*slow_weight*exp(ls*h)+lf*fast_weight*exp(lf*h))
    dist = sqrt((1+epsilon)*(x_split[0]-u_true)**2 + epsilon*(x_split[1]-v_true)**2)
    return x_split, [u_true, v_true], dist, (c*c, c*s)


def run():
    cases = 0
    for h, r in [(1., 1.), (log(2.), 1.), (0.8, 2.5), (1.4, 0.4)]:
        t = exp(-h/r)
        vals = []
        for k in [31, 100, 300, 600]:
            for offset in [0, pi/8, pi/4, pi/2, 3*pi/4]:
                eps = epsilon_for_phase(h, k*pi+offset)
                x, true, distance, phasepoint = endpoints(h, r, eps)
                assert abs(x[0] - phasepoint[0]) < 15*sqrt(eps)/r + 5e-6
                assert abs(sqrt(eps)*x[1] - phasepoint[1]) < 15*sqrt(eps)/r + 5e-6
                assert abs((phasepoint[0]-0.5)**2+phasepoint[1]**2-0.25) < 2e-12
                assert abs(true[0]-t) < 10*eps + 5e-5
                if k == 600:
                    vals.append((offset, distance))
                cases += 1
        minlim = min(t,1-t)
        maxlim = max(t,1-t)
        assert abs(vals[0][1]-maxlim) < 0.008 or abs(vals[0][1]-minlim) < 0.008
        assert abs(vals[3][1]-maxlim) < 0.008 or abs(vals[3][1]-minlim) < 0.008
        if abs(t-0.5)<1e-12:
            assert all(abs(distance-0.5) < 0.008 for _,distance in vals)
    print('VERIFY_OK exact split matrix; regularized-flow eigenvalues; 80 phase tests; sharp energy-norm envelope')


if __name__ == '__main__':
    run()
