"""Independent exact binary first-pivot recursion verification.

Run: python verify_recursion.py.  No external Python packages required.
"""
from functools import lru_cache
from collections import defaultdict


def positions(n):
    return [(i, j) for i in range(n) for j in range(i, n)]


def direct_fibers(n):
    pos = positions(n)
    masks = defaultdict(int)
    for z in range(1 << len(pos)):
        rows = [[0]*n for _ in range(n)]
        for k,(i,j) in enumerate(pos):
            rows[i][j] = z >> k & 1
        a = 0
        for k,(i,j) in enumerate(pos):
            bit = 0
            for r in range(i+1):
                bit ^= rows[r][i] & rows[r][j]
            a |= bit << k
        masks[a] += 1
    return masks


@lru_cache(None)
def count(n, mask):
    if n == 0:
        return 1
    pos = positions(n)
    coords = {ij: mask >> k & 1 for k,ij in enumerate(pos)}
    a = coords[(0,0)]
    b = tuple(coords[(0,j)] for j in range(1,n))
    m = n-1
    spos = positions(m)
    lower = sum(coords[(i+1,j+1)] << k for k,(i,j) in enumerate(spos))
    if a:
        correction = sum((b[i] & b[j]) << k for k,(i,j) in enumerate(spos))
        return count(m,lower ^ correction)
    if any(b):
        return 0
    answer = 0
    for x in range(1<<m):
        correction = sum(((x >> i & 1) & (x >> j & 1)) << k for k,(i,j) in enumerate(spos))
        answer += count(m, lower ^ correction)
    return answer


def main():
    for n in range(1,6):
        freq = direct_fibers(n)
        for target in range(1 << (n*(n+1)//2)):
            assert count(n,target) == freq.get(target,0),(n,target)
        assert freq.get(0,0) == freq.get(1<<(n*(n+1)//2-1),0)
        print('recursion_n=%d targets=%d zero=%d MATCH' % (n, 1 << (n*(n+1)//2), freq[0]))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
