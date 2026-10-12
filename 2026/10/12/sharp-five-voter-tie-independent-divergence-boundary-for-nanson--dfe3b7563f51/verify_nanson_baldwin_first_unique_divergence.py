#!/usr/bin/env python3
from itertools import permutations
from functools import lru_cache
from math import factorial
from fractions import Fraction
from collections import Counter

CANDS=(0,1,2,3)
BALLOTS=tuple(permutations(CANDS))
BINDEX={b:i for i,b in enumerate(BALLOTS)}

# Precompute Borda contributions for every surviving-candidate mask.
CONTRIB={}
for mask in range(1,1<<4):
    m=mask.bit_count()
    rows=[]
    for ballot in BALLOTS:
        rb=[x for x in ballot if (mask>>x)&1]
        row=[0]*4
        for pos,x in enumerate(rb):
            row[x]=m-1-pos
        rows.append(tuple(row))
    CONTRIB[mask]=tuple(rows)

def compositions(total, parts, prefix=()):
    if parts==1:
        yield prefix+(total,)
        return
    for x in range(total+1):
        yield from compositions(total-x,parts-1,prefix+(x,))

def multinomial(counts):
    z=factorial(sum(counts))
    for x in counts:
        z//=factorial(x)
    return z

def scores_fast(counts, mask):
    sc=[0,0,0,0]
    for mult,row in zip(counts,CONTRIB[mask]):
        if mult:
            sc[0]+=mult*row[0]
            sc[1]+=mult*row[1]
            sc[2]+=mult*row[2]
            sc[3]+=mult*row[3]
    return tuple(sc)

def baldwin_winner_set_fast(counts):
    # Union of winners over every allowed choice among tied lowest-Borda candidates.
    @lru_cache(None)
    def rec(mask):
        if mask & (mask-1)==0:
            return frozenset({mask.bit_length()-1})
        sc=scores_fast(counts,mask)
        mn=min(sc[i] for i in CANDS if (mask>>i)&1)
        low=[i for i in CANDS if (mask>>i)&1 and sc[i]==mn]
        out=set()
        for x in low:
            out.update(rec(mask^(1<<x)))
        return frozenset(out)
    return rec(15)

def nanson_outcome_fast(counts):
    # Narodytska-Walsh-Xia convention: eliminate all candidates STRICTLY below
    # the average Borda score. If everyone is tied at the average, the process
    # is unresolved; return the surviving set rather than imposing a tiebreak.
    mask=15
    while mask & (mask-1):
        sc=scores_fast(counts,mask)
        alive=[i for i in CANDS if (mask>>i)&1]
        total=sum(sc[i] for i in alive)
        m=len(alive)
        low=[i for i in alive if sc[i]*m < total]
        if not low:
            return frozenset(alive)
        for x in low:
            mask ^= 1<<x
    return frozenset({mask.bit_length()-1})

# Independent slow implementation, using explicit ballot lists and direct Borda recounts.
def expand_profile(counts):
    p=[]
    for mult,b in zip(counts,BALLOTS):
        p.extend([b]*mult)
    return tuple(p)

def slow_scores(profile, alive):
    m=len(alive)
    sc={x:0 for x in alive}
    for ballot in profile:
        rb=[x for x in ballot if x in alive]
        for pos,x in enumerate(rb):
            sc[x]+=m-1-pos
    return sc

def baldwin_winner_set_slow(profile):
    @lru_cache(None)
    def rec(alive_tuple):
        alive=set(alive_tuple)
        if len(alive)==1:
            return frozenset(alive)
        sc=slow_scores(profile,alive)
        mn=min(sc.values())
        low=[x for x,v in sc.items() if v==mn]
        out=set()
        for x in low:
            nxt=tuple(sorted(alive-{x}))
            out.update(rec(nxt))
        return frozenset(out)
    return rec(tuple(CANDS))

def nanson_outcome_slow(profile):
    alive=set(CANDS)
    while len(alive)>1:
        sc=slow_scores(profile,alive)
        total=sum(sc.values())
        m=len(alive)
        low={x for x,v in sc.items() if v*m < total}
        if not low:
            return frozenset(alive)
        alive-=low
    return frozenset(alive)

