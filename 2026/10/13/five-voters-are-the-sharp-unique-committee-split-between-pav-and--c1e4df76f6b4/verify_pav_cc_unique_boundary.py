#!/usr/bin/env python3
from itertools import product, combinations, permutations
from fractions import Fraction
from math import factorial, gcd
from collections import Counter, defaultdict

CANDS = (0,1,2)
BALLOTS = tuple(frozenset(i for i in CANDS if mask & (1<<i)) for mask in range(8))
COMMITTEES = tuple(frozenset(x) for x in combinations(CANDS,2))

def pav_score_direct(profile, W):
    s = Fraction(0)
    for A in profile:
        j = len(A & W)
        if j == 1:
            s += 1
        elif j == 2:
            s += Fraction(3,2)
    return s

def cc_score_direct(profile, W):
    return sum(bool(A & W) for A in profile)

def argmax_dict(d):
    m = max(d.values())
    return frozenset(k for k,v in d.items() if v == m)

def winners_direct(profile):
    ps = {W:pav_score_direct(profile,W) for W in COMMITTEES}
    cs = {W:cc_score_direct(profile,W) for W in COMMITTEES}
    return argmax_dict(ps), argmax_dict(cs), ps, cs

# Independent aggregated scoring from ballot-count vector.
def scores_from_counts(counts):
    # mask order 0..7; committee score computed via pretabulated exact integer half-units.
    pav2 = {}
    cc = {}
    for W in COMMITTEES:
        p2 = 0
        c = 0
        for mask, n in enumerate(counts):
            A = BALLOTS[mask]
            j = len(A & W)
            p2 += n * (0 if j == 0 else 2 if j == 1 else 3)
            c += n * (1 if j else 0)
        pav2[W] = p2
        cc[W] = c
    return pav2, cc

def winners_counts(counts):
    ps2, cs = scores_from_counts(counts)
    return argmax_dict(ps2), argmax_dict(cs), ps2, cs

def comps(total, k, prefix=()):
    if k == 1:
        yield prefix + (total,)
        return
    for x in range(total+1):
        yield from comps(total-x, k-1, prefix+(x,))

def multinomial(counts):
    n = sum(counts)
    z = factorial(n)
    for x in counts:
        z //= factorial(x)
    return z

def permute_mask(mask, p):
    out = 0
    for i in CANDS:
        if mask & (1<<i):
            out |= 1 << p[i]
    return out

def permute_counts(counts, p):
    out = [0]*8
    for mask,n in enumerate(counts):
        out[permute_mask(mask,p)] += n
    return tuple(out)

def canonical_counts(counts):
    return min(permute_counts(counts,p) for p in permutations(CANDS))

# Direct labeled enumeration.
labeled = {}
direct_bad_examples = {}
for n in range(1,6):
    both_unique = 0
    different_unique = 0
    set_different = 0
    bad_profiles = []
    for prof_masks in product(range(8), repeat=n):
        profile = tuple(BALLOTS[m] for m in prof_masks)
        pw,cw,_,_ = winners_direct(profile)
        if pw != cw:
            set_different += 1
        if len(pw)==len(cw)==1:
            both_unique += 1
            if pw != cw:
                different_unique += 1
                if len(bad_profiles)<5:
                    bad_profiles.append(prof_masks)
    labeled[n]=(8**n,both_unique,different_unique,set_different)
    direct_bad_examples[n]=bad_profiles

# Independent anonymous enumeration, weighted back to labeled profiles.
anonymous = {}
bad5 = []
for n in range(1,6):
    anon_total=anon_both=anon_bad=0
    weighted_total=weighted_both=weighted_bad=0
    for counts in comps(n,8):
        anon_total += 1
        weight = multinomial(counts)
        weighted_total += weight
        pw,cw,_,_ = winners_counts(counts)
        if len(pw)==len(cw)==1:
            anon_both += 1
            weighted_both += weight
            if pw != cw:
                anon_bad += 1
                weighted_bad += weight
                if n==5:
                    bad5.append(counts)
    anonymous[n]=(anon_total,anon_both,anon_bad,weighted_total,weighted_both,weighted_bad)

