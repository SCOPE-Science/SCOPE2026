#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter

N=6
V=list(range(1<<N))

def bits(x):
    return {i for i in range(N) if (x>>i)&1}

def wt(x): return x.bit_count()

def dz(x,y):
    X,Y=bits(x),bits(y)
    return max(len(X-Y),len(Y-X))

def zball(x):
    out={x}
    for i in range(N):
        if (x>>i)&1:
            out.add(x & ~(1<<i))
    return frozenset(out)

balls={x:zball(x) for x in V}

def compatible_a(x,y): return dz(x,y)>=2

def compatible_b(x,y): return balls[x].isdisjoint(balls[y])
for x,y in combinations(V,2):
    assert compatible_a(x,y)==compatible_b(x,y)

adj={x:set() for x in V}
for x,y in combinations(V,2):
    if compatible_a(x,y):
        adj[x].add(y); adj[y].add(x)
edges=sum(map(len,adj.values()))//2

maximal=[]
def bronk(R,P,X):
    if not P and not X:
        maximal.append(frozenset(R)); return
    U=P|X
    u=max(U,key=lambda z:len(P&adj[z])) if U else None
    for v in list(P-(adj[u] if u is not None else set())):
        bronk(R|{v},P&adj[v],X&adj[v])
        P.remove(v); X.add(v)
bronk(set(),set(V),set())
hist=Counter(map(len,maximal))
maximum=max(hist)
maxima={C for C in maximal if len(C)==maximum}
assert maximum==12 and len(maxima)==30

# Independent increasing-order fixed-size clique enumeration.
def k_cliques(k):
    out=[]
    def rec(prefix,cands):
        if len(prefix)==k:
            out.append(frozenset(prefix)); return
        need=k-len(prefix)
        if len(cands)<need: return
        while cands:
            v=cands[0]; cands=cands[1:]
            nxt=[u for u in cands if u in adj[v]]
            rec(prefix+[v],nxt)
    rec([],V[:])
    return out
k12=set(k_cliques(12))
assert k12==maxima and len(k12)==30
assert len(k_cliques(13))==0

# Perfect matchings of six labeled coordinate positions.
def matchings(items):
    items=tuple(items)
    if not items:
        yield (); return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        rest=items[1:j]+items[j+1:]
        for tail in matchings(rest):
            yield tuple(sorted(((min(a,b),max(a,b)),)+tail))
M=sorted(set(matchings(range(N))))
assert len(M)==15

def word(pos):
    z=0
    for i in pos: z |= 1<<i
    return z

def code_from_matching(m,parity):
    common={0,(1<<N)-1}
    for a,b in m:
        e=word((a,b)); common.add(e); common.add(((1<<N)-1)^e)
    trans=[]
    for mask in range(8):
        sel=[]
        for j,(a,b) in enumerate(m):
            sel.append(b if ((mask>>j)&1) else a)
        if (mask.bit_count()&1)==parity:
            trans.append(word(sel))
    C=frozenset(common|set(trans))
    assert len(C)==12
    assert all(compatible_a(x,y) for x,y in combinations(C,2))
    return C
constructed={code_from_matching(m,p) for m in M for p in (0,1)}
assert len(constructed)==30 and constructed==maxima

published=frozenset(int(s,2) for s in [
 '000000','000011','001100','001111','010101','011010',
 '100110','101001','110000','110011','111100','111111'])
assert published in maxima

expected_w=(1,0,3,4,3,0,1)
for C in maxima:
    assert 0 in C and 63 in C
    wh=tuple(sum(wt(x)==j for x in C) for j in range(7))
    assert wh==expected_w
    union=set().union(*(balls[x] for x in C))
    assert len(union)==48 and 64-len(union)==16
    w2=[x for x in C if wt(x)==2]
    supp=[bits(x) for x in w2]
    assert len(w2)==3 and set().union(*supp)==set(range(6))
    assert all(a.isdisjoint(b) for a,b in combinations(supp,2))
    assert {63^x for x in w2}=={x for x in C if wt(x)==4}

# Coordinate-permutation action.
def permute_word(x,p):
    y=0
    for i in range(N):
        if (x>>i)&1: y |= 1<<p[i]
    return y
perms=list(permutations(range(N)))
assert len(perms)==720
orbit={frozenset(permute_word(x,p) for x in published) for p in perms}
assert orbit==maxima
stabilizer=sum(frozenset(permute_word(x,p) for x in published)==published for p in perms)
assert stabilizer==24

hs=','.join(f'{k}:{hist[k]}' for k in sorted(hist))
print('VERIFY_OK',
      f'vertices={len(V)}',f'edges={edges}',f'maximal_hist={hs}',
      f'maximum={maximum}',f'labeled_maxima={len(maxima)}',
      f'independent_12cliques={len(k12)}', 'no_13_clique=true',
      f'matching_constructions={len(constructed)}',
      'weight_distribution=1,0,3,4,3,0,1', 'free_points=16',
      'coordinate_group=720','orbits=1','orbit_size=30',f'stabilizer={stabilizer}')
