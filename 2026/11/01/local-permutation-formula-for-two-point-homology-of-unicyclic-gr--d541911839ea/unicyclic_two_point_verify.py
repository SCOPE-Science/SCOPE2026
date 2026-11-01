#!/usr/bin/env python3
"""Exact finite regression checks for the unicyclic two-point character formula.
Uses only the Python standard library. No external data or software needed.
Finite checks illustrate, but do not replace, the all-graph proof.
"""
from itertools import combinations

def unicyclic_graph(n, attachments):
    # Cycle vertices 0..n-1; each attachment gives its parent (a new leaf is appended).
    edges={tuple(sorted((i,(i+1)%n))) for i in range(n)}
    size=n
    for parent in attachments:
        assert 0<=parent<size
        edges.add(tuple(sorted((parent,size))))
        size+=1
    return size, tuple(sorted(edges)), n

def automorphisms(N,edges):
    neigh=[set() for _ in range(N)]
    for a,b in edges: neigh[a].add(b);neigh[b].add(a)
    order=sorted(range(N),key=lambda v:(-len(neigh[v]),v))
    bydegree={d:[i for i in range(N) if len(neigh[i])==d] for d in set(map(len,neigh))}
    p={};used=set();perms=[]
    def visit(j):
        if j==N:
            perms.append(tuple(p[i] for i in range(N)));return
        u=order[j]
        for x in bydegree[len(neigh[u])]:
            if x in used:continue
            if any(((v in neigh[u])!=(p[v] in neigh[x])) for v in p):continue
            p[u]=x;used.add(x)
            visit(j+1)
            used.remove(x);del p[u]
    visit(0)
    return perms,neigh

def character(N,edges,n,p,neigh):
    edgenum={e:i for i,e in enumerate(edges)}
    emap=[];esgn=[]
    for u,v in edges:
        a,b=p[u],p[v]
        emap.append(edgenum[tuple(sorted((a,b)))]);esgn.append(1 if a<b else -1)
    vertices=list(range(N));E=len(edges)
    c0=sum(1 for u,v in combinations(vertices,2) if {p[u],p[v]}=={u,v})
    c1=sum(esgn[i] for i,(u,v) in enumerate(edges) for w in vertices
           if w!=u and w!=v and p[w]==w and emap[i]==i)
    c2=0
    for i,j in combinations(range(E),2):
        if set(edges[i]).intersection(edges[j]):continue
        if {emap[i],emap[j]}!={i,j}:continue
        c2+=esgn[i]*esgn[j]*(1 if emap[i]<emap[j] else -1)
    celltrace=1-c0+c1-c2
    # The orientation sign of the unique embedded n-cycle.
    eps=1 if p[1]==(p[0]+1)%n else -1
    loc=0
    for v in range(N):
        if p[v]!=v:continue
        f=sum(1 for w in neigh[v] if p[w]==w)
        f2=sum(1 for w in neigh[v] if p[p[w]]==w)
        loc+=(f*f-f2-2*f+2)//2
    formula=eps+loc
    assert celltrace==formula,(N,edges,p,(c0,c1,c2),celltrace,formula)
    return celltrace,eps,loc

def binary_rank_of_d2(N,edges):
    edge_vertex={(i,v):j for j,(i,v) in enumerate((i,v) for i,e in enumerate(edges)
             for v in range(N) if v not in e)}
    basis={};squares=0
    for i,j in combinations(range(len(edges)),2):
        a,b=edges[i];c,d=edges[j]
        if len({a,b,c,d})!=4:continue
        squares+=1
        z=0
        for t in ((i,c),(i,d),(j,a),(j,b)):
            z^=1<<edge_vertex[t]
        while z:
            k=z.bit_length()-1
            if k not in basis:
                basis[k]=z;break
            z^=basis[k]
    assert len(basis)==squares,('noninjective_d2',squares,len(basis))
    return squares,len(edge_vertex)

def go():
    tests=[
        ('pentagon',5,[]),
        ('sunlet_5',5,[0,1,2,3,4]),
        ('sunlet_6',6,[0,1,2,3,4,5]),
        ('sunlet_7',7,[0,1,2,3,4,5,6]),
        ('triangle_double_leaf',3,[0,0]),
        ('triangle_triple_leaf',3,[0,0,0]),
        ('pentagon_long_branch',5,[0,5]),
        ('hexagon_mixed_branch',6,[0,2,6,7]),
    ]
    count=0
    for name,n,att in tests:
        N,edges,n=unicyclic_graph(n,att)
        perms,neigh=automorphisms(N,edges)
        sq,c1=binary_rank_of_d2(N,edges)
        c0=N*(N-1)//2
        expected=1-c0+c1-sq
        local=1+sum((len(a)-1)*(len(a)-2)//2 for a in neigh)
        assert expected==local,(name,expected,local)
        chars=[]
        for p in perms:
            chars.append(character(N,edges,n,p,neigh)[0]);count+=1
        print('%s: V=%d E=%d aut=%d rank_d2=%d beta1=%d char_range=[%d,%d]'%
              (name,N,len(edges),len(perms),sq,expected,min(chars),max(chars)))
    print('UNICYCLIC_TWO_POINT_VERIFY_OK: graphs=%d automorphisms=%d'%(len(tests),count))
if __name__=='__main__':go()
