#!/usr/bin/env python3
"""Independent Latin-square and pairwise-move verifier, Python stdlib only."""
from itertools import product, combinations, permutations
from collections import Counter, deque

cells=[(r,c) for r in range(4) for c in range(4)]
# The Shrikhande graph is the complement of the cyclic Latin-square graph.
edge=set()
for i,j in combinations(range(16),2):
    r,c=cells[i];s,d=cells[j]
    if r!=s and c!=d and (r+c-s-d)%4!=0:edge.add((i,j))
def adj(i,j):return tuple(sorted((i,j))) in edge if i!=j else False
assert len(edge)==48
ind=[]
for t in combinations(range(16),4):
    if not any(adj(i,j) for i,j in combinations(t,2)):ind.append(frozenset(t))
assert len(ind)==16
assert not any(all(not adj(i,j) for i,j in combinations(t,2)) for t in combinations(range(16),5))
classes={}
for z in ind:
    coord=[cells[i] for i in z]
    r={x for x,y in coord};c={y for x,y in coord};s={(x+y)%4 for x,y in coord}
    if len(r)==1:tag='R'+str(next(iter(r)))
    elif len(c)==1:tag='C'+str(next(iter(c)))
    elif len(s)==1:tag='S'+str(next(iter(s)))
    else:
        assert len({x%2 for x,y in coord})==1 and len({y%2 for x,y in coord})==1
        tag='I'+str(next(iter(r))%2)+str(next(iter(c))%2)
    classes[z]=tag
assert Counter(t[0] for t in classes.values())=={'R':4,'C':4,'S':4,'I':4}

# Exact-cover enumeration using a different recursion from the first checker.
pools={i:[x for x in ind if i in x] for i in range(16)}
part=[]
def walk(uncovered, pieces):
    if not uncovered:
        if len(pieces)==4:part.append(tuple(pieces))
        return
    best=min(uncovered,key=lambda i:sum(z<=uncovered for z in pools[i]))
    for z in pools[best]:
        if z<=uncovered:walk(uncovered-z,pieces+[z])
walk(frozenset(range(16)),[])
part=[tuple(sorted(p,key=lambda z:classes[z])) for p in part]
assert len(part)==10 and len({frozenset(p) for p in part})==10

# Construct 240 colour assignments directly from each exact cover.
col=[]
for p in part:
    for pi in permutations(range(4)):
        f=tuple(next(pi[j] for j,z in enumerate(p) if v in z) for v in range(16))
        col.append(f)
col=sorted(set(col));assert len(col)==240

def induced_components(f,a,b):
    unseen={v for v in range(16) if f[v] in (a,b)}
    comps=[]
    while unseen:
        seed=unseen.pop(); todo=[seed]; comp={seed}
        while todo:
            w=todo.pop()
            for u in tuple(unseen):
                if adj(w,u):unseen.remove(u);comp.add(u);todo.append(u)
        comps.append(frozenset(comp))
    return comps

# Direct pairwise recognition, NOT generation by moves.
A=[set() for _ in col]
for i,j in combinations(range(len(col)),2):
    f,g=col[i],col[j]
    changed={v for v in range(16) if f[v]!=g[v]}
    if not changed:continue
    involved={f[v] for v in changed}|{g[v] for v in changed}
    if len(involved)!=2:continue
    a,b=sorted(involved)
    if any({f[v],g[v]}!={a,b} for v in changed):continue
    if frozenset(changed) in induced_components(f,a,b):
        A[i].add(j);A[j].add(i)
assert sum(len(s) for s in A)//2==1008
assert Counter(map(len,A))=={8:216,12:24}

hist=Counter();ecc=Counter()
for i in range(240):
    D=[-1]*240;D[i]=0;todo=deque([i])
    while todo:
        j=todo.popleft()
        for k in A[j]:
            if D[k]<0:D[k]=D[j]+1;todo.append(k)
    assert all(x>=0 for x in D)
    ecc[max(D)]+=1
    hist.update(D[j] for j in range(i+1,240))
assert ecc=={4:168,5:72} and hist=={1:1008,2:5400,3:13416,4:8280,5:576}

# Quotient edges, independently reconstructed from the pairwise full adjacency.
pid={frozenset(p):k for k,p in enumerate(part)}
def cls(f):return pid[frozenset(frozenset(v for v in range(16) if f[v]==a) for a in range(4))]
Q=set()
for i,j in combinations(range(240),2):
    if j not in A[i]:continue
    u,v=cls(col[i]),cls(col[j])
    if u!=v:Q.add(tuple(sorted((u,v))))
assert len(Q)==12
NG=[set() for _ in part]
for u,v in Q:NG[u].add(v);NG[v].add(u)
assert Counter(map(len,NG))=={2:9,6:1}
center=next(i for i in range(10) if len(NG[i])==6)
assert [classes[z][0] for z in part[center]].count('I')==4
# The three petal cycles each contain one pure-coordinate partition.
for typ in 'RCS':
    pure=next(i for i,p in enumerate(part) if all(classes[x].startswith(typ) for x in p))
    a,b=sorted(NG[pure]);assert center in NG[a] and center in NG[b]
assert len({next(i for i,p in enumerate(part) if all(classes[z].startswith(typ) for z in p)) for typ in 'RCS'})==3
# Explicit certificate that the Latin model equals the standard Cayley graph up to relabeling.
iso=(0,5,10,15,9,14,3,4,2,7,8,13,11,12,1,6)
assert set(iso)==set(range(16))
diffs={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
for i,j in combinations(range(16),2):
    r,c=cells[i];s,d=cells[j]
    assert (((r-s)%4,(c-d)%4) in diffs)==adj(iso[i],iso[j])

print('LATIN_PAIRWISE_KEMPE_PASS')
print('maxind_RCSI=4,4,4,4 exact_covers=10 named=240')
print('named_edges=1008 radius=4 diameter=5 hist=1008,5400,13416,8280,576')
print('quotient=three_C4_petals_with_all_intercalates_at_hub')
