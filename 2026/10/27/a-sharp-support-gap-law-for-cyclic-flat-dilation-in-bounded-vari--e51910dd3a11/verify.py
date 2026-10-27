#!/usr/bin/env python3
"""Independent finite-dimensional regression checks for cyclic flat dilations.

No external libraries are required. Exhaustive sweeps are supplementary evidence:
all-dimensional claims are proved analytically in RESULT.md.
"""
from itertools import permutations
from random import Random


def variation(x):
    return sum(abs(x[(i + 1) % len(x)] - x[i]) for i in range(len(x)))


def dilate(x, offsets):
    n = len(x)
    return [max(x[(i + j) % n] for j in offsets) for i in range(n)]


def selector(x, offsets):
    n = len(x)
    return [max(offsets, key=lambda j: (x[(i + j) % n], j)) for i in range(n)]


def selected(x, offsets, h):
    n = len(x)
    return [h[(i + j) % n] for i, j in enumerate(selector(x, offsets))]


def arcs(n):
    for start in range(n):
        for size in range(1, n):
            yield [int((i - start) % n < size) for i in range(n)]


def check_exhaustive():
    cases = 0
    for n in range(3, 8):
        expected = {3: 1, 4: 2, 5: 2}.get(n, 3)
        arcvecs = list(arcs(n))
        for x in permutations(range(n)):
            for h in arcvecs:
                v = variation(h)
                assert variation(selected(x, (0, 2), h)) <= expected * v
                cases += 1
            for ell in range(1, n+1):
                offs = range(ell)
                for h in arcvecs:
                    v = variation(h)
                    assert variation(selected(x, offs, h)) <= (ell < n) * v
                    cases += 1
    return cases


def check_witnesses():
    cases = 0
    eps = .125
    for n in range(3, 101):
        if n == 3:
            x, h, expected = [0, 1, 2], [0, 1, 0], 1
        elif n == 4:
            x, h, expected = [0, 1, 2, 3], [0, 0, 0, 1], 2
        elif n == 5:
            x, h, expected = [0, 1, 2, 3, 4], [0, 0, 0, 0, 1], 2
        else:
            x = [0, 3, 1, 2, 4, 5] + [-10-i for i in range(6,n)]
            h = [int(i in (2,3,4)) for i in range(n)]
            expected = 3
        a = dilate(x,(0,2))
        b = dilate([x[i]+eps*h[i] for i in range(n)], (0,2))
        assert abs(variation([b[i]-a[i] for i in range(n)])-eps*expected*variation(h))<1e-9
        cases += 1
        # One-input factor, n>=4
        if n>=4:
            e = [int(i==0) for i in range(n)]
            assert variation(dilate(e,(0,2))) == 2*variation(e)
            cases += 1
        for ell in range(1,n) if n <= 20 else []:
            e = [int(i==0) for i in range(n)]
            a=dilate(x,range(ell))
            b=dilate([x[i]+eps*h[i] for i in range(n)],range(ell))
            assert variation([b[i]-a[i] for i in range(n)]) <= eps*variation(h)+1e-9
            assert variation(dilate(e,range(ell))) == variation(e)
            cases+=1
    return cases


def check_random():
    rng=Random(260245)
    cases=0
    for n in range(3,22):
        for _ in range(25):
            x=[rng.randint(-15,15) for _ in range(n)]
            y=[rng.randint(-15,15) for _ in range(n)]
            h=[x[i]-y[i] for i in range(n)]
            for offs, limit in [((0,2),{3:1,4:2,5:2}.get(n,3)),
                                (tuple(range(1+rng.randrange(n))),1)]:
                d=[a-b for a,b in zip(dilate(x,offs),dilate(y,offs))]
                assert variation(d)<=limit*variation(h)
                cases+=1
            assert variation(dilate(x,(0,2)))<= (1 if n==3 else 2)*variation(x)
            cases+=1
    return cases


if __name__=='__main__':
    a=check_exhaustive()
    b=check_witnesses()
    c=check_random()
    print('PASS:',a,'exhaustive selector/arc comparisons;',b,'constructive and interval checks;',c,'random checks.')
