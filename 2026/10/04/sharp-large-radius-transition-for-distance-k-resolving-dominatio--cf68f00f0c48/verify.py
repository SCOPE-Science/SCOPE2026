from itertools import combinations
from collections import deque
from math import ceil

def balanced_spider(q,L):
    # center 0; arm i has vertices at depths 1..L
    n=1+q*L
    adj=[set() for _ in range(n)]
    for i in range(q):
        prev=0
        for d in range(1,L+1):
            v=1+i*L+(d-1)
            adj[prev].add(v); adj[v].add(prev)
            prev=v
    return adj

def all_distances(adj):
    n=len(adj)
    D=[]
    for s in range(n):
        dist=[10**9]*n
        dist[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dist[v]==10**9:
                    dist[v]=dist[u]+1
                    q.append(v)
        D.append(dist)
    return D

def is_resolving(D,S):
    seen=set()
    for v in range(len(D)):
        sig=tuple(D[v][s] for s in S)
        if sig in seen:
            return False
        seen.add(sig)
    return True

def is_k_dominating(D,S,k):
    return all(min(D[v][s] for s in S)<=k for v in range(len(D)))

def arm_depth(v,L):
    if v==0:
        return None
    x=v-1
    return x//L, x%L+1

def predicted_value(q,L,k):
    if k < (L+1)//2:
        return None
    return q if k<=L else q-1

def predicted_basis_count_superradius(q,L,k):
    # valid only k>=L+1
    if k>=2*L:
        return q*(L**(q-1))
    return q*(L**(q-1) - (2*L-k)**(q-1))

pairs=values_checked=bases_checked=small_sets_checked=0
for q in range(3,6):
    for L in range(2,6):
        adj=balanced_spider(q,L)
        D=all_distances(adj)
        n=len(adj)
        pairs+=1

        # Directly verify the standard metric-basis structure at size q-1.
        resolving_qm1=[]
        for S in combinations(range(n),q-1):
            small_sets_checked+=1
            if is_resolving(D,S):
                resolving_qm1.append(S)
                assert 0 not in S
                profiles=[arm_depth(v,L) for v in S]
                arms=[a for a,d in profiles]
                assert len(set(arms))==q-1
        assert len(resolving_qm1)==q*(L**(q-1))

        # In the theorem range, verify exact minimum values directly.
        for k in range((L+1)//2, 2*L+2):
            pred=predicted_value(q,L,k)
            assert pred is not None

            # No set smaller than the claimed value works.
            for r in range(1,pred):
                for S in combinations(range(n),r):
                    small_sets_checked+=1
                    assert not (is_resolving(D,S) and is_k_dominating(D,S,k)), (q,L,k,S)

            # Count/confirm minimum sets.
            mins=[]
            for S in combinations(range(n),pred):
                if is_resolving(D,S) and is_k_dominating(D,S,k):
                    mins.append(S)
            assert mins, (q,L,k)
            values_checked+=1
            bases_checked+=len(mins)

            if k>=L+1:
                assert len(mins)==predicted_basis_count_superradius(q,L,k), (
                    q,L,k,len(mins),predicted_basis_count_superradius(q,L,k)
                )
                # Complete classification of minimum sets.
                for S in mins:
                    assert 0 not in S
                    prof=[arm_depth(v,L) for v in S]
                    arms=[a for a,d in prof]
                    depths=[d for a,d in prof]
                    assert len(set(arms))==q-1
                    assert min(depths)<=k-L

print("VERIFY_OK")
print("parameter_pairs_checked =",pairs)
print("theorem_values_checked =",values_checked)
print("minimum_sets_checked =",bases_checked)
print("candidate_sets_checked_below_or_at_metric_threshold =",small_sets_checked)
print("parameters q = 3..5, L = 2..5")
print("all direct resolving and distance-k domination tests matched the phase formula")
print("all size-(q-1) resolving sets matched the one-vertex-per-q-1-arms structure")
print("all k >= L+1 minimum-set counts and depth-threshold classifications matched")
