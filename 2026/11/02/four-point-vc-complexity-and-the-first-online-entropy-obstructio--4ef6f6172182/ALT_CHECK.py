"""Independent literal-set recurrence for the entropy-bound obstructions."""
from VERIFY import layer
from functools import lru_cache

for n, depth in [(9,8),(10,9),(11,9)]:
    h = frozenset(layer(n))
    @lru_cache(None)
    def exists(S,d):
        if d==0:return bool(S)
        if len(S)<2**d:return False
        for pos in range(1,len(next(iter(S)))-1):
            z=frozenset(w for w in S if w[pos]=='D')
            o=S-z
            if min(len(z),len(o)) >= 2**(d-1) and exists(z,d-1) and exists(o,d-1):
                return True
        return False
    assert exists(h,depth-1) and not exists(h,depth)
    print('ALTERNATIVE_UPPER_PASS',n,'failed_depth',depth,'states',exists.cache_info().currsize,flush=True)
