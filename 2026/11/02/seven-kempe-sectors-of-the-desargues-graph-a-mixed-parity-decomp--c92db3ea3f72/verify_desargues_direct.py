#!/usr/bin/env python3
"""Exhaustive 3-edge-colouring Kempe certificate for GP(10,3); standard library only.

Run: python verify_desargues_direct.py
Optionally pass --emit certificate.json to write the canonical full adjacency certificate.
"""
from collections import Counter, deque
import hashlib, json, sys

def edges_gp():
    edges = set()
    for i in range(10):
        for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)):
            edges.add(tuple(sorted((a,b))))
    assert len(edges) == 30
    return tuple(sorted(edges))

def enumerate_colourings(E):
    incident = [0]*20
    c = [-1]*len(E)
    out=[]
    def rec(t):
        if t==len(E):
            out.append(''.join(map(str,c)))
            return
        u,v=E[t]
        free=7 & ~(incident[u]|incident[v])
        for colour in range(3):
            bit=1<<colour
            if free & bit:
                c[t]=colour;incident[u]|=bit;incident[v]|=bit
                rec(t+1)
                incident[u]^=bit;incident[v]^=bit
    rec(0)
    return tuple(sorted(out))

def neighbours(col, E):
    result=set()
    for a,b in ((0,1),(0,2),(1,2)):
        seen=set()
        at=[[] for _ in range(20)]
        for j,(u,v) in enumerate(E):
            if int(col[j]) in (a,b):
                at[u].append((v,j));at[v].append((u,j))
        for start in range(20):
            if start in seen:continue
            seen.add(start);todo=[start];used=[]
            for u in todo:
                for v,j in at[u]:
                    used.append(j)
                    if v not in seen:seen.add(v);todo.append(v)
            used=set(used)
            if used:
                c=list(col)
                for j in used:c[j]=str(a+b-int(c[j]))
                result.add(''.join(c))
    result.discard(col)
    return result

def components(A):
    todo=set(range(len(A)));out=[]
    while todo:
        st=min(todo);comp={st};queue=[st];todo.remove(st)
        for u in queue:
            for v in A[u]:
                if v in todo:todo.remove(v);comp.add(v);queue.append(v)
        out.append(tuple(sorted(comp)))
    return sorted(out, key=lambda x:(-len(x),x))

def distances(A,source):
    d={source:0};q=deque((source,))
    while q:
        u=q.popleft()
        for v in A[u]:
            if v not in d:d[v]=d[u]+1;q.append(v)
    return d

def bipartition(A,comp):
    dist=distances(A,comp[0]);
    return len(dist)==len(comp) and all((dist[u]-dist[v])%2 for u in comp for v in A[u])

def cycle_count(A,component,length):
    found=set()
    for start in component:
        stack=[(start,[start])]
        while stack:
            u,path=stack.pop()
            if len(path)==length:
                if start in A[u]:
                    seq=path
                    rotations=(tuple(seq[i:]+seq[:i]) for i in range(length))
                    rev=seq[::-1]
                    anti=(tuple(rev[i:]+rev[:i]) for i in range(length))
                    found.add(min(*rotations,*anti))
            else:
                for v in A[u]:
                    if v>start and v not in path:stack.append((v,path+[v]))
    return len(found)

def first_odd5(A,component):
    for s in component:
        stack=[(s,[s])]
        while stack:
            u,path=stack.pop()
            if len(path)==5:
                if s in A[u]:return path
            else:
                for v in A[u]:
                    if v>s and v not in path:stack.append((v,path+[v]))
    return None

def three_colouring(A, vertices):
    order=sorted(vertices,key=lambda v:(-len(A[v]),v)); colours={}
    def walk(t):
        if t==len(order):return True
        u=order[t]
        for c in range(3):
            if all(colours.get(w)!=c for w in A[u]):
                colours[u]=c
                if walk(t+1):return True
                del colours[u]
        return False
    if not walk(0):return None
    return {str(v):colours[v] for v in vertices}

def certificate():
    E=edges_gp(); C=enumerate_colourings(E)
    assert len(C)==192, ('states',len(C))
    idx={v:i for i,v in enumerate(C)}
    A=[]
    for colour in C:
        nbr=neighbours(colour,E)
        assert nbr <= idx.keys()
        A.append(tuple(sorted(idx[x] for x in nbr)))
    assert all(u in A[v] for u in range(len(C)) for v in A[u])
    cc=components(A);assert list(map(len,cc))==[120]+[12]*6
    assert sum(map(len,A))==1008
    assertions=[]; witnesses=[]
    for t,group in enumerate(cc):
        deg=Counter(len(A[v]) for v in group)
        profiles=Counter(tuple(Counter(distances(A,v).values()).get(k,0) for k in range(6 if t==0 else 3)) for v in group)
        square=cycle_count(A,group,4)
        odd5=cycle_count(A,group,5)
        odd=first_odd5(A,group)
        assert (deg,profiles,square,odd5,bipartition(A,group)) == (
            (Counter({6:120}),Counter({(1,6,27,48,32,6):120}),90,0,True)
            if t==0 else (Counter({4:12}),Counter({(1,4,7):12}),15,48,False))
        assertions.append({'size':len(group),'degree_counts':dict(deg),'distance_sphere_profiles':[[list(k),v] for k,v in profiles.items()],
                           'square_cycles':square,'pentagon_cycles':odd5,'is_bipartite':bipartition(A,group)})
        colouring3 = three_colouring(A,group) if t else None
        assert not t or colouring3 is not None
        assert colouring3 is None or all(colouring3[str(u)]!=colouring3[str(v)] for u in group for v in A[u])
        witnesses.append({'small_component_three_colouring':colouring3,'pentagon':odd if odd else None,
                          'distance_five_pair':(group[0], next((w for w,d in distances(A,group[0]).items() if d==5),None)) if t==0 else None})
    payload={'description':'All labelled proper three-edge-colourings of GP(10,3) and their single Kempe-switch adjacency.',
            'edge_order':E,'colourings':C,'adjacency':A,'components':cc,'component_statistics':assertions,'witness_indices':witnesses}
    print('DESARGUES_DIRECT_PASS',len(C),sum(map(len,A))//2,[len(x) for x in cc], 'C4',sum(x['square_cycles'] for x in assertions), 'C5',sum(x['pentagon_cycles'] for x in assertions))
    return payload
if __name__=='__main__':
    data=certificate()
    if len(sys.argv)==3 and sys.argv[1]=='--emit':
        with open(sys.argv[2],'w',encoding='utf-8',newline='\n') as f:json.dump(data,f,ensure_ascii=False,sort_keys=True,separators=(',',':'));f.write('\n')
        print('CERTIFICATE_EMITTED',sys.argv[2])
