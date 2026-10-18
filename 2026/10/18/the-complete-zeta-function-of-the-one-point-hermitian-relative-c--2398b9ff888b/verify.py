#!/usr/bin/env python3
"""Direct small-field point-count checks for a Hermitian-relative zeta formula.

Only Python's standard library is needed. This finite check is not a proof of
any statement quantified over infinitely many fields.
"""

CASES = (
    (2, 1, (1, 1, 1)),
    (2, 2, (1, 1, 0, 0, 1)),
    (3, 1, (1, 0, 1)),
    (3, 2, (2, 1, 0, 0, 1)),
    (3, 3, (2, 1, 0, 0, 0, 0, 1)),
    (3, 4, (2, 0, 1, 0, 0, 0, 0, 0, 1)),
    (5, 1, (2, 0, 1)),
    (5, 2, (2, 0, 0, 0, 1)),
    (2, 2, 1, (1, 1, 0, 0, 1)),
    (2, 2, 2, (1, 1, 0, 1, 1, 0, 0, 0, 1)),
    (3, 2, 1, (2, 1, 0, 0, 1)),
    (3, 2, 2, (2, 0, 1, 0, 0, 0, 0, 0, 1)),
)


def verify(p, r, n, modulus):
    degree = 2 * r * n
    s = p ** r
    size = p ** degree
    assert len(modulus) == degree + 1 and modulus[-1] == 1
    digits = [tuple((z // p ** k) % p for k in range(degree))
              for z in range(size)]

    def add(a, b):
        return sum(((digits[a][k] + digits[b][k]) % p) * p ** k
                   for k in range(degree))

    def mul(a, b):
        terms = [0] * (2 * degree - 1)
        for i, ai in enumerate(digits[a]):
            if ai:
                for j, bj in enumerate(digits[b]):
                    terms[i + j] += ai * bj
        for i in range(2 * degree - 2, degree - 1, -1):
            lead = terms[i] % p
            if lead:
                for j in range(degree):
                    terms[i - degree + j] -= lead * modulus[j]
        return sum((terms[i] % p) * p ** i for i in range(degree))

    def power(a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = mul(result, a)
            a = mul(a, a)
            exponent //= 2
        return result

    # Certify that the chosen quotient is a FIELD: every nonzero element
    # has multiplicative inverse a^(size-2).
    assert all(power(a, size - 1) == 1 for a in range(1, size))

    # The coefficient belongs to the quadratic subfield F_{p^2} but not F_p.
    eta = next(a for a in range(size)
               if power(a, s * s) == a and power(a, s) != a)

    # Affine patch Y=1: z^p+z = -x^(p+1)-eta. To count without solving,
    # use the size-p fibers of the additive trace-like map z -> z^p+z.
    image = {add(power(z, s), z) for z in range(size)}
    assert len(image) == size // s
    target_count = sum(add(power(x, s + 1), eta) in image
                       for x in range(size))
    actual = 1 + s * target_count  # one point Y=0 at infinity

    trace = s * ((s - 1) if n % p == 0 else -1) * ((-s) ** n)
    predicted = s ** (2 * n) + 1 - trace
    assert actual == predicted, (p, n, actual, predicted)
    print('p=%d r=%d n=%d coefficient=%d |C(F_%d)|=%d OK' %
          (p, r, n, eta, size, actual))


def main():
    for row in CASES:
        if len(row) == 3:
            p, n, mod = row
            verify(p, 1, n, mod)
        else:
            verify(*row)
    print('All finite-field tests passed; the general theorem uses a separate proof.')


if __name__ == '__main__':
    main()
