"""Exhaustive small-case tests for the binary code C_k.
Uses only Python standard library; independent of symbolic-algebra packages.
"""
from itertools import combinations, permutations
from collections import Counter


def words(k):
    m = (1 << k) - 1
    return {v | ((v ^ (m if v.bit_count() & 1 else 0)) << k)
            for v in range(1 << k)}


def permute_word(c, perm):
    out = 0
    for i,j in enumerate(perm):
        if (c >> i) & 1: out |= 1 << j
    return out


def is_auto(cset, perm):
    return all(permute_word(w, perm) in cset for w in cset)


def check(k):
    code = words(k)
    assert len(code) == 1<<k
    wt = Counter(w.bit_count() for w in code)
    assert wt[0] == 1
    if k >= 4 and k % 2 == 0:
        assert min(z for z in wt if z) == 4
    if k>=6 and k%2==0:
        fours = {w for w in code if w.bit_count() == 4}
        pair_masks = {(1 << i) | (1 << (i+k)) for i in range(k)}
        assert fours == {p|q for p,q in combinations(pair_masks,2)}
        sigs = [frozenset(w for w in fours if (w>>i)&1) for i in range(2*k)]
        assert all(sigs[i]==sigs[i+k] for i in range(k))
        assert all(sigs[i]!=sigs[j] for i in range(k) for j in range(k) if i!=j)
        # Every pair-preserving permutation is determined by a pair permutation
        # and a swap mask. Check the small k=6 case in full.
        if k==6:
            total_even=total_odd=0
            for pi in permutations(range(k)):
                for mask in range(1<<k):
                    perm = tuple((pi[i]+(k if (mask>>i)&1 else 0)) for i in range(k)) + tuple((pi[i]+(0 if (mask>>i)&1 else k)) for i in range(k))
                    assert is_auto(code,perm) == (mask.bit_count()%2==0)
                    if mask.bit_count()%2==0: total_even+=1
                    else:total_odd+=1
            assert total_even == (1<<(k-1))*5040//7
            assert total_odd == total_even
            print('k=6: full pair-permutation check',total_even,total_odd)
        print('k',k,'spectrum',dict(sorted(wt.items())),'weight-four',len(fours),'pair signatures',len(set(sigs)))
    else:
        print('k',k,'spectrum',dict(sorted(wt.items())))
    if k in (2,4):
        autos = [p for p in permutations(range(2*k)) if is_auto(code,p)]
        def full_cycle(p):
            seen={0}; t=p[0]
            while t not in seen:
                seen.add(t);t=p[t]
            return t==0 and len(seen)==2*k
        has = any(full_cycle(p) for p in autos)
        assert (k==2 and has) or (k==4 and not has)
        if k==4: assert len(autos)==1344
        print('k',k,'permutation automorphisms',len(autos),'has regular cycle',has)

for k in (2,4,6,8,10):
    check(k)
print('VERIFY_OK')
