"""Exact finite-field certificate for the first eight uniform-jump compound-Poisson orders.

Run: python3 verify.py
Uses only the Python standard library. A proof of the lifting step and the
large-intensity log-concavity argument is supplied in RESULT.md.
"""
from math import comb, factorial
from time import perf_counter

PRIME = 1000003
ORDERS = tuple(range(2, 9))


def trim_high(a):
    while a and not a[-1]:
        a.pop()
    return a


def modular_gcd(a, b, inverses):
    """Monic gcd in F_p[t], low-degree coefficient first."""
    a, b = a[:], b[:]
    while b:
        remainder = a[:]
        degree_span = len(b)
        leading_inverse = inverses[b[-1]]
        while len(remainder) >= degree_span:
            factor = remainder[-1] * leading_inverse % PRIME
            shift = len(remainder) - degree_span
            if factor:
                for j in range(degree_span - 1):
                    remainder[shift + j] = (
                        remainder[shift + j] - factor * b[j]
                    ) % PRIME
            remainder.pop()  # The leading coefficient has cancelled.
            trim_high(remainder)
        a, b = b, remainder
    if not a:
        return []
    scale = inverses[a[-1]]
    return [(v * scale) % PRIME for v in a]


def exact_polynomials(order, max_index):
    """Return H_n=n![z^n] exp(t(z+...+z^order)) over Z[t]."""
    fact = [factorial(i) for i in range(max_index + 1)]
    h = [[1]]
    for n in range(1, max_index + 1):
        coeff = [0] * n
        for jump in range(1, min(n, order) + 1):
            multiple = jump * fact[n - 1] // fact[n - jump]
            for degree, value in enumerate(h[n - jump]):
                coeff[degree] += multiple * value
        h.append([0] + coeff)
        assert h[n][-1] == 1 and h[n][0] == 0
    return h, fact


def exact_difference_reduced_mod_p(hi, hj, fi, fj):
    """Reduce integer polynomial fj*hi-fi*hj after stripping exact t-powers.

    Exact zero coefficients are removed before reduction, never modulo PRIME;
    this matters for the validity of the rational-factor lifting argument.
    """
    vals = [
        fj * (hi[m] if m < len(hi) else 0)
        - fi * (hj[m] if m < len(hj) else 0)
        for m in range(len(hj))
    ]
    assert vals[-1] == -fi
    while vals[0] == 0:
        vals.pop(0)
    reduced = [v % PRIME for v in vals]
    assert reduced[-1] != 0
    return reduced


def verify_order(order, inverses):
    max_index = order * (order + 1)
    h, fact = exact_polynomials(order, max_index)
    exceptional = []
    checked = 0
    for i in range(max_index + 1):
        pairs = [
            (j, exact_difference_reduced_mod_p(h[i], h[j], fact[i], fact[j]))
            for j in range(i + 1, max_index + 1)
        ]
        for position, (j, poly1) in enumerate(pairs):
            for ell, poly2 in pairs[position + 1:]:
                checked += 1
                common = modular_gcd(poly1, poly2, inverses)
                if len(common) > 1:
                    exceptional.append((i, j, ell, tuple(common)))
    assert checked == comb(max_index + 1, 3)
    expected = [(1, 3, 4, (6, 1))] if order >= 4 else []
    assert exceptional == expected, (order, exceptional)
    # A common characteristic-zero factor can only be the displayed linear
    # factor, because leading coefficients are nonzero modulo PRIME.
    # Confirm its exact polynomial identity by evaluating the integer H_n.
    if order >= 4:
        # h3-h1 = t^2(t+6)/6, h4-h1 = t^2(t+6)^2/24.
        assert [h[3][d] * fact[1] - (h[1][d] if d < len(h[1]) else 0) * fact[3]
                for d in range(4)] == [0, 0, 6, 1]
        assert [h[4][d] * fact[1] - (h[1][d] if d < len(h[1]) else 0) * fact[4]
                for d in range(5)] == [0, 0, 36, 12, 1]
    print(f"k={order}, bound={max_index}, triple_checks={checked}, "
          f"exceptional_gcds={exceptional}")
    return checked


def main():
    start = perf_counter()
    assert PRIME == 1000003
    inverses = [0] * PRIME
    inverses[1] = 1
    for value in range(2, PRIME):
        inverses[value] = PRIME - (PRIME // value) * inverses[PRIME % value] % PRIME
    total = sum(verify_order(k, inverses) for k in ORDERS)
    assert total == 109943
    print(f"PASS: {total} exact modular triple-gcd tests across orders 2..8")
    print(f"Elapsed {perf_counter()-start:.2f} seconds")


if __name__ == "__main__":
    main()
