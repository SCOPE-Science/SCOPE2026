"""Reproduce finite checks for the ordered power-of-two composition cutoff.

Scientific inputs: recurrence and integral formal-series factorization stated
in RESULT.md. No external packages or data are required.
"""

def recurrence(limit, modulus):
    v = [0] * limit
    v[0] = 1
    for n in range(1, limit):
        z = 1
        total = 0
        while z <= n:
            total += v[n - z]
            z *= 2
        v[n] = total % modulus
    return v


def factorized_coeffs(limit, modulus):
    # A = S/z; U = T/z in the exact identity F=A/(1-2U).
    a = [0] * limit
    exps = []
    j = 0
    while (1 << j) - 1 < limit:
        a[(1 << j) - 1] = 1
        exps.append(1 << j)
        j += 1
    support = []
    for i in range(len(exps)):
        for j in range(i + 1, len(exps)):
            e = exps[i] + exps[j] - 1
            if e < limit:
                support.append(e)
    power = a[:]
    output = [0] * limit
    coefficient = 1
    while coefficient < modulus:
        for n, x in enumerate(power):
            output[n] = (output[n] + coefficient * x) % modulus
        next_power = [0] * limit
        for u in support:
            for n in range(limit - u):
                if power[n]:
                    next_power[n + u] = (next_power[n + u] + power[n]) % modulus
        power = next_power
        coefficient *= 2
    return output


def check():
    limit = 1 << 19
    modulus = 1 << 9
    values = recurrence(limit, modulus)
    # Two independent series constructions agree coefficientwise.
    compare = 1 << 11
    expanded = factorized_coeffs(compare, modulus)
    assert expanded == values[:compare], 'formal-series identity failed'
    tests = 0
    nonvacuous = []
    for N in range(1, 10):
        m = 1 << N
        antecedents = 0
        for n, value in enumerate(values):
            if (n + N).bit_count() >= 2 * N:
                antecedents += 1
                assert value % m == 0, (n, N, value)
        tests += limit
        nonvacuous.append((N, antecedents))
    # Exact recurrence samples at small indices: 0,1,2,3,4,5.
    assert values[:6] == [1,1,2,3,6,10]
    print('VERIFY_OK independent_series_coefficients=', compare,
          'digit_weight_tests=', tests,
          'moduli=2^1..2^9')
    print('antecedent_counts=', nonvacuous)

if __name__ == '__main__':
    check()
