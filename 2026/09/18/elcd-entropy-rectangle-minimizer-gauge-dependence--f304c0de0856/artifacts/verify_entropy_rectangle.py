import math
import random

GAMMA = 1.4


def eta(rho, pressure, gamma=GAMMA, constant=0.0):
    return rho / (gamma - 1.0) * (
        gamma * math.log(rho) - math.log(pressure) - constant
    )


def exact_rectangle_minimizer(rho_lo, rho_hi, p_lo, p_hi, gamma=GAMMA, constant=0.0):
    p_star = p_hi
    unconstrained_rho = math.exp(-1.0 + constant / gamma) * p_star ** (1.0 / gamma)
    rho_star = min(max(unconstrained_rho, rho_lo), rho_hi)
    return rho_star, p_star, unconstrained_rho


def identric_mean(a, b):
    if a == b:
        return a
    return math.exp((b * math.log(b) - a * math.log(a)) / (b - a) - 1.0)


def excess_formula(rho, r, gamma=GAMMA):
    x = rho / r
    return gamma * r / (gamma - 1.0) * (x * math.log(x) - x + 1.0)


def counterexample():
    rho_lo, rho_hi = 0.1, 1.0
    p_lo, p_hi = 0.8, 1.0
    rho_star, p_star, r = exact_rectangle_minimizer(rho_lo, rho_hi, p_lo, p_hi)
    e_lo = eta(rho_lo, p_hi)
    e_star = eta(rho_star, p_star)
    e_hi = eta(rho_hi, p_hi)
    corner_best = min(e_lo, e_hi)
    I = identric_mean(rho_lo, rho_hi)
    c_cross = GAMMA * (
        rho_hi * math.log(rho_hi) - rho_lo * math.log(rho_lo)
    ) / (rho_hi - rho_lo) - math.log(p_hi)
    print("counterexample")
    print(f"rho_star={rho_star:.15f}")
    print(f"p_star={p_star:.15f}")
    print(f"eta(rho_lo,p_hi)={e_lo:.15f}")
    print(f"eta(rho_star,p_star)={e_star:.15f}")
    print(f"eta(rho_hi,p_hi)={e_hi:.15f}")
    print(f"corner_excess={corner_best-e_star:.15f}")
    print(f"identric_mean={I:.15f}")
    print(f"gauge_flip_constant={c_cross:.15f}")
    for constant in (0.0, c_cross - 1e-3, c_cross + 1e-3, 1.0):
        lo = eta(rho_lo, p_hi, constant=constant)
        hi = eta(rho_hi, p_hi, constant=constant)
        winner = "rho_lo" if lo < hi else "rho_hi"
        print(f"C={constant:.15f} winner={winner} lo={lo:.15f} hi={hi:.15f}")


def check_excess_identity():
    p = 1.7
    constant = 0.3
    r = math.exp(-1.0 + constant / GAMMA) * p ** (1.0 / GAMMA)
    base = eta(r, p, constant=constant)
    max_error = 0.0
    for x in (0.2, 0.5, 0.9, 1.0, 1.3, 2.0, 4.0):
        lhs = eta(x * r, p, constant=constant) - base
        rhs = excess_formula(x * r, r)
        max_error = max(max_error, abs(lhs - rhs))
    print(f"max_excess_identity_error={max_error:.3e}")
    assert max_error < 1e-12


def randomized_grid_check():
    random.seed(20260918)
    max_grid_excess = 0.0
    for _ in range(50):
        rho_lo = 10 ** random.uniform(-2.0, 0.2)
        rho_hi = rho_lo * 10 ** random.uniform(0.05, 1.0)
        p_lo = 10 ** random.uniform(-2.0, 0.5)
        p_hi = p_lo * 10 ** random.uniform(0.05, 1.0)
        constant = random.uniform(-2.0, 2.0)
        rho_star, p_star, _ = exact_rectangle_minimizer(
            rho_lo, rho_hi, p_lo, p_hi, constant=constant
        )
        exact_value = eta(rho_star, p_star, constant=constant)
        grid_value = float("inf")
        n = 200
        for i in range(n + 1):
            rho = rho_lo + (rho_hi - rho_lo) * i / n
            for j in range(n + 1):
                pressure = p_lo + (p_hi - p_lo) * j / n
                grid_value = min(grid_value, eta(rho, pressure, constant=constant))
        assert grid_value + 1e-12 >= exact_value
        max_grid_excess = max(max_grid_excess, grid_value - exact_value)
    print("randomized_rectangle_checks=50 passed")
    print(f"max_grid_excess_over_exact={max_grid_excess:.6e}")


if __name__ == "__main__":
    counterexample()
    check_excess_identity()
    randomized_grid_check()
