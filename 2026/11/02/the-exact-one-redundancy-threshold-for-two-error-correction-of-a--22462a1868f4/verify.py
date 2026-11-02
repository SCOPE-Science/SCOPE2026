"""Exact integer certificate for the two-error binary function-code threshold.

Run: python3 verify.py
Only Python standard library is required. A separate direct enumeration
checks the dynamic program on all smaller hypercubes.
"""
from functools import lru_cache
from itertools import combinations
from math import comb

RADIUS = 4

def choose(n, j):
    return comb(n, j) if 0 <= j <= n else 0

@lru_cache(None)
def full(n, j):
    """Length, sum, maximum-prefix sum, and its leftmost index.

    Entries are C(min(X),4)-1 for j-subsets X of {0,...,n-1},
    listed by decreasing lex order of bit strings. An empty set has min=n.
    """
    if j == 0:
        value = choose(n, RADIUS) - 1
        return (1, value, max(0, value), 1 if value > 0 else 0)
    count = total = best = where = 0
    for high in range(n-1, j-2, -1):
        c, s, b, a = full(high, j-1)
        if total+b > best:
            best, where = total+b, count+a
        count += c
        total += s
    assert count == comb(n, j)
    return (count, total, best, where)

@lru_cache(None)
def prefix(n, j, m):
    """The same four statistics restricted to the first m entries."""
    assert 0 <= m <= comb(n, j)
    if m == 0:
        return (0, 0, 0, 0)
    if m == comb(n, j):
        return full(n, j)
    assert j > 0
    count = total = best = where = 0
    for high in range(n-1, j-2, -1):
        if count >= m:
            break
        c = min(comb(high, j-1), m-count)
        _, s, b, a = prefix(high, j-1, c)
        if total+b > best:
            best, where = total+b, count+a
        count += c
        total += s
    assert count == m
    return (count, total, best, where)

def maximum_gap(n):
    """Maximum |N_4(I_M)|-(2^(n-1)+M), 1<=M<=2^(n-2)."""
    half_class = 1 << (n-2)
    previous = 0
    largest = -10**100
    witness = None
    for j in range(n+1):
        if previous >= half_class:
            break
        allowance = min(comb(n,j), half_class-previous)
        _, _, best, where = prefix(n,j,allowance)
        initial_ball = sum(comb(n,i) for i in range(min(n,j+3)+1))
        gap = initial_ball - (1 << (n-1)) - previous + best
        if gap > largest:
            largest = gap
            witness = (previous+where,j,previous,where)
        previous += comb(n,j)
    return largest,witness

def independent_small_cube():
    """Directly enumerate all radius-four neighborhoods for 6<=n<=11."""
    for n in range(6,12):
        bits = range(n)
        flips = [sum(1<<v for v in subset)
                 for d in range(5) for subset in combinations(bits,d)]
        words = sorted(range(1<<n), key=lambda z:(z.bit_count(),-z))
        covered = set()
        best = -10**100
        for m,x in enumerate(words[:1<<(n-2)],1):
            covered.update(x ^ flip for flip in flips)
            best = max(best,len(covered)-(1<<(n-1))-m)
        assert maximum_gap(n)[0] == best, (n,best,maximum_gap(n))

def certify():
    independent_small_cube()
    assert maximum_gap(36) == (329481574,(15771159390,16,13916802008,1854357382))
    assert maximum_gap(37) == (-452256184,(29687961398,16,22265701456,7422259942))
    # The source theorem covers all k >= 66. These are all intervening k.
    table = [(k,maximum_gap(k+1)[0]) for k in range(36,66)]
    assert len(table)==30 and all(value<0 for _,value in table)
    assert table[0] == (36,-452256184)
    assert table[-1] == (65,-9158393403190660545)
    # Independent direct evaluation of the announced k=35 witness.
    n,j,m = 36,16,1854357382
    vprev=sum(comb(n,i) for i in range(j))
    shadow=prefix(n,j,m)[1]+m
    neighborhood=sum(comb(n,i) for i in range(j+4))+shadow
    assert vprev == 13916802008 and shadow == 2965576714
    assert neighborhood == 50460379332
    assert neighborhood - ((1<<(n-1))+(vprev+m)) == 329481574
    print('INDEPENDENT_SMALL_CUBES_OK n=6..11')
    print('BOUNDARY_FAIL k=35 M=15771159390 gap=329481574')
    print('BOUNDARY_PASS k=36 maximal_gap=-452256184')
    print('FINITE_RANGE_OK k=36..65 all gaps strictly negative')
    print('CERTIFICATE_OK')

if __name__=='__main__':
    certify()
