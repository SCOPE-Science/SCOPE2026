"""Finite certificate for exact VC dimension of binary Hamming distance-2 shells.

Run: python verify_spheres.py (requires networkx 3.x for graph isomorphism).
All finite kernels are exhaustive; the mathematical reduction is in RESULT.md.
"""
from itertools import combinations
import networkx as nx


def graph_types(max_edges=6):
    current=[(0,())]
    counts={0:1}
    for k in range(1,max_edges+1):
        seen={}
        new=[]
        for n,edges in current:
            additions=list(combinations(range(n),2)) + [(i,n) for i in range(n)] + [(n,n+1)]
            for a,b in additions:
                if (a,b) in edges:
                    continue
                m=max(n,b+1)
                E=tuple(sorted(edges+((a,b),)))
                H=nx.Graph()
                H.add_nodes_from(range(m))
                H.add_edges_from(E)
                key=(m,tuple(sorted(dict(H.degree()).values())),
                     tuple(sorted(len(C) for C in nx.connected_components(H))))
                bucket=seen.setdefault(key,[])
                if any(nx.is_isomorphic(H,T) for T in bucket):
                    continue
                bucket.append(H)
                new.append((m,E))
        current=new
        counts[k]=len(current)
    return counts,current


def kernel_traces(edges,n,extra=4):
    """Every nonzero trace from ANY ambient dimension appears here.

    Centers of weights 2 and 4 suffice, and weight-zero center
    supplies the full trace. Empty trace is granted without restriction.
    """
    k=len(edges)
    masks={0,(1<<k)-1}
    for a in range(5):
        for R in combinations(range(n),a):
            RR=set(R)
            for weight in (2,4):
                if not 0<=weight-a<=extra:
                    continue
                target=weight//2
                masks.add(sum(1<<j for j,(u,v) in enumerate(edges)
                              if int(u in RR)+int(v in RR)==target))
    return masks


def exact_traces(d,edges):
    out=set()
    for c in range(1<<d):
        out.add(sum(1<<j for j,(a,b) in enumerate(edges)
                    if (c ^ (1<<a) ^ (1<<b)).bit_count()==2))
    return out


def run():
    counts,types=graph_types(6)
    assert counts=={0:1,1:1,2:2,3:5,4:11,5:26,6:68},counts
    best=0
    histogram={}
    for n,edges in types:
        tr=kernel_traces(edges,n)
        best=max(best,len(tr))
        histogram[len(tr)]=histogram.get(len(tr),0)+1
        assert len(tr)<64,(n,edges)
    print('SIX_EDGE_KERNEL', 'unlabeled_graphs',len(types),
          'maximum_patterns',best,'histogram',sorted(histogram.items()),'PASS')
    witness_by_d={2:1,3:2,4:2,5:3,6:4}
    for d,target in witness_by_d.items():
        vertices=list(combinations(range(d),2))
        witness=next((F for F in combinations(vertices,target)
                      if len(exact_traces(d,F))==(1<<target)),None)
        assert witness is not None,(d,target)
        if target+1<=len(vertices):
            checked=0
            for F in combinations(vertices,target+1):
                assert len(exact_traces(d,F))<(1<<(target+1)),(d,F)
                checked+=1
        else:checked=0
        print('SMALL',d,'VC',target,'no_larger_sets',checked,'witness',witness,'PASS')
    for d in range(7,11):
        F=tuple((0,i) for i in range(1,6))
        tr=exact_traces(d,F)
        assert len(tr)==32,(d,len(tr))
        print('STAR_WITNESS',d,'patterns',len(tr),'PASS')
    print('VERIFY_OK graph_isomorphism_kernel=PASS small_cases=PASS all_dimension_upper=REDUCTION star_lower=PASS')

if __name__=='__main__':run()
