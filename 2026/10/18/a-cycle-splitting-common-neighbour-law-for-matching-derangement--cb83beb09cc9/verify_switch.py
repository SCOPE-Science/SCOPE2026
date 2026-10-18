"""Independent exact checks of forbidden-edge matching counts and switching identity."""
from functools import lru_cache
from itertools import combinations
from math import comb
from collections import defaultdict


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return tuple(c)


@lru_cache(None)
def path_poly(length):
    if length <= 1:
        return (1,)
    x, y = path_poly(length-1), path_poly(length-2)
    out = [0] * (length//2+1)
    for i, a in enumerate(x):
        out[i] += a
    for i, a in enumerate(y):
        out[i+1] += a
    return tuple(out)


def cycle_poly(length):
    assert length >= 4 and length % 2 == 0
    x, y = path_poly(length-1), path_poly(length-2)
    out = [0] * (length//2+1)
    for i, a in enumerate(x):
        out[i] += a
    for i, a in enumerate(y):
        out[i+1] += 2*a
    return tuple(out)


def forbidden_poly(parts):
    c = (1,)
    for a in parts:
        c = poly_mul(c, (1, 1) if a == 1 else cycle_poly(2*a))
    return c


@lru_cache(None)
def odd_double_factorial(n):
    return 1 if n <= 1 else n * odd_double_factorial(n-2)


def linear_count(parts):
    n = sum(parts)
    c = forbidden_poly(parts)
    return sum((-1)**j * a * odd_double_factorial(2*(n-j)-1)
               for j, a in enumerate(c))


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    for a in range(1, min(n, cap if cap is not None else n)+1):
        for rest in partitions(n-a, a):
            yield (a,)+rest


def main():
    poly_cases = 0
    for m in range(2, 75):
        L = poly_mul(cycle_poly(2*m), cycle_poly(2*m))
        R = cycle_poly(4*m)
        assert len(L) == len(R) == 2*m+1
        assert all(x-y == (2 if j == 2*m else 0)
                   for j, (x,y) in enumerate(zip(L,R)))
        poly_cases += 1
    print('cycle-polynomial identities:', poly_cases, 'PASS')
    comparison_cases=0
    for m in range(2, 17):
        for r in range(0, 9):
            for rho in partitions(r):
                delta=linear_count((m,m)+rho)-linear_count((2*m,)+rho)
                assert delta == 2*linear_count(rho)
                assert (delta == 0) == (rho == (1,))
                comparison_cases += 1
    print('exact all-partition switching comparisons:', comparison_cases, 'PASS')
    full_census={}
    for n in range(2, 26):
        groups=defaultdict(list)
        for lam in partitions(n):
            groups[linear_count(lam)].append(lam)
        collisions=[tuple(v) for v in groups.values() if len(v)>1]
        full_census[n]=(sum(len(v) for v in groups.values()),len(groups),len(collisions))
        # This is an observed exact finite check, not an all-n classification.
        if n>=4 and n%2==0: assert not collisions
        if n>=5 and n%2==1:
            expected={tuple(sorted(((n-1)//2,(n-1)//2,1),reverse=True)), tuple(sorted((n-1,1),reverse=True))}
            assert len(collisions)==1 and set(collisions[0])==expected
    print('finite common-neighbour census n=2..25:', full_census, 'PASS')


if __name__ == '__main__':
    main()
