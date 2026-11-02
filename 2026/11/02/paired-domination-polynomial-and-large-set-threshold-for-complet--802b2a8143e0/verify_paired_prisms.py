from itertools import combinations
from functools import lru_cache
from math import comb

def is_paired(S,n):
    if len(S)%2 or not S:return False
    ss=set(S)
    def neighbors(v):
        if v<n:return [u for u in range(n) if u!=v]+[v+n]
        i=v-n;return [n+j for j in range(n) if j!=i]+[i]
    if any(not any(u in ss for u in neighbors(v)) for v in range(2*n)):
        return False
    @lru_cache(None)
    def match(t):
        if not t:return True
        v=t[0]
        for u in t[1:]:
            if u in neighbors(v) and match(tuple(i for i in t if i!=v and i!=u)):
                return True
        return False
    return match(tuple(sorted(S)))

def predicted(n,k):
    return comb(2*n,k)-(2+2**(k-1))*(comb(n,k) if k<=n else 0)+(2 if n%2==0 and k==n else 0)
for n in range(2,8):
    coeff={}
    for k in range(2,2*n+1,2):
        a=sum(is_paired(s,n) for s in combinations(range(2*n),k))
        b=predicted(n,k)
        assert a==b,(n,k,a,b)
        coeff[k]=a
    print(n, coeff)
print('VERIFY_OK')
