"""Exact dynamic programming over dominated-vertex masks for rook graphs."""
from functools import lru_cache


def expected(m, n):
    if m > n:
        m, n = n, m
    if m == n:
        return 2*m - 2
    if n == m + 1:
        return 2*m
    return m+n-2


def calculate(m, n):
    size = m*n
    all_mask = (1 << size)-1
    neighborhood = []
    for i in range(size):
        r,c=divmod(i,n)
        neighborhood.append(sum(1 << j for j in range(size)
                                if j != i and (j//n == r or j%n == c)))
    @lru_cache(None)
    def search(covered):
        if covered == all_mask:
            return 0
        choices = [search(covered | new) + 1 for new in neighborhood
                   if new & ~covered]
        assert choices
        return max(choices)
    val=search(0)
    return val,search.cache_info().currsize


def verify_construction(m,n):
    if m > n:m,n=n,m
    if n == m+1:
        seq=[(i,i) for i in range(m)]+[(i,n-1) for i in range(m)]
    else:
        seq=[(0,j) for j in range(n-1)]+[(i,0) for i in range(1,m)]
    seen=0
    for r,c in seq:
        new=sum(1 << (i*n+j) for i in range(m) for j in range(n)
                if (i==r or j==c) and (i,j)!=(r,c))
        assert new & ~seen, (m,n,r,c)
        seen |= new
    assert seen==(1 << (m*n))-1
    assert len(seq)==expected(m,n)

if __name__ == '__main__':
    for m in range(2,7):
        for n in range(m, min(m+5,9)):
            if m*n>42:continue
            val, states=calculate(m,n)
            assert val==expected(m,n), (m,n,val)
            verify_construction(m,n)
            print(f'{m}x{n} optimum={val}; DP_states={states}; construction=verified')
    print('PASS: all checked instances agree with the claimed formula')
