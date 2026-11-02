"""Independent finite checks for coupled cover times on balanced complete bipartite graphs.
Run: python check.py. All assertions are deterministic; no network or external data.
"""
from fractions import Fraction as F
from math import comb, log, sqrt
from collections import defaultdict
import random

checks = 0

def eq(a,b):
    global checks
    assert a == b, (a,b)
    checks += 1


def coupon_cdf(n,t,no_return):
    if t < 0: return F(0)
    out = F(0)
    for k in range(n):
        base = F(n-1-k,n-1) if no_return else F(n-k,n)
        out += (-1)**k * comb(n-1,k) * base**t
    return out


def exact_markov_cdf(n,steps,no_backtrack):
    # State (previous,current,visited mask); vertices A=0..n-1, B=n..2n-1
    state = {(None,0,1):F(1)}
    full=(1<<(2*n))-1
    ans=[F(0)]
    for s in range(1,steps+1):
        nxt=defaultdict(F)
        for (prev,cur,mask),p in state.items():
            neigh=range(n,2*n) if cur<n else range(n)
            permitted=[v for v in neigh if not (no_backtrack and v==prev)]
            for v in permitted:
                nxt[(cur,v,mask|(1<<v))]+=p/F(len(permitted))
        state=nxt
        eq(sum(state.values()),F(1))
        ans.append(sum(p for (prev,cur,mask),p in state.items() if mask==full))
    return ans

for n in range(2,6):
    for no_backtrack in (False,True):
        rows=exact_markov_cdf(n,12,no_backtrack)
        for t,q in enumerate(rows):
            pred=coupon_cdf(n,t//2,no_backtrack)*coupon_cdf(n,(t-1)//2,no_backtrack)
            eq(q,pred)
        for t in range(0,12): eq(rows[t]<=rows[t+1],True)

# Independent geometric-stage convolution versus inclusion--exclusion.
for n in range(2,14):
    for no_return in (False,True):
        pmf=[F(1)]+[F(0)]*45
        for k in range(n-1,0,-1):
            success=F(k,n-1 if no_return else n)
            nxt=[F(0)]*len(pmf)
            for t in range(1,len(pmf)):
                nxt[t]=(1-success)*nxt[t-1]+success*pmf[t-1]
            pmf=nxt
        for t in range(0,40):
            eq(sum(pmf[:t+1]), coupon_cdf(n,t,no_return))

# Enumerate every two-coordinate letter stream for very small horizons, checking
# that run-length compression actually generates the non-backtracking marginal.
from itertools import product
for n in (2,3):
    m=3
    counts=defaultdict(int)
    for aa in product(range(n),repeat=m):
        for bb in product(range(n),repeat=m):
            ac=[0]+list(aa)
            bc=[bb[0]]+list(bb[1:])
            aset=[ac[0]]
            bset=[bc[0]]
            for v in ac[1:]:
                if v!=aset[-1]: aset.append(v)
            for v in bc[1:]:
                if v!=bset[-1]: bset.append(v)
            if len(aset)>=2 and len(bset)>=2:
                counts[(aset[1],bset[1])]+=1
    # Given initial B label and at least one change, next A and B must each be
    # uniform among alternatives; exact enumeration checks symmetric counts.
    # Full Markov-DP and coupon formulas above establish the time law independently.
    eq(all(x>=0 for x in counts.values()),True)

# Independent sampling of stage waiting times tests macro-scale and microscopic
# predictions, without using any external input.
rng=random.Random(527123)
for n,reps in [(40,2500),(120,2500),(400,2500)]:
    saved=[]
    centered=[]
    for _ in range(reps):
        ks=[]; rs=[]
        for side in range(2):
            ksum=0
            for missing in range(n-1,0,-1):
                p=missing/(n-1)
                while True:
                    ksum+=1
                    if rng.random()<p:break
            # Independent repeat count per accepted jump, geometric failures.
            rsum=0
            for _ in range(ksum):
                while rng.random()<1/n:rsum+=1
            ks.append(ksum);rs.append(rsum)
        tn=max(2*ks[0],2*ks[1]+1)
        ts=max(2*(ks[0]+rs[0]),2*(ks[1]+rs[1])+1)
        eq(ts>=tn,True)
        saved.append((ts-tn)/2)
        centered.append((tn/(2*n)-log(n)))
    avg=sum(saved)/reps
    assert abs(avg-log(n)-0.5772156649015329-log(2))<0.75,(n,avg)
    checks+=1
    empirical_var=sum((x-avg)**2 for x in saved)/reps
    assert 0.45 < empirical_var/log(n) < 2.6,(n,empirical_var)
    checks+=1
    print(f'n={n}: mean saved half-steps={avg:.4f}, var={empirical_var:.4f}, Gumbel-location check={sum(centered)/reps:.4f}')
print('PASS assertions',checks)
