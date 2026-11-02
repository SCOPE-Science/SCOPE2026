#!/usr/bin/env python3
"""Independent word enumeration versus the rational generating function, stdlib-only."""
from itertools import product

NUM = [1, 5, -8, 8, 13, -4, -10, -8, 11, 2, -5, 2]

def multiply(p, q):
    r = [0] * (len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return r

def series(n):
    den = [1]
    for _ in range(7): den = multiply(den, [1, -1])
    for _ in range(2): den = multiply(den, [1, 1])
    den = multiply(den, [1, 1, 1])
    assert den[0] == 1
    a = []
    for k in range(n):
        val = NUM[k] if k < len(NUM) else 0
        for j in range(1, min(k,len(den)-1)+1):
            val -= den[j] * a[k-j]
        a.append(val)
    return a

if __name__ == '__main__':
    theoretical = series(13)
    for n in range(1, 12):
        seen = set()
        for word in product(range(3), repeat=n):
            counts = [0] * 9
            for left, right in zip(word, word[1:]):
                counts[3*left+right] += 1
            seen.add(tuple(counts))
        count = len(seen)
        assert count == theoretical[n-1], (n, count, theoretical[n-1])
        print('n=%d direct_words=%d rational=%d OK' % (n, count, theoretical[n-1]))
    print('PASS independent word enumeration through n=11')
