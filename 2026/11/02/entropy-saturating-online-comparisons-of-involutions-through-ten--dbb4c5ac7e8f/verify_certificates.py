#!/usr/bin/env python3
"""Independently replay finite adaptive comparison trees for involutions."""
import json
from itertools import combinations
from pathlib import Path

def via_last_element(n):
    family=[()]
    for size in range(1,n+1):
        current=[]
        # Every new largest element is fixed, or transposed with a smaller one.
        for p in family:
            current.append(p+(size-1,))
        if size>=2:
            for j in range(size-1):
                others=[v for v in range(size-1) if v!=j]
                for t in via_last_element(size-2):
                    p=[-1]*size
                    p[j]=size-1;p[size-1]=j
                    for old,label in enumerate(others):
                        p[label]=others[t[old]]
                    current.append(tuple(p))
        family=current
    return sorted(family)

def check():
    doc=json.loads(Path(__file__).with_name('adaptive_certificates.json').read_text(encoding='utf-8'))
    counts=[1,1]
    for n in range(2,11):counts.append(counts[-1]+(n-1)*counts[-2])
    for cert in doc['certificates']:
        n=cert['n'];p=via_last_element(n)
        assert len(p)==cert['concept_count']==counts[n]
        assert len(set(p))==len(p)
        assert all(sorted(q)==list(range(n)) and all(q[q[i]]==i for i in range(n)) for q in p)
        d=cert['depth'];nodes=cert['node_query_indices'];leaves=cert['leaf_witness_involution_indices'];pairs=list(combinations(range(n),2))
        assert len(nodes)==(1<<d)-1 and len(leaves)==(1<<d)
        assert all(0<=u<len(pairs) for u in nodes)
        assert len(set(leaves))==len(leaves)
        for leaf,witness in enumerate(leaves):
            assert 0<=witness<len(p)
            node=1
            for depth in range(d-1,-1,-1):
                response=(leaf>>depth)&1
                i,j=pairs[nodes[node-1]]
                assert (p[witness][i]<p[witness][j])==bool(response), (n,leaf,node)
                node=node*2+response
            assert node==(1<<d)+leaf
        assert (1<<d)<=len(p)<(1<<(d+1))
        # Independently construct an involution for each desired adjacent-descent set.
        for descent_bits in range(1<<(n-1)):
            perm=[];start=0
            for j in range(n-1):
                if not ((descent_bits>>j)&1):
                    perm.extend(range(j,start-1,-1));start=j+1
            perm.extend(range(n-1,start-1,-1))
            assert sorted(perm)==list(range(n))
            assert all(perm[perm[i]]==i for i in range(n))
            got=sum((1<<j) for j in range(n-1) if perm[j]>perm[j+1])
            assert got==descent_bits
        print('CERTIFICATE_PASS',n,'concepts',len(p),'depth',d,'nodes',len(nodes),'leaves',len(leaves),flush=True)
    print('ALL_INDEPENDENT_CHECKS_PASS',flush=True)
if __name__=='__main__':check()
