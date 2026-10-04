from fractions import Fraction

def armijo(beta, a, alpha):
    s = a * alpha
    return s <= 2 * (1 - beta)

def curvature(gamma, a, alpha):
    s = a * alpha
    return s >= 1 - gamma

def wolfe(beta, gamma, a, alpha):
    return armijo(beta, a, alpha) and curvature(gamma, a, alpha)

def grid_hit(beta, gamma, a, max_r=80):
    return any(wolfe(beta, gamma, a, Fraction(1, 2**r)) for r in range(max_r + 1))

# Exact counterexample.
beta = Fraction(1, 4)
gamma = Fraction(3, 4)
a = Fraction(1, 8)
assert (1 - gamma) / a == 2
assert 2 * (1 - beta) / a == 12
assert not grid_hit(beta, gamma, a)

# Rational-lattice replay of the exact frontier.
for beta_num in range(1, 8):
    beta = Fraction(beta_num, 10)
    for gamma_num in range(beta_num + 1, 10):
        gamma = Fraction(gamma_num, 10)
        for a_num in range(1, 81):
            a = Fraction(a_num, 20)
            expected = a >= 1 - gamma
            assert grid_hit(beta, gamma, a) == expected

# Two-sided dyadic repair on the same lattice.
for beta_num in range(1, 8):
    beta = Fraction(beta_num, 10)
    for gamma_num in range(beta_num + 1, 10):
        gamma = Fraction(gamma_num, 10)
        for a_num in range(1, 81):
            a = Fraction(a_num, 20)
            found = False
            for r in range(-20, 21):
                alpha = Fraction(2**r, 1) if r >= 0 else Fraction(1, 2**(-r))
                if wolfe(beta, gamma, a, alpha):
                    found = True
                    break
            assert found

print("VERIFY_OK")
