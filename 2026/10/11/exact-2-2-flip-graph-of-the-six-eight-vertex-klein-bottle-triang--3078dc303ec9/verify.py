from itertools import combinations, permutations, product
from collections import Counter, defaultdict, deque

START = [
(1,2,3),(3,7,2),(1,5,3),(1,7,5),(1,4,7),(1,6,2),(6,4,2),(1,6,8),
(1,4,8),(2,4,8),(6,4,3),(3,7,4),(6,8,5),(6,5,3),(8,2,5),(2,7,5)
]
START=frozenset(tuple(sorted(f)) for f in START)
V=tuple(range(1,9))

def degrees(fs):
    c=Counter()
    for f in fs:
        for v in f:c[v]+=1
    return c

def canon(fs):
    d=degrees(fs)
    groups=[]; target=[]; k=1
    for val in sorted(set(d.values())):
        src=sorted(v for v in V if d[v]==val)
        tgt=list(range(k,k+len(src))); k+=len(src)
        groups.append(src); target.append(tgt)
    best=None
    for choices in product(*[list(permutations(g)) for g in groups]):
        mp={}
        for perm,tgt in zip(choices,target):
            for s,t in zip(perm,tgt): mp[s]=t
        key=tuple(sorted(tuple(sorted(mp[x] for x in f)) for f in fs))
        if best is None or key<best:best=key
    return best

def edge_map(fs):
    em=defaultdict(list)
    for f in fs:
        a,b,c=f
        em[tuple(sorted((a,b)))].append(c)
        em[tuple(sorted((a,c)))].append(b)
        em[tuple(sorted((b,c)))].append(a)
    return em

def flips(fs):
    em=edge_map(fs); edges=set(em); out=[]
    for (a,b),cs in sorted(em.items()):
        if len(cs)!=2: raise AssertionError('not closed surface')
        c,d=cs
        if tuple(sorted((c,d))) in edges: continue
        old1=tuple(sorted((a,b,c))); old2=tuple(sorted((a,b,d)))
        nf=set(fs); nf.remove(old1); nf.remove(old2)
        nf.add(tuple(sorted((a,c,d)))); nf.add(tuple(sorted((b,c,d))))
        out.append(((a,b),frozenset(nf)))
    return out

def label(fs):
    d=degrees(fs); cnt=Counter(d.values())
    sig=tuple(sorted(d.values()))
    if sig==(5,5,6,6,6,6,7,7):return '242'
    if sig==(4,5,6,6,6,7,7,7):return '1133'
    if sig==(5,5,5,5,7,7,7,7):return '404'
    if sig==(5,6,6,6,6,6,6,7):return '161'
    if sig==(5,5,5,6,6,7,7,7):
        sevens=tuple(sorted(v for v in V if d[v]==7))
        return '323-A' if sevens in fs else '323-B'
    raise AssertionError(('unknown valence signature',sig))

def check_surface(fs):
    assert len(fs)==16
    em=edge_map(fs); assert len(em)==24 and all(len(x)==2 for x in em.values())
    # vertex links are cycles
    for v in V:
        L=defaultdict(set)
        for f in fs:
            if v in f:
                a,b=[x for x in f if x!=v]; L[a].add(b); L[b].add(a)
        assert len(L)==degrees(fs)[v]
        assert all(len(n)==2 for n in L.values())
        # connected link
        seen=set(); stack=[next(iter(L))]
        while stack:
            x=stack.pop()
            if x in seen:continue
            seen.add(x); stack.extend(L[x]-seen)
        assert len(seen)==len(L)

# Exhaust the 2-2 flip closure up to combinatorial isomorphism.
reps={canon(START):START}; q=deque([START])
while q:
    fs=q.popleft()
    for _,nf in flips(fs):
        k=canon(nf)
        if k not in reps:
            reps[k]=nf; q.append(nf)

assert len(reps)==6
bylabel={label(fs):fs for fs in reps.values()}
assert set(bylabel)=={'242','1133','404','161','323-A','323-B'}
for fs in bylabel.values(): check_surface(fs)

M={}
for name,fs in bylabel.items():
    c=Counter()
    for e,nf in flips(fs):
        c[label(bylabel[label(nf)] if canon(nf) in reps else nf)] += 1
    # simpler: label is invariant under relabeling, so direct label(nf)
    c=Counter(label(nf) for _,nf in flips(fs))
    M[name]=dict(sorted(c.items()))

expected={
'242':{'1133':2,'161':2,'323-A':2,'404':1},
'323-A':{'1133':2,'242':2,'323-B':2},
'404':{'242':4},
'161':{'1133':2,'161':2,'242':2,'323-B':2},
'1133':{'1133':1,'161':1,'242':1,'323-A':1,'323-B':1},
'323-B':{'1133':2,'161':2,'323-A':2},
}
assert M==expected,(M,expected)
# underlying simple graph, loops omitted
G={x:set() for x in expected}
for x,row in expected.items():
    for y in row:
        if x!=y:G[x].add(y);G[y].add(x)
assert {x:len(G[x]) for x in G}=={'242':4,'323-A':3,'404':1,'161':3,'1133':4,'323-B':3}
# all-pairs BFS diameter
D=0
for s in G:
    dist={s:0}; qq=deque([s])
    while qq:
        x=qq.popleft()
        for y in G[x]:
            if y not in dist:dist[y]=dist[x]+1;qq.append(y)
    assert len(dist)==6; D=max(D,max(dist.values()))
assert D==3
assert [x for x in G if len(G[x])==1]==['404']
assert {x for x,row in expected.items() if x in row}=={'1133','161'}
print('VERIFY_OK classes=6 flip_counts=242:7,323-A:6,404:4,161:8,1133:5,323-B:6 underlying_edges=9 diameter=3 leaf=404 self_flip_types=1133,161')
