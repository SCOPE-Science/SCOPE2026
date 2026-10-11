#!/usr/bin/env python3
from itertools import product, combinations


def all_faces(facets):
    faces={frozenset()}
    for F in facets:
        F=tuple(F)
        for j in range(1,len(F)+1):
            faces.update(frozenset(s) for s in combinations(F,j))
    return faces


def collapse_to_facet_trees(faces, facets):
    vertices=sorted({v for F in facets for v in F}, key=repr)
    target={frozenset((v,)) for v in vertices}
    for F in facets:
        c=min(F,key=repr)
        target.update(frozenset((c,v)) for v in F if v!=c)
    cur=set(faces); goal=target|{frozenset()}; steps=[]
    while cur!=goal:
        found=False
        for size in range(max(map(len,cur))-1,0,-1):
            cand=sorted((s for s in cur if len(s)==size and s not in target),key=lambda s:tuple(sorted(map(repr,s))))
            for s in cand:
                co=[t for t in cur if len(t)==size+1 and s<t]
                if len(co)!=1 or co[0] in target: continue
                t=co[0]
                if any(t<u for u in cur): continue
                cur.remove(s); cur.remove(t); steps.append((s,t)); found=True; break
            if found: break
        if not found: raise AssertionError('collapse stalled')
    return target,steps


def check_steiner(points,blocks,name):
    points=tuple(points); blocks=[frozenset(B) for B in blocks]
    v=len(points); k=len(blocks[0]); assert 2<=k<v
    assert all(len(B)==k for B in blocks)
    # lambda=1
    for x,y in combinations(points,2):
        assert sum(x in B and y in B for B in blocks)==1
    r0=[sum(x in B for B in blocks) for x in points]
    assert len(set(r0))==1; r=r0[0]; b=len(blocks)
    assert b*k==v*r
    # point-side component
    PF=all_faces(blocks); PT,ps=collapse_to_facet_trees(PF,blocks)
    ep=sum(len(s)==2 for s in PT); assert ep==b*(k-1)
    mup=ep-v+1
    # block-side component: one facet per point, consisting of blocks through it
    stars=[frozenset(i for i,B in enumerate(blocks) if x in B) for x in points]
    LF=all_faces(stars); LT,ls=collapse_to_facet_trees(LF,stars)
    el=sum(len(s)==2 for s in LT); assert el==v*(r-1)
    mul=el-b+1
    mu=v*r-v-b+1
    assert mup==mul==mu
    print(f'{name}: v={v} k={k} b={b} r={r} mu={mu} point_pairs={len(ps)} block_pairs={len(ls)}')


def affine_plane_3():
    P=list(product(range(3),repeat=2)); B=[]
    # vertical lines x=c
    for c in range(3): B.append({(c,y) for y in range(3)})
    # y=m x+c
    for m in range(3):
        for c in range(3): B.append({(x,(m*x+c)%3) for x in range(3)})
    return P,B


def pg2(p):
    def norm(v):
        for x in v:
            if x%p:
                inv=pow(x,-1,p); return tuple((y*inv)%p for y in v)
        raise ValueError
    P=sorted({norm(v) for v in product(range(p),repeat=3) if any(v)})
    L=P[:]
    B=[{x for x in P if sum(a*b for a,b in zip(l,x))%p==0} for l in L]
    return P,B


def main():
    P=list(range(5)); B=[set(e) for e in combinations(P,2)]
    check_steiner(P,B,'S(2,2,5)')
    P,B=affine_plane_3(); check_steiner(P,B,'AG(2,3)')
    for p in (2,3):
        P,B=pg2(p); check_steiner(P,B,f'PG(2,{p})')
    print('VERIFY_OK general_formula=mu=vr-v-b+1 projective_plane_specialization=mu=q^3')

if __name__=='__main__': main()
