"""Self-contained finite checks for the shifted Phi_3 gcd classification.
The theorem and proof apply for all positive shifts, beyond these tests.
Run with Python 3: python verify.py
"""
from fractions import Fraction
from math import gcd


def factors(n):
    ans = {}
    t = 2
    while t * t <= n:
        if n % t == 0:
            e = 0
            while n % t == 0:
                n //= t
                e += 1
            ans[t] = e
        t = 3 if t == 2 else t + 2
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def phi3(n):
    return n*n+n+1


def components(d):
    a = 1
    b = 1
    for p, e in factors(d).items():
        if p % 3 == 1:
            a *= p**e
    for p, e in factors(d*d+3).items():
        if p >= 5:
            b *= p**e
    c = 3 if d % 3 == 0 else 1
    return a, b, c


def predicted(d, n, comp=None):
    a, b, c = components(d) if comp is None else comp
    return gcd(a, phi3(n)) * gcd(b, 2*n+d+1) * (3 if c == 3 and n % 3 == 1 else 1)


def local_weight(p, e, v, root_count):
    if v == 0:
        return Fraction(p-root_count, p)
    if v < e:
        return Fraction(root_count*(p-1), p**(v+1))
    return Fraction(root_count, p**e)


def full_probabilities(a, b, c):
    probs = {1: Fraction(1)}
    channels = [(p, e, 2) for p, e in factors(a).items()] + [(p, e, 1) for p, e in factors(b).items()]
    if c == 3:
        channels.append((3, 1, 1))
    for p, e, roots in channels:
        new = {}
        for value, prob in probs.items():
            for v in range(e+1):
                new[value*p**v] = prob*local_weight(p, e, v, roots)
        probs = new
    assert sum(probs.values()) == 1
    return probs


def main():
    basic_checks = 0
    for d in range(1, 301):
        comp = components(d)
        for n in range(1, 401):
            assert gcd(phi3(n), phi3(n+d)) == predicted(d, n, comp), (d, n)
            basic_checks += 1
    print('PASS: direct gcd identity on', basic_checks, 'shift-index pairs')

    stabilization_checks = 0
    for d in range(1, 151):
        for n in range(1, 201):
            triple = gcd(phi3(n), phi3(n+d), phi3(n+2*d))
            assert triple == gcd(phi3(n), d), (d, n)
            assert gcd(triple, phi3(n+3*d), phi3(n+6*d)) == triple, (d, n)
            stabilization_checks += 1
    print('PASS: three-point stabilization and longer windows on', stabilization_checks, 'cases')

    period_shifts = 0
    observations = 0
    distribution_shifts = 0
    for d in range(1, 101):
        comp = components(d)
        a, b, c = comp
        period = a*b*c
        if period > 10000:
            continue
        values = [gcd(phi3(n), phi3(n+d)) for n in range(period)]
        observations += period
        assert max(values) == period, ('maximum', d)
        for p in factors(period):
            s = period // p
            assert any(values[n] != values[(n+s) % period] for n in range(period)), ('least period', d, p)
        expected = full_probabilities(a, b, c)
        observed = {x: values.count(x) for x in set(values)}
        assert set(expected) == set(observed), ('spectrum', d)
        for x, prob in expected.items():
            assert observed[x] == prob*period, ('frequency', d, x)
        # For every window of length at least three, the remaining
        # prime-power components are A and E, with no B factors.
        higher_period = a*c
        if higher_period <= 10000:
            higher_values = [gcd(phi3(n), d) for n in range(higher_period)]
            assert max(higher_values) == higher_period
            expected_higher = full_probabilities(a, 1, c)
            observed_higher = {x: higher_values.count(x) for x in set(higher_values)}
            assert set(expected_higher) == set(observed_higher)
            for x, prob in expected_higher.items():
                assert observed_higher[x] == prob*higher_period
            for p in factors(higher_period):
                assert any(higher_values[n] != higher_values[(n+higher_period//p)%higher_period]
                           for n in range(higher_period))
        period_shifts += 1
        distribution_shifts += 1
    print('PASS: exact least periods and maximal values for', period_shifts, 'shifts')
    print('PASS: divisor spectra and every exact frequency for', distribution_shifts, 'shifts')
    print('PASS: full-period direct observations:', observations)
    # An explicit higher-exponent test: 7 squared divides the shift.
    d = 49
    a, b, c = components(d)
    period = a*b*c
    rows = [gcd(phi3(n), phi3(n+d)) for n in range(period)]
    exact_weights = full_probabilities(a, b, c)
    assert set(rows) == set(exact_weights)
    for value, prob in exact_weights.items():
        assert rows.count(value) == period*prob
    for p in factors(period):
        assert any(rows[n] != rows[(n+period//p)%period] for n in range(period))
    print('PASS: squared-prime shift d=49, period 29449, six complete value frequencies')
    for d in (1, 2, 3, 6, 7, 14, 21):
        a, b, c = components(d)
        print('EXAMPLE: d={}, A={}, B={}, E={}, T={}'.format(d, a, b, c, a*b*c))

if __name__ == '__main__':
    main()
