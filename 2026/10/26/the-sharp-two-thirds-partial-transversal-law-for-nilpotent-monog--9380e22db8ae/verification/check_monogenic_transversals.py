"""Finite cross-check of an exact partial-transversal formula.
Run: python3 check_monogenic_transversals.py
"""
from functools import lru_cache


def predicted(n):
    return 1 + (2*n - 3)//3


def construction(n):
    t = predicted(n) - 1
    if t == 0:
        return [(0, 0, 0)]
    if t % 2:
        k = (t-1)//2
        pi = [((i-1+k) % t)+1 for i in range(1,t+1)]
    else:
        k = t//2
        pi = [(k*i) % (2*k+1) for i in range(1,t+1)]
    return [(0, 0, 0)] + [(i, pi[i-1], i+pi[i-1]) for i in range(1,t+1)]


def exhaustive(n):
    # Exact maximal rainbow matching on the strictly triangular sum table.
    # Every row index i occurs at most once and must satisfy 1<=i<=n-2.
    @lru_cache(None)
    def solve(i, cols_mask, sums_mask):
        if i >= n-1:
            return 0
        best = solve(i+1, cols_mask, sums_mask)
        for j in range(1,n-i):
            s = i+j
            if not (cols_mask >> j) & 1 and not (sums_mask >> s) & 1:
                best = max(best,1+solve(i+1, cols_mask | (1<<j), sums_mask | (1<<s)))
        return best
    return solve(1,0,0), solve.cache_info().currsize


def check(n, witness):
    assert all(0<=i<n and 0<=j<n and (s == (i+j if i+j<n else 0)) for i,j,s in witness)
    assert len({i for i,j,s in witness}) == len(witness)
    assert len({j for i,j,s in witness}) == len(witness)
    assert len({s for i,j,s in witness}) == len(witness)
    assert len(witness)==predicted(n)


def main():
    for n in range(2, 71):
        w=construction(n)
        check(n,w)
        if n<=12:
            opt,states=exhaustive(n)
            assert opt+1 == predicted(n), (n,opt,predicted(n))
            print(f'n={n} exhaustive={opt+1} predicted={predicted(n)} states={states}')
    print('VERIFY_OK: constructions n=2..70; exhaustive maximum n=2..12')


if __name__ == '__main__':
    main()
