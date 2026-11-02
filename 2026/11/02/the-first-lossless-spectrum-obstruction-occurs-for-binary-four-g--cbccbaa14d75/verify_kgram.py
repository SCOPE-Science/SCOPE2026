#!/usr/bin/env python3
"""Complete, independent state-space and SCC checks for binary k-gram supports."""
from collections import deque, Counter
from itertools import combinations


def debruijn(k):
    vertices=1<<(k-1)
    return vertices, [(e//2,e%vertices) for e in range(1<<k)]


def reachable_supports(k,allow_repeats):
    vertices, edges=debruijn(k)
    outgoing=[[] for _ in range(vertices)]
    for e,(a,b) in enumerate(edges):outgoing[a].append((e,b))
    q=deque((v,0) for v in range(vertices))
    seen=set(q)
    while q:
        v,mask=q.popleft()
        for e,w in outgoing[v]:
            if not allow_repeats and mask & (1<<e):continue
            nxt=(w,mask|(1<<e))
            if nxt not in seen:seen.add(nxt);q.append(nxt)
    return {mask for v,mask in seen if mask},len(seen)


def structural_feasible(k,mask):
    nv, E=debruijn(k)
    actual=[E[i] for i in range(len(E)) if mask>>i&1]
    if not actual:return False
    active={v for a,b in actual for v in (a,b)}
    reach=[1<<v for v in range(nv)]
    for a,b in actual:reach[a]|=1<<b
    for mid in range(nv):
        for v in range(nv):
            if reach[v]>>mid&1: reach[v]|=reach[mid]
    cid={};cs=[]
    for v in active:
        if v in cid:continue
        component=[w for w in active if reach[v]>>w&1 and reach[w]>>v&1]
        for w in component:cid[w]=len(cs)
        cs.append(component)
    nc=len(cs)
    if nc==1:return True
    incoming=[0]*nc;outgoing=[0]*nc;cross=0
    for a,b in actual:
        if cid[a]!=cid[b]:
            cross+=1
            outgoing[cid[a]]+=1;incoming[cid[b]]+=1
    return (cross==nc-1 and sorted(incoming)==[0]+[1]*(nc-1)
            and sorted(outgoing)==[0]+[1]*(nc-1))


def main():
    for k in (3,4):
        feasible,states=reachable_supports(k,True)
        trail,trail_states=reachable_supports(k,False)
        expected={s for s in range(1,1<<(1<<k)) if structural_feasible(k,s)}
        assert feasible==expected,(k,len(feasible),len(expected))
        assert trail<=feasible
        counts=Counter(s.bit_count() for s in feasible)
        e_counts=Counter(s.bit_count() for s in trail)
        bad=feasible-trail
        noncounts=Counter(s.bit_count() for s in bad)
        print('K',k,'FEASIBLE',len(feasible),'TRAIL',len(trail),'MUST_REPEAT',len(bad))
        print('K',k,'REACHABLE_STATES',states,'NONREPEATING_STATES',trail_states)
        print('K',k,'FEASIBLE_BY_CARD',sorted(counts.items()))
        print('K',k,'EULER_BY_CARD',sorted(e_counts.items()))
        print('K',k,'REPEAT_BY_CARD',sorted(noncounts.items()))
        if k==3:
            assert len(feasible)==len(trail)==121
            assert [counts[i] for i in range(1,9)]==[8,13,20,25,26,20,8,1]
            words=set()
            for n in range(3,11):
                for i in range(1<<n):
                    s=format(i,'0%db'%n)
                    mask=0
                    for j in range(n-2):mask|=1<<int(s[j:j+3],2)
                    words.add(mask)
            assert words==feasible
            print('K3 INDEPENDENT_WORD_ENUM',len(words),'MAX_WORD_LENGTH',10)
        else:
            assert len(feasible)==5921 and len(trail)==2611 and len(bad)==3310
            assert min(s.bit_count() for s in bad)==4
            four=sorted(s for s in bad if s.bit_count()==4)
            assert four==[sum(1<<i for i in ids) for ids in ((2,5,10,11),(4,5,10,13))]
            print('K4 FIRST_NONTRAIL_MASKS',four)
            print('K4 FIRST_NONTRAIL_SETS',[[format(i,'04b') for i in range(16) if s>>i&1] for s in four])
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
