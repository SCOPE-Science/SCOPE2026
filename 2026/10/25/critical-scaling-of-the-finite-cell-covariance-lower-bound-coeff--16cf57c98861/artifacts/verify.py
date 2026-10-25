"""Numerical corroboration for the midpoint-covariance asymptotics.

Only standard-library quadrature is used. The proof of the asymptotic statements
is analytic; these finite calculations are consistency checks, not a proof of a
limit.
"""
import math

PI = math.pi


def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    total += 4.0 * sum(f(a + i * h) for i in range(1, n, 2))
    total += 2.0 * sum(f(a + i * h) for i in range(2, n, 2))
    return total * h / 3.0


def floor_value(E, beta, M, per_cell_n=80):
    h = PI / M
    total = 0.0
    for j in range(M):
        a, b = j * h, (j + 1) * h
        mean = simpson(E, a, b, per_cell_n) / h
        total += simpson(
            lambda k: (E(k) - mean) * math.tanh(beta * E(k)),
            a, b, per_cell_n
        )
    return beta * total / PI


def sech2(x):
    if x > 350.0:
        return 0.0
    c = math.cosh(x)
    return 1.0 / (c * c)


def coefficient(E, dE, beta, n=50000):
    integral = simpson(
        lambda k: dE(k) ** 2 * sech2(beta * E(k)),
        0.0, PI, n
    )
    return PI * beta * beta * integral / 12.0


def main():
    # Critical transverse-field Ising dispersion: E(pi-s) ~ s for J=1.
    E1 = lambda k: 2.0 * math.cos(k / 2.0)
    dE1 = lambda k: -math.sin(k / 2.0)
    for beta in (1.0, 2.0, 4.0):
        C = coefficient(E1, dE1, beta)
        print("z=1 beta={:.1f} C/(beta*pi/12)={:.8f}".format(beta, C / (beta * PI / 12.0)))
        for M in (16, 32, 64):
            S = floor_value(E1, beta, M)
            print("  M={} M^2*S/C={:.8f}".format(M, M * M * S / C))

    # A smooth model with a quadratic critical endpoint, E(pi-s) ~ s^2.
    E2 = lambda k: (PI - k) ** 2
    dE2 = lambda k: -2.0 * (PI - k)
    # K_2 is evaluated independently from its defining integral.
    K2 = PI / 6.0 * simpson(lambda u: math.sqrt(u) * sech2(u), 0.0, 30.0, 100000)
    for beta in (20.0, 80.0):
        C = coefficient(E2, dE2, beta)
        print("z=2 beta={:.1f} C/sqrt(beta)={:.8f} K2={:.8f}".format(beta, C / math.sqrt(beta), K2))


if __name__ == "__main__":
    main()