def relabel_counts(counts, perm):
    out=[0]*24
    for mult,b in zip(counts,BALLOTS):
        if not mult:
            continue
        rb=tuple(perm[x] for x in b)
        out[BINDEX[rb]]+=mult
    return tuple(out)

def canonical_counts(counts):
    return min(relabel_counts(counts,p) for p in permutations(CANDS))

anon_totals={}
unique_both_anon={}
unique_both_labeled={}
diff_anon={}
diff_labeled={}
diff5=[]
pair_labeled=Counter()

for n in range(1,6):
    ta=uba=ubl=da=dl=0
    for counts in compositions(n,24):
        ta+=1
        B=baldwin_winner_set_fast(counts)
        N=nanson_outcome_fast(counts)
        w=multinomial(counts)

        # Independent replay for every anonymous profile in the claimed range.
        profile=expand_profile(counts)
        assert B==baldwin_winner_set_slow(profile)
        assert N==nanson_outcome_slow(profile)

        if len(B)==1 and len(N)==1:
            uba+=1
            ubl+=w
            if B!=N:
                da+=1
                dl+=w
                if n==5:
                    diff5.append(counts)
                    pair_labeled[(next(iter(B)),next(iter(N)))] += w
    anon_totals[n]=ta
    unique_both_anon[n]=uba
    unique_both_labeled[n]=ubl
    diff_anon[n]=da
    diff_labeled[n]=dl

assert anon_totals=={1:24,2:300,3:2600,4:17550,5:98280}
assert diff_anon=={1:0,2:0,3:0,4:0,5:384}
assert diff_labeled=={1:0,2:0,3:0,4:0,5:24480}
assert unique_both_labeled=={1:24,2:144,3:12288,4:143424,5:7232544}
assert len(diff5)==384
assert Fraction(24480,24**5)==Fraction(85,27648)
assert Fraction(24480,7232544)==Fraction(85,25113)
assert Fraction(384,98280)==Fraction(16,4095)
assert pair_labeled==Counter({(i,j):2040 for i in CANDS for j in CANDS if i!=j})

# Candidate-relabeling quotient of the 384 anonymous divergent profiles.
classes=Counter(canonical_counts(c) for c in diff5)
assert len(classes)==16
assert Counter(classes.values())==Counter({24:16})

# Clean tie-free witness: 2 BDCA, 1 CABD, 2 DCAB.
def counts_from_multiset(items):
    out=[0]*24
    for mult,b in items:
        out[BINDEX[b]]+=mult
    return tuple(out)

W=counts_from_multiset([
    (2,(1,3,2,0)), # BDCA
    (1,(2,0,1,3)), # CABD
    (2,(3,2,0,1)), # DCAB
])
assert scores_fast(W,15)==(4,7,9,10)
assert baldwin_winner_set_fast(W)==frozenset({1})
assert nanson_outcome_fast(W)==frozenset({3})

# Explicit round traces for the witness.
# Baldwin: A uniquely lowest; then C; then D, leaving B.
assert scores_fast(W,15)==(4,7,9,10)
assert scores_fast(W,14)==(0,5,4,6)
assert scores_fast(W,10)==(0,3,0,2)
# Nanson: avg 7.5 eliminates A,B; then D beats C 4-to-1 in the two-candidate recount.
assert sum(scores_fast(W,15))/4==Fraction(15,2)
assert scores_fast(W,12)==(0,0,1,4)

print('VERIFY_OK')
print('anonymous_totals',anon_totals)
print('unique_both_labeled',unique_both_labeled)
print('diff_anon',diff_anon)
print('diff_labeled',diff_labeled)
print('n5_all_profile_incidence','85/27648')
print('n5_conditional_unique_incidence','85/25113')
print('n5_anonymous_incidence','16/4095')
print('ordered_winner_pair_labeled_counts',dict(sorted(pair_labeled.items())))
print('candidate_relabel_classes',len(classes),'orbit_sizes',sorted(classes.values()))
print('witness_counts',W)
print('witness_first_scores',scores_fast(W,15))
print('witness_Baldwin','B')
print('witness_Nanson','D')
