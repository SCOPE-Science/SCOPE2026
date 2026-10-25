"""Independent finite verification of the two-agent S5 collapse census.

Usage: python checker.py
Only Python standard library is required.
"""
from itertools import product
from math import comb


def partitions(n):
    """Set partitions as tuples of nonempty frozenset blocks."""
    if n == 0:
        yield ()
        return
    for small in partitions(n - 1):
        a = n - 1
        yield small + (frozenset((a,)),)
        for j, block in enumerate(small):
            yield small[:j] + (block | frozenset((a,)),) + small[j + 1:]


def laminar(p, q):
    return all(not (a & b) or a <= b or b <= a for a, b in product(p, q))


def holds_K(p, q, n):
    """All valuations of two variables at all worlds, without assumptions."""
    U = range(n)
    def op(S, w):
        return any(all(z in S for z in block) for block in p + q if w in block)
    subsets = [frozenset(k for k in U if mask & (1 << k)) for mask in range(1 << n)]
    for P in subsets:
        for Q in subsets:
            imply = frozenset(U).difference(P.difference(Q))
            for w in U:
                if op(imply,w) and op(P,w) and not op(Q,w):
                    return False
    return True


def formula(n):
    Bell = [len(list(partitions(k))) for k in range(n + 1)]
    L = [1]
    for m in range(1,n + 1):
        L.append(sum(comb(m-1,k-1)*(2*Bell[k]-1)*L[m-k] for k in range(1,m+1)))
    return Bell,L


def run():
    Bell,L = formula(6)
    expected = [1,1,4,19,111,774,6229]
    assert L == expected, (L,expected)
    for n in range(1,7):
        ps = list(partitions(n))
        count = sum(laminar(p,q) for p in ps for q in ps)
        assert count == L[n], (n,count,L[n])
        if n<=3:
            for p,q in product(ps,repeat=2):
                assert holds_K(p,q,n) == laminar(p,q)
        print(f'n={n}: Bell={Bell[n]}, exact compatible={count}, recurrence={L[n]}')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    run()
