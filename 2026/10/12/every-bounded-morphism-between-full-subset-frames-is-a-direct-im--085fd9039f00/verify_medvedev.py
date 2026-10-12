"""Finite direct verification of all p-morphisms P_n -> P_m for n,m <= 3.

Frames are nonempty subsets of [n], reverse-inclusion order.
The verifier enumerates ALL functions between their worlds and checks the
forth/back relation without invoking the classification.
"""
from itertools import product
from math import factorial, comb


def frame(n):
    return range(1, 1 << n)


def direct_pmorphism(n, m, v):
    source = list(frame(n))
    target = list(frame(m))
    for A in source:
        above_A = [B for B in source if B & A == B]
        # Equality of upward images is exactly the forth+back condition.
        # Downward inclusion is the order in P_n.
        lhs = {v[B-1] for B in above_A}
        rhs = {T for T in target if T & v[A-1] == T}
        if lhs != rhs:
            return False
    return True


def canonical_map(n, m, c):
    result = []
    for A in frame(n):
        image = 0
        for i in range(n):
            if A & (1 << i):
                image |= (1 << c[i])
        result.append(image)
    return tuple(result)


def onto(v, m):
    return set(v) == set(frame(m))


def stirling(n, m):
    return sum((-1)**j * comb(m, j) * (m-j)**n
               for j in range(m+1)) // factorial(m)


def run():
    total_maps = 0
    total_pmorphisms = 0
    for n in (1,2,3):
        for m in (1,2,3):
            worlds_m = tuple(frame(m))
            canonical = {canonical_map(n,m,c)
                         for c in product(range(m),repeat=n)}
            actual = set()
            for v in product(worlds_m, repeat=(1<<n)-1):
                total_maps += 1
                if direct_pmorphism(n,m,v):
                    actual.add(v)
                    total_pmorphisms += 1
            expected_onto = factorial(m) * stirling(n,m)
            actual_onto = sum(onto(v,m) for v in actual)
            assert actual == canonical,(n,m,len(actual),len(canonical), actual-canonical)
            assert len(actual)==m**n
            assert actual_onto==expected_onto
            print('n=',n,'m=',m,'pmorphisms=',len(actual),
                  'surjective=',actual_onto,'enumerated_maps=',len(worlds_m)**((1<<n)-1))
    print('VERIFY_OK', 'all_maps_checked=',total_maps, 'all_p_morphisms=',total_pmorphisms)


if __name__ == '__main__':
    run()
