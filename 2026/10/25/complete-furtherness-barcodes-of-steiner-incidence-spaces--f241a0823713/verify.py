#!/usr/bin/env python3
"""Independent finite-incidence verification of furtherness barcodes.

Run with python3 verify.py. All finite models are constructed here; no input files.
"""
from itertools import combinations, product
from collections import Counter


def projective_binary(d):
    points = list(range(1,1<<d))
    blocks = sorted({tuple(sorted((x,y,x^y))) for x,y in combinations(points,2)})
    return len(points), [tuple(t-1 for t in block) for block in blocks]


def affine_plane_3():
    points=list(product(range(3),repeat=2))
    idx={pt:i for i,pt in enumerate(points)}
    blocks=set()
    for x,y in points:
        for dx,dy in [(1,0),(0,1),(1,1),(1,2)]:
            block=tuple(sorted(idx[((x+t*dx)%3,(y+t*dy)%3)] for t in range(3)))
            blocks.add(block)
    return 9,sorted(blocks)


def complete_pair_design(v):
    return v,list(combinations(range(v),2))


def check_design(v,blocks):
    k=len(blocks[0]); b=len(blocks)
    assert 2<=k<v and len(set(blocks))==b
    assert all(len(set(B))==k and all(0<=p<v for p in B) for B in blocks)
    pair_counts=Counter(tuple(sorted(pair)) for B in blocks for pair in combinations(B,2))
    assert len(pair_counts)==v*(v-1)//2 and set(pair_counts.values())=={1}
    r=(v-1)//(k-1)
    assert r*(k-1)==v-1 and b*k==v*r
    return k,b,r


def graph_persistence(v,blocks,root):
    # Reconstruct the exact finite T0 poset, principal downsets and furtherness.
    b=len(blocks)
    vertices=[('p',i) for i in range(v)]+[('B',j) for j in range(b)]
    down={('p',i):{('p',i)} for i in range(v)}
    down.update({('B',j):{('B',j)} | {('p',i) for i in B} for j,B in enumerate(blocks)})
    weight={a:len(down[a]-down[root]) for a in vertices}
    edges=[(('p',i),('B',j)) for j,B in enumerate(blocks) for i in B]
    parent={};birth={};component_birth={}; h0=[]; h1=[]
    def find(x):
        if parent[x]!=x:parent[x]=find(parent[x])
        return parent[x]
    for t in sorted(set(weight.values())):
        for a in vertices:
            if weight[a]==t:
                parent[a]=a; component_birth[a]=t
        for a,z in edges:
            if max(weight[a],weight[z])!=t:continue
            ra,rz=find(a),find(z)
            if ra==rz:
                h1.append(t)
            else:
                if (component_birth[ra],ra) <= (component_birth[rz],rz):
                    old,dead=ra,rz
                else:old,dead=rz,ra
                if component_birth[dead]<t:h0.append((component_birth[dead],t))
                parent[dead]=old
    assert len({find(x) for x in vertices})==1
    h0=Counter(h0);h1=Counter(h1)
    return weight,h0,h1


def check_case(label,v,blocks):
    k,b,r=check_design(v,blocks)
    B_star=1+k*(r-1)
    beta=b*(k-1)-v+1
    assert B_star <= b
    beta_early=(k-1)*(v-k)
    beta_late=(k-1)*(b-B_star)
    assert beta == beta_early+beta_late
    for p in range(v):
        wt,h0,h1=graph_persistence(v,blocks,('p',p))
        assert h0==Counter({(1,k):v-1})
        assert h1==Counter({k+1:beta})
        assert sum(wt[('B',j)]==k for j in range(b))==r
    for j in range(b):
        wt,h0,h1=graph_persistence(v,blocks,('B',j))
        assert h0==Counter({(1,k):v-k})
        assert h1==Counter({k:beta_early,k+1:beta_late}) if beta_late else h1==Counter({k:beta_early})
        assert sum(wt[('B',z)]==k for z in range(b))==B_star-1
    print(label,dict(v=v,k=k,r=r,b=b,early_blocks=B_star,beta=beta,early_h1=beta_early,late_h1=beta_late,roots_checked=v+b),flush=True)


def main():
    check_case('all-pairs-5',*complete_pair_design(5))
    check_case('Fano-plane',*projective_binary(3))
    check_case('affine-plane-3',*affine_plane_3())
    check_case('projective-space-3-over-2',*projective_binary(4))
    print('VERIFY_OK')

if __name__=='__main__': main()
