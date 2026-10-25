#!/usr/bin/env python3
"""Finite verification of colored two-layer abelian surface decomposition.
Scientific test only; not a proof of infinite theorem.
"""
from itertools import product
from collections import defaultdict, Counter, deque
from math import prod, gcd

def rank_mod(vectors, p):
    piv={}
    for items in vectors:
        v={i:c%p for i,c in items if c%p}
        while v:
            j=min(v)
            if j not in piv:
                v={i: c*pow(v[j],-1,p)%p for i,c in v.items() if c%p}
                piv[j]=v
                break
            scalar=v[j]
            for i,c in piv[j].items():
                new=(v.get(i,0)-scalar*c)%p
                if new: v[i]=new
                elif i in v: del v[i]
    return len(piv)

def verify(moduli,d,homology=True):
    A=list(product(*(range(m) for m in moduli)))
    z=tuple(0 for m in moduli)
    plus=lambda a,b:tuple((a[i]+b[i])%moduli[i] for i in range(len(moduli)))
    neg=lambda a:tuple(-a[i]%moduli[i] for i in range(len(moduli)))
    q=len(A)
    h=1; t=d
    while t!=z:
        t=plus(t,d); h+=1
        assert h<=q
    g=q//h
    H=[z]; t=z
    for _ in range(h-1):t=plus(t,d);H.append(t)
    cos={}
    for a in A:
        if a not in cos:
            idx=len(set(cos.values()))
            for b in H:cos[plus(a,b)]=idx
    assert len(set(cos.values()))==g
    vertices={(i,a):i*q+j for i in range(3) for j,a in enumerate(A)}
    faces2=[]
    for a,b in product(A,A):
        c0=neg(plus(a,b));c1=plus(c0,d)
        faces2.extend((vertices[(0,a)],vertices[(1,b)],vertices[(2,c)]) for c in [c0,c1])
    faces2=[tuple(sorted(t)) for t in faces2]
    edge_to_faces=defaultdict(list)
    for k,t in enumerate(faces2):
        for i,j in ((0,1),(0,2),(1,2)):
            edge_to_faces[tuple(sorted((t[i],t[j])))].append(k)
    edges=sorted(edge_to_faces)
    assert len(faces2)==2*q*q and len(edges)==3*q*q
    assert all(len(v)==2 for v in edge_to_faces.values())
    pieces=defaultdict(list)
    for k,t in enumerate(faces2):
        a=A[t[0]];b=A[t[1]-q]
        pieces[(cos[a],cos[b])].append(k)
    assert len(pieces)==g*g
    for name,ind in pieces.items():
        verts=set(v for k in ind for v in faces2[k]); pe=defaultdict(list)
        for k in ind:
            t=faces2[k]
            for i,j in ((0,1),(0,2),(1,2)):
                pe[tuple(sorted((t[i],t[j])))].append(k)
        assert len(verts)==3*h and len(pe)==3*h*h and len(ind)==2*h*h, (moduli,d,name)
        assert all(len(t)==2 for t in pe.values())
        # Each vertex link is connected and degree two => circle
        for v in verts:
            adj=defaultdict(set)
            for k in ind:
                tri=faces2[k]
                if v in tri:
                    aa,bb=[x for x in tri if x!=v]
                    adj[aa].add(bb); adj[bb].add(aa)
            assert len(adj)==2*h
            assert all(len(x)==2 for x in adj.values())
            seen={next(iter(adj))}; queue=list(seen)
            for w in queue:
                for x in adj[w]:
                    if x not in seen:seen.add(x);queue.append(x)
            assert len(seen)==len(adj)
    # Incidence graph of pieces against vertices; first Betti by Euler.
    incident=defaultdict(set)
    for name,ind in pieces.items():
        incident[name]={v for k in ind for v in faces2[k]}
    assert sum(map(len,incident.values()))==3*g*q
    assert len(set.union(*incident.values()))==3*q
    # Explicit connectivity of incidence graph
    adj=defaultdict(set)
    for name,verts in incident.items():
        for v in verts:
            adj[('p',name)].add(('v',v));adj[('v',v)].add(('p',name))
    st=next(iter(adj)); seen={st}; stack=[st]
    while stack:
        for x in adj[stack.pop()]:
            if x not in seen: seen.add(x);stack.append(x)
    assert len(seen)==len(adj)==g*g+3*q
    r=3*g*q-g*g-3*q+1
    b1=g*g*(h-1)*(h-2)+r
    assert b1==q*q-3*q+1+g*g
    if homology:
        eind={v:k for k,v in enumerate(edges)}
        b1matrix=[[(j,1),(i,-1)] for i,j in edges]  # boundary of edges
        b2matrix=[]
        for a,b,c in faces2:
            b2matrix.append([(eind[(b,c)],1),(eind[(a,c)],-1),(eind[(a,b)],1)])
        for p in (2,1009):
            rk1=rank_mod(b1matrix,p)
            rk2=rank_mod(b2matrix,p)
            assert rk1==3*q-1,(moduli,d,p,rk1)
            assert 2*q*q-rk2==g*g,(moduli,d,p,rk2,g)
            assert 3*q*q-rk1-rk2==b1,(moduli,d,p,b1)
    return {'group':moduli,'d':d,'order':q,'gap_order':h,'index':g,'surface_genus':(h-1)*(h-2)//2,'surfaces':g*g,'graph_loops':r,'betti1':b1,'betti2':g*g,'faces':(3*q,3*q*q,2*q*q)}

if __name__=='__main__':
    import json
    cases=[]
    for moduli in [(4,),(5,),(6,),(8,),(9,),(10,),(12,),(2,2),(2,3),(2,4),(3,3)]:
        for d in product(*(range(m) for m in moduli)):
            if all(x==0 for x in d): continue
            out=verify(moduli,d,homology=prod(moduli)<=10)
            if out['index']>1:cases.append(out)
    print('Verified non-generating gap cases:',len(cases))
    for case in cases:
        if case['group'] in [(6,),(2,4),(3,3)] and case['d'] in [(2,),(3,),(1,0),(0,1)]: print(json.dumps(case,sort_keys=True))
    assert cases
    print('PASS: all cases, manifold links, surface partition, incidence-graph connectedness; mod-2 and mod-1009 homology for groups of order <=10')
