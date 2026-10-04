import math


def exact(r, eps):
    alpha = math.acos(math.tanh(r) / math.tanh(r + eps))
    gamma = math.acos(math.sinh(r) / math.sinh(r + eps))
    delta = 2.0 * (gamma - math.cosh(r) * alpha)
    area = 2.0 * math.pi * (math.cosh(r + eps) - math.cosh(r))
    return delta, area


def coefficients(r):
    tau = math.tanh(r)
    L = 2.0 * math.sqrt(2.0 * tau) / 3.0
    M = -math.sqrt(2.0) * (tau * tau + 3.0) / (10.0 * math.sqrt(tau))
    A = L ** (-2.0 / 3.0)
    C1 = math.pi * (3.0 ** (2.0 / 3.0)) * math.sinh(r) / (tau ** (1.0 / 3.0))
    C2 = (math.pi * (3.0 ** (4.0 / 3.0)) * math.cosh(r) * (tau * tau + 8.0)
          / (20.0 * tau ** (2.0 / 3.0)))
    return L, M, A, C1, C2


def main():
    for r in (0.3, 1.0, 2.0):
        L, M, A, C1, C2 = coefficients(r)
        for eps, tol_delta, tol_area in ((1.0e-3, 5.0e-6, 5.0e-6),
                                         (3.0e-4, 5.0e-7, 5.0e-7)):
            delta, area = exact(r, eps)
            delta_approx = L * eps ** 1.5 + M * eps ** 2.5
            area_approx = C1 * delta ** (2.0 / 3.0) + C2 * delta ** (4.0 / 3.0)
            rel_delta = abs(delta - delta_approx) / delta
            rel_area = abs(area - area_approx) / area
            if rel_delta >= tol_delta or rel_area >= tol_area:
                raise AssertionError((r, eps, rel_delta, rel_area))
        # Leading coefficient must also match c_2 times the floating area.
        c2 = 3.0 ** (2.0 / 3.0) / 2.0
        floating_area = 2.0 * math.pi * math.sinh(r) * (1.0 / math.tanh(r)) ** (1.0 / 3.0)
        if abs(C1 - c2 * floating_area) > 1.0e-12 * max(1.0, abs(C1)):
            raise AssertionError((r, C1, c2 * floating_area))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
