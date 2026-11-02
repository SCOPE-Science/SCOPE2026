"""Self-contained exact checks for three-tap binary cyclic convolution."""
from itertools import combinations
from collections import Counter
from math import comb


def rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


def gcd(a, b):
    while b:
        a, b = b, rem(a, b)
    return a


def mul(a,b):
    out=0
    while b:
        if b&1:out ^= a
        a <<= 1
        b >>= 1
    return out

def divide(a, b):
    q = 0
    while a and a.bit_length() >= b.bit_length():
        d = a.bit_length()-b.bit_length()
        q ^= 1 << d
        a ^= b << d
    assert a == 0
    return q


def expected_level(triple, k):
    vals = tuple(triple)
    if len({x % 3 for x in vals}) != 3:
        return None
    a, b = vals[1] - vals[0], vals[2] - vals[0]
    def v2(x):
        return (x & -x).bit_length() - 1
    return min(v2(a),v2(b),k)


def check():
    checked = 0
    for k in range(5):
        m = 1 << k
        n = 3*m
        obs = Counter()
        xn = (1 << n) | 1
        for tr in combinations(range(n), 3):
            f = sum(1 << a for a in tr)
            g = gcd(f, xn)
            level = expected_level(tr, k)
            expected = 1 if level is None else (1 | (1 << (1 << level)) | (1 << (2*(1 << level))))
            assert g == expected, (k,tr,g,expected)
            obs[g.bit_length()-1 if g != 1 else 0] += 1
            checked += 1
        target = {0:comb(n,3)-m**3}
        for s in range(k):
            target[2 << s] = 3*m**3 // (4**(s+1))
        target[2 << k] = m
        if k == 0:
            target.pop(0, None) # no invertible weight-three matrix at n=3
        assert dict(obs) == target, (k,obs,target)
        print('RANK_CENSUS',k,n,dict(sorted(obs.items())))
    # The polynomial ideal kernel, rather than just rank, is tested on all its vectors.
    kernel_checked = 0
    for k in range(4):
        m = 1 << k
        n = 3*m
        xn = (1 << n)|1
        for s in range(k+1):
            d = 1 << s
            r = m // d
            h = 1 | (1 << d) | (1 << (2*d))
            quotient = divide(xn, h)
            predicted = Counter({2*r*j:comb(d,j)*3**j for j in range(d+1)})
            got = Counter()
            for u in range(1 << (2*d)):
                # Each basis vector of the ideal is the polynomial x^j*(xn/h).
                v = 0
                for j in range(2*d):
                    if u >> j & 1:
                        v ^= quotient << j
                assert v < (1 << n)
                assert rem(mul(v,h), xn) == 0
                got[v.bit_count()] += 1
                kernel_checked += 1
            assert got == predicted, (k,s,got,predicted)
            print('CODE_WEIGHT',k,s,dict(sorted(got.items())))
    print('VERIFY_OK', 'three_tap_matrices', checked, 'kernel_words',kernel_checked)


if __name__ == '__main__':
    check()
