"""Exact tests for the variation modulus of cyclic simplex projection.

Run: python3 checker.py
Tests are finite checks; the all-dimensional result has a separate proof.
"""
from fractions import Fraction
from itertools import product
from random import Random


def variation(v):
    return sum(abs(v[(i+1) % len(v)] - v[i]) for i in range(len(v)))


def sharp(n):
    N = n + 2
    return Fraction(N * N // 8, (N + 1) // 2)


def projection(x):
    n = len(x)
    for m in range(1, n + 1):
        ordered = sorted(x, reverse=True)
        tau = (sum(ordered[:m]) - 1) / m
        if m == n or ordered[m] <= tau:
            if ordered[m-1] > tau:
                return [max(Fraction(0), xi-tau) for xi in x]
    raise AssertionError('threshold')


def build_runs(total, runs):
    assert 1 <= runs <= total
    out = [1] * (total - runs + 1)
    for _ in range(runs - 1):
        out += [0, 1]
    return out


def sharp_witness(n):
    N = n + 2
    m = (N + 1) // 2
    a = (m+1)//2
    b = m//2
    r = a if N%2 == 0 else a-1
    s = b
    left, right = build_runs(a, r), build_runs(b, s)
    assert len(left)+len(right) == n
    active = left + right
    cut = [1]*len(left) + [0]*len(right)
    x = [Fraction(1,m) if t else Fraction(-1) for t in active]
    eps = Fraction(1,10*m)
    y = [xi+eps*bi for xi,bi in zip(x,cut)]
    numerator = variation([yi-xi for xi,yi in zip(projection(x),projection(y))])
    denominator = variation([yi-xi for xi,yi in zip(x,y)])
    assert denominator > 0
    return numerator / denominator, (a,b,r,s,active,cut)


def exhaustive_selectors(n):
    expected = sharp(n)
    best = Fraction(0)
    count = 0
    for mask in range(1, 1 << n):
        m = mask.bit_count()
        for start in range(n):
            im = 0
            for length in range(1, n):
                im |= 1 << ((start + length - 1) % n)
                a = (im & mask).bit_count()
                b = m-a
                if a == 0 or b == 0:
                    continue
                out = [(b if (im >> j) & 1 else -a) if (mask >> j) & 1 else 0 for j in range(n)]
                q = Fraction(variation(out),2*m)
                count += 1
                assert q <= expected, (n,mask,start,length,q,expected)
                best = max(best,q)
    assert best == expected,(n,best,expected)
    return count


def run():
    count = 0
    for n in range(2, 11):
        count += exhaustive_selectors(n)
        q, data = sharp_witness(n)
        assert q == sharp(n),(n,q,data)
    rng = Random(138427)
    for n in range(2, 21):
        for _ in range(120):
            x = [Fraction(rng.randint(-9,9),rng.randint(2,19)) for _ in range(n)]
            y = [Fraction(rng.randint(-9,9),rng.randint(2,19)) for _ in range(n)]
            denom = variation([xi-yi for xi, yi in zip(x,y)])
            if denom:
                numer = variation([xi-yi for xi, yi in zip(projection(x),projection(y))])
                assert numer <= sharp(n)*denom,(n,numer,denom)
            assert variation(projection(x)) <= variation(x)
    print('PASS: exhaustive selector/interval cases',count)
    print('PASS: attaining data pairs n=2..10 (9 dimensions)')
    print('PASS: random exact-rational input pairs',19*120)
    print('PASS: one-input variation inequality',19*120)

if __name__ == '__main__':
    run()
