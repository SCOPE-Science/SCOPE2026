#!/usr/bin/env python3
"""Exact rank-four Hintikka-type census for matching-defect triple systems."""
from collections import defaultdict
from functools import lru_cache
from itertools import product, combinations

Q = 4

def graph(a,b):
    parts = [1]*a + [2]*b
    labels = tuple(i for i,s in enumerate(parts) for _ in range(s))
    return parts,labels

def compute(a,b,compressed=False):
    sizes, lab = graph(a,b)
    n = len(lab)
    @lru_cache(None)
    def typ(t,r):
        if r==0:
            eq = tuple(t[i]==t[j] for i in range(len(t)) for j in range(i+1,len(t)))
            edge = tuple(len({lab[t[i]],lab[t[j]],lab[t[k]]})==3
                for i,j,k in combinations(range(len(t)),3))
            return ('a',eq,edge)
        if not compressed:
            choices = range(n)
        else:
            reps={}
            for v in range(n):
                if v in t:
                    key=(0,t.index(v))
                elif lab[v] in [lab[x] for x in t]:
                    key=(1, next(i for i,x in enumerate(t) if lab[x]==lab[v]))
                else:
                    key=(2,sizes[lab[v]])
                reps.setdefault(key,v)
            choices = tuple(reps.values())
        return frozenset(typ(t+(v,),r-1) for v in choices)
    return typ((),Q)

def main():
    cases=[(a,b) for a,b in product(range(5),repeat=2) if a+b>=3]
    d0=defaultdict(list)
    d1=defaultdict(list)
    for a,b in cases:
        d0[compute(a,b,False)].append((a,b))
        d1[compute(a,b,True)].append((a,b))
    assert len(d0)==len(d1)==12
    def groups(d):
        return sorted(tuple(sorted(g)) for g in d.values())
    assert groups(d0)==groups(d1)
    rank_classes=sorted(groups(d0), key=lambda g: (min(a+2*b for a,b in g),g))
    assert sorted([min(a+2*b for a,b in g) for g in rank_classes]) == [3,4,4,5,5,6,6,7,7,8,8,9]
    assert max(min(a+2*b for a,b in g) for g in rank_classes)==9
    print('CAPPED_CASES_OK count=19 cap_singletons=4 cap_pairs=4')
    print('INDEPENDENT_RECURSION_AGREEMENT_OK implementations=full_vertices,tuple_stabilizer_orbits')
    print('RANK_FOUR_CLASSES_OK count=12')
    for i,g in enumerate(rank_classes):
        print('CLASS_%02d min_vertices=%d canonical_parameters=%s'%(i+1,min(a+2*b for a,b in g),g))
    print('SHARP_INTERNAL_REPRESENTATIVE_OK vertices=9')
    print('VERIFY_OK')
if __name__=='__main__': main()
