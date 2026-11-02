#!/usr/bin/env python3
"""Direct edge-subset verification for perfect forests in complete bipartite graphs.
Python 3; no third-party packages."""
from functools import lru_cache
from math import comb

@lru_cache(maxsize=None)
def formula_component_counts(a,b):
    """EGF coefficient via distinguished-A-vertex decomposition.
    Keys are component counts; vertex labels within each shore are distinguished."""
    if a+b==0:
        return {0:1}
    if min(a,b)==0:
        return {}
    ans={}
    def add(mult,aa,bb):
        for c,v in formula_component_counts(aa,bb).items():
            ans[c+1]=ans.get(c+1,0)+mult*v
    # A distinguished vertex is the center of an odd star.
    for k in range(1,b+1,2):
        add(comb(b,k),a-1,b-k)
    # Or it is a leaf of a B-centered odd star.
    for k in range(1,a+1,2):
        add(b*comb(a-1,k-1),a-k,b-1)
    # K_2 was counted in both orientations.
    add(-b,a-1,b-1)
    assert all(v>=0 for v in ans.values())
    return {c:v for c,v in ans.items() if v}

def direct_edge_subsets(a,b):
    """Independently tests every edge subset, foresthood, odd degrees and induced components."""
    n=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    adj_all=set(edges)
    out={}
    for mask in range(1<<len(edges)):
        parent=list(range(n))
        rank=[0]*n
        degree=[0]*n
        chosen=set()
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        good=True
        for j,(u,v) in enumerate(edges):
            if (mask>>j)&1:
                degree[u]+=1; degree[v]+=1
                chosen.add((u,v))
                ru,rv=find(u),find(v)
                if ru==rv:
                    good=False; break
                if rank[ru]<rank[rv]:ru,rv=rv,ru
                parent[rv]=ru
                if rank[ru]==rank[rv]:rank[ru]+=1
        if not good or any((d&1)==0 for d in degree):continue
        for u,v in adj_all:
            if find(u)==find(v) and (u,v) not in chosen:
                good=False;break
        if good:
            c=len({find(i) for i in range(n)})
            out[c]=out.get(c,0)+1
    return out

def support(a,b):
    if (a+b)%2:return set()
    if a>b:a,b=b,a
    return set(range(1 if a==1 else 2+(a%2),a+1,2))

if __name__=='__main__':
    direct_cases=0
    edge_subset_tests=0
    for a in range(1,5):
        for b in range(a,9):
            if a*b>16:continue
            actual=direct_edge_subsets(a,b)
            expected=formula_component_counts(a,b)
            assert actual==expected,(a,b,actual,expected)
            direct_cases+=1
            edge_subset_tests+=2**(a*b)
    support_cases=0
    for a in range(1,16):
        for b in range(a,20):
            actual=set(formula_component_counts(a,b))
            expected=support(a,b)
            assert actual==expected,(a,b,actual,expected)
            support_cases+=1
    print(f'VERIFY_OK direct_graphs={direct_cases} edge_subsets={edge_subset_tests} support_pairs={support_cases}')
    for a,b in [(2,6),(3,5),(4,4),(4,6),(5,5),(6,6)]:
        print(f'K_{{{a},{b}}}: '+str({a+b-c:v for c,v in sorted(formula_component_counts(a,b).items())}))
