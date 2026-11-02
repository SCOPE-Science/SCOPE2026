#!/usr/bin/env python3
"""Independent finite checks for balanced 1-limited dominating sets of S(n,3).
Works with Python 3 standard library only. Public mathematical computation.
"""
from itertools import product
from math import comb

def vertices_and_neighbors(n, m=3):
    vs=list(product(range(m),repeat=n))
    idx={v:i for i,v in enumerate(vs)}
    nei=[set() for _ in vs]
    for i,u in enumerate(vs):
        for h in range(n):
            for a in range(m):
                if a==u[h] or u[h+1:]!=(a,)*(n-h-1):continue
                v=u[:h]+(a,)+(u[h],)*(n-h-1)
                j=idx[v]
                if i!=j:nei[i].add(j);nei[j].add(i)
    return vs,nei

def is_limited_dominating(picks, nei):
    for v, nv in enumerate(nei):
        if picks[v]:
            if sum(not picks[u] for u in nv)>1:return False
        elif not any(picks[u] for u in nv):return False
    return True

def exact_balanced(n):
    vs,nei=vertices_and_neighbors(n)
    roots=list(product(range(3), repeat=n-1))
    ix={v:i for i,v in enumerate(vs)}
    count=0
    for absent in product(range(3), repeat=len(roots)):
        chosen=[True]*len(vs)
        for prefix,a in zip(roots,absent):chosen[ix[prefix+(a,)]]=False
        if is_limited_dominating(chosen,nei):count+=1
    return count

def direct_matching_count(t, unmatched):
    vs,nei=vertices_and_neighbors(t)
    corners={vs.index((j,)*t) for j in range(3)}
    absent={vs.index((j,)*t) for j in unmatched}
    # Count graph matchings whose unmatched vertices are *exactly* absent.
    remaining=set(range(len(vs)))-absent
    cache={}
    def dfs(rem):
        if not rem:return 1
        if rem in cache:return cache[rem]
        v=min(rem, key=lambda x:len(nei[x]&rem))
        ans=sum(dfs(rem-{v,w}) for w in nei[v]&rem)
        cache[rem]=ans
        return ans
    return dfs(frozenset(remaining))

def rec_a(t):
    a=1
    for _ in range(2,t+1):a=2*a*a*a
    return a

if __name__=='__main__':
    for n in (2,3):
        got=exact_balanced(n)
        expected=2**((3**(n-2)+3)//2)
        assert got==expected,(n,got,expected)
        print('BASEWISE_EXHAUSTIVE',n,got)
    for t in (1,2,3):
        a=rec_a(t)
        for mask in range(8):
            subset=[j for j in range(3) if mask>>j&1]
            observed=direct_matching_count(t,subset)
            expected=a if len(subset)%2 else 0
            assert observed==expected,(t,subset,observed,expected)
        print('DIRECT_MATCHINGS',t,a)
    print('VERIFY_OK')

def four_local_states():
    vs,nei=vertices_and_neighbors(3)
    ix={v:i for i,v in enumerate(vs)}
    corners=[ix[(a,a,a)] for a in range(3)]
    # Independently extract balanced patterns with all three outer corners absent.
    balanced=[]
    roots=list(product(range(3),repeat=2))
    for absent in product(range(3),repeat=9):
        picked=[True]*27
        for prefix,a in zip(roots,absent):picked[ix[prefix+(a,)]]=False
        if all(not picked[c] for c in corners) and is_limited_dominating(picked,nei):
            balanced.append(tuple(picked))
    assert len(balanced)==2,len(balanced)
    active=[]
    for step in (1,2):
        chosen=[]
        for a,b,c in vs:
            chosen.append(b!=(a+step)%3)
        assert all(chosen[c] for c in corners)
        assert is_limited_dominating(chosen,nei)
        assert sum(chosen)==18
        active.append(tuple(chosen))
    states=balanced+active
    assert len(set(states))==4
    return states

def block_test(n, states, digits):
    vs,nei=vertices_and_neighbors(n)
    ix={u:i for i,u in enumerate(vs)}
    sel=[False]*len(vs)
    for pre,kind in zip(product(range(3),repeat=n-3),digits):
        for j,u in enumerate(product(range(3),repeat=3)):
            sel[ix[pre+u]]=states[kind][j]
    return sum(sel),is_limited_dominating(sel,nei)

if __name__=='__main__':
    states=four_local_states()
    print('FOUR_BOUNDARY_STATES_OK',len(states))
    for n in (3,4):
        cnt=0
        for digit in product(range(4),repeat=3**(n-3)):
            weight,good=block_test(n,states,digit)
            assert (weight,good)==(2*3**(n-1),True),(n,digit,weight,good)
            cnt+=1
        print('BLOCK_PRODUCTS_OK',n,cnt)
    import random
    random.seed(304)
    for n in (5,6):
        trials=25 if n==5 else 10
        for _ in range(trials):
            choices=[random.randrange(4) for _ in range(3**(n-3))]
            weight,good=block_test(n,states,choices)
            assert (weight,good)==(2*3**(n-1),True)
        print('RANDOM_BLOCK_PRODUCTS_OK',n,trials)
    print('FOUR_STATE_VERIFY_OK')
