"""Definition-level coalition-partition enumeration for leaf coronas.
Stdlib only. Each vertex i has one private pendant vertex n+i.
"""
from itertools import combinations
from math import comb

def restricted_growth_strings(N):
    a=[0]*N
    def rec(i,k):
        if i==N:
            yield tuple(a)
        else:
            for v in range(k+1):
                a[i]=v
                yield from rec(i+1,max(k,v+1))
    yield from rec(1,1)

def is_dominating_pendant_pairs(labels,n,p):
    return all(labels[i] in p or labels[n+i] in p for i in range(n))

def is_c_partition(labels,n):
    k=max(labels)+1
    full=set(range(k))
    # Corona of order >= 4 has no singleton dominating vertex.
    if any(is_dominating_pendant_pairs(labels,n,{i}) for i in full):
        return False
    return all(any(is_dominating_pendant_pairs(labels,n,{i,j})
                   for j in full if j!=i) for i in full)

def support_edges(labels,n):
    return {tuple(sorted((labels[i],labels[n+i]))) for i in range(n)}

def canon_edges(edges,k):
    from itertools import permutations
    return min(tuple(sorted(tuple(sorted((perm[a],perm[b])))
                            for a,b in edges)) for perm in permutations(range(k)))

def expected_4(n):
    s2=2**n-2
    s3=3**n-3*2**n+3
    s4=4**n-4*3**n+6*2**n-4
    return (2**n * (s2 + 4*s3 + s4))//8

print('VERIFY_OK')
T={}
for n in range(2,6):
    hist={}
    good_4=[]
    total=0
    for a in restricted_growth_strings(2*n):
        total+=1
        if is_c_partition(a,n):
            k=max(a)+1
            hist[k]=hist.get(k,0)+1
            if k==4:
                good_4.append(a)
    assert max(hist)==4,(n,hist)
    assert len(good_4)==expected_4(n),(n,len(good_4),expected_4(n))
    types={}
    for a in good_4:
        H=canon_edges(support_edges(a,n),4)
        types[H]=types.get(H,0)+1
    expected_types= {
        2: (2**n*(2**n-2))//8,
        3: (2**n*(3**n-3*2**n+3))//2,
        4: (2**n*(4**n-4*3**n+6*2**n-4))//8
    }
    assert len(types)==len([m for m,num in expected_types.items() if num])
    for H,cnt in types.items():
        assert cnt==expected_types[len(H)],(n,H,cnt,expected_types[len(H)])
    print(f'n={n}: partitions_checked={total}, max_coalition_blocks=4, optimal_partitions={len(good_4)}, supporting_edge_type_counts={dict(sorted((len(H),ct) for H,ct in types.items()))}')
    T[n]=len(good_4)

for n in range(2,51):
    # Explicit four-part construction. n pendant pairs split into two nonempty classes.
    p=[0]*(2*n)
    for i in range(n):
        if i==0:
            p[i],p[n+i]=0,1
        else:
            p[i],p[n+i]=2,3
    assert len(set(p))==4
    assert is_c_partition(p,n)

# Validate actual graph domination equivalence for small arbitrary base graphs.
def is_dominating_actual(labels,base_edges,n,parts):
    chosen={v for v in range(2*n) if labels[v] in parts}
    adj=[set() for _ in range(2*n)]
    for i,j in base_edges:
        adj[i].add(j);adj[j].add(i)
    for i in range(n):
        adj[i].add(n+i);adj[n+i].add(i)
    return all(v in chosen or (adj[v]&chosen) for v in range(2*n))
for n in range(2,6):
    allpairs=list(combinations(range(n),2))
    for es in ([],allpairs,[(i,i+1) for i in range(n-1)]):
        for a in restricted_growth_strings(2*n):
            for x in range(max(a)+1):
                for y in range(x,max(a)+1):
                    P={x,y}
                    assert is_dominating_actual(a,es,n,P)==is_dominating_pendant_pairs(a,n,P)
print('all direct graph-domination equivalence checks passed for empty, complete and path bases n=2..5')
print('four-block construction checked through n=50')
