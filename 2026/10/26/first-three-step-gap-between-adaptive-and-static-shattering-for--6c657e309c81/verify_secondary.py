from functools import lru_cache
from time import monotonic

def feasible(N,depth):
    q={x:sum(1 << (i-1) for i in range(x,N+1,x)) for x in range(2,N+1)}
    @lru_cache(None)
    def search(H,d):
        if d==0:return H!=0
        if H.bit_count()<2**d:return False
        for x in range(2,N+1):
            yes=H&q[x];no=H^yes
            if not yes or not no: continue
            if search(yes,d-1) and search(no,d-1):return True
        return False
    return search((1<<N)-1,depth),search.cache_info()
if __name__ == '__main__':
    thresholds=(2,4,9,27,81,320,1280)
    for d,n in enumerate(thresholds,1):
        assert not feasible(n-1,d)[0]
        assert feasible(n,d)[0]
    assert not feasible(1280,8)[0]
    print('SECONDARY_OK: exact 14 boundaries and depth-eight exclusion')
