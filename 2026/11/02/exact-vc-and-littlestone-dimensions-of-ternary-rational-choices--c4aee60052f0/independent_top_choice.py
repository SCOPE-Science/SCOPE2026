#!/usr/bin/env python3
"""Second exact implementation: permutations are worst-to-best label orders.
Membership uses the index of a candidate in an order, rather than rank vectors.
"""
import itertools,functools,math

def check(n):
    orders=list(itertools.permutations(range(n)))
    # Equivalent hypothesis orders differ only in the last two entries of the
    # worst-to-best listing; retain one per equivalence class.
    orders=[o for o in orders if o[0]<o[1]]
    index=[{x:i for i,x in enumerate(o)} for o in orders]
    q=[(menu,winner) for menu in itertools.combinations(range(n),3) for winner in menu]
    masks=[sum(1<<j for j,pos in enumerate(index) if pos[winner]>max(pos[y] for y in menu if y!=winner)) for menu,winner in q]
    full=(1<<len(orders))-1
    # All potential shattered supports with at least one query can be relabeled
    # so that the first query belongs to them.
    target=n-1; nodes=0; possible=False
    def find(k,blocks,d):
        nonlocal nodes,possible
        nodes+=1
        if d==target:
            possible=True;return
        for j in range(k,len(q)):
            new=[]
            for S in blocks:
                a=S&masks[j]
                if a==0 or a==S:break
                new.extend((a,S^a))
            else:
                find(j+1,new,d+1)
                if possible:return
    # q[0] is (menu=(0,1,2), winner=0): transitive under S_n.
    find(1,[masks[0],full^masks[0]],1)
    assert not possible
    # Lower bound uses all five alternatives except a fixed anchor pair.
    lower=[masks[q.index(((0,1,x),x))] for x in range(2,n)]
    traces={tuple(int(z>>j&1) for z in lower) for j in range(len(orders))}
    assert len(traces)==2**(n-2)
    expected_ld={3:1,4:3,5:5,6:7,7:10}[n]
    # Upper bound: each root has exactly n!/6 distinct positive hypotheses.
    assert all(m.bit_count()==math.factorial(n)//6 for m in masks)
    assert math.factorial(n)//6 <2**expected_ld
    if n<=6:
        @functools.lru_cache(None)
        def can(S,d):
            if d==0:return True
            if S.bit_count()<2**d:return False
            return any(can(S&v,d-1) and can(S^ (S&v),d-1)
                       for v in masks if min((S&v).bit_count(),(S^ (S&v)).bit_count())>=2**(d-1))
        assert can(full,expected_ld)
    print('INDEPENDENT_PASS',n,'concepts',len(orders),'queries',len(q),'VC',n-2,
          'LD_upper',expected_ld,'VC_search_nodes',nodes,flush=True)

for n in range(3,8):check(n)
