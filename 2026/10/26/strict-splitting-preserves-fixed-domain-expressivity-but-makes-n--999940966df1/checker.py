"""Finite checks for strict and lax splitting in nonemptiness team semantics."""
from functools import lru_cache
from itertools import combinations, product

# A flat classical subformula is represented by its set of satisfying rows.
TOP=('TOP',)
NE=('NE',)
def AND(a,b): return ('AND',a,b)
def OR(a,b): return ('OR',a,b)
def FLAT(s): return ('FLAT',s)

@lru_cache(None)
def eval_team(phi, team, strict):
    op=phi[0]
    if op=='TOP': return True
    if op=='NE': return team!=0
    if op=='FLAT': return team & ~phi[1] == 0
    if op=='AND': return eval_team(phi[1],team,strict) and eval_team(phi[2],team,strict)
    if op=='OR':
        sub=team
        while True:
            if eval_team(phi[1],sub,strict):
                if strict:
                    if eval_team(phi[2],team^sub,strict): return True
                else:
                    sub2=team
                    while True:
                        if (sub|sub2)==team and eval_team(phi[2],sub2,strict):return True
                        if sub2==0:break
                        sub2=(sub2-1)&team
            if sub==0:break
            sub=(sub-1)&team
        return False
    raise RuntimeError(op)

def hit(edge):return OR(AND(NE,FLAT(edge)),TOP)
def all_hit(edges):
    p=TOP
    for e in edges:p=AND(p,hit(e))
    return p

def partition_possible(n,edges):
    full=(1<<n)-1
    for red in range(1<<n):
        blue=full^red
        if all(red&e and blue&e for e in edges):return True
    return False

for n in range(2,6):
    triples=[sum(1<<i for i in e) for e in combinations(range(n),3)]
    tests=0
    for subset in range(1<<len(triples)):
        edges=[triples[j] for j in range(len(triples)) if subset>>j&1]
        phi=all_hit(edges)
        theory=OR(phi,phi)
        got=eval_team(theory,(1<<n)-1,True)
        assert got==partition_possible(n,edges),(n,subset)
        assert eval_team(theory,(1<<n)-1,False)
        tests+=1
    print('hypergraphs',n,tests,'strict reduction sound')
# Fano plane (projective PG(2,2)) is not two-colorable.
fano=[{0,1,2},{0,3,4},{0,5,6},{1,3,5},{1,4,6},{2,3,6},{2,4,5}]
phi=all_hit([sum(1<<i for i in e) for e in fano])
assert not eval_team(OR(phi,phi),127,True)
assert eval_team(OR(phi,phi),127,False)
print('Fano strict false/lax true')
# Counting closure under finite-domain strict split plus intersection.
for m in (1,2,3):
    subsets=range(1<<m)
    d=set()
    for B in subsets:
        d.add(sum(1<<T for T in subsets if (T & ~B)==0))
    d.add(sum(1<<T for T in subsets if T))
    def combo(x,y):
        ans=0
        for T in subsets:
            sub=T
            while True:
                if (x>>sub)&1 and (y>>(T^sub))&1:
                    ans|=1<<T;break
                if sub==0:break
                sub=(sub-1)&T
        return ans
    while True:
        old=list(d)
        for i,x in enumerate(old):
            for y in old[:i+1]:
                d.add(x&y)
                d.add(combo(x,y))
        if len(d)==len(old):break
    expected=set()
    for mask in range(1<<(1<<m)):
        fam=[s for s in subsets if (mask>>s)&1]
        if (all((a|b) in fam for a in fam for b in fam) and
            all(z in fam for a in fam for b in fam if (a&b)==a for z in subsets if (a&z)==a and (z&b)==z)):
            expected.add(mask)
    assert d==expected,(m,len(d),len(expected))
    print('finite domain',m,'expressible properties',len(d),'convex/union closed',len(expected))
# Nonlocality: if the ambient domain contains two different valuations
# both satisfying p, then (p AND NE) OR (p AND NE) is strict true.
p_ne=AND(NE,FLAT(3))
assert eval_team(OR(p_ne,p_ne),3,True)
assert not eval_team(OR(p_ne,p_ne),1,True)
print('nonlocality witness okay')
print('ALL_CHECKS_OK')
