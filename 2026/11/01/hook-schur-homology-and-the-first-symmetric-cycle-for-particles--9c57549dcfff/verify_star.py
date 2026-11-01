"""Finite checks for homology characters of configurations on a star graph.

Only Python's standard library is needed. The cubical count is independent
of the polynomial-chain computation used in the proof.
"""
from itertools import combinations, permutations
from math import comb


def representative(cycle_lengths):
    m=sum(cycle_lengths)
    p=list(range(m)); v=0
    for c in cycle_lengths:
        for k in range(c): p[v+k]=v+(k+1)%c
        v+=c
    return tuple(p)


def partition_lists(n, low=1):
    if not n:
        yield ()
        return
    for k in range(low,n+1):
        for rest in partition_lists(n-k,k):
            yield (k,)+rest


def complete_homogeneous_trace(m, n, sigma):
    cycles=[]; unseen=set(range(m))
    while unseen:
        a=min(unseen); b=a; sz=0
        while b in unseen:
            unseen.remove(b); sz+=1; b=sigma[b]
        assert b==a
        cycles.append(sz)
    coeff=[0]*(n+1); coeff[0]=1
    for c in cycles:
        for j in range(c,n+1): coeff[j]+=coeff[j-c]
    return coeff


def algebra_character(m,n,sigma):
    fixed=sum(i==sigma[i] for i in range(m))
    h=complete_homogeneous_trace(m,n,sigma)
    return (fixed-1)*h[n-1]-h[n]+1


def cubical_character(m,n,sigma):
    # Subdivide every leg into n+1 edges (satisfying Abrams' sufficient conditions).
    L=n+1
    # a vertex is represented by (-1,0) at the center, or (arm, depth).
    vertices=[(-1,0)]+[(a,r) for a in range(m) for r in range(1,L+1)]
    vi={v:i for i,v in enumerate(vertices)}
    edges=[(a,r) for a in range(m) for r in range(1,L+1)]
    num_v=len(vertices); num=num_v+len(edges)
    # closures of selected cells, as vertex-index bit sets
    atom_masks=[]
    for v in vertices:atom_masks.append(1<<vi[v])
    for a,r in edges:
        left=(-1,0) if r==1 else (a,r-1)
        atom_masks.append((1<<vi[left])|(1<<vi[(a,r)]))
    vmap=[vi[(-1,0)] if a==-1 else vi[(sigma[a],r)] for a,r in vertices]
    emap=[edges.index((sigma[a],r)) for a,r in edges]
    amap=vmap+[num_v+j for j in emap]
    # Count the alternating signed trace of sigma on independent-closure cubical cells.
    contributions=[0]*(n+1)
    counts=[0]*(n+1)
    selected=[]
    def rec(start, used, dim):
        if len(selected)==n:
            counts[dim]+=1
            mapped=tuple(sorted(amap[k] for k in selected))
            if mapped!=tuple(selected): return
            chosen_edges=[k-num_v for k in selected if k>=num_v]
            images=[emap[k] for k in chosen_edges]
            inversions=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
            contributions[dim]+=(-1)**inversions
            return
        for j in range(start,num-(n-len(selected))+1):
            b=atom_masks[j]
            if b & used: continue
            selected.append(j)
            rec(j+1,used|b,dim+(j>=num_v))
            selected.pop()
    rec(0,0,0)
    lef=sum((-1)**d*x for d,x in enumerate(contributions))
    return 1-lef, counts, contributions


def main():
    combos=[(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(4,5),(5,2),(5,3),(5,4)]
    for m,n in combos:
        for typ in partition_lists(m):
            sig=representative(typ)
            actual,counts,traces=cubical_character(m,n,sig)
            expected=algebra_character(m,n,sig)
            assert actual==expected,(m,n,typ,actual,expected)
        rank=(m-1)*comb(m+n-2,n-1)-comb(m+n-1,n)+1
        print('m=%d n=%d characters verified on %d conjugacy types; rank=%d; cubical cells=%s' % (m,n,len(list(partition_lists(m))),rank,counts),flush=True)
    print('VERIFY_OK')

if __name__=='__main__':main()
