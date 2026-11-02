"""Exact finite checks for cutoff sumset monoids. Python standard library only."""
from itertools import combinations, permutations


def mul(n, a, b):
    """Encode the presence of integers 1,...,n as successive bit positions."""
    ans = a | b
    for i in range(1, n + 1):
        if a & (1 << (i - 1)):
            for j in range(1, n + 1 - i):
                if b & (1 << (j - 1)):
                    ans |= 1 << (i + j - 1)
    return ans


def mul_by_sets(n, a, b):
    A = {0} | {i for i in range(1, n + 1) if a >> (i-1) & 1}
    B = {0} | {i for i in range(1, n + 1) if b >> (i-1) & 1}
    C = {x+y for x in A for y in B if x+y <= n}
    return sum(1 << (x-1) for x in C if x != 0)


def automorphism_count(t):
    m = len(t)
    target = list(range(m))
    result = 0
    for imgs in permutations(range(1,m)):
        f = (0,) + imgs
        # Preservation of multiplication; exhaustive bijections fixing the identity.
        if all(f[t[i][j]] == t[f[i]][f[j]]
               for i in target for j in target):
            result += 1
    return result


def main():
    for n in range(1,9):
        size = 1 << n
        top = 1 << (n-1)
        # Two separately specified multiplication algorithms.
        if n <= 6:
            for a in range(size):
                for b in range(size):
                    assert mul(n,a,b) == mul_by_sets(n,a,b)
        ranks = []
        for a in range(size):
            ranks.append(len({mul(n,a,b) for b in range(size)}))
        assert ranks[0] == size
        assert ranks[top] == size//2
        if n >= 4:
            assert [a for a in range(1,size) if ranks[a] == size//2] == [top]
            assert all(ranks[a] < size//2 for a in range(1,size) if a != top)
            # Every other element has strictly smaller multiplication-image rank.
        if n in (2,3):
            assert [a for a in range(1,size)
                    if ranks[a] == size//2 and mul(n,a,a) == a] == [top]
        # A characteristic principal ideal (identity of that ideal is top).
        ideal = {a | top for a in range(size)}
        assert len(ideal) == size//2
        for a in ideal:
            for b in ideal:
                assert mul(n,a,b) in ideal
                assert (mul(n,a,b) & (top-1)) == mul(n-1,a&(top-1),b&(top-1)) if n>1 else True
        if n <= 3:
            t = [[mul(n,a,b) for b in range(size)] for a in range(size)]
            assert automorphism_count(t) == 1
        # Counter-witness: a non-terminal singleton has missing image among sets containing it.
        if n >= 4:
            for k in range(1,n):
                x = 1 << (k-1)
                missing = (1 << (k-1)) | (1 << (0 if k>1 else 2))
                assert all(mul(n,x,b) != missing for b in range(size))
        print(f"n={n}; order={size}; terminal rank={ranks[top]}; intrinsic terminal=PASS; quotient=PASS")
    for n in range(1,5):
        size = 1<<n
        for a in range(size):
            for b in range(size):
                for c in range(size):
                    assert mul(n,mul(n,a,b),c) == mul(n,a,mul(n,b,c))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
