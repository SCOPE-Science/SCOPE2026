#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import json

H0="11100011000"
H1="11100111000"
assert len(H0)==len(H1)==11
P=[x if x==y else None for x,y in zip(H0,H1)]
assert P==["1","1","1","0","0",None,"1","1","0","0","0"]

# Robust symbolic residue test.  If a position has residue 5, its value is
# treated as an independent arbitrary bit.  This is stronger than using the
# actual correlations of the Thue-Morse word and therefore gives a genuine
# sufficient condition for every quotient of a shift by 11.
def robust(ra,rb):
    for u in range(11):
        residues=(u,(u+ra)%11,(u+rb)%11)
        variable=[j for j,r in enumerate(residues) if r==5]
        for bits in product("01",repeat=len(variable)):
            it=iter(bits)
            vals=[P[r] if P[r] is not None else next(it) for r in residues]
            if vals[0] not in (vals[1],vals[2]):
                return False
    return True

good=sorted((a,b) for a in range(11) for b in range(11) if robust(a,b))
expected=sorted([
 (1,4),(1,5),(1,10),(2,5),(4,1),(4,6),
 (5,1),(5,2),(5,6),(5,7),(6,4),(6,5),(6,9),(6,10),
 (7,5),(7,10),(9,6),(10,1),(10,6),(10,7)
])
assert good==expected
assert all(b!=(2*a)%11 for a,b in good)

# Check the fixed-residue mismatch witnesses used in the 3^+-power proof.
witness={1:2,2:1,3:0,4:0,5:8,6:2,7:1,8:0,9:0,10:0}
for d,r in witness.items():
    assert P[r] is not None and P[(r+d)%11] is not None
    assert P[r]!=P[(r+d)%11]

# All length-3 factors of Thue-Morse.  The morphism iteration independently
# reconstructs the classical six-factor set.
def mu(w):
    return ''.join("01" if c=="0" else "10" for c in w)
t="0"
for _ in range(8):
    t=mu(t)
fac3=sorted({t[i:i+3] for i in range(len(t)-2)})
assert fac3==["001","010","011","100","101","110"]

def h(w):
    return ''.join(H0 if c=="0" else H1 for c in w)

# For p <= 4, a hypothetical factor of period p and length 3p+1 spans at
# most three h-blocks.  Exhaust every length-3 Thue-Morse factor and every
# possible starting residue.
small_factor_counts={}
for p in range(1,5):
    L=3*p+1
    factors=set()
    for f in fac3:
        z=h(f)
        for off in range(11):
            if off+L<=len(z):
                s=z[off:off+L]
                factors.add(s)
                assert not all(s[j]==s[j+p] for j in range(L-p)), (p,f,off,s)
    small_factor_counts[p]=len(factors)
assert small_factor_counts=={1:8,2:14,3:20,4:26}

# Independent long finite stress test of all residue classes with b <= 300.
# The infinite proof itself is the symbolic residue check above.
def tm_prefix(n):
    return ''.join(str(i.bit_count()&1) for i in range(n))
S=h(tm_prefix(2000))
tested=0
for a in range(1,300):
    for b in range(a+1,301):
        if (a%11,b%11) in good:
            tested+=1
            assert all(S[i]==S[i+a] or S[i]==S[i+b]
                       for i in range(len(S)-b))
assert tested>1000

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["robust_oriented_residue_pairs"]==[list(x) for x in good]
assert cert["natural_density_among_a_lt_b"]=="20/121"
assert cert["good_pairs_with_1_le_a_lt_b_le_54_explained_by_residue_family"]==sum(
    1 for a in range(1,55) for b in range(a+1,55) if (a%11,b%11) in good
)
print("VERIFY_OK robust_classes=20 unordered=10 density=20/121 "
      "small_period_factors=8,14,20,26 mismatch_residues=1..10 "
      "no_doubling_class=1 finite_stress_b<=300 source_triangle_pairs=250")
