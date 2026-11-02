"""Exact standard-library verifier for four-by-two Fourier phase alphabets.

Run: python3 CHECK.py
All calculations are in Z[i] or Z[omega]; no floating point is used.
"""
import json
from collections import Counter
from itertools import product
from pathlib import Path

ROOTS = {
    2: [(1, 0), (-1, 0)],
    3: [(1, 0), (0, 1), (-1, -1)],
    4: [(1, 0), (0, 1), (-1, 0), (0, -1)],
    6: [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)],
}


def sqnorm(q, a, b):
    return a*a + b*b if q in (2, 4) else a*a - a*b + b*b


def score_correlations(q, phases):
    roots = ROOTS[q]
    total = 64
    for dx in range(4):
        for dy in range(-1, 2):
            if not (dx > 0 or (dx == 0 and dy > 0)):
                continue
            a = b = 0
            for j in range(4):
                for k in range(2):
                    if j + dx < 4 and 0 <= k + dy < 2:
                        x, y = roots[(phases[2*(j+dx)+(k+dy)]
                                      - phases[2*j+k]) % q]
                        a += x
                        b += y
            total += 2*sqnorm(q, a, b)
    return total


def score_convolutions(q, phases):
    roots = ROOTS[q]
    total = 0
    for j in range(7):
        for k in range(3):
            a = b = 0
            for j1 in range(4):
                for k1 in range(2):
                    j2, k2 = j-j1, k-k1
                    if 0 <= j2 < 4 and 0 <= k2 < 2:
                        x, y = roots[(phases[2*j1+k1]
                                      + phases[2*j2+k2]) % q]
                        a += x
                        b += y
            total += sqnorm(q, a, b)
    return total


def normalize(q, phases):
    """Unique common/linear-character gauge: indices 00,01,10 are zero."""
    p00 = phases[0]
    p01 = phases[1]
    p10 = phases[2]
    return tuple((phases[2*j+k] - p00 - j*(p10-p00)
                  - k*(p01-p00)) % q for j in range(4) for k in range(2))


def reflection_orbit(q, tail):
    a = (0, 0, 0) + tuple(tail)
    out = set()
    for flip_j, flip_k, conjugate in product((0, 1), repeat=3):
        arr = []
        for j in range(4):
            for k in range(2):
                jj = 3-j if flip_j else j
                kk = 1-k if flip_k else k
                arr.append(((-1 if conjugate else 1) * a[2*jj+kk]) % q)
        out.add(normalize(q, arr)[3:])
    return out


def calculation(q):
    counts = Counter()
    scores = {}
    for tail in product(range(q), repeat=5):
        phases = (0, 0, 0) + tail
        a = score_correlations(q, phases)
        b = score_convolutions(q, phases)
        assert a == b, (q, tail, a, b)
        counts[a] += 1
        scores[tail] = a
    assert len(scores) == q**5 and sum(counts.values()) == q**5
    optimum = min(counts)
    next_score = sorted(counts)[1]
    winners = {tail for tail, val in scores.items() if val == optimum}
    reps = []
    while winners:
        t = min(winners)
        orbit = reflection_orbit(q, t)
        assert orbit <= winners, (q, t, orbit-winners)
        reps.append({'representative': list(t), 'size_gauge': len(orbit)})
        winners -= orbit
    return {
        'q': q,
        'normalized_patterns_checked': q**5,
        'minimum_fourth_moment': optimum,
        'next_distinct_fourth_moment': next_score,
        'gap': next_score-optimum,
        'maximum_fourth_moment': max(counts),
        'normalized_minimizer_count': counts[optimum],
        'all_minimizer_count': counts[optimum]*q**3,
        'geometric_symmetry_orbits': reps,
        'histogram': [[int(k), int(v)] for k, v in sorted(counts.items())],
    }


def main():
    certificate = json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text(encoding='utf-8'))
    assert certificate['algebras'] == {'2': 'Gaussian', '3': 'Eisenstein', '4': 'Gaussian', '6': 'Eisenstein'}
    total = 0
    for q in (2, 3, 4, 6):
        actual = calculation(q)
        expected = certificate['alphabets'][str(q)]
        assert actual == expected, (q, actual, expected)
        total += actual['normalized_patterns_checked']
        print('q=', q, 'minimum=', actual['minimum_fourth_moment'],
              'gap=', actual['gap'], 'minimizers=', actual['all_minimizer_count'],
              'orbits=', len(actual['geometric_symmetry_orbits']))
    assert total == 9075
    print('CHECK_OK', total, 'exact exhaustive normalized arrays, double evaluated')


if __name__ == '__main__':
    main()
