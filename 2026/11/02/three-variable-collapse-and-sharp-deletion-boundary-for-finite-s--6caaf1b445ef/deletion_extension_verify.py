#!/usr/bin/env python3
"""Independent exhaust over every deleted point in four Steiner triple systems.
No reliance on the finite-variable refinement code or imported project modules.
"""
from itertools import combinations
from collections import Counter

def generate(n,kind):
    if kind=='binary':
        return [{a-1,b-1,(a^b)-1} for a,b in combinations(range(1,n+1),2)]
    if kind=='affine':
        return [{u,v,((-(u//3)-(v//3))%3)*3+(-(u%3)-(v%3))%3} for u,v in combinations(range(9),2)]
    if kind=='cyclic':
        return [{(x+t)%13 for x in b} for t in range(13) for b in ((0,1,4),(0,2,7))]
    raise ValueError(kind)

def main():
    specimens=[(7,'binary'),(9,'affine'),(13,'cyclic'),(15,'binary')]
    processed=0
    checked_pairs=0
    checked_thirds=0
    for n,kind in specimens:
        parent={frozenset(b) for b in generate(n,kind)}
        assert len(parent)==n*(n-1)//6
        pair_coverage=Counter(frozenset(p) for block in parent for p in combinations(block,2))
        assert len(pair_coverage)==n*(n-1)//2 and all(v==1 for v in pair_coverage.values())
        for removed in range(n):
            V=set(range(n))-{removed}
            triples={b for b in parent if removed not in b}
            pair_to_third={}
            for b in triples:
                for a,c in combinations(b,2):
                    assert frozenset((a,c)) not in pair_to_third
                    pair_to_third[frozenset((a,c))]=next(iter(b-{a,c}))
            missing={frozenset(p) for p in combinations(V,2) if frozenset(p) not in pair_to_third}
            assert len(missing)==(n-1)//2
            assert all(sum(a in e for e in missing)==1 for a in V)
            mate={a:next(iter(next(e for e in missing if a in e)-{a})) for a in V}
            nonmissing_pairs=0
            for a in V:
                for b in V:
                    cats=Counter()
                    for z in V:
                        if z==a:cat='anchor_a'
                        elif z==b:cat='anchor_b'
                        elif z==mate[a]:cat='mate_a'
                        elif z==mate[b]:cat='mate_b'
                        elif frozenset((a,b,z)) in triples and len({a,b,z})==3:cat='third'
                        else:cat='free'
                        cats[cat]+=1
                        checked_thirds+=1
                    checked_pairs+=1
                    if a==b:
                        expected=Counter({'anchor_a':1,'mate_a':1,'free':n-3})
                    elif b==mate[a]:
                        expected=Counter({'anchor_a':1,'anchor_b':1,'free':n-3})
                    else:
                        expected=Counter({'anchor_a':1,'anchor_b':1,'mate_a':1,'mate_b':1,'third':1,'free':n-6})
                        nonmissing_pairs+=1
                    assert cats==expected,(n,removed,a,b,cats,expected)
            # The explicit FO^4 separator is true exactly when a completed anchor pair
            # has at least two distinct free extensions. For this system, each such pair
            # has exactly n-6 free extensions by direct enumeration above.
            four_width_separates=nonmissing_pairs>0 and n-6>=2
            assert four_width_separates == (n>=9)
            processed+=1
        print('PARENT',n,'all',n,'punctures verified','FO4_separator',n>=9)
    print('DELETE_CHECK_PASS','punctures',processed,'anchor_pairs',checked_pairs,'third_vertices',checked_thirds)
if __name__=='__main__': main()
