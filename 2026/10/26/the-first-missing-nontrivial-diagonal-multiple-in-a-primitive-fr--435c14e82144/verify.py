#!/usr/bin/env python3
"""Exact, finite checks for the first nontrivial missing diagonal multiplier."""
from itertools import product
from math import gcd

PRIMES = (2, 3, 5, 7, 11, 13)


def allowed_state(m, states):
    # State A: p | a; B: p | b; N: p divides neither.
    # These alternatives are mutually exclusive because gcd(a,b)=1.
    for j in range(1, m):
        bad = False
        for p, state in zip(PRIMES, states):
            if state == "A" and j % p == 0:
                bad = True
            elif state == "B" and (m-j) % p == 0:
                bad = True
            elif state == "N" and j % p == 0 and (m-j) % p == 0:
                bad = True
            if bad:
                break
        if not bad:
            return True
    return False


def predicted_failure(states):
    where = dict(zip(PRIMES, states))
    return (all(where[p] == "A" for p in (5, 11))
            and all(where[p] == "B" for p in (3, 7, 13))) or ( 
            all(where[p] == "B" for p in (5, 11))
            and all(where[p] == "A" for p in (3, 7, 13)))


def has_primitive_representation(m, a, b):
    assert a >= 2 and b >= 2 and gcd(a, b) == 1
    return any(gcd(b*j, a*(m-j)) == 1 for j in range(1, m))


def main():
    states_examined = 0
    for states in product("ABN", repeat=len(PRIMES)):
        states_examined += 1
        for m in range(2, 16):
            assert allowed_state(m, states), (m, states)
        assert (not allowed_state(16, states)) == predicted_failure(states), states

    pairs_examined = 0
    for a in range(2, 151):
        for b in range(2, 151):
            if gcd(a, b) != 1:
                continue
            pairs_examined += 1
            for m in range(2, 16):
                assert has_primitive_representation(m, a, b), (m, a, b)
            expected = ((a % 55 == 0 and b % 273 == 0) or
                        (a % 273 == 0 and b % 55 == 0))
            assert (not has_primitive_representation(16, a, b)) == expected
    for a, b in ((55, 273), (273, 55), (110, 273), (55, 546), (55, 274)):
        if gcd(a, b) == 1:
            expected = ((a % 55 == 0 and b % 273 == 0) or
                        (a % 273 == 0 and b % 55 == 0))
            assert (not has_primitive_representation(16, a, b)) == expected
    assert not has_primitive_representation(16, 55, 273)
    assert has_primitive_representation(15, 55, 273)
    assert has_primitive_representation(2, 55, 273)
    print(f"VERIFY_OK state_assignments={states_examined} coprime_pairs={pairs_examined} diagonal_range=2..16")

if __name__ == "__main__":
    main()
