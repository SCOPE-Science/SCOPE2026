#!/usr/bin/env python3
from itertools import product

PRIMES = (3, 5, 7, 11, 13)

def radius(m):
    return 1 if m % 2 == 0 else 2

def witness(profile, p, B):
    dp = {0: ()}
    for c in profile:
        nd = {}
        for s, w in dp.items():
            for t in range(-B, B + 1):
                if t % p == c % p:
                    continue
                ns = s + t
                if ns not in nd:
                    nd[ns] = w + (t,)
        dp = nd
    return dp.get(0)

def check_pair_triple():
    pair_cases = 0
    triple_cases = 0
    for p in PRIMES:
        for c in product(range(p), repeat=2):
            w = witness(c, p, 1)
            assert w is not None and sum(w) == 0 and max(map(abs, w)) <= 1
            pair_cases += 1
        for c in product(range(p), repeat=3):
            w = witness(c, p, 2)
            assert w is not None and sum(w) == 0 and max(map(abs, w)) <= 2
            triple_cases += 1
    return pair_cases, triple_cases

def check_full_profiles():
    profiles = 0
    ranges = [(m, 3) for m in range(2, 10)] + [(m, 5) for m in range(2, 7)] + [(m, 7) for m in range(2, 6)]
    for m, p in ranges:
        B = radius(m)
        for c in product(range(p), repeat=m):
            w = witness(c, p, B)
            assert w is not None
            assert sum(w) == 0
            assert all(abs(t) <= B and t % p != ci for t, ci in zip(w, c))
            profiles += 1
    return profiles

def check_lower_bounds():
    cases = 0
    for m in range(2, 10):
        zero = (0,) * m
        assert witness(zero, 3, 0) is None
        cases += 1
        if m % 2 == 1:
            assert witness(zero, 3, 1) is None
            cases += 1
    return cases

def check_zero_sum_triples():
    Z = [(a,b,c) for a in range(-2,3) for b in range(-2,3) for c in range(-2,3) if a+b+c == 0]
    assert len(Z) == 19
    slices = {}
    for coord in range(3):
        for value in range(-2,3):
            slices[(coord,value)] = sum(1 for z in Z if z[coord] == value)
            assert slices[(coord,value)] <= 5
    return len(Z), max(slices.values())

def main():
    pair_cases, triple_cases = check_pair_triple()
    profiles = check_full_profiles()
    lower = check_lower_bounds()
    zcount, maxslice = check_zero_sum_triples()
    print(f"VERIFY_OK pair_cases={pair_cases} triple_cases={triple_cases} full_profiles={profiles} lower_bound_cases={lower} zero_sum_triples={zcount} max_coordinate_slice={maxslice}")

if __name__ == '__main__':
    main()
