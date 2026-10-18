"""Exact finite checks for a local-sieve full-support theorem.

Uses only the Python standard library; finite tests supplement the proof.
"""
from itertools import combinations
from math import gcd, prod, comb


def primes_below(n):
    return [i for i in range(2, n) if all(i % j for j in range(2, int(i**0.5) + 1))]


def crt_for_selection(h, small_primes, selected):
    modulus = prod(small_primes)
    residue = 0
    for p in small_primes:
        component = modulus // p
        desired = 2 if p in selected else 1
        residue += desired * component * pow(component, -1, p)
    return residue % modulus, modulus


def check_selected(h, selected, ps):
    b, modulus = crt_for_selection(h, ps, selected)
    assert gcd(b * (b + h), modulus) == 1, (h, selected, 'endpoint')
    survived = {i + 1 for i in range(1, h) if gcd(b + i, modulus) == 1}
    assert survived == set(selected), (h, selected, survived)
    return b


def main():
    number_primes = 0
    selected_patterns = 0
    for P in primes_below(102):
        if P < 7:
            continue
        h = P - 1
        ps = primes_below(h)
        togglable = [p for p in ps if h // 2 < p and (h + 2) % p != 0]
        seen = set()
        counts = {}
        for k in range(len(togglable) + 1):
            for selected_tuple in combinations(togglable, k):
                selected = set(selected_tuple)
                b = check_selected(h, selected, ps)
                assert b not in seen
                seen.add(b)
                counts[k] = counts.get(k, 0) + 1
                selected_patterns += 1
            assert counts[k] == comb(len(togglable), k)
        number_primes += 1
        print(f'P={P:3d}, h={h:3d}, togglable={len(togglable):2d}, verified={len(seen):4d}')

    # Independent direct enumeration: exact support bound for small anchors.
    for P in [7, 11, 13, 17, 19]:
        h = P - 1
        ps = primes_below(h)
        mod = prod(ps)
        U = [p for p in ps if h//2 < p and (h+2) % p]
        histogram = {}
        for b in range(mod):
            if gcd(b * (b+h), mod) > 1:
                continue
            k = sum(gcd(b+i, mod) == 1 for i in range(1, h))
            histogram[k] = histogram.get(k, 0) + 1
        assert all(histogram.get(k, 0) >= comb(len(U), k) for k in range(len(U) + 1))
        print(f'EXHAUSTIVE P={P}, modulus={mod}, admissible={sum(histogram.values())}, counts={sorted(histogram.items())}')

    print(f'PASS: {selected_patterns} distinct CRT subset patterns at {number_primes} prime anchors; five exhaustive local models.')

if __name__ == '__main__':
    main()
