"""Standalone finite-field checks for zero-product sandwich fibers.
Run with Python 3: python verify.py
"""
from itertools import product
from math import prod


def gaussian(n, k, q):
    if not 0 <= k <= n:
        return 0
    return prod(q ** (n - j) - 1 for j in range(k)) // prod(
        q ** (k - j) - 1 for j in range(k)
    )


def general_linear(n, q):
    return prod(q ** n - q ** j for j in range(n))


def expected_pair_count(n, r, a, b, q):
    if min(a, b) < r or a + b > n:
        return 0
    return (gaussian(n-r, a-r, q) * gaussian(n-r, b-r, q)
            * gaussian(n, a, q) * gaussian(n-a, b, q)
            * general_linear(a, q) * general_linear(b, q))


def expected_witnesses(n, r, q):
    return sum(expected_pair_count(n, r, a, b, q) * q**(n*n-a*b)
               for a in range(n+1) for b in range(n+1))


def multiply(a, b, n, q):
    return tuple(sum(a[n*i+k] * b[n*k+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def rank(a, rows, cols, q):
    arr = [list(a[i*cols:(i+1)*cols]) for i in range(rows)]
    pivot = 0
    for col in range(cols):
        k = next((i for i in range(pivot, rows) if arr[i][col] % q), None)
        if k is None: continue
        arr[pivot], arr[k] = arr[k], arr[pivot]
        v = pow(arr[pivot][col], -1, q)
        arr[pivot] = [(x*v) % q for x in arr[pivot]]
        for i in range(rows):
            if i == pivot: continue
            t = arr[i][col]
            if t:
                arr[i] = [(arr[i][j] - t*arr[pivot][j]) % q for j in range(cols)]
        pivot += 1
        if pivot == rows: break
    return pivot


def image_contains(a, x, n, q):
    joined = tuple(v for i in range(n) for j in range(2*n)
                   for v in [(a[i*n+j] if j < n else x[i*n+j-n])])
    return rank(joined, n, 2*n, q) == rank(a, n, n, q)


def kernel_contained(b, x, n, q):
    return rank(b+x, 2*n, n, q) == rank(b, n, n, q)


def exhaustive_small_fibers(q):
    n = 2
    mats = list(product(range(q), repeat=n*n))
    zero = (0,) * 4
    targets = [(0,)*4, (1,0,0,0)]
    counts = {t:0 for t in targets}
    for a in mats:
        for b in mats:
            if multiply(a,b,n,q)!=zero: continue
            for r in mats:
                x=multiply(multiply(a,r,n,q),b,n,q)
                if x in counts: counts[x]+=1
    for x in targets:
        assert counts[x] == expected_witnesses(n,rank(x,n,n,q),q), (q,x,counts[x])
    return counts


def independent_pair_census():
    n=3;q=2
    mats = list(product(range(q), repeat=n*n))
    zr = (0,)*9
    targets=[zr,(1,0,0,0,0,0,0,0,0),(1,0,0,0,1,0,0,0,0)]
    for x in targets:
        rr=rank(x,n,n,q)
        actual = {}
        for a in mats:
            ar=rank(a,n,n,q)
            if not image_contains(a,x,n,q):continue
            for b in mats:
                if multiply(a,b,n,q)!=zr:continue
                if not kernel_contained(b,x,n,q):continue
                br=rank(b,n,n,q)
                actual[ar,br]=actual.get((ar,br),0)+1
        for a in range(n+1):
            for b in range(n+1):
                expected=expected_pair_count(n,rr,a,b,q)
                assert actual.get((a,b),0)==expected, (rr,a,b,actual.get((a,b),0),expected)
    return True


def total_pairs_independent(n,q):
    return sum(gaussian(n,a,q)**2 * gaussian(n,b,q)*gaussian(n-a,b,q)
               * general_linear(a,q)*general_linear(b,q)
               for a in range(n+1) for b in range(n-a+1))


def rank_shell_count(n,r,q):
    return gaussian(n,r,q)**2 * general_linear(r,q)


def main():
    for q in (2,3):
        print('M2 F',q,'direct_fibers',exhaustive_small_fibers(q))
    assert independent_pair_census()
    print('M3 F2: exhaustive ordered (A,B) counts OK')
    for n in (2,3,4,5):
        for q in (2,3):
            summed=sum(rank_shell_count(n,r,q)*expected_witnesses(n,r,q)
                       for r in range(n+1))
            expected=total_pairs_independent(n,q)*q**(n*n)
            assert summed==expected, (n,q,summed,expected)
        print('n',n,'total-fiber identity OK')
    assert [expected_witnesses(4,r,2) for r in range(5)] == [35813933056,689848320,5160960,0,0]
    print('VERIFY_OK')

if __name__=='__main__':main()
