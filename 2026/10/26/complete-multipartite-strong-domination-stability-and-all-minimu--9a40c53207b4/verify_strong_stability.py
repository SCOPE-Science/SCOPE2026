#!/usr/bin/env python3
"""Direct subset checks of strong domination and deletion stability in multipartite graphs.

This script requires Python 3 only. Its finite checks do not constitute a proof
for arbitrary graph orders.
"""
from itertools import combinations
from functools import lru_cache


def graph(parts):
    labels = tuple(i for i, s in enumerate(parts) for _ in range(s))
    n = len(labels)
    adj = tuple(sum(1 << j for j in range(n) if labels[i] != labels[j]) for i in range(n))
    return labels, adj


def strong_domination_number_direct(adj, remaining):
    n=len(adj)
    selected_indices=[i for i in range(n) if (remaining>>i)&1]
    if not selected_indices:
        return 0
    degrees={i:(adj[i]&remaining).bit_count() for i in selected_indices}
    for k in range(1,len(selected_indices)+1):
        for chosen in combinations(selected_indices,k):
            mask=sum(1<<i for i in chosen)
            ok=True
            for j in selected_indices:
                if (mask>>j)&1: continue
                if not any(((adj[j]>>i)&1) and degrees[i]>=degrees[j] for i in chosen):
                    ok=False; break
            if ok:return k
    return len(selected_indices)


def predicted_gamma(parts):
    live=tuple(sorted(s for s in parts if s>0))
    if not live:return 0
    m=live[0]
    if m==1:return 1
    if len(live)==1:return m
    return 2 if live.count(m)>1 else m


def predicted_stability(parts):
    p=sorted(parts)
    if p==[1]*len(p):return None
    k=p.count(1)
    if k:return k
    return 2 if p[0]==3 and p.count(3)>1 else 1


def predicted_min_changing_deletions(parts,labels):
    n=len(labels);m=min(parts);count_min=parts.count(m)
    crit=[]
    if m==1:
        k=parts.count(1)
        singleton_mask=sum(1<<i for i,c in enumerate(labels) if parts[c]==1)
        return {singleton_mask}
    if m==3 and count_min>1:
        return {sum(1<<i for i in pair) for c,s in enumerate(parts) if s==3
                for pair in combinations([i for i,v in enumerate(labels) if v==c],2)}
    for i,c in enumerate(labels):
        if m==2:
            if parts[c]==2:crit.append(1<<i)
        elif count_min==1:
            if parts[c] in (m,m+1):crit.append(1<<i)
        else:
            if parts[c]==m:crit.append(1<<i)
    return set(crit)


def evaluate(parts):
    labels,adj=graph(parts)
    n=len(labels)
    full=(1<<n)-1
    base=strong_domination_number_direct(adj,full)
    assert base==predicted_gamma(parts),(parts,'base',base,predicted_gamma(parts))
    target=predicted_stability(parts)
    candidate=set()
    if target is None:
        for delete in range(1,full):
            got=strong_domination_number_direct(adj,full^delete)
            assert got==base,(parts,delete,got)
        return 1
    for k in range(1,target+1):
        for comb in combinations(range(n),k):
            deletion=sum(1<<i for i in comb)
            actual=strong_domination_number_direct(adj,full^deletion)
            if k<target:
                assert actual==base,(parts,'early deletion',deletion,actual,base)
            elif actual!=base:candidate.add(deletion)
    expected=predicted_min_changing_deletions(parts,labels)
    assert candidate==expected,(parts,'min deletion families',sorted(candidate),sorted(expected))
    return 1


def partitions(total,start=1):
    if total==0:
        yield ()
        return
    for p in range(start,total+1):
        for tail in partitions(total-p,p):
            yield (p,)+tail


def main():
    tests=0
    for total in range(3,12):
        for parts in partitions(total):
            if len(parts)<2:continue
            evaluate(parts)
            tests+=1
    print('DIRECT_BRUTE_FORCE_PART_SIZE_PROFILES',tests)
    print('DIRECT_MINIMAL_DELETION_SETS_OK')
    print('VERIFY_OK')

if __name__=='__main__': main()
