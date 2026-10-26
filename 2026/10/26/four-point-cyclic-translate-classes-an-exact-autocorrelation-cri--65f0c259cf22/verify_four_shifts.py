"""Reproducible exact finite checks for four-point cyclic translate families.
No external libraries. Run: python3 verify_four_shifts.py
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter

def class_info(n, A):
    A=frozenset(A)
    translates=tuple(frozenset((a+c)%n for a in A) for c in range(n))
    concepts=tuple(sorted(set(translates),key=lambda x:tuple(sorted(x))))
    period_count=n//len(concepts)
    overlaps=[len(A & {(a+t)%n for a in A}) for t in range(1,n)]
    if period_count==4:
        pred=1
    elif period_count==2:
        pred=2
    else:
        assert period_count==1
        pred=3 if 2 in overlaps else 2
    return concepts,period_count,overlaps,pred

def exact_ldim(n, concepts):
    masks=[]
    for x in range(n):
        masks.append(sum(1<<i for i,C in enumerate(concepts) if x in C))
    @lru_cache(None)
    def can(s, depth):
        if depth==0:return True
        if s.bit_count() < (1<<depth):return False
        for m in masks:
            a=s&m; b=s&~m
            if a.bit_count() < (1<<(depth-1)) or b.bit_count() < (1<<(depth-1)):continue
            if can(a, depth-1) and can(b, depth-1):return True
        return False
    full=(1<<len(concepts))-1
    return max(d for d in range(4) if can(full,d))

def vc(n, concepts):
    for k in range(4,0,-1):
        for points in combinations(range(n), k):
            patterns={tuple(x in C for x in points) for C in concepts}
            if len(patterns)==2**k:return k
    return 0

def witness(n, A):
    concepts,period,overlap,pred=class_info(n,A)
    masks=[sum(1<<i for i,C in enumerate(concepts) if x in C) for x in range(n)]
    @lru_cache(None)
    def make(s, depth):
        if depth==0:
            return {'centers_representative': min(i for i in range(len(concepts)) if (s>>i)&1)}
        for x,m in enumerate(masks):
            pos=s&m;neg=s&~m
            if pos.bit_count()<1<<(depth-1) or neg.bit_count()<1<<(depth-1):continue
            l=make(neg,depth-1);r=make(pos,depth-1)
            if l is not None and r is not None:
                return {'query':x,'zero':l,'one':r}
        return None
    tree=make((1<<len(concepts))-1,pred)
    assert tree
    leaves=0
    def verify(t,requirements):
        nonlocal leaves
        if 'query' not in t:
            i=t['centers_representative']
            assert all((x in concepts[i])==bool(label) for x,label in requirements)
            leaves+=1
        else:
            x=t['query'];verify(t['zero'],requirements+[(x,0)]);verify(t['one'],requirements+[(x,1)])
    verify(tree,[])
    assert leaves==2**pred
    return {'n':n,'A':sorted(A),'period_orbit_size':period,'ldim':pred,'vc':vc(n,concepts),'tree':tree,'leaves':leaves}

def main():
    total=0;counts=Counter()
    for n in range(8,21):
        for A in combinations(range(n),4):
            concepts,period,overlap,pred=class_info(n,A)
            got=exact_ldim(n,concepts)
            assert got==pred,(n,A,period,overlap,pred,got)
            total+=1;counts[(n,pred)]+=1
        print('n',n,'verified',sum(counts[(n,k)] for k in (1,2,3)),'counts',tuple(counts[(n,k)] for k in (1,2,3)),flush=True)
    print('EXHAUSTIVE_OK',total,'input sets')
    for n,A in [(8,(0,1,2,3)),(13,(0,1,3,9)),(15,(0,1,3,7)),(15,(0,1,2,3)),(16,(0,4,8,12)),(10,(0,1,5,6)),(9,(0,1,3,6))]:
        print('WITNESS',witness(n,A))
    print('ALL_CHECKS_OK')
if __name__=='__main__':main()
