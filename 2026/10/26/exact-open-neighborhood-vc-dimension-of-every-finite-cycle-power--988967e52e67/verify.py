"""Independent finite checks for the exact open-neighborhood VC dimension of powers of cycles.
Run: python verify.py. Standard library only.
The infinite theorem is proved separately; this program only checks finite instances and explicit witness schemes.
"""
from itertools import combinations


def expected(n, r):
    if n <= 2*r + 2:
        return 1
    if n == 2*r + 3:
        return 2
    if r == 2 and n == 8:
        return 3
    if r >= 3 and n >= 2*r + 4:
        return 3
    return 2


def neighbor_masks(n, r):
    return [sum(1 << x for x in range(n)
                if 0 < min((x-v) % n, (v-x) % n) <= r)
            for v in range(n)]


def traces(ns, A):
    seen = 0
    for mask in ns:
        t = sum(((mask >> x) & 1) << i for i, x in enumerate(A))
        seen |= 1 << t
    return seen


def shattered(ns, A):
    return traces(ns, A) == (1 << (1 << len(A))) - 1


def dimension_by_search(n, r):
    ns = neighbor_masks(n, r)
    for k in range(min(4, n.bit_length()-1), 0, -1):
        for S in combinations(range(n), k):
            if shattered(ns, S):
                return k
    return 0


def check_exhaustive():
    total = 0
    for n in range(3, 23):
        for r in range(1, n//2 + 1):
            got = dimension_by_search(n, r)
            goal = expected(n, r)
            assert got == goal, (n, r, got, goal)
            total += 1
    print('EXHAUSTIVE_SMALL', total, 'parameter_pairs', 'PASS')


def check_constructions():
    tested = 0
    for r in range(3, 41):
        for n in range(2*r+4, 5*r+11):
            if n <= 3*r+2:
                S = (0, 1, r+2)
                centers = ('A', (r+2, r+3, 0, r+1, 1, n-r, n-1, 2))
            else:
                S = (0, 2, r+1)
                centers = ('B', (2*r+2, r+3, 0, r+2, n-r, 2, n-1, 1))
            ns = neighbor_masks(n, r)
            for pattern, v in enumerate(centers[1]):
                got = sum(((ns[v] >> x) & 1) << i for i, x in enumerate(S))
                # list is ordered by strings '000','001','010',... in printed three-bit order
                want = int(format(pattern, '03b')[::-1], 2)
                assert got == want, (r, n, S, centers[0], pattern, v, got, want)
            tested += 1
    ns = neighbor_masks(8, 2)
    assert shattered(ns, (0, 1, 4))
    for n in range(9, 151):
        ns = neighbor_masks(n, 2)
        for S in ((n-2,n-1,1),(n-2,n-1,2),(n-2,1,2),(n-1,1,2)):
            assert not shattered(ns, S)
    print('WITNESS_TABLE', tested, 'parameter_pairs', 'PASS')
    print('RADIUS_TWO_OBSTRUCTIONS', 142, 'orders', 'PASS')


if __name__ == '__main__':
    check_exhaustive()
    check_constructions()
    print('VERIFY_OK open_neighborhood=PASS universal_pattern=PASS small_exhaustion=PASS')
