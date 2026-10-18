"""Finite checks for an exact planar symmetric-sample halfspace-depth identity."""
from math import comb

def claimed_count(n, r):
    if r < 1:
        return 1 << n
    if r > n // 2:
        return 0
    H = n - 2*r + 2
    return (1 << n) - H*sum(comb(n,j) for j in range(n+1) if (j-r+1) % H == 0)

def exact_count(n,r):
    total = 0
    for bits in range(1 << n):
        w = 0
        partial = [0]
        for j in range(n):
            w += 1 if (bits >> j) & 1 else -1
            partial.append(w)
        depth = (n - max(abs(w - 2*p) for p in partial)) // 2
        total += (depth >= r)
    return total

if __name__ == '__main__':
    checks=0
    for n in range(2,15):
        for r in range(1,n//2+2):
            assert claimed_count(n,r) == exact_count(n,r), (n,r)
            checks+=1
        assert claimed_count(n,1) == (1<<n)-2*n
        checks+=1
    for n in range(5,15):
        assert claimed_count(n,2) == (1<<n)-2*n*(n-2)
        checks+=1
    print('PASS:', checks, 'exhaustive threshold identities, each comparing all 2^n fair-sign sequences, 2 <= n <= 14')
