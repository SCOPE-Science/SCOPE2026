"""Independent verifier: re-derives everything from (E,L) + witness supports in disproof.json.
Exact integer-bit arithmetic over F2. Prints VERIFY_OK or fails loudly.
"""
import json, os
ART = os.path.dirname(os.path.abspath(__file__))
L = 7
E = [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,1]]
def b1(j1,q,b): return (j1*5+q)*7+b
def b2(s,l,b): return 175+(s*3+l)*7+b
def ctz(x): return (x & -x).bit_length()-1
def wt(v): return bin(v).count('1')
def ref_basis(rows):
    basis = {}
    for v in rows:
        w = v
        for p in sorted(basis):
            if (w >> p) & 1: w ^= basis[p]
        if w:
            piv = ctz(w)
            for p in list(basis):
                if (basis[p] >> piv) & 1: basis[p] ^= w
            basis[piv] = w
    return basis
def rem(basis, v):
    w = v
    for p in sorted(basis):
        if (w >> p) & 1: w ^= basis[p]
    return w

B = []
for i in range(3):
    for a in range(7):
        v = 0
        for j in range(5):
            v |= 1 << (j*7+(a+E[i][j]) % 7)
        B.append(v)
HX = []
for i1 in range(3):
    for p in range(5):
        for a in range(7):
            v = 0
            for j1 in range(5): v |= 1 << b1(j1,p,(a+E[i1][j1])%7)
            for l in range(3): v |= 1 << b2(i1,l,(a-E[l][p])%7)
            HX.append(v)
HZ = []
for p_ in range(5):
    for q_ in range(3):
        for a in range(7):
            v = 0
            for q in range(5): v |= 1 << b1(p_,q,(a+E[q_][q])%7)
            for s in range(3): v |= 1 << b2(s,q_,(a-E[s][p_])%7)
            HZ.append(v)

assert len(HX)==105 and len(HZ)==105
assert all(wt(v)==8 for v in HX+HZ), "w0=8"
bad = sum(1 for r in range(105) for r2 in range(105)
          if bin(HZ[r2]&HX[r]).count('1')%2) and None
# orthogonality: each HX row has zero syndrome under HZ
for r in range(105):
    for r2 in range(105):
        assert bin(HZ[r2]&HX[r]).count('1')%2==0, "CSS orth fail"
bX = ref_basis(HX); bZ = ref_basis(HZ)
assert len(bX)==97 and len(bZ)==97, (len(bX),len(bZ))
assert 238-len(bX)-len(bZ)==44, "k=44"
print("base checks OK: orth=0, w0=8, ranks 97/97, k=44, N=238")

d = json.load(open(os.path.join(ART,"disproof.json")))
sup = d["logical_support238"]
v = 0
for c in sup: v |= 1 << c
assert wt(v)==6==d["logical_weight"], "weight 6"
# classical codeword check
csup = d["classical_codeword_support35"]
c = 0
for (var,sh) in csup: c |= 1 << (var*7+sh)
assert wt(c)==6
for r in B: assert bin(r&c).count('1')%2==0, "not in ker(B)"
# lift consistency
assert sup == sorted(b1(d["lift_block_j"],var,sh) for (var,sh) in csup)
# quantum checks
for r in HZ: assert bin(r&v).count('1')%2==0, "H_Z l != 0"
assert rem(bX,v)!=0, "l in rowspace(HX)!"
assert len(ref_basis(HX+[v]))==98, "rank augmentation"
print("witness checks OK: H_Z l=0, l not in rowspace(H_X), wt=6")
print("CONCLUSION VERIFIED: d(Q*)<=6, so d>=9 is FALSE")
print("VERIFY_OK")
