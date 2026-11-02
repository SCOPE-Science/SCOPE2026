#!/usr/bin/env python3
"""Exact five-round online adversarial game verifier (standard Python only)."""
from functools import lru_cache
from itertools import product
N, M = 3, 5

def masks(owners, t):
    remaining = [i for i in range(N) if owners[i] == -1]
    subsets = (range(1 << len(remaining)) if t < M-1 else [(1 << len(remaining))-1])
    return [sum(1 << remaining[j] for j in range(len(remaining)) if s >> j & 1) for s in subsets]

def step(counts, owners, mask, recipient):
    c = list(counts); c[recipient] += 1
    return tuple(c), tuple(recipient if mask >> i & 1 else owners[i] for i in range(N))

def exact_test(counts, owners, H, p, q):
    # Check p * residual <= q * own (alpha = p/q), in integers.
    for i in range(N):
        own = counts[i] + (H-1)*int(owners[i] == i)
        for j in range(N):
            if i == j or not counts[j]: continue
            residual = counts[j]-1+(H-1)*int(owners[i] == j and counts[j] > 1)
            if p*residual > q*own: return False
    return True

def infinite_test(c, o):
    # Strong enough to yield alpha=1/2 for every real H>=4.
    for i in range(N):
        if o[i] == i: continue
        if c[o[i]] > 1: return False
        if any(2*c[i] < c[j]-1 for j in range(N) if i != j): return False
    return True

def mid_test(c, o):
    return (exact_test(c,o,1,1,1) and exact_test(c,o,2,1,1)
            and exact_test(c,o,4,1,2))

def certify_policy(terminal):
    @lru_cache(None)
    def viable(t,c,o):
        if t == M:return terminal(c,o)
        return all(any(viable(t+1,*step(c,o,mask,j)) for j in range(N)) for mask in masks(o,t))
    start=(0,(0,0,0),(-1,-1,-1))
    assert viable(*start)
    moves={}; encountered=set()
    def construct(t,c,o):
        if (t,c,o) in encountered:return
        encountered.add((t,c,o))
        if t == M:return
        for mask in masks(o,t):
            j=next(j for j in range(N) if viable(t+1,*step(c,o,mask,j)))
            moves[(t,c,o,mask)] = j
            construct(t+1,*step(c,o,mask,j))
    construct(*start)
    leaves=set()
    def replay(t,c,o):
        if t == M:
            assert terminal(c,o)
            leaves.add((c,o)); return
        for mask in masks(o,t):
            j=moves[(t,c,o,mask)]
            assert j in range(N)
            replay(t+1,*step(c,o,mask,j))
    replay(*start)
    return viable.cache_info().currsize, len(moves), len(leaves)

# On [1,2], all terminal EFX inequalities are affine in H,
# so H=1,2 suffice. On [2,4], for agents without their spike,
# H*own - 2*residual is affine in H; for spike owners it is
# H*(H+c_i-1)-2*(c_j-1), increasing on H>=2.
# Thus the mid policy proves alpha=min(1,2/H) for all 1<=H<=4.
mid=certify_policy(mid_test)
# If a spike owner has her spike, her own value is >=H and all
# opponents' EFX residuals are at most 4. Hence H>=4 suffices.
# If a nonowner has her spike in another singleton, its removal
# leaves zero. With other opponents, only counts c_j-1 matter.
high=certify_policy(infinite_test)

# Adversary upper bound: first three goods are common-low.
# For initial pattern (2,1,0), the fourth is high only for the
# holder of 2 goods. For (3,0,0) or (1,1,1), it is high for all.
# The fifth uses precisely the high marks still unused.
# Each possible final response admits an EFX comparison proving
# alpha<=2/H throughout [2,4], and alpha<=1/2 for H>=4.
def witness(c,o,kind):
    for i in range(N):
        for j in range(N):
            if i==j or not c[j]:continue
            def own(H):return c[i]+(H-1)*int(o[i]==i)
            def residual(H):return c[j]-1+(H-1)*int(o[i]==j and c[j]>1)
            if kind=='middle':
                # H*own(H) <= 2*residual(H) at H=2,4;
                # the actual witness has no self-spike, hence is affine.
                if o[i]!=i and all(H*own(H)<=2*residual(H) for H in (2,4)):
                    return (i,j)
            else:
                if o[i]!=i and 2*own(4)<=residual(4):
                    # For nonowners: RHS grows with H or stays fixed.
                    return (i,j)
    return None

upper_cases=0
for first3 in product(range(N),repeat=3):
    c=[first3.count(i) for i in range(N)]
    mask4=(1<<c.index(2)) if max(c)==2 else 7
    for x,y in product(range(N),repeat=2):
        c4,o4=step(tuple(c),(-1,-1,-1),mask4,x)
        c5,o5=step(c4,o4,7^mask4,y)
        assert witness(c5,o5,'middle') is not None, (first3,x,y,'middle')
        assert witness(c5,o5,'high') is not None, (first3,x,y,'high')
        upper_cases+=1

print('VERIFY_OK', 'mid_states=%d mid_policy=%d mid_leaves=%d'%mid,
      'high_states=%d high_policy=%d high_leaves=%d'%high,
      'upper_paths=%d'%upper_cases)
