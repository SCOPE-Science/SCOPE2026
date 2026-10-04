#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction
from collections import Counter

def is_antichain(fam):
    fam = tuple(fam)
    for i,a in enumerate(fam):
        for b in fam[i+1:]:
            if (a & b) == a or (a & b) == b:
                return False
    return True

def antichains_recursive(n):
    subs = list(range(1,1<<n))
    out = set()
    def rec(cands, cur):
        if not cands:
            out.add(tuple(sorted(cur)))
            return
        m = cands[0]
        rec(cands[1:], cur)
        rec([x for x in cands[1:] if not ((x&m)==x or (x&m)==m)], cur+[m])
    rec(subs, [])
    out.discard(())
    return out

def antichains_bruteforce(n):
    subs = list(range(1,1<<n))
    out=set()
    for bits in range(1,1<<len(subs)):
        fam=[subs[j] for j in range(len(subs)) if (bits>>j)&1]
        if is_antichain(fam):
            out.add(tuple(sorted(fam)))
    return out

def winning(mwcs, S):
    return any((M&S)==M for M in mwcs)

def proper(mwcs,n):
    full=(1<<n)-1
    return all(not (winning(mwcs,S) and winning(mwcs,full^S)) for S in range(1<<n))

def pgi_dp_raw(mwcs,n):
    pgi=[0]*n
    dp=[Fraction(0) for _ in range(n)]
    for M in mwcs:
        k=M.bit_count()
        for i in range(n):
            if (M>>i)&1:
                pgi[i]+=1
                dp[i]+=Fraction(1,k)
    return tuple(pgi),tuple(dp)

def weak_order(v):
    return tuple((v[i]>v[j])-(v[i]<v[j]) for i in range(len(v)) for j in range(i+1,len(v)))

def permute_mask(mask,p):
    out=0
    for i,j in enumerate(p):
        if (mask>>i)&1:
            out |= 1<<j
    return out

def canon(mwcs,n):
    return min(tuple(sorted(permute_mask(M,p) for M in mwcs)) for p in permutations(range(n)))

def game_from_weights(q,w):
    n=len(w)
    wins=[S for S in range(1,1<<n) if sum(w[i] for i in range(n) if (S>>i)&1)>=q]
    mins=[]
    for S in wins:
        if all(sum(w[i] for i in range(n) if ((S^(1<<j))>>i)&1)<q for j in range(n) if (S>>j)&1):
            mins.append(S)
    return tuple(sorted(mins))

expected = {
    1:(1,1),
    2:(4,3),
    3:(18,11),
    4:(166,80),
}
div_counts={}
classes4=Counter()

for n in range(1,5):
    A=antichains_recursive(n)
    B=antichains_bruteforce(n)
    assert A==B
    props=[g for g in A if proper(g,n)]
    assert (len(A),len(props))==expected[n]
    div=[]
    for g in props:
        pg,dp=pgi_dp_raw(g,n)
        if weak_order(pg)!=weak_order(dp):
            div.append(g)
    div_counts[n]=len(div)
    if n<4:
        assert len(div)==0
    else:
        assert len(div)==30
        for g in div:
            classes4[canon(g,n)]+=1

assert classes4 == Counter({
    (3,13):12,
    (3,5,14):12,
    (3,13,14):6,
})

# Weighted representatives for every divergent four-player isomorphism class.
reps = {
    (3,13):(5,(3,2,1,1)),
    (3,5,14):(5,(3,2,2,1)),
    (3,13,14):(4,(2,2,1,1)),
}
for mwcs,(q,w) in reps.items():
    assert game_from_weights(q,w)==mwcs
    pg,dp=pgi_dp_raw(mwcs,4)
    assert weak_order(pg)!=weak_order(dp)

# Exact raw-index vectors for the canonical classes.
assert pgi_dp_raw((3,13),4) == (
    (2,1,1,1),
    (Fraction(5,6),Fraction(1,2),Fraction(1,3),Fraction(1,3))
)
assert pgi_dp_raw((3,5,14),4) == (
    (2,2,2,1),
    (Fraction(1,1),Fraction(5,6),Fraction(5,6),Fraction(1,3))
)
assert pgi_dp_raw((3,13,14),4) == (
    (2,2,2,2),
    (Fraction(5,6),Fraction(5,6),Fraction(2,3),Fraction(2,3))
)

# Show why properness matters: without it, divergence already occurs at n=3.
all3=antichains_recursive(3)
unrestricted_div=[g for g in all3 if weak_order(pgi_dp_raw(g,3)[0]) != weak_order(pgi_dp_raw(g,3)[1])]
assert len(unrestricted_div)==3
assert all(not proper(g,3) for g in unrestricted_div)
assert canon(unrestricted_div[0],3)==(1,6)  # {1}, {2,3}

print("VERIFY_OK")
print("simple_and_proper_counts", expected)
print("proper_divergence_counts", div_counts)
print("four_player_divergent_isomorphism_classes", dict(classes4))
print("weighted_representatives", reps)
print("unrestricted_three_player_divergence", len(unrestricted_div), "canonical", canon(unrestricted_div[0],3))
