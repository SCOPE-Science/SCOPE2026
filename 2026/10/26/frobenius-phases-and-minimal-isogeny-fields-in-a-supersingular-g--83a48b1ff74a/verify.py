"""Exact finite-field point counts and Frobenius-extension comparison.

Run with Python 3 and no third-party packages: python verify.py
"""
from collections import Counter

# The degree-2 and degree-4 extension fields, respectively, use
# u^2+u+1 and v^4+v+1 as defining polynomials over F_2.
FIELDS = {1: (2, 0b111, 0b10), 2: (4, 0b10011, 0b110)}


def multiply(a, b, degree, modulus):
    product = 0
    while b:
        if b & 1:
            product ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= modulus
    return product


def power(a, exponent, degree, modulus):
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, a, degree, modulus)
        a = multiply(a, a, degree, modulus)
        exponent >>= 1
    return result


def absolute_trace(a, degree, modulus):
    answer = 0
    for _ in range(degree):
        answer ^= a
        a = multiply(a, a, degree, modulus)
    assert answer in (0, 1)
    return answer


def count_quotient(extension, leading, cube):
    degree, modulus, alpha = FIELDS[extension]
    assert multiply(alpha, alpha, degree, modulus) == (alpha ^ 1)
    values = {'0': 0, '1': 1, 'alpha': alpha, 'alpha2': alpha ^ 1}
    a, b = values[leading], values[cube]
    assert a != 0
    return 1 + 2 * sum(
        absolute_trace(
            multiply(a, power(x, 5, degree, modulus), degree, modulus)
            ^ multiply(b, power(x, 3, degree, modulus), degree, modulus),
            degree, modulus,
        ) == 0
        for x in range(1 << degree)
    )


def coefficients(n1, n2):
    s1, s2 = 5 - n1, 17 - n2
    assert (s1 * s1 - s2) % 2 == 0
    return (1, -s1, (s1 * s1 - s2) // 2, -4 * s1, 16)


def multiply_polynomials(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return tuple(c)


E = (1, 0, 8, 0, 16)                    # (1+4T^2)^2
B = (1, 0, -4, 0, 16)                   # Phi_12(2T) reciprocally
D = (1, 2, 4, 8, 16)                    # Phi_5(2T) reciprocally
EXPECTED = {
    '0': (E, E, E),
    '1': (E, B, B),
    'alpha': (E, D, D),
    'alpha2': (E, D, D),
}
EXPECTED_JAC = {'0': 15625, '1': 4225, 'alpha': 24025, 'alpha2': 24025}

# Every entry is an exact count, since it enumerates all 4 or 16 x-values.
for lam, expected in EXPECTED.items():
    actual = []
    counts = []
    for eta in ('1', 'alpha', 'alpha2'):
        c = '0' if eta == '1' else lam
        n1 = count_quotient(1, eta, c)
        n2 = count_quotient(2, eta, c)
        counts.append((n1, n2))
        actual.append(coefficients(n1, n2))
    assert tuple(actual) == expected, (lam, counts, actual)
    combined = (1,)
    for factor in actual:
        combined = multiply_polynomials(combined, factor)
    assert len(combined) == 13
    assert sum(combined) == EXPECTED_JAC[lam]
    print('QUOTIENTS', lam, counts, 'JAC', sum(combined))

# Normalize F_4-Frobenius eigenvalues by 2 and regard all roots
# of unity as 60th roots. Each exponent has the indicated multiplicity.
root_frequencies = {
    '0': Counter({15: 6, 45: 6}),
    '1': Counter({15: 2, 45: 2, 5: 2, 25: 2, 35: 2, 55: 2}),
    'alpha': Counter({15: 2, 45: 2, 12: 2, 24: 2, 36: 2, 48: 2}),
}


def power_multiset(freq, extension):
    out = Counter()
    for exponent, multiplicity in freq.items():
        out[exponent * extension % 60] += multiplicity
    return out

for a, b, expected_minimum in (('0', '1', 3), ('0', 'alpha', 20),
                                ('1', 'alpha', 60)):
    degrees = [r for r in range(1, 121)
               if power_multiset(root_frequencies[a], r)
               == power_multiset(root_frequencies[b], r)]
    assert degrees[0] == expected_minimum
    assert degrees == [r for r in range(1, 121) if r % expected_minimum == 0]
    print('ISOGENY_EXTENSION', a, b, expected_minimum)

print('VERIFY_OK')
