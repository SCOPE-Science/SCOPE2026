#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter

def stable_rankmap(mp, wp):
    n=len(mp)
    mr=[{w:i+1 for i,w in enumerate(p)} for p in mp]
    wr=[{m:i+1 for i,m in enumerate(p)} for p in wp]
    out=[]
    for M in permutations(range(n)):
        inv=[0]*n
        for m,w in enumerate(M): inv[w]=m
        ok=True
        for m in range(n):
            for w in range(n):
                if M[m]==w: continue
                if mr[m][w] < mr[m][M[m]] and wr[w][m] < wr[w][inv[w]]:
                    ok=False
                    break
            if not ok: break
        if ok:
            ranks=tuple(mr[m][M[m]] for m in range(n))+tuple(wr[w][inv[w]] for w in range(n))
            out.append((M,ranks))
    return tuple(out)

def stable_listindex(mp, wp):
    n=len(mp)
    out=[]
    for M in permutations(range(n)):
        inv=[0]*n
        for m,w in enumerate(M): inv[w]=m
        ok=True
        for m in range(n):
            for w in range(n):
                if M[m]==w: continue
                if mp[m].index(w) < mp[m].index(M[m]) and wp[w].index(m) < wp[w].index(inv[w]):
                    ok=False
                    break
            if not ok: break
        if ok:
            ranks=tuple(mp[m].index(M[m])+1 for m in range(n))+tuple(wp[w].index(inv[w])+1 for w in range(n))
            out.append((M,ranks))
    return tuple(out)

def profile(ranks,n):
    return tuple(ranks.count(k) for k in range(1,n+1))

def rankmax_profile(stable,n):
    sig={M:profile(r,n) for M,r in stable}
    best=max(sig.values())
    return {M for M,s in sig.items() if s==best},sig

def rankmax_steep(stable,n):
    # There are 2n agents, so base 2n+1 encodes lexicographic profile exactly.
    B=2*n+1
    score={}
    for M,r in stable:
        score[M]=sum(B**(n-x) for x in r)
    best=max(score.values())
    return {M for M,v in score.items() if v==best}

def egal_direct(stable):
    cost={M:sum(r) for M,r in stable}
    best=min(cost.values())
    return {M for M,c in cost.items() if c==best},cost

def egal_profile(stable,n):
    sig={M:profile(r,n) for M,r in stable}
    cost={M:sum((k+1)*s[k] for k in range(n)) for M,s in sig.items()}
    best=min(cost.values())
    return {M for M,c in cost.items() if c==best}

def relation(R,E):
    if R==E:return "equal"
    if R<E:return "rankmax_subset_egalitarian"
    if E<R:return "egalitarian_subset_rankmax"
    if R&E:return "overlap_nonnested"
    return "disjoint"

# n=2 complete strict domain.
orders2=list(permutations(range(2)))
h2=Counter(); sh2=Counter()
for mp in product(orders2, repeat=2):
    for wp in product(orders2, repeat=2):
        A=stable_rankmap(mp,wp); B=stable_listindex(mp,wp); assert A==B
        sh2[len(A)]+=1
        R1,_=rankmax_profile(A,2); R2=rankmax_steep(A,2); assert R1==R2
        E1,_=egal_direct(A); E2=egal_profile(A,2); assert E1==E2
        h2[relation(R1,E1)] += 1
assert h2==Counter({"equal":16})
assert sh2==Counter({1:14,2:2})

# n=3 complete strict domain.
orders3=list(permutations(range(3)))
h3=Counter(); sh3=Counter(); detail=Counter()
witness=None
for mp in product(orders3, repeat=3):
    for wp in product(orders3, repeat=3):
        A=stable_rankmap(mp,wp); B=stable_listindex(mp,wp); assert A==B
        sh3[len(A)]+=1
        R1,sig=rankmax_profile(A,3); R2=rankmax_steep(A,3); assert R1==R2
        E1,cost=egal_direct(A); E2=egal_profile(A,3); assert E1==E2
        rel=relation(R1,E1)
        h3[rel]+=1
        detail[(rel,len(A),len(R1),len(E1))]+=1
        if rel=="disjoint" and witness is None:
            witness=(mp,wp,A,R1,E1,sig,cost)

assert sh3==Counter({1:34080,2:11484,3:1092})
assert h3==Counter({
    "equal":42756,
    "rankmax_subset_egalitarian":2928,
    "disjoint":972,
})
assert detail[("disjoint",2,1,1)]==720
assert detail[("disjoint",3,1,1)]==144
assert detail[("disjoint",3,1,2)]==72
assert detail[("disjoint",3,2,1)]==36
assert detail[("rankmax_subset_egalitarian",2,1,2)]==2304
assert detail[("rankmax_subset_egalitarian",3,1,2)]==216
assert detail[("rankmax_subset_egalitarian",3,1,3)]==216
assert detail[("rankmax_subset_egalitarian",3,2,3)]==192

mp,wp,A,R,E,sig,cost=witness
assert mp==((0,1,2),(0,1,2),(1,2,0))
assert wp==((2,0,1),(1,0,2),(0,2,1))
assert A==(
    ((0,1,2),(1,2,2,2,1,2)),
    ((2,1,0),(3,2,3,1,1,1)),
)
assert R=={(2,1,0)}
assert E=={(0,1,2)}
assert sig[(0,1,2)]==(2,4,0)
assert sig[(2,1,0)]==(3,1,2)
assert cost[(0,1,2)]==10
assert cost[(2,1,0)]==11

print("VERIFY_OK")
print("n2_relation_hist",dict(h2))
print("n2_stable_count_hist",dict(sh2))
print("n3_relation_hist",dict(h3))
print("n3_stable_count_hist",dict(sh3))
print("n3_disagreement",3900,"of",6**6,"=", "325/3888")
print("n3_disjoint",972,"of",6**6,"=","1/48")
print("witness_men",mp)
print("witness_women",wp)
print("witness_stable",A)
print("witness_rankmax",sorted(R))
print("witness_egalitarian",sorted(E))
print("witness_signatures",sig)
print("witness_costs",cost)
