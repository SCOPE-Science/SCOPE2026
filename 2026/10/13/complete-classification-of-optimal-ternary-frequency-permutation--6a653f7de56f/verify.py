#!/usr/bin/env python3
import itertools, collections, hashlib, json

def hdist(a,b): return sum(x!=y for x,y in zip(a,b))
words=sorted(set(itertools.permutations((0,0,1,1,2,2))))
assert len(words)==90
idx={w:i for i,w in enumerate(words)}
adj=[set() for _ in words]
for i in range(90):
    for j in range(i+1,90):
        if hdist(words[i],words[j])>=4:
            adj[i].add(j); adj[j].add(i)
assert sum(map(len,adj))//2==2745
# Bron-Kerbosch with pivot; enumerate all maximal cliques.
maximal=[]
def bk(R,P,X):
    if not P and not X:
        maximal.append(tuple(sorted(R))); return
    U=P|X
    u=max(U,key=lambda v: len(P & adj[v])) if U else None
    cand=sorted(P - (adj[u] if u is not None else set()))
    for v in cand:
        bk(R|{v}, P & adj[v], X & adj[v])
        P.remove(v); X.add(v)
bk(set(),set(range(90)),set())
count=collections.Counter(map(len,maximal))
assert count=={6:38895,7:20160,8:20520,9:10320,11:720,15:12}, count
maxima=sorted(c for c in maximal if len(c)==15)
assert len(maxima)==12
# Direct pairwise check and distance distribution.
for C in maxima:
    assert all(hdist(words[i],words[j])>=4 for i,j in itertools.combinations(C,2))
    for p in range(6):
        assert collections.Counter(words[i][p] for i in C)=={0:5,1:5,2:5}
D=collections.Counter(hdist(words[i],words[j]) for i,j in itertools.combinations(maxima[0],2))
assert D=={4:90,6:15}, D
# Natural group S_6 on coordinates and S_3 on symbols.
coord=list(itertools.permutations(range(6)))
sym=list(itertools.permutations(range(3)))
def trword(w,cp,sp): return tuple(sp[w[cp[p]]] for p in range(6))
def trcode(C,cp,sp): return tuple(sorted(idx[trword(words[i],cp,sp)] for i in C))
rep=maxima[0]; orbit=set(); stab=0
for cp in coord:
    for sp in sym:
        T=trcode(rep,cp,sp); orbit.add(T)
        if T==rep: stab+=1
assert len(coord)*len(sym)==4320
assert len(orbit)==12 and stab==360 and orbit==set(maxima)
rep_words=[''.join(map(str,words[i])) for i in rep]
canon='\n'.join(','.join(''.join(map(str,words[i])) for i in C) for C in maxima).encode()
sha=hashlib.sha256(canon).hexdigest()
out={
 'vertices':90,'compatibility_edges':2745,'maximal_cliques':len(maximal),
 'maximal_clique_size_distribution':dict(sorted(count.items())),
 'maximum':15,'maximum_codes':12,'natural_group_order':4320,
 'orbits':1,'orbit_size':12,'stabilizer':360,
 'representative':rep_words,'representative_distance_distribution':dict(sorted(D.items())),
 'coordinate_symbol_counts':[5,5,5],'census_sha256':sha}
print('VERIFY_OK '+json.dumps(out,sort_keys=True,separators=(',',':')))
