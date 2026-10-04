#!/usr/bin/env python3
from itertools import product
from collections import defaultdict


def edges_of_mask(n, mask):
    pairs=[]
    bit=0
    for i in range(n):
        for j in range(i+1,n):
            if (mask>>bit)&1:
                pairs.append((i,j))
            bit += 1
    return pairs


def edge_mask_from_pairs(n, edges):
    em=0; bit=0; S=set(edges)
    for i in range(n):
        for j in range(i+1,n):
            if (i,j) in S or (j,i) in S:
                em |= 1<<bit
            bit += 1
    return em


def d_from_edge_mask(n, em, i, j):
    if i==j: return 0
    if i>j: i,j=j,i
    bit=0
    for a in range(n):
        for b in range(a+1,n):
            if a==i and b==j:
                return 1 if ((em>>bit)&1) else 2
            bit += 1
    raise AssertionError


def katetov_poly_direct(n, em):
    out=defaultdict(int)
    for f0 in product((1,2,3), repeat=n):
        ok=True
        for i in range(n):
            for j in range(i+1,n):
                d=d_from_edge_mask(n,em,i,j)
                if not (abs(f0[i]-f0[j]) <= d <= f0[i]+f0[j]):
                    ok=False; break
            if not ok: break
        if ok:
            out[(f0.count(1),f0.count(2),f0.count(3))] += 1
    return dict(out)


def components_after_delete(n, em, delete_mask):
    alive=[v for v in range(n) if not ((delete_mask>>v)&1)]
    if not alive: return []
    adj=[[] for _ in range(n)]
    for i,j in edges_of_mask(n,em):
        if not ((delete_mask>>i)&1) and not ((delete_mask>>j)&1):
            adj[i].append(j); adj[j].append(i)
    seen=set(); comps=[]
    for s in alive:
        if s in seen: continue
        stack=[s]; seen.add(s); comp=[]
        while stack:
            u=stack.pop(); comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        comps.append(comp)
    return comps


def katetov_poly_component_formula(n, em):
    # dictionary keyed by (#1,#2,#3)
    ans=defaultdict(int)
    for Z in range(1<<n):
        zsize=Z.bit_count()
        # multiply product over components (x^|C| + z^|C|)
        poly={(0,zsize,0):1}
        for C in components_after_delete(n,em,Z):
            s=len(C)
            nxt=defaultdict(int)
            for (a,b,c),coef in poly.items():
                nxt[(a+s,b,c)] += coef
                nxt[(a,b,c+s)] += coef
            poly=dict(nxt)
        for k,v in poly.items(): ans[k]+=v
    return dict(ans)


def wr_count_formula(n, em):
    return sum(1 << len(components_after_delete(n,em,Z)) for Z in range(1<<n))


def scalar(poly):
    return sum(poly.values())

# Exhaust all labeled graph metrics through 5 vertices and compare the direct
# Katetov inequalities to the component/Widom--Rowlinson formula.
checked=0
for n in range(0,6):
    m=n*(n-1)//2
    vals=[]
    for em in range(1<<m):
        pd=katetov_poly_direct(n,em)
        pc=katetov_poly_component_formula(n,em)
        assert pd==pc, (n,em,pd,pc)
        c=scalar(pd)
        assert c==wr_count_formula(n,em)
        vals.append(c); checked += 1
    assert min(vals)==2**(n+1)-1 if n else min(vals)==1
    assert max(vals)==3**n
    # for n>=1, complete and edgeless graphs are the unique extrema (they coincide for n=1)
    if n>=2:
        assert vals.count(min(vals))==1, (n,'min multiplicity',vals.count(min(vals)))
        assert vals.count(max(vals))==1, (n,'max multiplicity',vals.count(max(vals)))

# Independently test all 6-vertex graphs at the scalar level using the local forbidden-edge mask.
n=6
m=n*(n-1)//2
assign_forbidden=[]
for f0 in product((1,2,3), repeat=n):
    forb=0; bit=0
    for i in range(n):
        for j in range(i+1,n):
            if {f0[i],f0[j]}=={1,3}:
                forb |= 1<<bit
            bit += 1
    assign_forbidden.append(forb)
vals6=[]
for em in range(1<<m):
    direct=sum(1 for forb in assign_forbidden if not (forb & em))
    formula=wr_count_formula(n,em)
    assert direct==formula, (em,direct,formula)
    vals6.append(direct)
assert min(vals6)==2**7-1 and vals6.count(min(vals6))==1
assert max(vals6)==3**6 and vals6.count(max(vals6))==1

# Samples: empty graph, complete graph, paths.
def path_mask(n):
    return edge_mask_from_pairs(n, [(i,i+1) for i in range(n-1)])
path_counts=[wr_count_formula(n,path_mask(n)) for n in range(0,9)]
assert path_counts==[1,3,7,17,41,99,239,577,1393], path_counts

print('all_graph_metrics_poly_checked_n_le_5', checked)
print('all_6_vertex_graph_metrics_scalar_checked', 1<<15)
print('path_counts_n_0_to_8', path_counts)
print('extremes_n_6', min(vals6), max(vals6))
print('VERIFY_OK')
