#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
from math import factorial

C = (0,1,2)
BALLOTS = tuple(permutations(C))
BINDEX = {b:i for i,b in enumerate(BALLOTS)}

def pairwise(profile):
    s=[[0]*3 for _ in range(3)]
    for ballot in profile:
        pos={c:i for i,c in enumerate(ballot)}
        for a in C:
            for b in C:
                if a!=b and pos[a] < pos[b]:
                    s[a][b]+=1
    return s

def borda_position(profile):
    sc=[0,0,0]
    for ballot in profile:
        for pos,c in enumerate(ballot):
            sc[c] += 2-pos
    best=max(sc)
    return frozenset(i for i,x in enumerate(sc) if x==best), tuple(sc)

def borda_pairwise(profile):
    s=pairwise(profile)
    sc=tuple(sum(s[a][b] for b in C if b!=a) for a in C)
    best=max(sc)
    return frozenset(i for i,x in enumerate(sc) if x==best), sc

def sign(x):
    return (x>0)-(x<0)

def copeland_direct(profile):
    s=pairwise(profile)
    sc=[]
    for a in C:
        v=Fraction(0)
        for b in C:
            if a==b: continue
            if s[a][b]>s[b][a]: v+=1
            elif s[a][b]==s[b][a]: v+=Fraction(1,2)
        sc.append(v)
    best=max(sc)
    return frozenset(i for i,x in enumerate(sc) if x==best), tuple(sc)

def copeland_margin(profile):
    s=pairwise(profile)
    sc=[]
    for a in C:
        total=sum(sign(s[a][b]-s[b][a]) for b in C if b!=a)
        sc.append(Fraction(2+total,2))
    best=max(sc)
    return frozenset(i for i,x in enumerate(sc) if x==best), tuple(sc)

def relation(B,K):
    if B==K: return 'equal'
    if B<K: return 'borda_subset_copeland'
    if K<B: return 'copeland_subset_borda'
    if B & K: return 'overlap_nonnested'
    return 'disjoint'

def compositions(total,parts,prefix=()):
    if parts==1:
        yield prefix+(total,)
    else:
        for x in range(total+1):
            yield from compositions(total-x,parts-1,prefix+(x,))

def expand_counts(counts):
    p=[]
    for k,b in zip(counts,BALLOTS):
        p.extend([b]*k)
    return tuple(p)

def multinomial(counts):
    ans=factorial(sum(counts))
    for x in counts: ans//=factorial(x)
    return ans

def relabel_counts(counts,p):
    out=[0]*6
    for k,b in zip(counts,BALLOTS):
        rb=tuple(p[x] for x in b)
        out[BINDEX[rb]] += k
    return tuple(out)

def canonical_counts(counts):
    return min(relabel_counts(counts,p) for p in permutations(C))

def relabel_profile(profile,p):
    return tuple(tuple(p[x] for x in b) for b in profile)

expected={
1:Counter({('equal',1,1):6}),
2:Counter({('equal',1,1):24,('equal',2,2):6,('equal',3,3):6}),
3:Counter({('equal',1,1):186,('copeland_subset_borda',2,1):18,('equal',3,3):12}),
4:Counter({('equal',1,1):972,('equal',2,2):162,('equal',3,3):90,('borda_subset_copeland',1,2):72}),
5:Counter({('equal',1,1):6396,('copeland_subset_borda',2,1):780,('equal',3,3):360,('borda_subset_copeland',1,3):180,('disjoint',1,1):60}),
}

hist={}
conflict_profiles=[]
for n in range(1,6):
    h=Counter()
    for profile in product(BALLOTS, repeat=n):
        B1,bs1=borda_position(profile)
        B2,bs2=borda_pairwise(profile)
        assert B1==B2 and bs1==bs2
        C1,cs1=copeland_direct(profile)
        C2,cs2=copeland_margin(profile)
        assert C1==C2 and cs1==cs2
        r=relation(B1,C1)
        h[(r,len(B1),len(C1))]+=1
        if len(B1)==len(C1)==1 and B1!=C1:
            assert n==5
            conflict_profiles.append(profile)
            cw=next(iter(C1))
            s=pairwise(profile)
            assert all(s[cw][d] > s[d][cw] for d in C if d!=cw)
    hist[n]=h
    assert h==expected[n], (n,h,expected[n])

assert len(conflict_profiles)==60
assert Fraction(60,6**5)==Fraction(5,648)

# Independent anonymous enumeration of five-voter profiles.
anon_conflicts=[]
weighted=0
for counts in compositions(5,6):
    profile=expand_counts(counts)
    B,_=borda_position(profile)
    K,_=copeland_direct(profile)
    if len(B)==len(K)==1 and B!=K:
        anon_conflicts.append(counts)
        weighted += multinomial(counts)
assert len(anon_conflicts)==6
assert weighted==60
assert Fraction(6,252)==Fraction(1,42)

canon=Counter(canonical_counts(c) for c in anon_conflicts)
assert len(canon)==1
canonical=next(iter(canon))
assert canonical==(0,0,0,3,2,0)
assert canon[canonical]==6
orbit={relabel_counts(canonical,p) for p in permutations(C)}
assert orbit==set(anon_conflicts) and len(orbit)==6
assert {multinomial(c) for c in anon_conflicts}=={10}

# Combined candidate/voter relabeling orbit is exactly all 60 labeled conflicts.
rep=expand_counts(canonical)
combined=set()
for p in permutations(C):
    rp=relabel_profile(rep,p)
    for q in permutations(range(5)):
        combined.add(tuple(rp[q[i]] for i in range(5)))
assert len(combined)==60
assert combined==set(conflict_profiles)

B,bs=borda_position(rep)
K,cs=copeland_direct(rep)
s=pairwise(rep)
margins=(s[0][1]-s[1][0], s[0][2]-s[2][0], s[1][2]-s[2][1])
assert bs==(2,6,7)
assert B==frozenset({2})
assert K==frozenset({1})
assert margins==(-1,-5,1)

print('VERIFY_OK')
for n in range(1,6):
    print('n',n,'hist',dict(hist[n]))
print('unique_conflicts',len(conflict_profiles),'of',6**5,'=','5/648')
print('anonymous_unique_conflicts',len(anon_conflicts),'of',252,'=','1/42')
print('anonymous_candidate_orbits',len(canon))
print('canonical_counts',canonical)
print('combined_orbit_size',len(combined))
print('representative_borda_scores',bs,'winner',sorted(B))
print('representative_copeland_scores',cs,'winner',sorted(K))
print('representative_pairwise_margins',margins)