# Cross-check independent domains and scoring.
for n in range(1,6):
    assert anonymous[n][3] == 8**n == labeled[n][0]
    assert anonymous[n][4] == labeled[n][1]
    assert anonymous[n][5] == labeled[n][2]

# Exact boundary.
assert [labeled[n][2] for n in range(1,6)] == [0,0,0,0,120]
assert anonymous[5][2] == 6
assert anonymous[5][1] == 231
assert labeled[5][1] == 11970
assert labeled[5][3] == 15648

# Canonical boundary form: 3x {A,B}, 1x {A}, 1x {C}.
canonical = [0]*8
canonical[1] = 1        # {A}
canonical[3] = 3        # {A,B}
canonical[4] = 1        # {C}
canonical = tuple(canonical)
assert canonical in bad5
classes = Counter(canonical_counts(c) for c in bad5)
assert len(classes) == 1 and list(classes.values()) == [6]
assert canonical_counts(canonical) in classes

# Every bad profile has no empty/full ballot, multiplicities 3,1,1.
for c in bad5:
    assert c[0] == 0 and c[7] == 0
    assert sorted((x for x in c if x), reverse=True) == [3,1,1]
    assert multinomial(c) == 20

# Verify canonical scores.
pw,cw,p2,cs = winners_counts(canonical)
AB=frozenset((0,1)); AC=frozenset((0,2)); BC=frozenset((1,2))
assert pw == frozenset((AB,))
assert cw == frozenset((AC,))
assert p2 == {AB:11, AC:10, BC:8}
assert cs == {AB:4, AC:5, BC:4}

# Exhaustively verify the analytic inequality certificate after relabeling:
# For every bad count vector, relabel so PAV=AB and CC=AC; then
# b < min(a,c), and PAB>PAC forces x-y > 2(c-b).
def normalize_bad(counts):
    pw,cw,_,_=winners_counts(counts)
    P=next(iter(pw)); Q=next(iter(cw))
    # brute find relabeling mapping P to AB and Q to AC
    for p in permutations(CANDS):
        pc=permute_counts(counts,p)
        ppw,pcw,_,_=winners_counts(pc)
        if ppw==frozenset((AB,)) and pcw==frozenset((AC,)):
            return pc
    raise AssertionError
for counts in bad5:
    c=normalize_bad(counts)
    a,b,cc = c[1],c[2],c[4]
    x,y,z = c[3],c[5],c[6]
    assert b < a and b < cc
    assert (x-y) > 2*(cc-b)
    assert a+cc+x >= 5
    assert c == canonical

# Independent direct replay of one canonical labeled ordering.
profile = (BALLOTS[3],BALLOTS[3],BALLOTS[3],BALLOTS[1],BALLOTS[4])
pw,cw,ps,csd=winners_direct(profile)
assert pw==frozenset((AB,)) and cw==frozenset((AC,))
assert ps[AB]==Fraction(11,2) and ps[AC]==5 and ps[BC]==4
assert csd[AB]==4 and csd[AC]==5 and csd[BC]==4

num, den = 120, 8**5
g=gcd(num,den)
inc=(num//g,den//g)
num2,den2=120,labeled[5][1]
g2=gcd(num2,den2)
cond=(num2//g2,den2//g2)

print("VERIFY_OK")
print("labeled_table", labeled)
print("anonymous_table", anonymous)
print("n5_bad_anonymous", len(bad5))
print("n5_bad_candidate_orbits", len(classes), dict(classes))
print("n5_bad_labeled", labeled[5][2])
print("n5_unconditional_incidence", f"{inc[0]}/{inc[1]}")
print("n5_both_unique_labeled", labeled[5][1])
print("n5_conditional_incidence", f"{cond[0]}/{cond[1]}")
print("canonical_counts_mask0to7", canonical)
print("canonical_PAV_half_scores_AB_AC_BC", [p2[AB],p2[AC],p2[BC]])
print("canonical_CC_scores_AB_AC_BC", [cs[AB],cs[AC],cs[BC]])
