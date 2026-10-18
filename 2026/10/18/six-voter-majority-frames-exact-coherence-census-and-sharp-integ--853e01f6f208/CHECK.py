from itertools import combinations, permutations, product
from collections import Counter

N=6
U=set(range(N))
TRIPLES=[frozenset(x) for x in combinations(range(N),3) if 0 in x]
ALL3=[frozenset(x) for x in combinations(range(N),3)]
COMPLEMENTS=[frozenset(U-t) for t in TRIPLES]
assert len(TRIPLES)==10
PERMS=list(permutations(range(N)))

def chosen(mask):
    return {TRIPLES[i] if mask&(1<<i) else COMPLEMENTS[i] for i in range(10)}

def mask_of(ch):
    return sum(1<<i for i,t in enumerate(TRIPLES) if t in ch)

def action(mask,perm):
    return mask_of({frozenset(perm[i] for i in t) for t in chosen(mask)})

def balanced4(mask):
    cs=list(chosen(mask))
    for quad in combinations(cs,4):
        if all(sum(i in t for t in quad)==2 for i in U):
            return tuple(''.join(str(i+1) for i in sorted(t)) for t in quad)
    return None

def weighted_mask(w,require_full=True):
    total=sum(w)
    if require_full:
        for sub in (t for r in range(3) for t in combinations(U,r)):
            if 2*sum(w[i] for i in sub)>=total: return None
        for sub in (t for r in range(4,7) for t in combinations(U,r)):
            if 2*sum(w[i] for i in sub)<=total: return None
    mm=0
    for i,t in enumerate(TRIPLES):
        d=2*sum(w[j] for j in t)-total
        if d==0: return None
        if d>0:mm|=1<<i
    return mm

ALL=set(range(1024)); orbits=[]; remaining=set(ALL)
while remaining:
    rep=min(remaining)
    orbit={action(rep,p) for p in PERMS}
    assert orbit<=remaining
    remaining-=orbit
    orbits.append((rep,orbit))
assert not remaining and len(orbits)==13
assert sum(map(lambda e:len(e[1]),orbits))==1024

WIT={}
for w in product(range(1,5),repeat=6):
    mask=weighted_mask(w)
    if mask is not None and mask not in WIT: WIT[mask]=w
WIT3={}
for w in product(range(1,4),repeat=6):
    mask=weighted_mask(w)
    if mask is not None and mask not in WIT3: WIT3[mask]=w
assert len(WIT)==332,(len(WIT),len(WIT3))
assert len(WIT3)<332

result=[]
for rep,orbit in orbits:
    weighted=rep in WIT
    all_bal=[balanced4(mm) for mm in orbit]
    if weighted:
        assert orbit<=set(WIT)
        assert not any(all_bal)
    else:
        assert orbit.isdisjoint(WIT)
        assert all(all_bal)
    result.append((rep,len(orbit),weighted,WIT.get(rep),balanced4(rep)))
assert Counter((s for _,s,y,_,_ in result if y))==Counter({6:2,20:1,60:2,180:1})
assert sum(s for _,s,y,_,_ in result if y)==332
assert sum(s for _,s,y,_,_ in result if not y)==692
assert sum(y for _,_,y,_,_ in result)==6
assert sum(not y for _,_,y,_,_ in result)==7
assert 3 not in WIT3 and 3 in WIT
print('all 1024 orientations partition into 13 orbits; weighted=332 in six orbits; nonweighted=692 in seven orbits')
for r in result:print(r)
print('weighted masks max weights <=3',len(WIT3), 'max <=4',len(WIT))
