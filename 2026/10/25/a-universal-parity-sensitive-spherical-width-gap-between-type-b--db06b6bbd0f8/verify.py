"""Reproduce finite orbit-support identities for two signed-permutation orbit polytopes."""
import itertools
import math
import random


def support_brute(direction, weights, even_signs):
    """Directly maximize over signed permutations; use only in small ranks."""
    n = len(weights)
    best = -float('inf')
    for perm in itertools.permutations(weights):
        for signs in itertools.product((-1, 1), repeat=n):
            if even_signs and math.prod(signs) != 1:
                continue
            v = sum(direction[i] * signs[i] * perm[i] for i in range(n))
            best = max(best, v)
    return best


def predicted(direction, weights):
    vals = sorted(abs(x) for x in direction)
    s = sum(a*b for a,b in zip(weights, vals))
    odd = sum(x < 0 for x in direction)%2
    return s, s-2*odd*weights[0]*vals[0]


def test_orbits():
    rng = random.Random(712)
    count = 0
    for n in (2,3,4,5):
        reps = 8 if n < 5 else 3
        for _ in range(reps):
            weights = sorted(rng.uniform(.1,10.0) for _ in range(n))
            direction = [rng.uniform(-1,1) for _ in range(n)]
            b, d = predicted(direction,weights)
            assert abs(b-support_brute(direction,weights,False)) < 1e-10
            assert abs(d-support_brute(direction,weights,True)) < 1e-10
            b2,d2 = predicted([-x for x in direction],weights)
            gap = b+b2-d-d2
            signed = sum(x<0 for x in direction)%2
            formula = (2 if n%2 else 4*signed)*weights[0]*min(map(abs,direction))
            assert abs(gap-formula) < 1e-10
            count += 1
    print('Exact orbit support/width tests passed:',count)


def test_asymptotics():
    rng = random.Random(2023)
    rate = math.sqrt(2/math.pi)
    for n, reps in ((50,1500),(200,1000),(800,300)):
        v = []
        for _ in range(reps):
            g = [rng.gauss(0,1) for _ in range(n)]
            v.append(n**1.5*min(map(abs,g))/math.sqrt(sum(x*x for x in g)))
        print('n =',n,'mean n^(3/2) min|U_i| =',round(sum(v)/reps,4),'limit mean =',round(1/rate,4))

if __name__=='__main__':
    test_orbits()
    test_asymptotics()
