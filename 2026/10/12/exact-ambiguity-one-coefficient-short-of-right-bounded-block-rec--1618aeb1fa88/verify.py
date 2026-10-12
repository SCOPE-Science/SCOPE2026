#!/usr/bin/env python3
from itertools import product
from collections import defaultdict
from math import comb
from pathlib import Path
import json

def run_vector(w):
    m=w.count("a")
    s=[0]*(m+1)
    j=0
    for ch in w:
        if ch=="a":
            j+=1
        else:
            s[j]+=1
    return tuple(s)

def coeff_pattern_direct(w, pattern):
    # Standard subsequence-count DP, independent of the run-vector formula.
    dp=[0]*(len(pattern)+1)
    dp[0]=1
    for ch in w:
        for j in range(len(pattern)-1,-1,-1):
            if pattern[j]==ch:
                dp[j+1]+=dp[j]
    return dp[-1]

def moments(s):
    m=len(s)-1
    return tuple(sum(comb(j,l)*s[j] for j in range(l,m+1)) for l in range(m))

def kernel(m):
    return tuple(((-1)**j)*comb(m,j) for j in range(m+1))

def thresholds(s):
    m=len(s)-1
    Te=min(s[j]//comb(m,j) for j in range(0,m+1,2))
    To=min(s[j]//comb(m,j) for j in range(1,m+1,2))
    return Te,To

def predicted_family(s):
    m=len(s)-1
    v=kernel(m)
    Te,To=thresholds(s)
    return {
        tuple(s[j]+t*v[j] for j in range(m+1))
        for t in range(-Te,To+1)
    }

# Exact binomial-annihilation identity and primitivity of the kernel vector.
for m in range(1,21):
    v=kernel(m)
    assert abs(v[-1])==1
    for l in range(m):
        assert sum(comb(j,l)*v[j] for j in range(l,m+1))==0

# Engine A: enumerate nonnegative run vectors for a broad finite box, group by
# the complete truncated moment vector, and compare every fibre with the
# predicted integer interval on the primitive Pascal-kernel direction.
run_fibres=0
run_vectors_checked=0
for m in range(1,9):
    for B in range(0,10):
        groups=defaultdict(set)
        def rec(prefix, left, slots):
            if slots==1:
                yield tuple(prefix+[left])
                return
            for x in range(left+1):
                yield from rec(prefix+[x], left-x, slots-1)
        for s in rec([],B,m+1):
            groups[moments(s)].add(s)
            run_vectors_checked+=1
        for fam in groups.values():
            rep=next(iter(fam))
            assert fam==predicted_family(rep),(m,B,rep,fam,predicted_family(rep))
            Te,To=thresholds(rep)
            assert len(fam)==1+Te+To
            run_fibres+=1

# Engine B: direct binary-word enumeration.  Here n and m are fixed, and the
# supplied coefficient data are a, ab, ..., a^(m-1)b.  b is inferred from n,m.
# Coefficients are computed by generic subsequence DP rather than the moment
# formula.  We compare each collision class with the family predicted from runs.
word_groups=0
words_checked=0
for n in range(1,13):
    groups=defaultdict(set)
    for bits in product("ab", repeat=n):
        w="".join(bits)
        m=w.count("a")
        B=n-m
        if not (1<=m<=B):
            continue
        data=[m]
        for l in range(1,m):
            data.append(coeff_pattern_direct(w, "a"*l+"b"))
        groups[tuple(data)].add(w)
        words_checked+=1

    for fam in groups.values():
        rep=min(fam)
        s=run_vector(rep)
        predicted_runs=predicted_family(s)
        predicted_words=set()
        for r in predicted_runs:
            out=[]
            for j,x in enumerate(r):
                out.append("b"*x)
                if j<len(r)-1:
                    out.append("a")
            predicted_words.add("".join(out))
        assert fam==predicted_words,(n,rep,fam,predicted_words)
        Te,To=thresholds(s)
        assert len(fam)==1+Te+To
        word_groups+=1

# One concrete nontrivial fibre as a readable regression anchor.
s=(0,3,0,0)  # m=3
v=kernel(3)  # (1,-3,3,-1)
fam=predicted_family(s)
# Use a genuinely feasible nontrivial regression fibre instead:
s=(0,3,0,1)
fam=predicted_family(s)
assert (0,3,0,1) in fam
for r in fam:
    assert all(x>=0 for x in r)
    assert moments(r)==moments(s)

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["source_primary_msc"]=="68Q45"
assert cert["kernel_vector"]=="v_j=(-1)^j binom(m,j), 0<=j<=m"

print(
    "VERIFY_OK "
    f"kernel_m=1..20 run_vectors={run_vectors_checked} run_fibres={run_fibres} "
    f"direct_words={words_checked} direct_groups={word_groups} "
    "ambiguity=1+T_even+T_odd"
)
