#!/usr/bin/env python3
"""Independent fixed-point census versus the exact multiplicity cutoff."""
from itertools import combinations_with_replacement
from collections import Counter
from verify_cycle_pebbles import graph,canonical_pair_class

def main():
    types=[]
    for m in range(1,5):
        for xs in combinations_with_replacement(range(3,11),m):
            if sum(xs)<=10: types.append(xs)
    checked=0;equal=0;depth=0
    by_k={}
    for k in (1,2,3):
        checked_k=0;equal_k=0
        for i,a in enumerate(types):
            for b in types[i:]:
                ca,cb=Counter(a),Counter(b)
                if k==1:want=True
                elif k==2:want=(a==(3,)) == (b==(3,))
                else:want=all(min(ca.get(n,0),k)==min(cb.get(n,0),k) for n in range(3,11))
                got,rounds,_=canonical_pair_class(graph(a),graph(b),k)
                assert got==want,(k,a,b,got,want)
                checked_k+=1;equal_k+=got;depth=max(depth,rounds)
        by_k[k]=(checked_k,equal_k)
        checked+=checked_k;equal+=equal_k
    print('CENSUS_OK graph_types=%d comparisons=%d equivalent=%d per_width=%s max_refinements=%d'%(len(types),checked,equal,by_k,depth))
if __name__=='__main__':main()
