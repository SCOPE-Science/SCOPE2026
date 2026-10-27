#!/usr/bin/env python3
"""Standalone finite checks for the adjacent-divisor-gap classification."""

def prime(p):
    if p < 2:
        return False
    return all(p % d for d in range(2, int(p**0.5) + 1))


def divisors(a, p, b):
    return sorted(2**i * p**j for j in range(b + 1) for i in range(a + 1))


def gap_closed(a, p, b):
    n = 2**a * p**b
    ds = divisors(a, p, b)
    return all(n % (y-x) == 0 for x, y in zip(ds, ds[1:]))


def prediction(a, p, b):
    return p == 3 and (a <= 4 or b <= 2) or p >= 5 and p == 2**a + 1


def run():
    cases = 0
    for p in range(3, 501, 2):
        if not prime(p):
            continue
        for a in range(1, 16):
            for b in range(1, 9):
                assert gap_closed(a,p,b) == prediction(a,p,b), (a,p,b)
                cases += 1
    for a in range(1, 5):
        for b in (10, 20, 50, 100):
            assert gap_closed(a,3,b)
            cases += 1
    for a in (16,24,32,64,100):
        for b in (1,2,3):
            assert gap_closed(a,3,b) == (b <= 2)
            cases += 1
    for a,p in [(2,5),(4,17),(8,257),(16,65537)]:
        assert prime(p)
        for b in (1,2,7):
            assert gap_closed(a,p,b)
            cases += 1
    d = divisors(5,3,3)
    i=d.index(27)
    assert d[i+1] == 32 and (2**5*3**3) % 5 != 0
    print(f'VERIFY_OK: {cases} independent two-prime parameter cases; boundary 27 to 32.')

if __name__ == '__main__':
    run()
