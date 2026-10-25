#!/usr/bin/env python3
"""Independent exact checks for minimum paired domination in triangular graphs."""
from itertools import combinations
from collections import Counter,deque
from math import factorial

def perfect_matching_in_selected_line_graph(S):
    if not S: return True
    e=S[0]
    for j in range(1,len(S)):
        if set(e)&set(S[j]) and perfect_matching_in_selected_line_graph(S[1:j]+S[j+1:]):
            return True
    return False

def is_pair_dom(S,n):
    used=set(x for e in S for x in e)
    return n-len(used)<=1 and perfect_matching_in_selected_line_graph(S)

def brute(n,k):
    E=list(combinations(range(n),2)); result=[]
    for sel in combinations(E,2*k):
        if is_pair_dom(sel,n):result.append(frozenset(sel))
    return result

def canon(h,blocks):
    return h,tuple(sorted((c,tuple(sorted((a,b)))) for c,a,b in blocks))

def all_states(n):
    k=(n-1)//3
    init=canon(n-1,[(3*i,3*i+1,3*i+2) for i in range(k)])
    q=[init]; visited={init}
    for x in q:
        for y in neighbors(x):
            if y not in visited: visited.add(y);q.append(y)
    return q

def neighbors(state):
    hole,blocks=state
    for i,(center,(a,b)) in enumerate(blocks):
        for leaf,other in ((a,b),(b,a)):
            # Move unused label into one leaf slot, same center.
            B=list(blocks);B[i]=(center,tuple(sorted((hole,other))))
            yield (leaf, tuple(sorted(B)))
            # Exchange a leaf with the center label, same hole.
            B=list(blocks);B[i]=(leaf,tuple(sorted((center,other))))
            yield (hole,tuple(sorted(B)))

def to_edge_set(state):
    return frozenset(tuple(sorted((c,x))) for c,(a,b) in state[1] for x in (a,b))

if __name__=='__main__':
    for n in (4,7):
        k=(n-1)//3
        br=set(brute(n,k))
        st=all_states(n)
        ss={to_edge_set(s) for s in st}
        assert br==ss, (n,len(br),len(ss))
        deg=Counter(len(set(neighbors(s))) for s in st)
        assert deg=={4*k:len(st)},(n,deg)
        print('brute',n,'minimum_size',2*k,'configuration_count',len(br),'degrees',dict(deg),'formula',factorial(n)//(2**k*factorial(k)))
    for n in (4,7,10):
        k=(n-1)//3
        q=all_states(n)
        assert len(q)==factorial(n)//(2**k*factorial(k)),(n,len(q))
        from_root={q[0]:0}
        bfs=deque([q[0]])
        while bfs:
            x=bfs.popleft()
            for y in neighbors(x):
                if y not in from_root:
                    from_root[y]=from_root[x]+1;bfs.append(y)
        assert len(from_root)==len(q)
        hist=dict(sorted(Counter(from_root.values()).items()))
        edge_count=2*k*len(q)
        print('slide',n,'states',len(q),'edges',edge_count,'degree',4*k,'diameter',max(from_root.values()),'distance_hist',hist)
