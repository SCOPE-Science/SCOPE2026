"""Exact finite checks for the cyclic-core/origin dependence theorem.

Run: python verification.py
Only finite checks are performed; the proof and asymptotic arguments are in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, sqrt, e, pi


def count_core_and_origins(mapping):
    n = len(mapping)
    origins = n - len(set(mapping))
    cyclic = set()
    done = set()
    for start in range(n):
        if start in done:
            continue
        path = []
        seen = {}
        x = start
        while x not in seen and x not in done:
            seen[x] = len(path)
            path.append(x)
            x = mapping[x]
        if x in seen:
            cyclic.update(path[seen[x]:])
        done.update(path)
    return len(cyclic), origins


def conditional_mass(n, r):
    return [independent_mass(n, r, z) for z in range(n+1)]


def independent_mass(n, r, z):
    # Inclusion-exclusion of the r eligible cells in r-1 uniform draws.
    if r == 0:
        return Fraction(z == 0)
    if z < 1 or z > r:
        return Fraction(0)
    return Fraction(comb(r, z) * sum((-1)**j * comb(r-z,j) * (n-z-j)**(r-1)
                                    for j in range(r-z+1)), n**(r-1))


def core_mass(n, k):
    numer = k
    for j in range(k):
        numer *= n-j
    return Fraction(numer, n**(k+1))


def test_exact():
    tests = 0
    brute_total = 0
    for n in range(2, 7):
        cnt = Counter(count_core_and_origins(f) for f in product(range(n), repeat=n))
        brute_total += n**n
        for k in range(1, n+1):
            r = n-k
            pred = conditional_mass(n, r)
            assert sum(pred) == 1
            assert sum(cnt[k,z] for z in range(n+1)) == n**n * core_mass(n,k)
            for z in range(n+1):
                assert Fraction(cnt[k,z], n**n) == core_mass(n,k)*pred[z], (n,k,z)
                tests += 1
        for j in range(0,n):
            for k in range(1,n+1):
                lhs = Fraction(sum(cnt[k,z] * ( __import__('math').factorial(z)//__import__('math').factorial(z-j) if z>=j else 0) for z in range(n+1)), n**n)
                fall = __import__('math').factorial(n)//__import__('math').factorial(n-j)
                rhs = Fraction(fall*(n-j)**n,n**n) * (core_mass(n-j,k) if k<=n-j else 0)
                assert lhs==rhs, ('factorial-transfer',n,j,k,lhs,rhs)
                tests += 1
        ek= sum(Fraction(k * sum(cnt[k,z] for z in range(n+1)),n**n) for k in range(1,n+1))
        ez= sum(Fraction(z * sum(cnt[k,z] for k in range(1,n+1)),n**n) for z in range(n+1))
        ekz= sum(Fraction(k*z*cnt[k,z],n**n) for k in range(1,n+1) for z in range(n+1))
        ek_prev=sum(k*core_mass(n-1,k) for k in range(1,n))
        assert ekz-ek*ez==n*Fraction((n-1)**n,n**n)*(ek_prev-ek)
        tests += 1
    for n in range(2, 26):
        for r in range(0,n):
            dist = conditional_mass(n,r)
            assert sum(dist)==1
            h = Fraction(r*(n-1)**(r-1), n**(r-1)) if r>=1 else Fraction(0)
            assert sum(z*dist[z] for z in range(n+1)) == h
            tests += n+2
        for r in range(1,n-1):
            # Check, without using it in the theorem, that conditional means fall with K.
            qold = sum(z*conditional_mass(n,r)[z] for z in range(n+1))
            qnew = sum(z*conditional_mass(n,r+1)[z] for z in range(n+1))
            assert qnew > qold
            tests += 1
    return tests, brute_total


def check_covariance():
    outputs = []
    target = -sqrt(pi/2)/(2*e)
    for n in (20,100,500,2000,10000):
        p = 1.0
        ek = ez = ekz = 0.0
        for k in range(1,n+1):
            p *= (n-k+1)/n
            w = p*k/n
            h = (n-k)*((n-1)/n)**(n-k-1) if k<n else 0.0
            ek += k*w
            ez += h*w
            ekz += k*h*w
        cov = ekz-ek*ez
        assert cov < 0
        outputs.append((n, cov/sqrt(n)))
    assert abs(outputs[-1][1]-target) < 2e-4
    return outputs, target


if __name__ == '__main__':
    checks, brute = test_exact()
    numbers, target = check_covariance()
    print('PASS exact conditional checks:', checks)
    print('PASS mappings enumerated:', brute)
    print('PASS covariance/scaling:')
    for n,v in numbers:
        print('n=%d covariance/sqrt(n)=%.9f' % (n,v))
    print('predicted limit=%.9f' % target)
