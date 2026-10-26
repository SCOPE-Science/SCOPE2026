"""Finite-state checks for deterministic NEC-majority on a two-row ring.
Requires only Python >=3.9. Uses exact integer enumeration; does not prove all n.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, gcd


def majority(a, b, c):
    return 1 if a + b + c >= 2 else 0


def direct_update(state, n):
    """Rows are separately encoded as n bits, in cyclic column order."""
    upper, lower = state[:n], state[n:]
    return tuple(majority(upper[i], lower[i], upper[(i+1)%n]) for i in range(n)) + tuple(
        majority(lower[i], upper[i], lower[(i+1)%n]) for i in range(n))


def quotient_update(state, n):
    cols = [(state[i],state[n+i]) for i in range(n)]
    out = [cols[i] if cols[i][0]==cols[i][1] else cols[(i+1)%n] for i in range(n)]
    return tuple(x[0] for x in out)+tuple(x[1] for x in out)


def run_length(mask):
    n=len(mask)
    if all(mask) or not any(mask):return 0
    longest = current = 0
    for bit in list(mask) * 2:
        current = current + 1 if bit else 0
        longest = max(longest, current)
    return longest


def composition_count(k, total, cap):
    dp = [1]+[0]*total
    for _ in range(k):
        new=[0]*(total+1)
        for s, count in enumerate(dp):
            if count:
                for z in range(min(cap,total-s)+1):new[s+z]+=count
        dp=new
    return dp[total]


def cumulative_entrants(n,t):
    # Each binary anchor/mismatch mask has 2**n state refinements.
    masks=1 # the all-mismatch invariant mask
    for k in range(1,n+1):
        marked=n*composition_count(k,n-k,t)
        assert marked%k==0
        masks+=marked//k
    return (2**n)*masks


def mobius(n):
    if n == 1:
        return 1
    factors = 0
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            factors += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors += 1
    return (-1)**factors


def verify(n):
    basins=defaultdict(int)
    cumulative=Counter()
    recurrent_by_period=Counter()
    every=0
    for s in product((0,1),repeat=2*n):
        nxt=direct_update(s,n)
        assert nxt==quotient_update(s,n), ('incorrect reduced rule',n,s)
        seen={}; cur=s
        while cur not in seen:
            seen[cur]=len(seen);cur=direct_update(cur,n)
        entry=seen[cur]; primitive=len(seen)-entry
        m=tuple(s[i]!=s[i+n] for i in range(n))
        predicted=run_length(m)
        assert entry==predicted, ('incorrect transient',n,s,entry,predicted)
        cumulative[entry]+=1
        if entry==0: recurrent_by_period[primitive]+=1
        if not all(m):
            assert cur[:n]==cur[n:]
            assert primitive==1
            basins[cur[:n]]+=1
        else:
            assert entry==0
        every+=1
    assert every==4**n
    assert sum(recurrent_by_period.values())==2**(n+1)
    assert recurrent_by_period[1]==2**n+2
    for d,count in recurrent_by_period.items():
        assert n%d==0
        from_mismatch=sum(mobius(d//e)*2**e for e in range(1,d+1) if d%e==0)
        assert count==from_mismatch+(2**n if d==1 else 0),('wrong primitive count',n,d,count)
    for y in product((0,1),repeat=n):
        boundaries=sum(y[i]!=y[(i+1)%n] for i in range(n))
        expected=3**(n-boundaries) if boundaries else 3**n-2**n
        assert basins[y]==expected, ('wrong basin',n,y,expected,basins[y])
    for t in range(n):
        expected=cumulative_entrants(n,t)
        observed=sum(count for tau,count in cumulative.items() if tau<=t)
        assert expected==observed,('wrong cdf',n,t,expected,observed)
    assert max(cumulative)==n-1
    print('n=%s states=%s recurrent=%s fixed=%s cycles=%s depths=%s' %
          (n,every,sum(recurrent_by_period.values()),recurrent_by_period[1],
           sorted(recurrent_by_period.items()),sorted(cumulative.items())))


for n in range(2,9):verify(n)
print('VERIFY_OK')
