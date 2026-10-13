#!/usr/bin/env python3
from itertools import permutations, product
from math import factorial
from fractions import Fraction
from collections import Counter

CANDS=(0,1,2)
RANKS=tuple(permutations(CANDS))
RIDX={r:i for i,r in enumerate(RANKS)}

def comps(k,n,p=()):
    if k==1:
        yield p+(n,); return
    for x in range(n+1):
        yield from comps(k-1,n-x,p+(x,))

def multinom(c):
    z=factorial(sum(c))
    for x in c: z//=factorial(x)
    return z

def generic_put(counts, mode, active=CANDS):
    active=tuple(active)
    if len(active)==1: return frozenset(active)
    score={a:0 for a in active}
    for m,r in zip(counts,RANKS):
        if not m: continue
        rr=[a for a in r if a in active]
        if mode=='STV': score[rr[0]] += m
        elif mode=='COOMBS': score[rr[-1]] -= m
        else: raise ValueError(mode)
    lo=min(score.values())
    losers=[a for a,v in score.items() if v==lo]
    out=set()
    for e in losers:
        out |= set(generic_put(counts, mode, tuple(a for a in active if a!=e)))
    return frozenset(out)

def pairwise(counts,a,b):
    va=sum(m for m,r in zip(counts,RANKS) if r.index(a)<r.index(b))
    vb=sum(counts)-va
    if va>vb:return a
    if vb>va:return b
    return None

def direct_three(counts, mode):
    # Independent closed three-candidate formulation: identify every tied first-round loser,
    # then take the pairwise winner of the two survivors; a tied head-to-head returns both.
    if mode=='STV':
        s={a:sum(m for m,r in zip(counts,RANKS) if r[0]==a) for a in CANDS}
        target=min(s.values()); losers=[a for a,v in s.items() if v==target]
    elif mode=='COOMBS':
        s={a:sum(m for m,r in zip(counts,RANKS) if r[-1]==a) for a in CANDS}
        target=max(s.values()); losers=[a for a,v in s.items() if v==target]
    else: raise ValueError(mode)
    out=set()
    for e in losers:
        surv=[a for a in CANDS if a!=e]
        w=pairwise(counts,*surv)
        if w is None: out.update(surv)
        else: out.add(w)
    return frozenset(out)

def relabel_counts(c,p):
    out=[0]*6
    for r,m in zip(RANKS,c):
        rr=tuple(p[a] for a in r)
        out[RIDX[rr]] += m
    return tuple(out)

def canonical(c):
    return min(relabel_counts(c,p) for p in permutations(CANDS))

def condorcet_winner(c):
    for a in CANDS:
        if all(a==b or pairwise(c,a,b)==a for b in CANDS): return a
    return None

anon_counts={}; labeled_counts={}; unique_both={}
first_pats=[]
for n in range(1,6):
    ac=lc=ub=0
    for c in comps(6,n):
        for mode in ('STV','COOMBS'):
            assert generic_put(c,mode)==direct_three(c,mode)
        s=generic_put(c,'STV'); q=generic_put(c,'COOMBS')
        w=multinom(c)
        if len(s)==len(q)==1:
            ub += w
            if s!=q:
                ac += 1; lc += w
                if n==5:first_pats.append(c)
    anon_counts[n]=ac; labeled_counts[n]=lc; unique_both[n]=ub

assert anon_counts=={1:0,2:0,3:0,4:0,5:6}
assert labeled_counts=={1:0,2:0,3:0,4:0,5:180}
assert unique_both=={1:6,2:12,3:132,4:576,5:6516}
assert Fraction(180,6**5)==Fraction(5,216)
assert Fraction(180,6516)==Fraction(5,181)
assert Fraction(6,252)==Fraction(1,42)

# Direct labeled replay, independent of multinomial weighting.
for n in range(1,6):
    cnt=0
    for prof in product(range(6), repeat=n):
        c=[0]*6
        for i in prof:c[i]+=1
        s=generic_put(tuple(c),'STV'); q=generic_put(tuple(c),'COOMBS')
        if len(s)==len(q)==1 and s!=q: cnt+=1
    assert cnt==labeled_counts[n]

orbits=Counter(canonical(c) for c in first_pats)
assert len(orbits)==1 and next(iter(orbits.values()))==6
rep=next(iter(orbits))
# Canonical representative under our fixed ranking order.
assert rep==(0,1,2,0,2,0)
stv=generic_put(rep,'STV'); co=generic_put(rep,'COOMBS')
assert stv==frozenset({2}) and co==frozenset({0})
assert condorcet_winner(rep)==0
# Every one of the six anonymous conflicts has Coombs selecting the Condorcet winner.
for c in first_pats:
    cw=condorcet_winner(c)
    assert cw is not None
    assert generic_put(c,'COOMBS')==frozenset({cw})
    assert generic_put(c,'STV')!=frozenset({cw})

# Canonical first/last-place and pairwise data.
first={a:sum(m for m,r in zip(rep,RANKS) if r[0]==a) for a in CANDS}
last={a:sum(m for m,r in zip(rep,RANKS) if r[-1]==a) for a in CANDS}
pw={(a,b):(sum(m for m,r in zip(rep,RANKS) if r.index(a)<r.index(b)),
           sum(m for m,r in zip(rep,RANKS) if r.index(b)<r.index(a)))
    for a in CANDS for b in CANDS if a<b}
assert first=={0:1,1:2,2:2}
assert last=={0:0,1:3,2:2}
assert pw=={(0,1):(3,2),(0,2):(3,2),(1,2):(2,3)}

print('VERIFY_OK')
print('anonymous_disagreements',anon_counts)
print('labeled_disagreements',labeled_counts)
print('unique_both_labeled',unique_both)
print('unconditional_incidence',Fraction(180,6**5))
print('conditional_incidence',Fraction(180,6516))
print('anonymous_incidence',Fraction(6,252))
print('anonymous_orbits',dict(orbits))
print('canonical_profile',rep)
print('ranking_order',RANKS)
print('STV_winner',next(iter(stv)),'Coombs_winner',next(iter(co)),'Condorcet_winner',condorcet_winner(rep))
print('first_counts',first,'last_counts',last,'pairwise',pw)
