#!/usr/bin/env python3
"""Finite regression for the explicit antidictionary of a sparse binary word.
The infinite classification is established by the separate mathematical proof.
"""
from itertools import product


def power2(g):
    return g > 0 and (g & (g - 1)) == 0


def proposed(max_length):
    b = {'111'}
    for g in range(1, max_length):
        core = '1' + '0' * (g - 1) + '1'
        if not power2(g):
            if len(core) <= max_length:
                b.add(core)
        else:
            left = '0' * (1 if g == 1 else g // 2) + core
            right = core + '0' * (2 * g)
            if len(left) <= max_length:
                b.add(left)
            if len(right) <= max_length:
                b.add(right)
    return b


def main():
    nsource = 1 << 15
    positions = {(1 << j) - 1 for j in range(16)}
    word = ''.join('1' if i in positions else '0' for i in range(nsource))
    max_n = 40
    predicted = proposed(max_n)
    # Every observed candidate has both proper factors and is absent in the
    # long prefix. The independent analytical proof covers unbounded indices.
    obs_previous = {''}
    tests = 0
    for n in range(1, max_n + 1):
        obs = {word[i:i+n] for i in range(nsource-n+1)}
        if n >= 2:
            actual = {u+b for u in obs_previous for b in '01'
                      if u+b not in obs and (u+b)[1:] in obs_previous}
            expected = {u for u in predicted if len(u) == n}
            assert actual == expected, (n, sorted(actual ^ expected))
            tests += len(obs_previous) + len(obs)
        obs_previous = obs
    # Independent all-word factor-language test at short lengths.
    for n in range(1, 13):
        obs = {word[i:i+n] for i in range(nsource-n+1)}
        for tup in product('01', repeat=n):
            v = ''.join(tup)
            avoided = all(forbidden not in v for forbidden in predicted)
            assert (v in obs) == avoided, (n, v)
            tests += 1
    # Lacunary length profile from the closed generating series.
    for n in range(1, max_n + 1):
        predicted_n = sum(len(x) == n for x in predicted)
        g = n - 1
        count = int(n >= 2 and not power2(g)) + (2 if n == 3 else 0)
        q = g // 3
        if g >= 3 and g % 3 == 0 and power2(q):
            count += 2
        assert count == predicted_n, (n, count, predicted_n)
        tests += 1
    print('VERIFY_OK checks=', tests, 'lengths=', max_n,
          'distinct_forbidden_up_to_length=', len(predicted))


if __name__ == '__main__':
    main()
