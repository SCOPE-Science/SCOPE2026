"""Exact finite-case checks for local automorphisms of dihedral groups.

This is an independent checker of the explicit pairwise-interpolation definition.
No third-party packages are required.  Run: python check.py
"""
from itertools import permutations
from math import factorial, gcd, prod


def units(n):
    return [a for a in range(n) if gcd(a, n) == 1]


def gcd_isometries(n):
    for pi in permutations(range(n)):
        if all(gcd(i-j, n) == gcd(pi[i]-pi[j], n)
               for i in range(n) for j in range(i)):
            yield pi


def count_formula(n):
    a = n
    result = len(units(n))
    p = 2
    while p*p <= a:
        if a % p == 0:
            e = 0
            while a % p == 0:
                a //= p
                e += 1
            result *= factorial(p)**((p**e-1)//(p-1))
        p += 1
    if a > 1:
        result *= factorial(a)
    return result


def autos(n):
    # Encode r^i s^j by (i,j), using integer i+n*j.
    return [tuple((a*i+b*j) % n+n*j
                  for j in (0,1) for i in range(n))
            for a in units(n) for b in range(n)]


def local_maps(n):
    for a in units(n):
        rotation = [(a*i) % n for i in range(n)]
        for pi in gcd_isometries(n):
            yield tuple(rotation + [n+pi[i] for i in range(n)])


def group_product(n, x, y):
    i, j = x%n, x//n
    k, ell = y%n, y//n
    return (i+(-1)**j*k) % n + n*((j+ell)%2)


def all_group_auts_by_brute(n):
    size = 2*n
    multiplication = [[group_product(n,x,y) for y in range(size)] for x in range(size)]
    return [f for f in permutations(range(size)) if f[0] == 0 and
            all(f[multiplication[x][y]] == multiplication[f[x]][f[y]]
                for x in range(size) for y in range(size))]


def main():
    for n in range(3, 9):
        arr = autos(n)
        pair_images = {(i,j): {(f[i],f[j]) for f in arr}
                       for i in range(2*n) for j in range(i+1,2*n)}
        maps = list(local_maps(n))
        for f in maps:
            assert all((f[i],f[j]) in candidates for (i,j),candidates in pair_images.items())
        assert len(set(maps)) == len(maps)
        assert len(maps) == count_formula(n)
        assert len(arr) == n*len(units(n))
        print('n=',n, 'group_order=',2*n,'automorphisms=',len(arr),
              'local_automorphisms=',len(maps),'verified_pairs=',len(pair_images))
    for n in (1, 2, 3):
        arr = all_group_auts_by_brute(n)
        pair_images = {(i,j): {(f[i],f[j]) for f in arr}
                       for i in range(2*n) for j in range(i+1,2*n)}
        possible = []
        for f in permutations(range(2*n)):
            if f[0] != 0:
                continue
            if all((f[i],f[j]) in v for (i,j),v in pair_images.items()):
                possible.append(f)
        assert (len(arr),len(possible)) == {1:(1,1),2:(6,6),3:(6,12)}[n]
        print('direct_bijective_maps_n=',n, 'automorphisms=',len(arr), 'local=',len(possible))
    print('VERIFY_OK')


if __name__=='__main__':
    main()
