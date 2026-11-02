"""Independent finite tests for a local criterion on pairs of shifted gcds.

Run: python3 verify_na.py
Uses only the Python standard library.
"""
from math import gcd
from functools import lru_cache
from itertools import product, combinations


def factor(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors.append((p, e))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def local_criterion(n, a, b):
    for p, e in factor(n):
        if p == 2:
            if e >= 2 and a % 2 and b % 2 and (a-b) % 4 == 0:
                return False
        elif a % p and b % p and (a-b) % p == 0:
            return False
    return True


def upward_sets(n):
    divisors = [d for d in range(1, n+1) if n % d == 0]
    accepted = []
    for mask in range(1 << len(divisors)):
        selected = {d for j,d in enumerate(divisors) if mask & (1 << j)}
        if all(not (d in selected and d2 not in selected and d2 % d == 0)
               for d in divisors for d2 in divisors):
            accepted.append(selected)
    return accepted


def finite_negative_association(n, a, b):
    units = [u for u in range(n) if gcd(u,n) == 1]
    x = [gcd(u-a,n) for u in units]
    y = [gcd(u-b,n) for u in units]
    length = len(units)
    for left in upward_sets(n):
        left_count = sum(z in left for z in x)
        for right in upward_sets(n):
            right_count = sum(z in right for z in y)
            joint = sum(v in left and w in right for v,w in zip(x,y))
            if length*joint > left_count*right_count:
                return False
    return True


def opposite_shift_prediction(n):
    two = dict(factor(n)).get(2,0)
    out = 4*two if two else 1
    for p, e in factor(n):
        if p != 2:
            out *= 2*e+1
    return out


@lru_cache(None)
def vector_upper_sets(n, dimension):
    divisors = [d for d in range(1,n+1) if n%d == 0]
    points = list(product(divisors, repeat=dimension))
    assert len(points) <= 16, (n, dimension)
    supersets = []
    for point in points:
        supersets.append(sum(1 << j for j, higher in enumerate(points)
                         if all(y % x == 0 for x,y in zip(point,higher))))
    upsets = []
    for mask in range(1 << len(points)):
        if all(not(mask & (1 << i)) or (mask & sup) == sup
               for i,sup in enumerate(supersets)):
            upsets.append(frozenset(points[i] for i in range(len(points)) if mask & (1 << i)))
    return upsets


def full_vector_association(n, shifts):
    units = [u for u in range(n) if gcd(u,n) == 1]
    samples = [tuple(gcd(u-a,n) for a in shifts) for u in units]
    assert len(shifts) == 3
    tests = 0
    # Every pair of disjoint nonempty coordinate sets is handled.
    for imask in range(1, 1 << 3):
        for jmask in range(1, 1 << 3):
            if imask & jmask:
                continue
            ix = tuple(i for i in range(3) if imask & (1 << i))
            jx = tuple(i for i in range(3) if jmask & (1 << i))
            left = [tuple(x[i] for i in ix) for x in samples]
            right = [tuple(x[i] for i in jx) for x in samples]
            # Cache projections as masks of samples: repeated upper sets collapse.
            left_events = {tuple(v in A for v in left) for A in vector_upper_sets(n,len(ix))}
            right_events = {tuple(v in B for v in right) for B in vector_upper_sets(n,len(jx))}
            for event1 in left_events:
                count1 = sum(event1)
                for event2 in right_events:
                    assert len(samples)*sum(x and y for x,y in zip(event1,event2)) <= count1*sum(event2), (n,shifts,ix,jx,event1,event2)
                    tests += 1
    return tests


def vector_criterion(n, shifts):
    for p,e in factor(n):
        if p == 2:
            if e >= 2:
                odd_residues = [a%4 for a in shifts if a%2]
                if len(odd_residues) != len(set(odd_residues)):
                    return False
        else:
            unit_residues = [a%p for a in shifts if a%p]
            if len(unit_residues) != len(set(unit_residues)):
                return False
    return True


def test():
    count = 0
    for n in range(1, 32):
        for a in range(-5,6):
            for b in range(-5,6):
                predicted = local_criterion(n,a,b)
                found = finite_negative_association(n,a,b)
                assert predicted == found, (n,a,b,predicted,found)
                count += 1
    means = 0
    for n in range(1, 200):
        units = [u for u in range(n) if gcd(u,n) == 1]
        actual = sum(gcd(u-1,n)*gcd(u+1,n) for u in units)
        expect = opposite_shift_prediction(n) * len(units)
        assert actual == expect, (n,actual,expect)
        means += 1
    vector_cases = 0
    certified = 0
    for n in range(1,11):
        for shifts in product(range(-2,3), repeat=3):
            expected = vector_criterion(n,shifts)
            # The full NA definition can be checked only for predicted cases:
            # non-NA cases are rejected by a pairwise threshold obstruction.
            if expected:
                certified += full_vector_association(n,shifts)
            else:
                witness = any(not finite_negative_association(n,shifts[i],shifts[j])
                              for i,j in combinations(range(3),2))
                assert witness, (n,shifts)
            vector_cases += 1
    print('VERIFY_OK: %d two-shift parameter triples; %d three-shift triples; %d full-NA event inequalities; %d opposite-shift exact moments' % (count,vector_cases,certified,means))


if __name__ == '__main__':
    test()
