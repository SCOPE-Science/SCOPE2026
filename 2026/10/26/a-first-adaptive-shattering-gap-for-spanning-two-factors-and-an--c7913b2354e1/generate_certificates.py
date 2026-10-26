#!/usr/bin/env python3
"""Finite edge-query shattering certificates for 2-factor families."""
from functools import lru_cache
from itertools import combinations
import json
import sys


def factors(n):
    edges=list(combinations(range(n),2))
    rows=[]
    for ids in combinations(range(len(edges)),n):
        degrees=[0]*n
        for i in ids:
            u,v=edges[i];degrees[u]+=1;degrees[v]+=1
        if all(x==2 for x in degrees): rows.append(sum(1<<i for i in ids))
    return edges,rows

def analyze(n):
    edges,rows=factors(n)
    N=len(rows);q=len(edges);universe=(1<<N)-1
    ones=[sum(1<<i for i,row in enumerate(rows) if row>>j&1) for j in range(q)]
    zeros=[universe^x for x in ones]
    @lru_cache(None)
    def rank(U):
        if U.bit_count()<=1:return 0
        return max([1+min(rank(U&x),rank(U&y)) for x,y in zip(ones,zeros) if U&x and U&y] or [0])
    L=rank(universe)
    VC=0; good=[]
    for k in range(1,q+1):
        found=None
        for indices in combinations(range(q),k):
            witness={sum(((row>>j)&1)<<t for t,j in enumerate(indices)): row for row in rows}
            if len(witness)==2**k:
                found=(indices,witness);break
        if found is None:break
        VC=k;good=found
    def sorted_edges(mask):
        return [list(edges[i]) for i in range(q) if mask>>i&1]
    def tree(U,d):
        if d==0:
            assert U
            idx=(U&-U).bit_length()-1
            return {'witness_edges':sorted_edges(rows[idx])}
        for j in range(q):
            a,b=U&zeros[j], U&ones[j]
            if a and b and rank(a)>=d-1 and rank(b)>=d-1:
                return {'query':list(edges[j]),'zero':tree(a,d-1),'one':tree(b,d-1)}
        raise AssertionError('rank certificate missing')
    item={'n':n,'number_of_factors':N,'vc_dimension':VC,'littlestone_dimension':L,'vc_queries':[list(edges[j]) for j in good[0]] if VC else [],'vc_witnesses': [sorted_edges(good[1][m]) for m in range(1<<VC)] if VC else [sorted_edges(rows[0])], 'adaptive_tree':tree(universe,L)}
    print('order',n,'2-factors',N,'VC',VC,'Ldim',L,'rank states',rank.cache_info().currsize,flush=True)
    return item

if __name__=='__main__':
    obj={'format':'edge-query-two-factor-certificates-v1','description':'0 and 1 denote absence and presence of queried undirected edge; each leaf lists a spanning 2-factor witness.','cases':[analyze(n) for n in range(3,7)]}
    with open(sys.argv[1] if len(sys.argv)>1 else 'two_factor_certificates.json','w') as f:json.dump(obj,f,sort_keys=True,indent=2);f.write('\n')
