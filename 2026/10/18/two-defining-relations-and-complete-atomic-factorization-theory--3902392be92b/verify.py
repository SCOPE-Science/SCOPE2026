#!/usr/bin/env python3
"""Exact finite regression checks for the 13-smooth factorial monoid."""
from collections import defaultdict
from math import factorial

PRIMES = (2, 3, 5, 7, 11, 13)
INDICES = (2, 3, 5, 7, 11, 13, 14, 15)
GENERATORS = tuple(factorial(n) for n in INDICES)
BOUND = 10**20


def prime_vector(n):
    v = []
    for p in PRIMES:
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        v.append(a)
    assert n == 1
    return v


def coords(n):
    e2, e3, e5, e7, e11, e13 = prime_vector(n)
    return (e2-e3-2*e5-e13, e3-e5-e7-e11-e13,
            e5-e7-e11, e7-e11, e11-e13, e13)


def factorizations_count(n):
    c1,c2,c3,c4,c5,c6 = coords(n)
    if c5 < 0:
        return 0
    lower_t = max(0,-c2)
    upper_t = min(c4,c6)
    lower_r = max(0,-c3)
    total = 0
    for t in range(lower_t,upper_t+1):
        upper_r = min(t,(c1+2*t)//3)
        total += max(0,upper_r-lower_r+1)
    return total


def canonical(fac):
    x = list(fac)
    while x[6] > 0 and x[2] > 0:
        x[6] -= 1; x[2] -= 1; x[7] += 1; x[0] += 3
    while x[3] > 0 and x[5] > 0:
        x[3] -= 1; x[5] -= 1; x[7] += 1; x[0] += 2; x[1] += 1
    return tuple(x)


vectors = defaultdict(list)
checks = [0]

def exhaust(j, val, fac):
    if j == len(GENERATORS):
        f = tuple(fac)
        vectors[val].append(f)
        checks[0] += 1
        return
    exponent = 0
    while val * (GENERATORS[j] ** exponent) <= BOUND:
        fac.append(exponent)
        exhaust(j+1, val * (GENERATORS[j] ** exponent), fac)
        fac.pop()
        exponent += 1

exhaust(0,1,[])
assert GENERATORS[6]*GENERATORS[2] == GENERATORS[7]*GENERATORS[0]**3
assert GENERATORS[3]*GENERATORS[5] == GENERATORS[7]*GENERATORS[0]**2*GENERATORS[1]
assert len(GENERATORS) == len(set(GENERATORS))
for n, lst in vectors.items():
    assert len(lst) == factorizations_count(n), (n,len(lst),factorizations_count(n))
    assert len({canonical(f) for f in lst}) == 1, n
    ls = sorted(set(map(sum,lst)))
    assert ls == list(range(ls[0],ls[-1]+1,2)), (n,ls)
    c1,c2,c3,c4,c5,c6 = coords(n)
    r0=max(0,-c3)
    m=min(c4,c6)
    tmin=max(0,-c2,r0, -((c1-3*r0)//2))
    smin=max(0, -((c1-tmin)//3))
    assert ls == list(range(sum((c1,c2,c3,c4,c5,c6))+2*smin,
                            sum((c1,c2,c3,c4,c5,c6))+2*(m-r0)+1,2)), (n,ls)
    # Every one-step rewrite is an actual equality, and repeated rewriting terminates.
    for f in lst:
        v=list(f)
        if v[6] and v[2]:
            v[6]-=1;v[2]-=1;v[7]+=1;v[0]+=3
            assert tuple(v) in lst
        v=list(f)
        if v[3] and v[5]:
            v[3]-=1;v[5]-=1;v[7]+=1;v[0]+=2;v[1]+=1
            assert tuple(v) in lst
    for f in lst:
        assert canonical(f) in lst, (n,f,canonical(f))
# Check the elementary collision witnesses have exactly their two claimed atomic factorizations.
for n in (GENERATORS[6]*GENERATORS[2],GENERATORS[3]*GENERATORS[5]):
    assert len(vectors[n]) == 2, (n,vectors[n])
    assert sorted(map(sum, vectors[n])) == [2,4]
# Every generator is an atom: its only atomic-factorization vector is its basis vector.
for i,g in enumerate(GENERATORS):
    assert vectors[g] == [tuple(int(k==i) for k in range(8))]
print('VERIFY_OK', 'bound='+str(BOUND),'distinct_numbers='+str(len(vectors)),
      'factorizations='+str(checks[0]),'relation_checks=2',
      'full_count_and_normal_form_checks='+str(len(vectors)),
      'atomic_generators=8', 'length_set_checks='+str(len(vectors)))
