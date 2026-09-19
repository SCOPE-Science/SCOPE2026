import cmath
import math
import mpmath as mp

EULER_GAMMA = mp.euler


def f(x):
    y = 1.0 / x
    if y < 1e-5:
        return y / 2 - y * y / 6 + y**3 / 24 - y**4 / 120
    if x < 1e-8:
        return 1.0 - x
    return 1.0 - x * (-math.expm1(-y))


def p_direct(d, theta, cutoff=120):
    out = -theta
    for j in range(-cutoff, 1):
        out += f(d ** (j - theta)) - 1.0
    for j in range(1, cutoff + 1):
        out += f(d ** (j - theta))
    return out


def fourier_coeff(d, ell):
    chi = 2j * math.pi * ell / math.log(d)
    return complex(mp.gamma(1 - chi)) / (
        math.log(d) * chi * (1 + chi)
    )


def p_fourier(d, theta, cutoff=30):
    out = -0.5 + (float(EULER_GAMMA) - 1.0) / math.log(d)
    for ell in range(1, cutoff + 1):
        c = fourier_coeff(d, ell)
        out += 2.0 * (
            c * cmath.exp(2j * math.pi * ell * theta)
        ).real
    return out


def occupancy_deficit(N, Q):
    if N <= 0:
        return 0.0
    if Q > 1e14:
        return N * (N - 1) / (2.0 * Q)
    Q = float(Q)
    return N - Q + Q * math.exp(N * math.log1p(-1.0 / Q))


def occupancy_proxy(n, d):
    m = int(math.floor(math.log(n, d)))
    # Terms after m+60 are negligible at printed precision.
    stop = min(n, m + 60)
    return sum(
        occupancy_deficit(n - k + 1, d**k)
        for k in range(1, stop + 1)
    )


for d in (2, 3, 4, 10):
    errors = []
    values = []
    for r in range(1000):
        theta = r / 1000.0
        a = p_direct(d, theta)
        b = p_fourier(d, theta)
        errors.append(abs(a - b))
        values.append(a)
    mean = -0.5 + (float(EULER_GAMMA) - 1.0) / math.log(d)
    print(
        f"d={d} mean={mean:.15f} "
        f"min={min(values):.15f} max={max(values):.15f} "
        f"peak_to_peak={max(values)-min(values):.15g} "
        f"max_direct_fourier_error={max(errors):.3e}"
    )

for d in (2, 3):
    print(f"occupancy proxy, d={d}")
    for n in (100, 1000, 10000, 100000):
        theta = math.log(n, d) % 1.0
        proxy = occupancy_proxy(n, d)
        asym = (
            n * math.log(n, d)
            + n * p_direct(d, theta)
        )
        remainder = proxy - asym
        print(
            f"n={n:6d} proxy={proxy:.9f} asym={asym:.9f} "
            f"remainder={remainder:.9f} "
            f"remainder/(ln n)^2={remainder/(math.log(n)**2):.9f}"
        )
