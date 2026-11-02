"""Independent exact n=7 upper-bound verifier using poset closures and linear-extension counts."""
from functools import lru_cache
import time
n=7
pairs=[(a,b) for a in range(n) for b in range(a+1,n)]
@lru_cache(None)
def extend_count(pred):
    @lru_cache(None)
    def rec(done):
        if done == (1<<n)-1:return 1
        total=0
        for v in range(n):
            if not done>>v&1 and pred[v]&~done==0:total+=rec(done|1<<v)
        return total
    return rec(0)

def add(pred,a,b):
    # Add a<b, assuming incomparable, then close transitively.
    anc=pred[a] | (1<<a)
    x=list(pred)
    for v in range(n):
        if v==b or ((pred[v]>>b)&1):
            x[v] |= anc
    return tuple(x)

@lru_cache(None)
def can(pred,d):
    if d==0:return True
    if extend_count(pred)<(1<<d):return False
    for a,b in pairs:
        if (pred[a]>>b)&1 or (pred[b]>>a)&1:continue
        pos=add(pred,a,b);neg=add(pred,b,a)
        if extend_count(pos)<(1<<(d-1)) or extend_count(neg)<(1<<(d-1)):continue
        if can(pos,d-1) and can(neg,d-1):return True
    return False
root=add(tuple([0]*n),0,1)
t=time.time();result=can(root,11)
print('N7_CONDITIONED_11',result,'SECONDS',round(time.time()-t,3),'STATES',can.cache_info().currsize,'COUNTSTATES',extend_count.cache_info().currsize,flush=True)
assert result is False
print('NO_DEPTH_12_FULL_PERMUTATION_SHATTERING_FOR_N7')
