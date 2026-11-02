"""Independent transport/duality and cyclic-rotation tests (standard Python 3)."""
from collections import deque
from functools import lru_cache
from itertools import combinations


def neighbors(x,n):
    ans=set()
    for i in range(n-2):
        bits=(x>>i)&7
        for nxt in ((bits>>1)|((bits&1)<<2), ((bits<<1)&7)|(bits>>2)):
            ans.add((x&~(7<<i))|(nxt<<i))
    ans.discard(x)
    return ans


def all_distances(x,n):
    q=deque([x]); ds={x:0}
    while q:
        u=q.popleft()
        for v in neighbors(u,n):
            if v not in ds:
                ds[v]=ds[u]+1;q.append(v)
    return ds


def matching_distance(x,y,n):
    s=[i for i in range(n) if x&(1<<i)]
    t=[i for i in range(n) if y&(1<<i)]
    k=len(s)
    @lru_cache(None)
    def solve(mask):
        i=mask.bit_count()
        if i==k: return 0
        return min((abs(s[i]-t[j])+1)//2+solve(mask|1<<j)
                   for j in range(k) if not(mask&(1<<j)))
    return solve(0)


def check():
    tested=0
    for n in range(3,10):
        for k in range(1,n):
            words=[sum(1<<i for i in c) for c in combinations(range(n),k)]
            D=(k*(n-k)+1)//2
            observed=0
            for x in words:
                ds=all_distances(x,n)
                assert len(ds)==len(words), (n,k,x)
                observed=max(observed,max(ds.values()))
                for y in words:
                    if ds[y]!=matching_distance(x,y,n):
                        raise AssertionError((n,k,x,y,ds[y],matching_distance(x,y,n)))
                    tested+=1
            assert observed==D,(n,k,observed,D)
    print('TRANSPORT_VERIFY_OK n=3..9; pairs='+str(tested))

if __name__=='__main__': check()
