#!/usr/bin/env python3
"""Direct finite checks for alternating-word minimal absent subsequences."""
from collections import Counter
from itertools import product


def is_subsequence(pattern, target):
    iterator = iter(target)
    return all(any(c == p for c in iterator) for p in pattern)


def direct_minimal(pattern, target):
    if not pattern or is_subsequence(pattern, target):
        return False
    return all(is_subsequence(pattern[:i] + pattern[i+1:], target)
               for i in range(len(pattern)))


def first_greedy_position(word):
    if not word:
        return 0
    return len(word) + (word[0] == 'b') + sum(
        word[i] == word[i+1] for i in range(len(word)-1))


def predicted(pattern, m):
    if len(pattern) < 2:
        return False
    length = first_greedy_position(pattern)
    if length not in (2*m+1, 2*m+2):
        return False
    if pattern.startswith('ab'):
        return False
    if any(pattern[i-1] == pattern[i+1] != pattern[i]
           for i in range(1, len(pattern)-1)):
        return False
    return length == 2*m+1 or pattern[-1] == pattern[-2]


def polynomial_counts(limit=50):
    # Rational univariate series: F=z(1+z+z^2)/(1-z^2-z^3), H=z^2F.
    coefficients = [0] * (limit+1)
    for n in range(1,limit+1):
        coefficients[n] = int(n in (1,2,3))
        if n >= 2:
            coefficients[n] += coefficients[n-2]
        if n >= 3:
            coefficients[n] += coefficients[n-3]
    return coefficients


def bivariate_coefficients(limit=40):
    # F(u,z)=u*z*(1+z+u*z*z)/(1-u*z*z-u*u*z*z*z).
    out = [Counter() for _ in range(limit+1)]
    out[1][1] += 1
    out[2][1] += 1
    out[3][2] += 1
    for n in range(1,limit+1):
        if n>=3:
            for k,v in out[n-2].items():
                out[n][k+1]+=v
        if n>=4:
            for k,v in out[n-3].items():
                out[n][k+2]+=v
    return out


def run():
    c = polynomial_counts(52)
    f = bivariate_coefficients(40)
    for m in range(1, 8):
        target = 'ab'*m
        actual = Counter()
        predicted_count = Counter()
        for k in range(1, 2*m+3):
            for letters in product('ab', repeat=k):
                v = ''.join(letters)
                direct = direct_minimal(v, target)
                candidate = predicted(v,m)
                assert direct == candidate, (m,v,direct,candidate)
                if direct:
                    actual[(first_greedy_position(v),len(v))] += 1
                    predicted_count[len(v)] += 1
        total=sum(actual.values())
        from_gf = c[2*m+1] + c[2*m]  # H=z^2 F.
        assert total == from_gf, (m, total, from_gf)
        gf_refined=Counter(f[2*m+1])
        for k,v in f[2*m].items():
            gf_refined[k+1]+=v
        assert dict(gf_refined) == dict(predicted_count), (m, gf_refined, predicted_count)
        print('m=%d total=%d expected=%d by_length=%s cost_odd=%d cost_even=%d' % (
            m,total,from_gf,dict(sorted(predicted_count.items())),
            sum(v for (cost, length),v in actual.items() if cost==2*m+1),
            sum(v for (cost, length),v in actual.items() if cost==2*m+2)))
    sequence = [c[2*m]+c[2*m+1] for m in range(1,20)]
    assert all(sequence[i] == 2*sequence[i-1] - sequence[i-2] + sequence[i-3]
               for i in range(3,len(sequence)))
    print('all finite checks and recurrence assertions passed')

if __name__ == '__main__':
    run()
