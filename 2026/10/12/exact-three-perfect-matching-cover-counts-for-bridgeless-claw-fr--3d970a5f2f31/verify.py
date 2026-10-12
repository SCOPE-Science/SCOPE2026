#!/usr/bin/env python3
from itertools import product, combinations

COLORS=(0,1,2)

def count_edge_colorings(edges):
    inc={}
    for i,(u,v) in enumerate(edges):
        inc.setdefault(u,[]).append(i); inc.setdefault(v,[]).append(i)
    adj=[set() for _ in edges]
    for ids in inc.values():
        for a,b in combinations(ids,2): adj[a].add(b); adj[b].add(a)
    order=sorted(range(len(edges)), key=lambda i:-len(adj[i]))
    color=[-1]*len(edges); total=0
    def rec(k):
        nonlocal total
        if k==len(order): total+=1; return
        e=order[k]
        used={color[j] for j in adj[e] if color[j]>=0}
        for c in COLORS:
            if c not in used:
                color[e]=c; rec(k+1)
        color[e]=-1
    rec(0); return total

def local_triangle_counts():
    # vertices 0,1,2; external half-edge colors prescribed; internal triangle edges 01,02,12
    out={}
    for ext in product(COLORS, repeat=3):
        cnt=0
        for c01,c02,c12 in product(COLORS, repeat=3):
            if len({ext[0],c01,c02})<3: continue
            if len({ext[1],c01,c12})<3: continue
            if len({ext[2],c02,c12})<3: continue
            cnt+=1
        out[ext]=cnt
    return out

def local_diamond_counts():
    # terminals a,b have external colors x,y; internals ac,ad,bc,bd,cd
    out={}
    for x,y in product(COLORS, repeat=2):
        cnt=0
        for ac,ad,bc,bd,cd in product(COLORS, repeat=5):
            if len({x,ac,ad})<3: continue
            if len({y,bc,bd})<3: continue
            if len({ac,bc,cd})<3: continue
            if len({ad,bd,cd})<3: continue
            cnt+=1
        out[(x,y)]=cnt
    return out

def local_two_cycle_counts():
    out={}
    for x,y in product(COLORS, repeat=2):
        cnt=sum(1 for p,q in product(COLORS, repeat=2)
                if len({x,p,q})==3 and len({y,p,q})==3)
        out[(x,y)]=cnt
    return out

def normalize_core(vertices, edges):
    inc={v:[] for v in vertices}
    for eid,(u,v) in enumerate(edges):
        inc[u].append(eid); inc[v].append(eid)
    assert all(len(inc[v])==3 for v in vertices)
    return inc

def expand(vertices, core_edges, channel_units):
    # channel_units[eid] is a list over {'D','C'} (diamond, 2-cycle)
    inc=normalize_core(vertices, core_edges)
    E=[]; nextv=0; port={}
    # one port vertex per core incidence
    for v in vertices:
        ps=[]
        for eid in inc[v]:
            port[(v,eid)]=nextv; ps.append(nextv); nextv+=1
        E += [(ps[0],ps[1]),(ps[0],ps[2]),(ps[1],ps[2])]
    for eid,(u,v) in enumerate(core_edges):
        left=port[(u,eid)]; right=port[(v,eid)]
        units=channel_units.get(eid,[])
        if not units:
            E.append((left,right)); continue
        prev=left
        for idx,t in enumerate(units):
            if t=='D':
                a,b,c,d=range(nextv,nextv+4); nextv+=4
                E.append((prev,a))
                E += [(a,c),(a,d),(b,c),(b,d),(c,d)]
                prev=b
            elif t=='C':
                a,b=range(nextv,nextv+2); nextv+=2
                E.append((prev,a)); E += [(a,b),(a,b)]
                prev=b
            else: raise ValueError(t)
        E.append((prev,right))
    return list(range(nextv)),E


def ring(units):
    E=[]; nextv=0; terminals=[]
    for t in units:
        if t=='D':
            a,b,c,d=range(nextv,nextv+4); nextv+=4
            E += [(a,c),(a,d),(b,c),(b,d),(c,d)]
            terminals.append((a,b))
        elif t=='C':
            a,b=range(nextv,nextv+2); nextv+=2
            E += [(a,b),(a,b)]
            terminals.append((a,b))
        else: raise ValueError(t)
    q=len(units)
    for i in range(q):
        E.append((terminals[i][1], terminals[(i+1)%q][0]))
    return list(range(nextv)),E

def degrees(vertices, edges):
    d={v:0 for v in vertices}
    for u,v in edges: d[u]+=1; d[v]+=1
    return d

def petersen():
    V=list(range(10))
    E=[(i,(i+1)%5) for i in range(5)]
    E += [(i,5+i) for i in range(5)]
    E += [(5,7),(7,9),(9,6),(6,8),(8,5)]
    return V,E

def k4():
    V=list(range(4)); E=list(combinations(V,2)); return V,E

def main():
    tri=local_triangle_counts()
    assert all(tri[e]==(1 if len(set(e))==3 else 0) for e in tri)
    dia=local_diamond_counts()
    cyc=local_two_cycle_counts()
    assert all(dia[(a,b)]==(2 if a==b else 0) for a,b in dia)
    assert all(cyc[(a,b)]==(2 if a==b else 0) for a,b in cyc)

    V,E=k4(); c=count_edge_colorings(E); assert c==6
    V0,E0=expand(V,E,{})
    assert set(degrees(V0,E0).values())=={3}
    assert count_edge_colorings(E0)==c
    # one diamond on core edge 0 and one 2-cycle on core edge 1: factor 4
    V2,E2=expand(V,E,{0:['D'],1:['C']})
    assert set(degrees(V2,E2).values())=={3}
    assert count_edge_colorings(E2)==4*c

    for units in (['D','D'],['D','C'],['C','C'],['D','C','D']):
        VR,ER=ring(units)
        assert set(degrees(VR,ER).values())=={3}
        assert count_edge_colorings(ER)==3*(2**len(units))
    VP,EP=petersen(); cp=count_edge_colorings(EP); assert cp==0
    VTP,ETP=expand(VP,EP,{})
    assert len(VTP)==30 and set(degrees(VTP,ETP).values())=={3}
    print('ALL CHECKS PASSED; triangle_external_patterns=27; diamond_external_pairs=9; two_cycle_external_pairs=9; K4_colorings=6; K4_two_unit_expansion_colorings=24; ring_tests=4; Petersen_colorings=0; Petersen_truncation_vertices=30')

if __name__=='__main__': main()
