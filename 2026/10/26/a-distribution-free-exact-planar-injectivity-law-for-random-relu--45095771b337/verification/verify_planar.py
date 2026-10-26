#!/usr/bin/env python3
"""Independent finite checks of a planar ReLU injectivity probability law."""
import itertools
import math
import random
from fractions import Fraction


def count_good_words(m):
    good = 0
    for word in itertools.product((0, 1), repeat=m):
        h = sum(word)
        acceptable = 2 <= h <= m - 2
        for bit in word:
            h += 1 - 2 * bit
            acceptable &= (2 <= h <= m - 2)
        good += acceptable
    return good


def good_angles(angles):
    m = len(angles)
    a = sorted(x % 1 for x in angles)
    gaps = [(a[(j+1) % m] + (j == m-1) - a[j]) for j in range(m)]
    return all(gaps[j] + gaps[(j+1)%m] < 0.5 for j in range(m))


def good_signs_given_lines(phi, mask):
    m = len(phi)
    return good_angles([phi[j] + 0.5 * ((mask >> j)&1) for j in range(m)])


results=[]
for m in range(4, 14):
    count = count_good_words(m)
    expected = 2**m - 2*m*(m-2)
    assert count == expected, (m,count,expected)
    exact = Fraction(count,2**m)
    results.append((m, count, str(exact)))

# Changing line positions should not change conditional sign-orientation counts.
rng = random.Random(29471)
geometry_results=[]
for m in range(4, 10):
    for profile in range(4):
        if profile == 0:
            phi = [(j + 0.35)/(2*m) for j in range(m)]
        elif profile == 1:
            phi = [(j + 1)/(m*m*20) for j in range(m)]
        elif profile == 2:
            phi = [0.5 - (m-j)/(m*m*20) for j in range(m)]
        else:
            phi = sorted(rng.uniform(0,0.5) for _ in range(m))
        count=sum(good_signs_given_lines(phi,mask) for mask in range(2**m))
        assert count == 2**m - 2*m*(m-2),(m,profile,count)
        geometry_results.append((m,profile,count))

# The normalized angular-gap formulation agrees with direct semicircle counts
# in random configurations. This is an exploratory finite diagnostic.
for m in range(4, 12):
    for _ in range(2000):
        a=sorted(rng.random() for _ in range(m))
        actual=good_angles(a)
        counts=[]
        for i in range(m):
            ref=a[i]
            counts.append(sum(0 < ((a[j]-ref) % 1) < 0.5 for j in range(m) if j!=i))
        assert actual == (min(counts)>=2)

# Monte Carlo comparison is not used as proof.
mc=[]
for m in (5,6,8,10):
    N=45000
    successful=sum(good_angles([rng.random() for _ in range(m)]) for _ in range(N))
    target=1-m*(m-2)/2**(m-1)
    se=math.sqrt(target*(1-target)/N)
    assert abs(successful/N-target) < 7*se + 0.0001
    mc.append((m,N,successful,successful/N,target))

print('EXACT WORD COUNTS m good numerator / denominator:')
for m,c,p in results:print(m,c,p)
print('Deterministic line-orientation checks:',len(geometry_results))
print('Direct semicircle-point checks:',8*2000)
print('Monte Carlo comparisons (m,N,success,observed,target):')
for x in mc:print(*x)
print('All checks passed. Finite enumeration is not an infinite proof.')
