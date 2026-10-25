"""Finite exact checks of CRT residue programming and prime-set exchange inequalities."""
from math import gcd, factorial, exp
from itertools import takewhile

def primes():
    yield 2
    k = 3
    while True:
        if all(k % j for j in range(3, int(k**.5) + 1, 2)):
            yield k
        k += 2

def crt_pair(a, m, b, n):
    assert gcd(m, n) == 1
    t = ((b-a) * pow(m, -1, n)) % n
    return (a+m*t)%(m*n), m*n

def test_residue_programming():
    for m in range(1, 121):
        t = max(m + 1, 5)
        residues = {(s + (t-1) - 2*j) % m for s in (2, 3) for j in range(t)}
        assert residues == set(range(m)), (m, residues)

def test_isolation_crt():
    for m in range(1, 14):
        for a in range(m):
            if gcd(a, m) != 1: continue
            for H in range(1, 6):
                rr, nn = a, m
                pool = (p for p in primes() if p > H and m % p)
                for h in [*range(-H,0), *range(1,H+1)]:
                    ell=next(pool)
                    rr,nn=crt_pair(rr,nn,-h,ell)
                    assert (rr+h)%ell == 0
                    assert rr % m == a
                assert gcd(rr,nn)==1

def test_exchange_numerics():
    for a in range(1, 100):
        assert factorial(a-1)/exp(a) > 1/11
    # Both seeds represent their prime sums with the smallest prime products.
    primes_under50 = list(takewhile(lambda p: p < 50, primes()))
    for s in (2,3):
        from itertools import combinations
        opts=[q for k in range(1,3) for q in combinations(primes_under50,k) if sum(q)==s]
        assert len(opts)==1 and opts[0]==(s,)

if __name__=='__main__':
    test_residue_programming()
    test_isolation_crt()
    test_exchange_numerics()
    print('VERIFY_OK: 120 moduli; CRT 13 moduli and 5 gap thresholds; factorial exchange bounds')
