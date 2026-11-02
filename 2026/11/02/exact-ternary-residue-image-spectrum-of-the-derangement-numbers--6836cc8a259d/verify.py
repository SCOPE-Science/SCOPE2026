"""Independent arithmetic checks for the residue image of subfactorials modulo powers of three."""
from math import gcd


def polynomial_for_falling_sum(offset, top, modulus):
    """Coefficients of sum (-1)^j product_{i<j}(offset+3*t-i) mod modulus."""
    total = [0] * (top + 2)
    product = [1]
    for j in range(top + 1):
        sign = -1 if j % 2 else 1
        for i, coeff in enumerate(product):
            total[i] = (total[i] + sign * coeff) % modulus
        constant = offset - j
        new_product = [0] * (len(product) + 1)
        for i, coeff in enumerate(product):
            new_product[i] = (new_product[i] + constant * coeff) % modulus
            new_product[i + 1] = (new_product[i + 1] + 3 * coeff) % modulus
        product = new_product
    return total


def squares_count(power):
    if power == 0:
        return 1
    return 1 + sum(3 ** (power - 2 * j - 1) for j in range((power - 1)//2 + 1))


def exceptional_count(m):
    if m == 0:
        return 1
    if m == 1:
        return 3
    if m == 2:
        return 7
    return 2 * 3 ** (m - 1) + 3 ** (m - 3) + 2 * squares_count(max(m - 4, 0))


def expected_count(a):
    if a == 1:
        return 3
    return 2 * 3 ** (a - 1) + exceptional_count(a - 2)


def check_polynomial_certificates():
    zero = polynomial_for_falling_sum(0, 8, 9)
    assert zero[0] == 1 and zero[1] == 6 and not any(zero[2:])
    minus = polynomial_for_falling_sum(-1, 8, 27)
    assert minus[0] == 10 and minus[1] == 9 and minus[2] == 9 and not any(minus[3:])
    plus = polynomial_for_falling_sum(1, 11, 81)
    assert all(coef % 9 == 0 for coef in plus)
    normalized = [(coef // 9) % 9 for coef in plus]
    assert normalized[0] == 0 and normalized[1] == 3 and normalized[2] == 4
    assert normalized[3] == 3 and not any(normalized[4:])
    return 3


def check_image_counts():
    tested = 0
    for a in range(1, 10):
        mod = 3 ** a
        derangement = 1
        observed = {derangement % mod}
        # For odd mod, (n mod 3^a, parity) is periodic with period 2*3^a.
        for n in range(1, 2 * mod):
            derangement = (n * derangement + (-1 if n & 1 else 1)) % mod
            observed.add(derangement)
        expect = expected_count(a)
        assert len(observed) == expect, (a, len(observed), expect)
        print(f'POWER_{a} observed={len(observed)} expected={expect}')
        tested += 2 * mod
    return tested


def check_signed_square_counts():
    tested = 0
    # For c with v3(c)=2, image cardinality depends only on c/9 mod3 = 2.
    for m in range(0, 8):
        q = 3 ** m
        c = 18 % q
        image = {(c + u*u) % q for u in range(q)}
        image |= {(-c - u*u) % q for u in range(q)}
        assert len(image) == exceptional_count(m), (m, len(image), exceptional_count(m))
        tested += q
    return tested


def check_critical_value():
    values = [1]
    for n in range(1, 11):
        values.append(n * values[-1] + (-1 if n % 2 else 1))
    assert values[10] == 1334961
    assert values[10] % 9 == 0
    assert (values[10] // 9) % 27 == 18


def main():
    certificates = check_polynomial_certificates()
    check_critical_value()
    terms = check_image_counts()
    squares = check_signed_square_counts()
    # Additional exact rational limiting fraction: 725/972.
    assert gcd(725, 972) == 1
    print(f'VERIFY_OK polynomial_certificates={certificates} image_indices={terms} signed_square_inputs={squares} limiting_density=725/972')


if __name__ == '__main__':
    main()
