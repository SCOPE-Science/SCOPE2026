"""Exhaustive small-case checks for the monomial-unit torsion formula."""
from itertools import product


def standard_monomials(bounds, extra_generators=()):
    """Return standard exponent vectors for (x_i**bounds_i, extra monomials)."""
    out = []
    for alpha in product(*(range(b) for b in bounds)):
        if any(all(alpha[i] >= gen[i] for i in range(len(alpha)))
               for gen in extra_generators):
            continue
        out.append(tuple(alpha))
    return tuple(out)


def multiply(a, b, monomials, p):
    index = {alpha: i for i, alpha in enumerate(monomials)}
    out = [0] * len(monomials)
    for i, alpha in enumerate(monomials):
        if not a[i]:
            continue
        for j, beta in enumerate(monomials):
            if not b[j]:
                continue
            gamma = tuple(alpha[t] + beta[t] for t in range(len(alpha)))
            k = index.get(gamma)
            if k is not None:
                out[k] = (out[k] + a[i] * b[j]) % p
    return tuple(out)


def power(a, exponent, monomials, p):
    one = tuple(1 if alpha == (0,) * len(alpha) else 0
                for alpha in monomials)
    out, base = one, a
    while exponent:
        if exponent & 1:
            out = multiply(out, base, monomials, p)
        base = multiply(base, base, monomials, p)
        exponent >>= 1
    return out


def predicted_count(monomials, p, r):
    monomial_set = set(monomials)
    p_to_r = p ** r
    survivors = sum(
        tuple(p_to_r * coordinate for coordinate in alpha) in monomial_set
        for alpha in monomials
    )
    return p ** (len(monomials) - survivors)


def exhaustive_count(monomials, p, r):
    nonconstant = [i for i, alpha in enumerate(monomials) if any(alpha)]
    zero = (0,) * len(monomials)
    total = 0
    for coefficients in product(range(p), repeat=len(nonconstant)):
        z = [0] * len(monomials)
        for i, coefficient in zip(nonconstant, coefficients):
            z[i] = coefficient
        if power(tuple(z), p ** r, monomials, p) == zero:
            total += 1
    return total


def main():
    rings = {
        "(x^3,xy,y^2)": standard_monomials((3, 2), ((1, 1),)),
        "(x^4,x^2y,y^2)": standard_monomials((4, 2), ((2, 1),)),
        "(x^3,y^3)": standard_monomials((3, 3)),
        "(x^2,xy,y^3)": standard_monomials((2, 3), ((1, 1),)),
    }
    checks = 0
    for name, monomials in rings.items():
        for p in (2, 3):
            for r in (1, 2, 3):
                observed = exhaustive_count(monomials, p, r)
                expected = predicted_count(monomials, p, r)
                assert observed == expected, (name, p, r, observed, expected)
                checks += 1
    print(f"PASS: {checks} exhaustive ring/field/exponent comparisons")


if __name__ == "__main__":
    main()
