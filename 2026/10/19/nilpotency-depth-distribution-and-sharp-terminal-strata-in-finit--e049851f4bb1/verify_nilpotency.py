"""Independent finite-field checks of Munn-algebra nilpotency-depth counts.
Run with Python 3: python3 verify_nilpotency.py. Uses no dependencies.
"""
from collections import Counter
from itertools import product
from math import prod


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for first in range(min(maximum, n), 0, -1):
        for tail in partitions(n-first, first):
            yield (first,) + tail


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    numerator = prod(q**(n-i)-1 for i in range(k))
    denominator = prod(q**(k-i)-1 for i in range(k))
    assert numerator % denominator == 0
    return numerator // denominator


def rank_matrices(rows, cols, rank, q):
    return gaussian(rows, rank, q) * prod(q**cols-q**i for i in range(rank))


def orbit_size(part, q):
    r = sum(part)
    centralizer_exponent = sum(sum(t >= j for t in part)**2 for j in range(1, max(part)+1))
    multiplicities = Counter(part)
    denominator_shift = sum(v*(v+1)//2 for v in multiplicities.values())
    centralizer = q**(centralizer_exponent-denominator_shift)
    for v in multiplicities.values():
        centralizer *= prod(q**j-1 for j in range(1, v+1))
    gl = prod(q**r-q**i for i in range(r))
    assert gl % centralizer == 0
    return gl//centralizer


def predicted(r, b, c, q):
    cumulative = [0, 1]
    for j in range(2, r+3):
        tally = 0
        for lam in partitions(r):
            if lam[0] > j:
                continue
            counts = Counter(lam)
            a, e = counts[j], counts[j-1]
            for t in range(min(e, b)+1):
                tally += (orbit_size(lam, q)
                          * q**(b*c + (r-a-e)*b + c*(r-a-t))
                          * rank_matrices(e, b, t, q))
        cumulative.append(tally)
    return cumulative


def operations(q):
    if q == 4:
        add = lambda a, b: a ^ b
        def mul(a, b):
            a0, a1 = a & 1, a >> 1
            b0, b1 = b & 1, b >> 1
            return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1) << 1)
        return add, mul
    assert q in (2, 3, 5)
    return lambda a, b: (a+b) % q, lambda a, b: (a*b) % q


def brute(r, b, c, q):
    rows, cols = r+c, r+b
    add, mul = operations(q)
    hist = Counter()
    def sand(x, y):
        z = [0]*(rows*cols)
        for i in range(rows):
            for j in range(cols):
                accum=0
                for h in range(r):
                    accum=add(accum, mul(x[i*cols+h],y[h*cols+j]))
                z[i*cols+j]=accum
        return tuple(z)
    for entries in product(range(q), repeat=rows*cols):
        z=entries
        for j in range(1,r+3):
            if not any(z):
                hist[j]+=1
                break
            z=sand(z,entries)
        else:
            if not any(z):
                hist[r+3]+=1
    return hist


def sharp_top(r,b,c,q):
    regular_orbit=orbit_size((r,),q)
    if b and c:
        return r+2, regular_orbit*q**((r-1)*(b+c)+b*c)*(q**b-1)*(q**c-1)
    if b:
        return r+1,regular_orbit*q**((r-1)*b)*(q**b-1)
    if c:
        return r+1,regular_orbit*q**((r-1)*c)*(q**c-1)
    return r,regular_orbit


def main():
    cases = [(1,1,1,2),(1,1,1,3),(1,1,1,4),(1,1,1,5),
             (1,2,1,2),(2,1,1,2),(2,1,1,3),
             (2,1,0,2),(2,0,1,2),(2,1,0,3),(2,0,1,3),
             (2,1,0,4),(2,0,1,4),(2,0,0,2),(2,0,0,3),
             (3,0,0,2),(3,1,0,2),(3,1,1,2)]
    for r,b,c,q in cases:
        actual=brute(r,b,c,q)
        expected=predicted(r,b,c,q)
        for j in range(1,r+3):
            got=sum(cnt for idx,cnt in actual.items() if idx<=j)
            assert got==expected[j], (r,b,c,q,j,got,expected[j])
        upper=q**(r*r-r+r*(b+c)+b*c)
        assert expected[-1]==upper,(r,b,c,q,upper,expected[-1])
        d, number=sharp_top(r,b,c,q)
        assert actual[d]==number, (r,b,c,q,d,actual[d],number)
        print(f'PASS r={r} b={b} c={c} q={q}: depth counts '+
              str([actual[j] for j in range(1,r+3)]))
    print('VERIFY_OK_MUNN_NILPOTENCY_DEPTHS')

if __name__=='__main__':
    main()
