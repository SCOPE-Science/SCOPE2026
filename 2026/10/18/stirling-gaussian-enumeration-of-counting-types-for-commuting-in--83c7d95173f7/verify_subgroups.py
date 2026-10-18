#!/usr/bin/env python3
"""Independent finite verification of C2 signature fibres for commuting involutions."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement

@lru_cache(None)
def all_subspaces(k):
    seen={frozenset([0])}; queue=[frozenset([0])]
    while queue:
        h=queue.pop()
        for v in range(1<<k):
            new=frozenset(h | {u^v for u in h})
            if new not in seen:
                seen.add(new); queue.append(new)
    return sorted(seen,key=lambda h:(len(h), tuple(sorted(h))))

def signature(k,h):
    return tuple((i,j) for i in range(k+1) for j in range(i+1,k+1)
                 if ((0 if i==0 else 1<<(i-1)) ^ (0 if j==0 else 1<<(j-1))) in h)

def all_structures(k,n):
    hs=all_subspaces(k)
    sizes=[(1<<k)//len(h) for h in hs]
    sigs=[signature(k,h) for h in hs]
    ans=[]
    counts=[0]*len(hs)
    def go(j,left):
        if j==len(hs):
            if left==0:
                fingerprint=Counter()
                for h,sig,siz,m in zip(hs,sigs,sizes,counts):
                    if m: fingerprint[sig]+=siz*m
                ans.append((tuple(sorted(fingerprint.items())),tuple(counts)))
            return
        for m in range(left//sizes[j]+1):
            counts[j]=m; go(j+1,left-sizes[j]*m)
        counts[j]=0
    go(0,n)
    return hs,ans

def main():
    for k,maxn in [(1,12),(2,12),(3,8)]:
        print('generators',k,'subgroups',len(all_subspaces(k)))
        for n in range(1,maxn+1):
            hs,st=all_structures(k,n)
            classes=defaultdict(list)
            for fp,inventory in st: classes[fp].append(inventory)
            doubles=[v for v in classes.values() if len(v)>1]
            print('n',n,'types',len(st),'fingerprints',len(classes),'collision_pairs',sum(len(v)*(len(v)-1)//2 for v in doubles))
            if k==3 and n==8:
                assert len(doubles)==1 and len(doubles[0])==2
                for inv in doubles[0]:
                    print('  witness orbit subgroup multiset',[(sorted(hs[i]),m) for i,m in enumerate(inv) if m])
            else: assert not doubles
    for k in range(1,7):
        seen={}
        for h in all_subspaces(k):
            sz=(1<<k)//len(h)
            if sz<=4:
                key=signature(k,h)
                assert key not in seen or seen[key]==h,(k,key)
                seen[key]=h
        print('rank<=2 kernel reconstruction verified for',k,'generators:',len(seen),'types')
    print('VERIFY_SUBGROUPS_OK')
if __name__=='__main__': main()
