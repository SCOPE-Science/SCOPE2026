"""Exact finite corroboration of complement-orbit rigidity for 2**a * p**2.

Run: python3 verify.py
This is a finite check, not a proof of the unrestricted theorem.
"""


def primes_through(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for d in range(2, int(limit ** 0.5) + 1):
        if sieve[d]:
            for multiple in range(d * d, limit + 1, d):
                sieve[multiple] = 0
    return [d for d in range(3, limit + 1, 2) if sieve[d]]


def complement_orbits(a, p):
    n = (2 ** a) * (p ** 2)
    divisors = [2 ** i * p ** j for i in range(a + 1) for j in range(3)]
    assert len(set(divisors)) == 3 * (a + 1)
    orbits = sorted({tuple(sorted((d, n // d))) for d in divisors})
    assert sum(x if x == y else x + y for x, y in orbits) == sum(divisors)
    return n, divisors, orbits


def verify():
    checked = 0
    found = []
    singleton_checked = 0
    for a in range(1, 31):
        for p in primes_through(997):
            n, divisors, orbits = complement_orbits(a, p)
            weights = [x if x == y else x + y for x, y in orbits]
            assert sum(divisors) == (2 ** (a + 1) - 1) * (p ** 2 + p + 1)
            deficit = sum(divisors) - 2 * n
            if a % 2 == 0:
                singletons = [o for o in orbits if o[0] == o[1]]
                assert singletons == [(2 ** (a // 2) * p,) * 2]
                singleton_checked += 1
            else:
                assert all(x != y for x, y in orbits)
            matches = []
            if deficit == 0:
                matches.append(())
            for i in range(len(orbits)):
                if weights[i] == deficit:
                    matches.append((i,))
                for j in range(i + 1, len(orbits)):
                    if weights[i] + weights[j] == deficit:
                        matches.append((i, j))
            checked += 1
            if matches:
                decoded = [tuple(orbits[i] for i in ids) for ids in matches]
                found.append((a, p, decoded))
                assert a == 2 and p == 3
                assert decoded == [((4, 9), (6, 6))]
    assert found == [(2, 3, [((4, 9), (6, 6))])]
    assert {1, 2, 3, 12, 18, 36} == set(complement_orbits(2, 3)[1]) - {4, 6, 9}
    assert sum([1, 2, 3, 12, 18, 36]) == 72
    print(
        "VERIFY_OK"
        f" independent_parameter_pairs={checked}"
        f" square_root_checks={singleton_checked}"
        " sole_at_most_two_orbit_case=36"
        " exact_integer_arithmetic=PASS finite_only=YES"
    )


if __name__ == "__main__":
    verify()
