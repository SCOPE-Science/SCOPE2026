"""Independent reconstruction of cyclic BWT run counts for sparse binary words.
Run with Python 3 standard library: python verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def direct_bwt(word):
    n = len(word)
    order = sorted(range(n), key=lambda i: word[i:] + word[:i])
    return ''.join(word[(i - 1) % n] for i in order)


def gap_bwt(gaps):
    """Sort cyclic rotations by leading zero count, then following gap tuple."""
    a = tuple(gaps)
    out = []
    for ell in range(max(a), -1, -1):
        valid = [j for j in range(3) if a[j] >= ell]
        valid.sort(key=lambda j: (-a[(j + 1) % 3],
                                   -a[(j + 2) % 3], -a[j]))
        out.extend('1' if ell == a[j] else '0' for j in valid)
    return ''.join(out)


def runs(w):
    return 1 + sum(u != v for u, v in zip(w, w[1:]))


def gap_prediction(g):
    x, y, z = sorted(g)
    if x == z or z - x == 1:
        return 2
    if x == y or y == z:
        return 4
    j = g.index(x)
    return (6 if (z - y >= 2) else 4) if g[(j+1) % 3] == y else (6 if (y-x >= 2) else 4)


def predicted_census(n):
    twos = n if n % 3 else n // 3
    sixes = n * sum(n - 6 - 3*j for j in range(max(0, (n-7)//3+1)))
    return {2:twos, 4:comb(n,3)-twos-sixes, 6:sixes}


def main():
    total_words = 0
    for n in range(4, 23):
        actual = Counter()
        for chosen in combinations(range(n),3):
            a,b,c = chosen
            g = (b-a-1, c-b-1, n-c+a-1)
            word = ''.join('1' if j in chosen else '0' for j in range(n))
            bwt1 = direct_bwt(word)
            bwt2 = gap_bwt(g)
            assert bwt1 == bwt2, (n,g,bwt1,bwt2)
            observed = runs(bwt1)
            assert observed == gap_prediction(g), (n,g,observed)
            actual[observed] += 1
        expected = predicted_census(n)
        assert dict(actual) == {k:v for k,v in expected.items() if v}, (n,actual,expected)
        total_words += comb(n,3)
    # Independently check the structural gap law for all ordered triples with sum up to 90.
    gap_checks = 0
    for t in range(1, 36):
        for a in range(t+1):
            for b in range(t-a+1):
                g = (a,b,t-a-b)
                assert runs(gap_bwt(g)) == gap_prediction(g), g
                gap_checks += 1
    print('ALL_CHECKS_PASS', 'full_word_count=', total_words,
          'gap_triples_checked=', gap_checks,
          'max_word_length=', 22, 'max_gap_sum=', 35)

if __name__ == '__main__':
    main()
