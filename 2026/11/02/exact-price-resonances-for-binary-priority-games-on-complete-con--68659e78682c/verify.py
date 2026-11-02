"""Independent exhaustive check of binary priced rank-game equilibria.

No third-party packages are required. Execute: python3 verify.py
"""
from fractions import Fraction
from itertools import product


def utility(profile, i, choice, price):
    # Larger announced priority precedes smaller priority; smaller index wins ties.
    preceding = sum(
        int(profile[j] > choice or (profile[j] == choice and j < i))
        for j in range(len(profile)) if j != i
    )
    return -preceding - price * choice


def direct_equilibria(n, price):
    result = set()
    for profile in product((0, 1), repeat=n):
        if all(utility(profile, i, profile[i], price) >=
               utility(profile, i, 1 - profile[i], price)
               for i in range(n)):
            result.add(profile)
    return result


def predicted_equilibria(n, price):
    if price > n - 1:
        return {(0,) * n}
    if price.denominator != 1:
        return set()
    r = int(price)
    if r < 1 or r > n - 1:
        return set()
    candidates = set()
    for t in (2*r-n+1, 2*r-n+2):
        if 1 <= t <= n:
            candidates.add((0,) * t + tuple(1 if j % 2 == 0 else 0
                                           for j in range(n-t)))
    for t in (n-2*r, n-2*r-1):
        if 1 <= t < n:
            candidates.add((1,) * t + tuple(0 if j % 2 == 0 else 1
                                           for j in range(n-t)))
    return candidates


def run():
    trials = 0
    profiles = 0
    for n in range(2, 12):
        for numerator in range(1, 2*n+3):
            price = Fraction(numerator, 2)
            observed = direct_equilibria(n, price)
            predicted = predicted_equilibria(n, price)
            assert observed == predicted, (n, price, observed, predicted)
            assert len(predicted) == (2 if price.denominator == 1 and price <= n-1
                                     else 1 if price > n-1 else 0)
            trials += 1
            profiles += 2**n
    # Compare exact ordinal gain to the derived A_i-price identity,
    # independently of equilibrium selection.
    gains = 0
    for n in range(2, 10):
        for profile in product((0, 1), repeat=n):
            for i in range(n):
                earlier_zeros = sum(profile[j] == 0 for j in range(i))
                later_ones = sum(profile[j] == 1 for j in range(i+1, n))
                assert (utility(profile, i, 1, Fraction(3, 2)) -
                        utility(profile, i, 0, Fraction(3, 2)) ==
                        earlier_zeros + later_ones - Fraction(3, 2))
                gains += 1
    print(f'VERIFY_OK game_instances={trials} scanned_profiles={profiles} exact_gain_identites={gains}')


if __name__ == '__main__':
    run()
