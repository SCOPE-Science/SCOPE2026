from math import comb


def c_formula(n):
    total = 0
    for a in range(n // 3 + 1):
        for b in range(n - 3 * a + 1):
            total += (
                comb(n, a)
                * comb(n - a, a + b) ** 2
                * comb(2 * a + 2 * b, b)
                * comb(2 * n - 4 * a - 2 * b, n - 3 * a - b)
            )
    return total


def c_recurrence(limit):
    c = [0] * (limit + 1)
    c[0] = 1
    if limit >= 1:
        c[1] = 4
    if limit >= 2:
        c[2] = 28
    for k in range(2, limit):
        numerator = (
            2 * (2 * k + 1) * (5 * k * k + 5 * k + 2) * c[k]
            - 8 * k * (7 * k * k + 1) * c[k - 1]
            + 22 * k * (k - 1) * (2 * k - 1) * c[k - 2]
        )
        denominator = (k + 1) ** 3
        assert numerator % denominator == 0
        c[k + 1] = numerator // denominator
    return c


def target_index(n):
    odd_part = n
    while odd_part % 2 == 0:
        odd_part //= 2
    return odd_part in (1, 3)


def summand(n, a, b):
    return (
        comb(n, a)
        * comb(n - a, a + b) ** 2
        * comb(2 * a + 2 * b, b)
        * comb(2 * n - 4 * a - 2 * b, n - 3 * a - b)
    )


def v2(x):
    assert x > 0
    return (x & -x).bit_length() - 1


c = c_recurrence(500)
for n in range(41):
    assert c_formula(n) == c[n]

for n in range(1, 501):
    assert c[n] % 8 in (0, 4)
    assert (c[n] % 8 == 4) == target_index(n)

symmetry_cases = 0
for n in range(1, 61):
    for a in range(n // 3 + 1):
        for b in range(n - 3 * a + 1):
            bp = n - 3 * a - b
            assert summand(n, a, b) == summand(n, a, bp)
            symmetry_cases += 1

positive_a_terms = 0
fixed_exceptions = []
for n in range(1, 81):
    for a in range(1, n // 3 + 1):
        for b in range(n - 3 * a + 1):
            value = summand(n, a, b)
            assert value % 4 == 0
            positive_a_terms += 1
            if 2 * b == n - 3 * a:
                if value % 8 == 4:
                    fixed_exceptions.append((n, a, b))
                else:
                    assert value % 8 == 0

expected_fixed = [
    (3 * (1 << k), 1 << k, 0)
    for k in range(5)
    if 3 * (1 << k) <= 80
]
assert fixed_exceptions == expected_fixed

carry_lemma_cases = 0
for a in range(1, 100):
    t = v2(a)
    for w in range(a, 300):
        if ((w >> t) & 1) == 0:
            assert comb(2 * w, w - a) % 4 == 0
            carry_lemma_cases += 1

print(
    "VERIFY_OK formula_recurrence=0..40 residue_pattern=1..500 "
    f"symmetry_cases={symmetry_cases} a_positive_terms={positive_a_terms} "
    f"carry_lemma_cases={carry_lemma_cases} fixed_exceptions={len(fixed_exceptions)}"
)
