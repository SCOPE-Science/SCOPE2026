#!/usr/bin/env python3
"""Independent finite tests for hyperplane sections of crosspolytope prisms.
All sign counts and graph edges are computed using exact integer arithmetic.
The proof in RESULT.md is general; these checks are finite corroboration.
"""
from itertools import product
from random import Random


def vertex_edges(d):
    # Vertex i in [0,2d): (i//2)th basis vector with sign + (even) or - (odd).
    # Vertices 0..2d-1 are top, 2d..4d-1 are bottom.
    e = []
    for level in (0, 1):
        off = 2*d*level
        for i in range(2*d):
            for j in range(i+1,2*d):
                if i//2 != j//2:
                    e.append((off+i,off+j))
    e.extend((i,i+2*d) for i in range(2*d))
    assert len(e) == 4*d*(d-1)+2*d
    return e


def signs(d, xs, t, c):
    top = []
    bottom = []
    for z, arr in ((t,top),(-t,bottom)):
        for x in xs:
            arr.extend([x+z-c, -x+z-c])
    return top+bottom


def g(d,k):
    return k*(2*d-k)-min(k,2*d-k)


def count_brute(d,vals,edges):
    return sum((vals[i]>0)!=(vals[j]>0) for i,j in edges)


def model(d,vals,t):
    u,v=vals[:2*d],vals[2*d:]
    if t<0:
        u,v=v,u
    k=sum(x>0 for x in u)
    l=sum(x>0 for x in v)
    assert l<=k
    return g(d,k)+g(d,l)+k-l,k,l


def construction(d,k,l):
    assert 0<=l<=k<=2*d
    if k<=d:
        xs=[6]*l+[4]*(k-l)+[2]*(d-k)
        return xs,1,4
    if l>=d:
        xs=[2]*(l-d)+[4]*(k-l)+[6]*(2*d-k)
        return xs,1,-4
    a,b=k-d,l
    if a+b<=d:
        xs=[2]*a+[4]*(d-a-b)+[6]*b
        return xs,4,1
    xs=[2]*(d-b)+[4]*(a+b-d)+[6]*(d-a)
    return xs,4,-1


def check():
    total=0; spectrum=0; best=[]
    for d in range(2,9):
        edges=vertex_edges(d)
        pred=2*d*(d-1)+2
        candidate=signs(d,[0]+[2]*(d-1),1,0)
        assert all(candidate)
        assert count_brute(d,candidate,edges)==pred
        best.append((d,pred))
        values=set()
        for k in range(2*d+1):
            for l in range(k+1):
                xs,t,c=construction(d,k,l)
                vals=signs(d,xs,t,c)
                assert all(vals), (d,k,l)
                v,kk,ll=model(d,vals,t)
                assert kk==k and ll==l, (d,k,l,kk,ll)
                assert v==count_brute(d,vals,edges), (d,k,l,v)
                assert v<=pred
                if v:values.add(v)
                spectrum+=1
        assert max(values)==pred
        if d==3:assert 7 not in values and 13 in values
    # Confirm the graph-combinatorial benchmark without assuming hyperplane
    # realizability: exhaust all sign assignments for d=2,3,4.
    maxcut_verified=[]
    for d in range(2,5):
        edges=vertex_edges(d)
        observed=max(sum(((mask>>i)&1)!=((mask>>j)&1) for i,j in edges)
                     for mask in range(1<<(4*d)))
        predicted=2*d*d+2*d-2*(d%2)
        assert observed==predicted, (d, observed, predicted)
        maxcut_verified.append((d, observed))
    # For each small integer functional, check all generic sections and exact cut equation.
    for d,coeffs,tc in [(2,range(-4,5),range(-4,5)),(3,range(-3,4),range(-3,4)),(4,range(-2,3),range(-2,3))]:
        edges=vertex_edges(d)
        for xs in product(coeffs,repeat=d):
            for t in tc:
                for c in tc:
                    vals=signs(d,xs,t,c)
                    if 0 in vals:continue
                    brute=count_brute(d,vals,edges)
                    v,k,l=model(d,vals,t)
                    assert brute==v<=2*d*(d-1)+2,(d,xs,t,c,brute,v,k,l)
                    total+=1
    rng=Random(20261016)
    for d in range(5,11):
        edges=vertex_edges(d)
        for _ in range(1600):
            xs=[rng.randrange(-30,31) for _ in range(d)]
            t=rng.randrange(-30,31)
            c=rng.randrange(-30,31)
            vals=signs(d,xs,t,c)
            if 0 in vals: continue
            v,k,l=model(d,vals,t)
            assert count_brute(d,vals,edges)==v<=2*d*(d-1)+2
            total+=1
    print('CROSS_PRISM_CHECK_OK exhaustive_integer_hyperplanes=',total,'all_realizable_count_pairs=',spectrum,'sharp_maxima=',best,'maxcut_verified=',maxcut_verified)

if __name__=='__main__':check()
