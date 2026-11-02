"""Independent exact checks of the finite Harsanyi-kernel census."""
from itertools import product, permutations
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def weak_comps(d,n):
    if n==1: return ((d,),)
    return tuple((x,)+rest for x in range(d+1) for rest in weak_comps(d-x,n-1))

def row_harsanyi(rows):
    # Use support of every probability vector, not a partition formula.
    return all(rows[j]==rows[i] for i,row in enumerate(rows) for j,num in enumerate(row) if num)

def partitions(n):
    # independent set-partition recursion based on restricted growth strings
    if n==0: yield ();return
    def rec(k,parts):
        if k==n:
            yield tuple(tuple(z) for z in parts);return
        for j in range(len(parts)):
            parts[j].append(k)
            yield from rec(k+1,parts)
            parts[j].pop()
        parts.append([k]);yield from rec(k+1,parts);parts.pop()
    yield from rec(0,[])

def formula(n,d):
    return sum(__import__('math').prod(comb(d+len(b)-1,len(b)-1) for b in pi) for pi in partitions(n))

def orbit_formula(n,d):
    @lru_cache(None)
    def p_le(s,rem):
        if s==0:return int(rem==0)
        return sum(p_le(s-1,rem-k*s) for k in range(rem//s+1))
    @lru_cache(None)
    def dp(max_size, remaining):
        if max_size==0:return int(remaining==0)
        ways=0
        # number of distinct block decoration choices p_{<=size}(d)
        c=p_le(max_size,d)
        for k in range(remaining//max_size+1):
            ways+=comb(k+c-1,k)*dp(max_size-1,remaining-k*max_size)
        return ways
    return dp(n,n)

def canonical(rows):
    n=len(rows)
    return min(tuple(rows[p[i]][p[j]] for i in range(n) for j in range(n)) for p in permutations(range(n)))

if __name__=='__main__':
    for n in range(1,5):
        for d in (1,2,3):
            if len(weak_comps(d,n))**n>400000:continue
            seq=weak_comps(d,n)
            hs=[rs for rs in product(seq,repeat=n) if row_harsanyi(rs)]
            predicted=formula(n,d)
            print(f'n={n} d={d} brute={len(hs)} formula={predicted}')
            assert len(hs)==predicted
            if n<=3:
                obs=len({canonical(rs) for rs in hs})
                exp=orbit_formula(n,d)
                print(f' orbit brute={obs} formula={exp}')
                assert obs==exp
    for n in range(1,8):
        for d in (1,2,3):
            assert formula(n,d)>=1
    for n in range(1,8):
        assert formula(n,1)==sum(comb(n,k)*k**(n-k) for k in range(1,n+1))
    # Idempotent but non-Harsanyi witness: 3-state K with half-half transient type.
    K=((2,0,0),(0,2,0),(1,1,0))
    assert not row_harsanyi(K)
    assert all(sum(K[i][j]*K[j][k] for j in range(3))==2*K[i][k]
               for i in range(3) for k in range(3))
    print('ALL_CHECKS_OK')
