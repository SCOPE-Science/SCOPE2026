#!/usr/bin/env python3
import itertools
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True

def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)

def sigma_squarefree_2pq(p, q):
    return 3*(p+1)*(q+1)

LABELS = [
    ("1", 0, 0, 1),
    ("2", 0, 0, 2),
    ("p", 1, 0, 0),
    ("2p",2, 0, 0),
    ("q", 0, 1, 0),
    ("2q",0, 2, 0),
]

EXPECTED = {
    (5,13): (1,2,5),
    (7,11): (2,7,11),
    (5,17): (1,5,10),
    (7,13): (1,13,14),
    (5,29): (1,10,29),
    (7,31): (7,31,62),
}

def classify():
    found = {}
    rows = []
    for triple in itertools.combinations(LABELS, 3):
        names = tuple(x[0] for x in triple)
        a = sum(x[1] for x in triple)
        b = sum(x[2] for x in triple)
        c = sum(x[3] for x in triple)
        C = (a+3)*(b+3) + c + 3
        row_solutions = []
        for u in divisors(C):
            p = b + 3 + u
            q = a + 3 + C//u
            if not (p < q and p % 2 and q % 2 and is_prime(p) and is_prime(q)):
                continue
            delta = p*q - 3*p - 3*q - 3
            values = {"1":1, "2":2, "p":p, "2p":2*p, "q":q, "2q":2*q}
            chosen = tuple(values[name] for name in names)
            if sum(chosen) != delta:
                raise AssertionError(("factorization mismatch", names, p, q))
            row_solutions.append((p,q))
            found[(p,q)] = tuple(sorted(chosen))
        rows.append((names, a, b, c, C, tuple(row_solutions)))
    assert len(rows) == 20
    return rows, found

def direct_check(p, q, ds):
    n = 2*p*q
    sig = sigma_squarefree_2pq(p,q)
    assert len(set(ds)) == 3
    assert all(1 <= d < n and n % d == 0 for d in ds)
    assert sig == 2*n - sum(ds)
    return n

def main():
    rows, found = classify()
    assert found == {k: tuple(sorted(v)) for k,v in EXPECTED.items()}
    ns = sorted(direct_check(p,q,ds) for (p,q),ds in EXPECTED.items())
    assert ns == [130,154,170,182,290,434]

    # Independent bounded regression over many prime pairs.
    primes = [n for n in range(3,1000,2) if is_prime(n)]
    brute = set()
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            n = 2*p*q
            delta = 2*n - sigma_squarefree_2pq(p,q)
            if delta <= 0:
                continue
            proper = [1,2,p,2*p,q,2*q,p*q]
            if any(sum(t) == delta for t in itertools.combinations(proper,3)):
                brute.add((p,q))
    assert brute == set(EXPECTED)

    print("VERIFY_OK")
    print("rows=20")
    print("prime_pairs=" + repr(sorted(EXPECTED)))
    print("integers=" + repr(ns))

if __name__ == "__main__":
    main()
