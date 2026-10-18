#!/usr/bin/env python3
"""Exhaustive small-instance checks for fixed points of generalized Mycielskian independence complexes.
Pure Python 3; reconstructs group orbits, graph folding, signed Lefschetz traces,
and integral mod-two boundary ranks directly from definitions.
"""
from itertools import combinations


def graph(n, ell):
    verts=[(j,a) for j in range(ell+1) for a in range(n)]+['w']
    edges=set()
    for j in range(ell):
        for a in range(n):
            for b in range(n):
                if a!=b: edges.add(frozenset(((j,a),(j+1,b))))
    for a,b in combinations(range(n),2):edges.add(frozenset(((ell,a),(ell,b))))
    for a in range(n):edges.add(frozenset(('w',(0,a))))
    return verts,edges


def cycles(p):
    unseen=set(range(len(p))); ans=[]
    while unseen:
        a=min(unseen); x=a; c=[]
        while x in unseen:
            unseen.remove(x);c.append(x);x=p[x]
        assert x==a
        ans.append(tuple(c))
    return ans


def orbit_graph(n,ell,p):
    verts,edges=graph(n,ell)
    blocks=[]; tags=[]
    for j in range(ell+1):
        for c in cycles(p):
            block=frozenset((j,a) for a in c)
            if all(not e.issubset(block) for e in edges):
                blocks.append(block)
                tags.append(('F',c[0],j) if len(c)==1 else ('U',c,j))
    blocks.append(frozenset(('w',))); tags.append(('W',))
    adj={frozenset((i,k)) for i in range(len(blocks)) for k in range(i+1,len(blocks))
         if any(e.issubset(blocks[i]|blocks[k]) for e in edges)}
    return tags,adj


def retract_check(n,ell,p):
    tags,edges=orbit_graph(n,ell,p)
    fixed=[i for i in range(n) if p[i]==i]
    active=set(range(len(tags)))
    ne=lambda i: {j for j in active if frozenset((i,j)) in edges}
    if fixed:
        keep={i for i,t in enumerate(tags) if t[0]!='U'}
        for i,t in enumerate(tags):
            if t[0]!='U':continue
            dom=next(k for k,x in enumerate(tags) if x==('F',fixed[0],t[2]))
            assert ne(dom)<=ne(i),(n,ell,p,t,ne(dom),ne(i))
            active.remove(i)
        assert active==keep
    else:
        if ell:
            first=next(t[1] for t in tags if t[0]=='U')
            keep={i for i,t in enumerate(tags) if t[0]!='U' or t[1]==first}
            for i,t in enumerate(tags):
                if i in keep:continue
                dom=next(k for k in keep if tags[k]==('U',first,t[2]))
                assert ne(i)==ne(dom),(n,ell,p,t)
                active.remove(i)
        else:keep=set(active)
        assert active==keep
    compact={i:(('a',t[1],t[2]) if t[0]=='F' else ('u',t[2]) if t[0]=='U' else ('w',))
             for i,t in enumerate(tags) if i in keep}
    got={frozenset((compact[i],compact[j])) for i in keep for j in keep
         if i<j and frozenset((i,j)) in edges}
    if fixed:
        want_vs,want_edges=graph(len(fixed),ell)
        # Relabel the fixed-label graph to its original labels.
        relabel={(j,k):('a',fixed[k],j) for j in range(ell+1) for k in range(len(fixed))}
        relabel['w']=('w',)
        want={frozenset(relabel[v] for v in e) for e in want_edges}
    else:
        want={frozenset((('w',),('u',0)))} if ell else set()
        for j in range(ell-1):want.add(frozenset((('u',j),('u',j+1))))
    assert got==want,(n,ell,p,got^want)
    return len(tags),len(keep),len(got)


def independent_faces(m,edge_indices):
    edge_list=[tuple(e) for e in edge_indices]
    faces=[]
    for r in range(m+1):
        for s in combinations(range(m),r):
            ss=set(s)
            if all(not (a in ss and b in ss) for a,b in edge_list):faces.append(s)
    return faces


