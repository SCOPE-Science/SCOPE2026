"""Independent finite checks of a half-graph Grundy domination theorem.

Run with Python 3.10 or later: python check_halfgraph.py
No third-party dependencies.
"""
from functools import lru_cache


def neighbors(n, removed=None):
    out = [1 << k for k in range(2*n)]
    for i in range(1,n+1):
        for j in range(i,n+1):
            if (i,j)==removed:
                continue
            a=i-1
            b=n+j-1
            out[a] |= 1 << b
            out[b] |= 1 << a
    return out


def ground_optimum(n, removed=None):
    masks=neighbors(n,removed)
    full=(1<<(2*n))-1
    @lru_cache(None)
    def best(covered):
        if covered==full:
            return 0
        return 1+max(best(covered|mask) for mask in masks if (covered|mask)!=covered)
    return best(0)


def xm(k):
    return k-1


def ym(n,k):
    return n+k-1


def edge_witness(n, i, j):
    assert n>=3 and 1<=i<=j<=n and (i,j) not in {(1,1),(n,n)}
    X=lambda k:xm(k)
    Y=lambda k:ym(n,k)
    if j==n and i>=2:
        # The graph is invariant under reflection and side exchange.
        source=edge_witness(n,1,n+1-i)
        return [2*n-1-u for u in source]
    if i==1 and j==n:
        return [Y(k) for k in range(n-2,0,-1)]+[X(1),Y(n-1),X(n-1),Y(n)]
    if i==1:
        return [Y(1),X(1),X(j+1)]+[Y(k) for k in range(2,j)]+[Y(j+1),Y(j)]+[Y(k) for k in range(j+2,n+1)]
    if i==j:
        return [X(i),X(i+1)]+[Y(k) for k in range(1,i-1)]+[Y(i+1),Y(i-1),Y(i)]+[Y(k) for k in range(i+2,n+1)]
    return [X(i),X(j+1)]+[Y(k) for k in range(1,i-1)]+[Y(i),Y(i-1)]+[Y(k) for k in range(i+1,j)]+[Y(j+1),Y(j)]+[Y(k) for k in range(j+2,n+1)]


def check_seq(n,removed,seq):
    masks=neighbors(n,removed)
    assert len(seq)==len(set(seq))
    covered=0
    for v in seq:
        assert 0<=v<2*n
        fresh=masks[v]&~covered
        assert fresh, (n,removed,seq,v)
        covered |= masks[v]
    assert covered == (1<<(2*n))-1


def main():
    witness_checks=0
    for n in range(3,31):
        for i in range(1,n+1):
            for j in range(i,n+1):
                if (i,j) in {(1,1),(n,n)}:
                    continue
                seq=edge_witness(n,i,j)
                assert len(seq)==n+2
                check_seq(n,(i,j),seq)
                witness_checks+=1
    print('ALL_ORDER_WITNESS_OK dimensions=3..30 witnesses=',witness_checks,sep='')
    exact_checks=0
    for n in range(2,9):
        expected=n+1 if n>=2 else 1
        assert ground_optimum(n)==expected, ('base',n)
        for i in range(1,n+1):
            for j in range(i,n+1):
                val=ground_optimum(n,(i,j))
                want=n+1 if (i,j) in {(1,1),(n,n)} else n+2
                if n==2 and (i,j)==(1,2):
                    want=2
                assert val==want,(n,i,j,val,want)
                exact_checks+=1
    print('ORIGINAL_DEFINITION_DP_OK n=2..8 edge_deletions=',exact_checks,sep='')
    print('BOUNDARY_OK n=2 exceptional middle-edge value=2')
    print('VERIFICATION_OK')

if __name__=='__main__':
    main()
