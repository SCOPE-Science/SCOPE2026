"""Finite reproducibility checks for four-prime unitary divisor partitions.

Run with Python 3.9 or newer: python3 verify.py.
Only elementary integer arithmetic is used.
"""

R_EXCEPTIONS = (11, 13, 17, 19)
CORRECTION_WITNESSES = {11: (1,7,28), 13: (28,), 17: (12,), 19: (4,)}
HALF_WITNESSES = {
    11: (1, 28, 77, 84, 308),
    13: (3, 12, 39, 156, 364),
    17: (1, 17, 28, 204, 476),
    19: (4, 57, 76, 133, 532),
}


def sieve_spf(bound):
    spf = list(range(bound + 1))
    for p in range(2, int(bound**0.5) + 1):
        if spf[p] == p:
            for j in range(p*p, bound + 1, p):
                if spf[j] == j:
                    spf[j] = p
    return spf


def prime_power_factors(n, spf):
    answer = []
    while n > 1:
        p = spf[n]
        pp = 1
        while n % p == 0:
            n //= p
            pp *= p
        answer.append((p, pp))
    return answer


def unitary_divisors(factors):
    ds = [1]
    for _, pp in factors:
        ds += [d * pp for d in ds]
    return sorted(ds)


def is_partitionable(divisors, target):
    achievable = 1
    for d in divisors:
        achievable |= achievable << d
    return bool((achievable >> target) & 1)


def is_prime_power_r(r, spf):
    f = prime_power_factors(r, spf)
    return len(f) == 1 and f[0][0] > 5


def theorem_family(n, factors, spf):
    if n == 840:
        return True
    if n % 60 == 0 and n // 60 > 1 and is_prime_power_r(n // 60, spf):
        return True
    if n // 84 in R_EXCEPTIONS and n % 84 == 0:
        return True
    return False


def finite_census(bound=100000):
    spf = sieve_spf(bound)
    tested = 0
    positives = 0
    half_positives = 0
    for n in range(4, bound + 1, 4):
        factors = prime_power_factors(n, spf)
        if len(factors) != 4:
            continue
        tested += 1
        divisors = unitary_divisors(factors)
        sigma_star = sum(divisors)
        is_zumkeller = sigma_star % 2 == 0 and is_partitionable(divisors, sigma_star // 2)
        predicted = theorem_family(n, factors, spf)
        assert is_zumkeller == predicted, (n, is_zumkeller, predicted)
        if is_zumkeller:
            positives += 1
            proper = divisors[:-1]
            assert (sigma_star-n) % 2 == 0
            assert is_partitionable(proper, (sigma_star-n)//2)
            half_positives += 1
    print('FINITE_CENSUS', 'up_to=', bound, 'four_support_divisible_by_four=', tested,
          'unitary_zumkeller=', positives, 'unitary_half=', half_positives)
    return spf


def verify_symbolic_certificates(spf):
    for r in R_EXCEPTIONS:
        n = 84*r
        ds = unitary_divisors(prime_power_factors(n, spf))
        sigma = sum(ds)
        assert sigma == 160*(r+1)
        d = 80-4*r
        corr = CORRECTION_WITNESSES[r]
        assert len(set(corr)) == len(corr)
        assert all(x in ds and x<n for x in corr)
        assert sum(corr) == d
        assert n+sum(corr) == sigma//2
        witness = HALF_WITNESSES[r]
        assert len(set(witness)) == len(witness)
        assert all(x in ds and x<n for x in witness)
        assert sum(witness)*2 == sigma-n
    ds = unitary_divisors(prime_power_factors(840,spf))
    assert sum(ds) == 1728 and 840+24 == 1728//2
    w=(280,105,56,3)
    assert all(x in ds and x<840 for x in w) and 2*sum(w) == sum(ds)-840
    for r in (7,11,13,17,19,23,29,49,121,343):
        assert is_prime_power_r(r, spf)
        n = 60*r
        ds = unitary_divisors(prime_power_factors(n, spf))
        assert sum(ds) == 120*(r+1)
        assert 60+r*60 == sum(ds)//2
        w=(3*r, 12*r, 15*r, 60)
        assert len(set(w)) == 4 and all(x in ds and x<n for x in w)
        assert 2*sum(w)==sum(ds)-n
    print('CERTIFICATES_OK')


if __name__ == '__main__':
    spf=finite_census()
    verify_symbolic_certificates(spf)
    print('VERIFY_OK')
