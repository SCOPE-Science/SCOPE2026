"""Independent full multiplication-and-conjugation checker for graphical 2-groups.
Enumerates actual commuting pairs and conjugation orbits; no rank calculations.
"""
from itertools import product
from collections import Counter

def check(n,edges,expected):
    xs=list(product((0,1),repeat=n))
    zs=list(product((0,1),repeat=len(edges)))
    onez=(0,)*len(edges)
    zero=(0,)*n
    def mul(g,h):
        x,z=g;xx,zz=h
        return tuple(a^b for a,b in zip(x,xx)),tuple(z[i]^zz[i]^(x[u]&xx[v]) for i,(u,v) in enumerate(edges))
    identity=(zero,onez)
    def inv(g):
        x,z=g
        return x,tuple(z[i]^(x[u]&x[v]) for i,(u,v) in enumerate(edges))
    gs=[(x,z) for x in xs for z in zs]
    assert all(mul(g,inv(g))==identity and mul(inv(g),g)==identity for g in gs)
    tuples=[]
    for g in gs:
        for h in gs:
            if mul(g,h)==mul(h,g):tuples.append((g,h))
    remaining=set(tuples)
    gens=[]
    for j in range(n):
        x=tuple(int(i==j) for i in range(n));y=(x,onez);gens.append((y,inv(y)))
    hist=Counter()
    while remaining:
        p=next(iter(remaining));orbit={p};todo=[p]
        while todo:
            u,v=todo.pop()
            for h,hinv in gens:
                pair=(mul(mul(h,u),hinv),mul(mul(h,v),hinv))
                if pair not in orbit:
                    orbit.add(pair);todo.append(pair)
        assert orbit<=remaining
        remaining-=orbit
        hist[len(orbit)]+=1
    assert sum(hist.values())==expected,(hist,expected)
    print('PASS GROUP',edges,'group_order',len(gs),'commuting_pairs',len(tuples),'orbit_hist',dict(hist),'total_orbits',sum(hist.values()))

if __name__=='__main__':
    check(4,[(0,1),(0,2),(0,3)],2272)
    check(4,[(0,1),(0,2),(1,2)],1600)
