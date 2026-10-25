"""Exact finite cross-check of minimum semitotal dominating sets on subdivided bicliques.

Uses only the Python 3 standard library; this is not an infinite-domain proof.
"""
from collections import Counter
from itertools import combinations
from math import comb


def expected_profiles(p,q):
    if (p,q)==(2,2):
        return None
    ans=Counter()
    for j in range(2,q):
        ans[(p-1,q-j,j)]+=p*comb(q,j)
    for i in range(2,p):
        ans[(p-i,q-1,i)]+=q*comb(p,i)
    return ans


def check(p,q):
    n=p+q+p*q
    neighbors=[set() for _ in range(n)]
    for i in range(p):
        for j in range(q):
            w=p+q+i*q+j
            b=p+j
            neighbors[i].add(w); neighbors[w].add(i)
            neighbors[b].add(w); neighbors[w].add(b)
    n_masks=[sum(1<<t for t in s) for s in neighbors]
    distance2=[]
    for v in range(n):
        within_two={v}|neighbors[v]
        for u in neighbors[v]:within_two.update(neighbors[u])
        within_two.discard(v)
        distance2.append(sum(1<<t for t in within_two))
    full=(1<<n)-1
    def good(mask):
        outside=full^mask
        while outside:
            bit=outside&-outside
            v=bit.bit_length()-1
            if n_masks[v]&mask==0:return False
            outside-=bit
        selected=mask
        while selected:
            bit=selected&-selected
            v=bit.bit_length()-1
            if distance2[v]&mask==0:return False
            selected-=bit
        return True
    minsets=[]
    for k in range(1,p+q+1):
        for subset in combinations(range(n),k):
            mask=sum(1<<v for v in subset)
            if good(mask):minsets.append((mask,subset))
        if minsets:break
    if (p,q)==(2,2):
        assert k==4 and len(minsets)==30,(p,q,k,len(minsets))
        independent=sum(all(not(n_masks[v]&mask) for v in subset) for mask,subset in minsets)
        assert independent==2,(p,q,independent)
    else:
        wanted=expected_profiles(p,q)
        profile=Counter((sum(v<p for v in subset),
                         sum(p<=v<p+q for v in subset),
                         sum(v>=p+q for v in subset)) for mask,subset in minsets)
        assert k==p+q-1,(p,q,k)
        assert profile==wanted,(p,q,profile,wanted)
        assert all(all(not(n_masks[v]&mask) for v in subset) for mask,subset in minsets)
        assert len(minsets)==p*(2**q-q-2)+q*(2**p-p-2)
    return k,len(minsets)

if __name__=='__main__':
    for p,q in ((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4)):
        k,c=check(p,q)
        print(f'({p},{q}): min={k}; number={c}; PASS')
