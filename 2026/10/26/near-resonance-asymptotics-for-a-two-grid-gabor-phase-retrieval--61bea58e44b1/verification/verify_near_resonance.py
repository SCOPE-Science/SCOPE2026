"""Finite numerical stress test for the exact near-resonance asymptotic.

The theorem and dominated-convergence proof are in RESULT.md. This script
checks the derived coefficient against direct quadrature for one parameter
choice; it is not used as a proof of the infinite-series statement.
"""
import math


def simpson(f, left, right, n):
    if n % 2:
        n += 1
    h = (right - left) / n
    total = f(left) + f(right)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(left + j * h)
    return total * h / 3.0


def rho(x, a):
    return math.exp(math.pi * x / a - math.pi / (2.0 * a * a))


def leading_coefficient(a, m):
    def integrand(x):
        r = rho(x, a)
        return math.exp(-math.pi * x * x) * (r * r / (1.0 + r * r))

    I = simpson(integrand, -8.0, 8.0, 12000)
    S = 2.0 * sum(
        k * k * math.exp(-math.pi * (m * a) ** 2 * k * k)
        for k in range(1, 16)
    )
    return 2.0 * math.pi * math.sqrt(I * S), I, S


def data_discrepancy(a, m, eps):
    b = a * (m + eps)
    total = 0.0
    for k in range(-15, 16):
        if k == 0:
            continue
        s = math.sin(math.pi * eps * k)

        def integrand(x):
            r = rho(x, a)
            plus2 = max(0.0, 1.0 + r * r + 2.0 * r * s)
            minus2 = max(0.0, 1.0 + r * r - 2.0 * r * s)
            gap = math.sqrt(plus2) - math.sqrt(minus2)
            envelope = math.exp(-math.pi * 0.5 * (x * x + b * b * k * k))
            return (envelope * gap) ** 2

        total += simpson(integrand, -8.0, 8.0, 4000)
    return math.sqrt(total)


def main():
    a, m = 0.5, 1
    C, I, S = leading_coefficient(a, m)
    c = math.exp(-math.pi / (2.0 * a * a))
    signal_distance = 2.0 * math.sqrt(1.0 - c)
    print(f"parameters: a={a}, m={m}")
    print(f"I(a)={I:.12g}")
    print(f"sum k^2 exp(-pi*(m*a)^2*k^2)={S:.12g}")
    print(f"leading coefficient C(a,m)={C:.12g}")
    print(f"phase-invariant signal distance={signal_distance:.12g}")
    ratios = []
    for power in (2, 3, 4):
        eps = math.sqrt(2.0) * 10.0 ** (-power)
        delta = data_discrepancy(a, m, eps)
        ratio = delta / abs(eps)
        rel = abs(ratio - C) / C
        ratios.append(rel)
        print(f"eps={eps:.12g} discrepancy={delta:.12g} ratio={ratio:.12g} relative_error={rel:.6g}")
    assert ratios[2] < 0.001, "small-epsilon ratio did not approach the predicted coefficient"
    assert ratios[2] < ratios[1] < ratios[0], "relative errors did not decrease"
    print("PASS: finite numerical stress test converges to the analytical coefficient")


if __name__ == "__main__":
    main()
