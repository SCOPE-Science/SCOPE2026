#!/usr/bin/env python3
import itertools, json
from collections import Counter

BASE = tuple(sorted(set(itertools.permutations((0,0,1,1,2,2)))))
INDEX = {w:i for i,w in enumerate(BASE)}
N=len(BASE)

def dist(a,b):
    return sum(x!=y for x,y in zip(a,b))

adj=[0]*N
for i in range(N):
    m=0
    for j in range(N):
        if i!=j and dist(BASE[i],BASE[j])>=4:
            m |= 1<<j
    adj[i]=m

maximal=[]
def bk(R,P,X):
    if not P and not X:
        maximal.append(R)
        return
    U=P|X
    if U:
        # deterministic pivot maximizing neighbors in P
        us=[i for i in range(N) if (U>>i)&1]
        u=max(us,key=lambda z:(adj[z]&P).bit_count())
        cand=P & ~adj[u]
    else:
        cand=P
    while cand:
        b=cand & -cand
        v=b.bit_length()-1
        bk(R|b, P&adj[v], X&adj[v])
        P &= ~b
        X |= b
        cand &= ~b
bk(0,(1<<N)-1,0)
size_counter=Counter(r.bit_count() for r in maximal)
max_size=max(size_counter)
maxima=sorted(r for r in maximal if r.bit_count()==max_size)
assert max_size==15
assert len(maxima)==12
assert size_counter==Counter({6:38895,7:20160,8:20520,9:10320,11:720,15:12})

def matching(w):
    return tuple(sorted(tuple(i for i,x in enumerate(w) if x==a) for a in range(3)))

def members(mask):
    return [i for i in range(N) if (mask>>i)&1]

def fact_signature(mask):
    c=Counter(matching(BASE[i]) for i in members(mask))
    assert sorted(c.values())==[3,3,3,3,3]
    ms=tuple(sorted(c))
    edges=[]
    for M in ms: edges.extend(M)
    assert len(edges)==15 and len(set(edges))==15
    return ms
facts=Counter(fact_signature(m) for m in maxima)
assert len(facts)==6 and set(facts.values())=={2}

# Independently enumerate every labeled 1-factorization of K_6.
all_matchings=sorted(set(matching(w) for w in BASE))
assert len(all_matchings)==15
one_factorizations=[]
for comb in itertools.combinations(all_matchings,5):
    edges=[e for M in comb for e in M]
    if len(set(edges))==15:
        one_factorizations.append(tuple(sorted(comb)))
assert len(one_factorizations)==6
assert set(facts)==set(one_factorizations)

coord_perms=list(itertools.permutations(range(6)))
sym_perms=list(itertools.permutations(range(3)))
maxset=set(maxima)

def transform(mask,cp,sp):
    out=0
    for i in members(mask):
        w=BASE[i]
        z=tuple(sp[w[cp[j]]] for j in range(6))
        out |= 1<<INDEX[z]
    return out
rep=maxima[0]
orb={transform(rep,cp,sp) for cp in coord_perms for sp in sym_perms}
assert orb==maxset
stab=sum(transform(rep,cp,sp)==rep for cp in coord_perms for sp in sym_perms)
assert stab==360 and len(orb)==12 and 4320//stab==12

with open(__file__.replace('verify.py','maxima.json'),encoding='utf-8') as f:
    expected=json.load(f)
actual=[]
for mask in maxima:
    actual.append(sorted(''.join(map(str,BASE[i])) for i in members(mask)))
actual=sorted(actual)
assert actual==sorted(expected['maxima'])
print('VERIFY_OK words=90 maximum=15 labeled_maxima=12 factorizations=6 maxima_per_factorization=2 orbit_size=12 stabilizer=360 maximal_cliques='+str(sum(size_counter.values())))
