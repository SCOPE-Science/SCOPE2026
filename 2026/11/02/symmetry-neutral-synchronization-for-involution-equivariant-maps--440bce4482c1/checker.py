"""Independent finite checks for constant-power transformation counts.

Run: python checker.py
Only the Python standard library is required.
"""
from itertools import product
from math import comb


def eventual_constant(F):
    """Test whether some positive iterate is a constant map on finite carrier."""
    m = len(F)
    current = list(range(m))
    for _ in range(m):
        current = [F[j] for j in current]
        if all(x == current[0] for x in current):
            return True, current[0]
    return False, None


def magma_count(n):
    pairs = list(product(range(n), repeat=2))
    position = {pair: index for index, pair in enumerate(pairs)}
    good = 0
    by_target = [0] * n
    for table in product(range(n), repeat=n*n):
        F = [position[(table[position[(x,y)]], table[position[(y,x)]])]
             for x,y in pairs]
        yes, root = eventual_constant(F)
        if yes:
            assert pairs[root][0] == pairs[root][1]
            good += 1
            by_target[pairs[root][0]] += 1
    return good, by_target


def involution_count(f, m):
    """Directly enumerate the commuting maps, without using forest counting."""
    N = f + 2*m
    swap = list(range(N))
    for k in range(m):
        a, b = f+2*k, f+2*k+1
        swap[a],swap[b]=b,a
    total = 0
    good = 0
    by_root = [0]*f
    for diag_images in product(range(f),repeat=f):
        for orbit_images in product(range(N),repeat=m):
            F = list(diag_images) + [0]*(2*m)
            for k, z in enumerate(orbit_images):
                F[f+2*k]=z
                F[f+2*k+1]=swap[z]
            assert all(F[swap[x]]==swap[F[x]] for x in range(N))
            yes, root=eventual_constant(F)
            total += 1
            if yes:
                good += 1
                assert root < f
                by_root[root] += 1
    return total, good, by_root


def weighted_forest_count(f, m):
    """Direct enumeration of directed forests rooted at one absorbing vertex."""
    total = 0
    sink = m
    for parents in product(range(m+1), repeat=m):
        if any(parents[i] == i for i in range(m)):
            continue
        good = True
        for start in range(m):
            at = start
            seen = set()
            while at != sink:
                if at in seen:
                    good = False
                    break
                seen.add(at)
                at = parents[at]
            if not good:
                break
        if good:
            weight = 1
            for dest in parents:
                weight *= f if dest == sink else 2
            total += weight
    return total


def main():
    for n in (1,2,3):
        found,by_root=magma_count(n)
        expected=n**(n*n-2) if n>1 else 1
        assert found==expected, (n,found,expected)
        assert by_root==[found//n]*n
        print(f'magma(n={n}): verified {found} / {n**(n*n)}; per target {by_root}')
    for f in (1,2,3):
        for m in (0,1,2):
            total,good,by_root=involution_count(f,m)
            N=f+2*m
            assert total==f**f * N**m
            assert good*N==total
            assert by_root==[good//f]*f
            print(f'involution(f={f},m={m}): verified {good} / {total}; per target {by_root}')
    for f in range(1,5):
        for m in range(1,6):
            count = weighted_forest_count(f,m)
            assert count == f*(f+2*m)**(m-1), (f,m,count)
    for n in range(2,15):
        m=comb(n,2)
        # Weighted arborescence determinant factorization.
        assert n*(n+2*m)**(m-1)==n*(n*n)**(m-1)
        assert n*n == n+2*m
    print('VERIFY_OK')

if __name__=='__main__':
    main()