def rank2(vectors):
    piv={}
    for x in vectors:
        while x:
            h=x.bit_length()-1
            if h in piv:x^=piv[h]
            else:piv[h]=x;break
    return len(piv)


def reduced_betti_mod2(verts,edges):
    v={x:i for i,x in enumerate(verts)}
    faces=independent_faces(len(verts),[{v[a],v[b]} for a,b in (tuple(e) for e in edges)])
    bydeg={d:[f for f in faces if len(f)==d+1] for d in range(len(verts))}
    ranks={}
    for d in range(1,len(verts)):
        if not bydeg[d]:continue
        idx={f:i for i,f in enumerate(bydeg[d-1])}
        columns=[]
        for face in bydeg[d]:
            x=0
            for q in range(len(face)):x^=1<<idx[face[:q]+face[q+1:]]
            columns.append(x)
        ranks[d]=rank2(columns)
    return tuple(len(bydeg[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
                 for d in range(len(verts)) if bydeg[d])


def signed_lefschetz(n,ell,p):
    verts,edges=graph(n,ell)
    ix={v:i for i,v in enumerate(verts)}
    ep={frozenset(ix[v] for v in e) for e in edges}
    perm=[ix[(v[0],p[v[1]])] if v!='w' else ix['w'] for v in verts]
    Lef=-1
    for face in independent_faces(len(verts),ep):
        if not face:continue
        image=tuple(perm[i] for i in face)
        if set(image)!=set(face):continue
        inv=sum(image[i]>image[j] for i in range(len(face)) for j in range(i+1,len(face)))
        Lef+=(-1)**(len(face)-1+inv)
    return Lef


def known_betti(f,ell):
    if f==0:
        if ell%3==0:return ()
        return (ell//3,)
    if f==1:
        return ((0,1),) if ell==0 else ()
    k=ell//3
    return ((2*k, f*(f-1)**k) if ell%3==0 else (2*k+1,(f-1)**(k+1)),)


def main():
    perms=[(1,0),(1,2,0),(1,0,3,2),(1,2,0,4,3),
           (1,0,3,2,5,4),(1,2,3,0),(1,0,2),(1,0,3,2,4),
           (1,0,3,2,4,5),(1,2,0,3),(1,2,0,4,3,5),
           (1,2,3,4,0),(1,2,3,0,4)]
    folds=0; traces=0; mod2=0
    for p in perms:
        n=len(p);f=sum(i==x for i,x in enumerate(p))
        for ell in range(9):
            retract_check(n,ell,p);folds+=1
            if n*(ell+1)+1<=14:
                L=signed_lefschetz(n,ell,p)
                # Euler characteristic from the full published homology character,
                # serving here only as an independent arithmetic cross-check.
                k=ell//3
                if ell%3==0: character=f*(f-1)**k
                else:character=(f-1)**(k+1)
                expected=character*(1 if ell%3==0 else -1)
                assert L==expected,(p,ell,L,expected)
                traces+=1
    for m in range(1,13):
        vertices=list(range(m)); edges={frozenset((j,j+1)) for j in range(m-1)}
        got=reduced_betti_mod2(vertices,edges)
        exp=[0]*len(got)
        if m%3==0:exp[m//3-1]=1
        elif m%3==2:exp[(m-2)//3]=1
        assert got==tuple(exp),(m,got,exp)
        mod2+=1
    for f in (1,2,3):
        for ell in range(6):
            if f*(ell+1)+1>13:continue
            verts,edges=graph(f,ell)
            got=reduced_betti_mod2(verts,edges)
            exp=[0]*len(got)
            for dim,mult in known_betti(f,ell):exp[dim]=mult
            assert got==tuple(exp),(f,ell,got,exp)
            mod2+=1
    print(f'VERIFY_OK orbit_graph_folds={folds} signed_full_Lefschetz={traces} complete_mod2_homologies={mod2}')
if __name__=='__main__': main()
