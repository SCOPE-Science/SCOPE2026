#!/usr/bin/env python3
"""Exact rational checker for adjacent-two-deletion coding certificates."""
import json
from fractions import Fraction
from pathlib import Path


def shadow_string(n, value):
    bits = format(value, f"0{n}b")
    return {int(bits[:i] + bits[i + 2:], 2) if n > 2 else 0
            for i in range(n - 1)}


def shadow_bits(n, value):
    # Delete the two positions starting at i, with i counted from the left.
    return {((value >> (n - i)) << (n - 2 - i)) |
            (value & ((1 << (n - 2 - i)) - 1))
            for i in range(n - 1)}


def check():
    certificate = json.loads((Path(__file__).parent / 'certificate.json').read_text('utf-8'))
    expected_integer = {2: 1, 3: 2, 4: 4, 5: 4, 6: 8, 7: 13, 8: 20}
    expected_fractional = {**{n: Fraction(s) for n, s in expected_integer.items()}, 8: Fraction(21)}
    all_shadows = {}
    for record in certificate['small_sizes']:
        n = record['n']
        assert n in expected_integer and n not in all_shadows
        shadows = {}
        for x in range(1 << n):
            a = shadow_string(n, x)
            b = shadow_bits(n, x)
            assert a == b, (n, x, a, b)
            assert a and all(0 <= y < 1 << (n - 2) for y in a)
            shadows[x] = a
        all_shadows[n] = shadows

        code = record['witness']
        assert len(code) == expected_integer[n] and len(set(code)) == len(code)
        output_to_codeword = {}
        for x in code:
            assert 0 <= x < 1 << n
            for y in shadows[x]:
                assert y not in output_to_codeword, (n, x, output_to_codeword.get(y), y)
                output_to_codeword[y] = x

        primal = {x: Fraction(v) for x, v in record['shadow_primal']}
        dual = {y: Fraction(v) for y, v in record['shadow_dual']}
        assert len(primal) == len(record['shadow_primal'])
        assert len(dual) == len(record['shadow_dual'])
        assert all(0 <= x < 1 << n and v >= 0 for x, v in primal.items())
        assert all(0 <= y < 1 << (n - 2) and v >= 0 for y, v in dual.items())
        assert sum(primal.values(), Fraction(0)) == expected_fractional[n]
        assert sum(dual.values(), Fraction(0)) == expected_fractional[n]
        for y in range(1 << (n - 2)):
            assert sum((primal.get(x, Fraction(0)) for x in range(1 << n)
                        if y in shadows[x]), Fraction(0)) <= 1, ('primal', n, y)
        for x in range(1 << n):
            assert sum((dual.get(y, Fraction(0)) for y in shadows[x]), Fraction(0)) >= 1, ('dual', n, x)

    assert len(all_shadows) == len(expected_integer)
    n = 8
    shadows = all_shadows[n]
    cliques = certificate['eight_word_clique_cover']
    assert len(cliques) == 77
    cover = [Fraction(0)] * (1 << n)
    total = Fraction(0)
    for clique in cliques:
        vertices = clique['codewords']
        weight = Fraction(clique['weight'])
        assert weight > 0 and len(vertices) >= 2 and len(set(vertices)) == len(vertices)
        assert all(isinstance(x, int) and 0 <= x < 1 << n for x in vertices)
        for i, x in enumerate(vertices):
            for y in vertices[:i]:
                assert not shadows[x].isdisjoint(shadows[y]), ('not a clique', x, y)
            cover[x] += weight
        total += weight
    assert all(weight >= 1 for weight in cover)
    assert total == Fraction(482, 23)
    assert 20 < total < 21
    print('VERIFY_OK')
    print('integer maxima n=2..8: ' + ','.join(map(str, expected_integer.values())))
    print('fractional optima n=2..8: ' + ','.join(map(str, expected_fractional.values())))
    print('n=8 clique-cover weight:', str(total), '; distinct cliques:', len(cliques))
    print('first fractional gap: n=8')


if __name__ == '__main__':
    check()
