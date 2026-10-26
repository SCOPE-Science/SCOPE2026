#!/usr/bin/env python3
"""Independent finite-extension and one-edge sensitivity checks, stdlib only."""
from itertools import product
from random import Random


def edge_masks(p, q, mask):
    return tuple((i, p + j) for i in range(p) for j in range(q)
                 if (mask >> (i*q+j)) & 1)


def independent_sets(n, edges):
    """Enumerate independent vertex subsets directly."""
    cnt = 0
    for z in range(1 << n):
        if all(not ((z >> u) & 1 and (z >> v) & 1) for u,v in edges):
            cnt += 1
    return cnt


def direct_poset_extensions(p, q, edges):
    """Count actual labelled 1-point extensions, checking transitive closure.

    No use of the ideal/filter or graph-polynomial formulas.
    """
    n=p+q
    base=[0]*(n+1)
    for u,v in edges:base[u]|=1<<v
    total=0
    for rel in product((-1,0,1),repeat=n):
        # -1=old vertex strictly below new x; +1=x strictly below old
        below=[*base]
        for i,r in enumerate(rel):
            if r==-1: below[i]|=1<<n
            elif r==1: below[n]|=1<<i
        for k in range(n+1):
            bit=1<<k
            for i in range(n+1):
                if below[i]&bit:below[i]|=below[k]
        if any((below[i]>>i)&1 for i in range(n+1)):continue
        # No new relation among the original, individually named elements.
        if any((below[i] & ((1 << n)-1)) != base[i] for i in range(n)): continue
        # Claimed positions of x must be precisely the closure positions.
        if any(((below[i]>>n)&1)!=int(rel[i]==-1) or
               ((below[n]>>i)&1)!=int(rel[i]==1)
               for i in range(n)):continue
        total+=1
    return total


def expected_count(p,q,edges):
    n=p+q
    full={(i,p+j) for i in range(p) for j in range(q)}
    return 2*independent_sets(n,edges)+independent_sets(n, full-set(edges))-(1<<p)-(1<<q)


def predicted_delta(p,q,edges,a,b):
    n=p+q; edges=set(edges)
    left=set(range(p)); right=set(range(p,n))
    na={v for u,v in edges if u==a}   # subset right
    nb={u for u,v in edges if v==b}   # subset left
    rem=(left-{a}-nb)|(right-{b}-na)
    hi=nb|na
    complement={(u,v) for u in nb for v in na if (u,v) not in edges}
    # Count sets only on the selected vertices.
    def induced_count(verts, subset_edges):
        verts=sorted(verts); m={x:i for i,x in enumerate(verts)}
        return independent_sets(len(verts),{(m[u],m[v]) for u,v in subset_edges})
    f=induced_count(rem,{(u,v) for u,v in edges if u in rem and v in rem})
    h=induced_count(hi,complement)
    return h-2*f, h, f


def check_case(p,q,mask, counters, counts):
    edges=set(edge_masks(p,q,mask)); n=p+q
    t=counts[mask]
    assert t == expected_count(p,q,edges), (p,q,mask,'type formula',t,expected_count(p,q,edges))
    counters['graph']+=1
    for a in range(p):
        for b in range(p,n):
            if (a,b) in edges: continue
            after=set(edges);after.add((a,b))
            post=counts[mask | (1 << (a*q+(b-p)))]
            delta,h,f=predicted_delta(p,q,edges,a,b)
            assert post-t==delta, (p,q,mask,a,b,'delta',post-t,delta)
            assert 1-(1<<(n-1)) <= delta <= (1<<(n-2))-2
            # Characterize both exact equality cases.
            max_case = len(edges)==p*q-1  # missing exactly (a,b)
            min_case = len(edges)==0
            assert (delta == (1<<(n-2))-2) == max_case, (p,q,mask,a,b,'upper')
            assert (delta == 1-(1<<(n-1))) == min_case, (p,q,mask,a,b,'lower')
            counters['step']+=1


def check_reduction(p,q,hm, counters):
    # H on [p]+[p..p+q); G on [p+1]+[p+1..p+1+q]
    H=set(edge_masks(p,q,hm))
    a=p; b=p+1+q; n=p+q+2
    # Remap Y vertices to the new B block.
    edges={(x,p+1+j) for x in range(p) for j in range(q) if (x,p+j) not in H}
    edges|={(x,b) for x in range(p)}
    edges|={(a,p+1+j) for j in range(q)}
    z=direct_poset_extensions(p+1,q+1,edges)
    zz=direct_poset_extensions(p+1,q+1,edges|{(a,b)})
    assert zz-z+2 == independent_sets(p+q,H), (p,q,hm,zz-z+2,independent_sets(p+q,H))
    counters['reduction']+=1


def main():
    c=dict(graph=0,step=0,reduction=0)
    for n in range(2,7):
        for p in range(1,n):
            q=n-p
            counts=[direct_poset_extensions(p,q,set(edge_masks(p,q,mask))) for mask in range(1<<(p*q))]
            for mask in range(1<<(p*q)):
                check_case(p,q,mask,c,counts)
    print('ALL_BIPARTITE_GRAPHS_UP_TO_N6_PASS graphs=%d edge_additions=%d'%(c['graph'],c['step']))
    for p,q in ((1,1),(1,2),(2,1),(2,2)):
        for mask in range(1<<(p*q)):
            check_reduction(p,q,mask,c)
    rng=Random(73019)
    for p,q in ((2,3),(3,2),(3,3)):
        for _ in range(3):
            check_reduction(p,q,rng.randrange(1<<(p*q)),c)
    print('REDUCTION_GADGET_PASS cases=%d'%c['reduction'])
    print('ALL_TESTS_PASS')
if __name__=='__main__':main()
