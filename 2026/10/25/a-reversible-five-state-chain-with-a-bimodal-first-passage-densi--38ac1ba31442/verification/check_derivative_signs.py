from fractions import Fraction

Q = [
    [-100, 0, 0, 100],
    [0, -12, 10, 1],
    [0, 10, -20, 10],
    [100, 1, 10, -112],
]
r = [0, 1, 0, 1]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]


def taylor_sum_for_derivative(t, order=400):
    # f'(t) = e_0^T exp(Qt) Qr.  All terms are exact rational numbers.
    w = matvec(Q, r)
    total = Fraction(0, 1)
    t_power = Fraction(1, 1)
    factorial = 1
    for k in range(order + 1):
        if k:
            t_power *= t
            factorial *= k
        total += Fraction(w[0], factorial) * t_power
        w = matvec(Q, w)
    return total


cases = [
    (Fraction(1, 100), Fraction(1115, 100), Fraction(1117, 100), 1),
    (Fraction(3, 100), Fraction(-68, 100), Fraction(-66, 100), -1),
    (Fraction(1, 10), Fraction(24, 1000), Fraction(26, 1000), 1),
    (Fraction(3, 10), Fraction(-138, 1000), Fraction(-135, 1000), -1),
]

for t, lo, hi, sign in cases:
    exact_sum = taylor_sum_for_derivative(t)
    assert lo < exact_sum < hi, (t, exact_sum, lo, hi)
    assert (exact_sum > 0) == (sign > 0)
    print(f"t={t}: S_400 in ({lo}, {hi}); approx={float(exact_sum):.12g}")

# For 0 <= t <= 0.3, ||Q||_2 <= 224 and ||Qr||_2 = sqrt(22842).
# The analytic bound exp(67.2) * 67.2**401 / 401! < 1e-109
# makes |f'(t)-S_400(t)| < 2e-107.  The interval margins above are
# vastly larger, so the signs of f' are the signs asserted here.
print("Exact rational interval checks passed.")
