from fractions import Fraction as F


def step(lam, delta, q, z, mu):
    # alpha = 2, rho = delta for the scalar split quadratic.
    x = (delta*z - mu - q) / (lam + delta)
    z_new = (mu + delta*(2*x - z)) / (2*delta)
    mu_new = mu + delta*(2*(x - z_new) - (z - z_new))
    return x, z_new, mu_new


def check_case(lam, delta, q, z0, mu0):
    x_star = -q / (lam + delta)
    eta0 = mu0 - delta*z0
    x1, z1, mu1 = step(lam, delta, q, z0, mu0)
    assert x1 - x_star == -eta0 / (lam + delta)
    assert z1 - x_star == (lam - delta)*eta0 / (2*delta*(lam + delta))
    assert mu1 == delta*z1
    x2, z2, mu2 = step(lam, delta, q, z1, mu1)
    assert x2 == x_star
    assert z2 == x_star
    assert mu2 == delta*x_star
    if eta0 == 0:
        assert x1 == x_star and z1 == x_star and mu1 == delta*x_star
    else:
        assert x1 != x_star


# Published-claim witness: arbitrary initialization does not terminate in one update.
lam, delta, q, z0, mu0 = F(2), F(1), F(-3), F(0), F(1)
x1, z1, mu1 = step(lam, delta, q, z0, mu0)
assert (x1, z1, mu1) == (F(2,3), F(7,6), F(7,6))
x2, z2, mu2 = step(lam, delta, q, z1, mu1)
assert (x2, z2, mu2) == (F(1), F(1), F(1))

for lam in map(F, [1,2,3,5]):
    for delta in map(F, [1,2,4]):
        for q in map(F, [-5,-1,2]):
            for z0 in map(F, [-2,0,3]):
                for mu0 in map(F, [-3,0,4]):
                    check_case(lam, delta, q, z0, mu0)

print('all exact rational checks passed')
