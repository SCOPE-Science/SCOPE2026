"""Standalone finite checks for the interval-collapse cyclic automata theorem.

All tests are finite diagnostics. The infinite statement requires the
inverse-image interval argument given in RESULT.md.
"""
from collections import deque


def a_image(mask, n):
    full = (1 << n) - 1
    return ((mask << 1) & full) | (mask >> (n - 1))


def b_image(mask, n, k):
    ell = n - k
    low = (1 << ell) - 1
    return (mask & low) | int(bool(mask & ~low))


def minimum_reset(n, k):
    full = (1 << n) - 1
    queue = deque([(full, 0)])
    seen = {full}
    while queue:
        mask, dist = queue.popleft()
        if mask.bit_count() == 1:
            return dist
        for nxt in (a_image(mask, n), b_image(mask, n, k)):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, dist + 1))
    raise AssertionError('non-synchronizing')


def proposed(n, k):
    ell = n - k
    t = (n - 2) // k
    mask = (1 << n) - 1
    mask = b_image(mask, n, k)
    for _ in range(t):
        for _ in range(ell):
            mask = a_image(mask, n)
        mask = b_image(mask, n, k)
    assert mask.bit_count() == 1, (n, k, mask)
    return 1 + t * (ell + 1)


def inverse_b_of_hole(hole, n, k):
    ell = n-k
    full = (1 << n) - 1
    h = full ^ ((1 << ell) - 1)
    if hole & 1:
        return hole | h
    return hole & ~h


def reverse_a_hole(mask, r, n):
    if r == 0:
        return mask
    return ((mask >> r) | (mask << (n-r))) & ((1 << n)-1)


def symbolic_finite_sweep():
    cases=0
    for n in range(4, 71):
        for k in range(2, n-1):
            ell=n-k
            h=((1 << n)-1) ^ ((1 << ell)-1)
            for u in range(1, ell):
                prior=sum(1 << j for j in range(u,ell))
                for r in range(n):
                    moved=reverse_a_hole(prior,r,n)
                    after=inverse_b_of_hole(moved,n,k)
                    gain=after.bit_count()<moved.bit_count()
                    if gain:
                        assert r>=ell, (n,k,u,r,'early gain')
                        assert after.bit_count()>=moved.bit_count()-k
                        assert all(not(after & (1 << j)) for j in range(ell,n))
                        if after:
                            assert (after & 1)==0
                            start=next(j for j in range(1,ell) if after & (1 << j))
                            assert after==sum(1 << j for j in range(start,ell))
                    cases+=1
    return cases


def run():
    pairs=0
    for n in range(4, 16):
        for k in range(2, n-1):
            got=minimum_reset(n,k)
            bound=proposed(n,k)
            assert got==bound,(n,k,got,bound)
            pairs+=1
    long_witnesses=0
    for n in (18, 25, 32, 49, 100, 317):
        for k in range(2,n-1):
            proposed(n,k)
            long_witnesses+=1
    cases=symbolic_finite_sweep()
    print(f'VERIFY_OK exact_subset_BFS_pairs={pairs} interval_cases={cases} long_witnesses={long_witnesses}')


if __name__=='__main__':
    run()
