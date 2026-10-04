import cmath
import itertools
import math


def stft_support(p, f, g, tol=1e-8):
    w = cmath.exp(-2j * math.pi / p)
    count = 0
    for x in range(p):
        for xi in range(p):
            z = 0j
            for y, fy in f.items():
                gy = g.get((y-x) % p, 0)
                z += fy * complex(gy).conjugate() * (w ** ((xi*y) % p))
            if abs(z) > tol:
                count += 1
    return count


def udiff(p, S):
    a,b = sorted(S)
    d = (b-a) % p
    return frozenset((d, (-d) % p))


def orient_pair(p, A, B):
    a0,a1 = sorted(A)
    d = (a1-a0) % p
    b0,b1 = sorted(B)
    if (b1-b0) % p == d:
        return a0,a1,b0,b1
    # reverse B orientation
    return a0,a1,b1,b0

primes = [5,7,11,13]
checked = 0
for p in primes:
    pairs = list(itertools.combinations(range(p), 2))
    for A in pairs:
        for B in pairs:
            aligned = udiff(p,A) == udiff(p,B)
            # generic equal coefficients
            f = {A[0]:1, A[1]:1}
            g = {B[0]:1, B[1]:1}
            got = stft_support(p,f,g)
            want = 3*p if aligned else 4*p
            assert got == want, (p,A,B,'generic',got,want)
            checked += 1
            if aligned:
                a0,a1,b0,b1 = orient_pair(p,A,B)
                f2 = {a0:1, a1:1}
                g2 = {b0:-1, b1:1}
                got2 = stft_support(p,f2,g2)
                assert got2 == 3*p-1, (p,A,B,'cancel',got2,3*p-1)
                checked += 1

# Explicit representatives of all three values for every tested prime.
for p in primes:
    assert stft_support(p,{0:1,1:1},{0:-1,1:1}) == 3*p-1
    assert stft_support(p,{0:1,1:1},{0:1,1:1}) == 3*p
    assert stft_support(p,{0:1,1:1},{0:1,2:1}) == 4*p

print('VERIFY_OK', checked)
