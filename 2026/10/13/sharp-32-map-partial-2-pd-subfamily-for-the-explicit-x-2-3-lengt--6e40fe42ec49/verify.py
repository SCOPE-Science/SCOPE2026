from itertools import combinations
from collections import defaultdict, Counter

# GF(64)=F2[theta]/(theta^6+theta^4+theta^3+theta+1), theta represented by 2.
MOD=0x5b
TH=2

def add(a,b): return a^b

def mul(a,b):
    r=0
    while b:
        if b&1: r^=a
        b >>= 1
        a <<= 1
        if a & 0x40: a ^= MOD
    return r & 63

def powf(a,n):
    r=1
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a); n >>= 1
    return r

EXP=[1]
for _ in range(1,63): EXP.append(mul(EXP[-1],TH))
LOG={v:i for i,v in enumerate(EXP)}
assert len(LOG)==63

def ptheta(e): return EXP[e%63]

def omega(a,x):
    # q=2, r=3 specialization of the source polynomial.
    return add(add(mul(powf(a,32),powf(x,4)),mul(powf(a,16),powf(x,2))),mul(powf(a,8),x))

# Example 3.5 source ordering O_1,...,O_14, then O_15={(0,1)}, O_16={(0,0)}.
YEXP=[18,36,31,9,47,55,21,54,45,59,27,61,62,42]
points=[]; orbits=[]
for j,ey in enumerate(YEXP, start=1):
    ex=((j-1)%7)+1
    orb=[]
    for t in range(1,10):
        x=ptheta(ex+(t-1)*7); y=ptheta(ey)
        assert add(mul(y,y),y)==powf(x,9)
        orb.append(len(points)); points.append((x,y))
    orbits.append(orb)
orbits += [[126],[127]]
points += [(0,1),(0,0)]
assert len(points)==128 and len(set(points))==128
PINDEX={p:i for i,p in enumerate(points)}

# Proposition 3.7 at lambda=67 gives k=64:
# O1..O6 plus first 7 of O7 plus first 3 of O8 are information positions.
I=set()
for oi in range(6): I.update(orbits[oi])
I.update(orbits[6][:7]); I.update(orbits[7][:3])
H=set(range(128))-I
assert len(I)==len(H)==64

# Full Theorem-4.5 family, described independently of the arbitrary choice of b_a:
# Phi_{a,c}(x,y)=(x+a, y+omega_a(x)+c), where c+omega_a(a) is a root of z^2+z=a^9.
def constants_for_a(a):
    ans=[]
    for c in range(64):
        z=add(c,omega(a,a))
        if add(mul(z,z),z)==powf(a,9): ans.append(c)
    assert len(ans)==2
    return ans

def permutation(a,c):
    p=[]
    for x,y in points:
        q=(add(x,a), add(add(y,omega(a,x)),c))
        assert q in PINDEX
        p.append(PINDEX[q])
    assert len(set(p))==128
    return p

family=[]
for a in range(64):
    for c in constants_for_a(a): family.append((a,c,permutation(a,c)))
assert len(family)==128 and len({tuple(p) for _,_,p in family})==128

# Verify that the full source family is a partial 2-PD set.
pairs=list(combinations(range(128),2))
cover_count={pair:0 for pair in pairs}
for a,c,p in family:
    preH=[i for i in range(128) if p[i] in H]
    assert len(preH)==64
    for pair in combinations(preH,2): cover_count[pair]+=1
assert min(cover_count.values())>=1
assert Counter(cover_count.values())==Counter({6:64,24:192,26:512,28:384,30:384,31:384,32:4608,33:128,34:384,36:320,38:704,40:64})

# Structural lower bound. Each x has exactly two curve points.
byx=defaultdict(list)
for i,(x,y) in enumerate(points): byx[x].append(i)
assert len(byx)==64 and all(len(v)==2 for v in byx.values())
T={x for x,ids in byx.items() if set(ids)<=H}
assert T=={0,1,ptheta(56)}
W={0,1,ptheta(56),ptheta(1)}
assert T==W-{ptheta(1)}
# A map with translation a sends fiber x to fiber x+a, so it covers exactly a+T among vertical pairs.
for a,c,p in family:
    preH={i for i in range(128) if p[i] in H}
    xs={x for x,ids in byx.items() if set(ids)<=preH}
    assert xs=={add(a,t) for t in T}
# The 64 x-values split into 16 affine W-cosets. One translate a+T misses one point of its coset,
# so at least two distinct translations are needed per coset: 32 maps in any covering subfamily.
seen=set(); cosets=[]
for a in range(64):
    if a in seen: continue
    C={add(a,w) for w in W}; cosets.append(C); seen |= C
assert len(cosets)==16 and all(len(C)==4 for C in cosets)
LOWER_BOUND=2*len(cosets)
assert LOWER_BOUND==32

# An explicit 32-map witness. Exponents use theta; (None,0) denotes a=0,c=1.
EXP_PAIRS=[
(None,0),(56,21),(49,42),(57,18),(3,59),(50,54),(58,36),(25,9),
(4,27),(35,21),(51,45),(54,47),(31,31),(6,62),(46,27),(37,36),
(30,36),(45,59),(34,55),(39,9),(12,47),(24,31),(55,55),(48,55),
(60,9),(32,27),(9,36),(7,21),(23,36),(11,9),(38,59),(33,47)]
selected=[]
for ea,ec in EXP_PAIRS:
    a=0 if ea is None else ptheta(ea)
    c=ptheta(ec)
    assert c in constants_for_a(a)
    selected.append((a,c,permutation(a,c)))
assert len(selected)==32 and len({a for a,_,_ in selected})==32

selected_count={pair:0 for pair in pairs}
for a,c,p in selected:
    preH=[i for i in range(128) if p[i] in H]
    for pair in combinations(preH,2): selected_count[pair]+=1
assert min(selected_count.values())==1
assert sum(v==0 for v in selected_count.values())==0
assert Counter(selected_count.values())==Counter({1:52,2:117,3:264,4:429,5:699,6:979,7:1096,8:1102,9:1058,10:897,11:624,12:382,13:214,14:127,15:56,16:26,17:3,18:3})

print('POINTS',len(points),'INFORMATION',len(I),'CHECK',len(H))
print('SOURCE_FAMILY',len(family),'PAIR_REQUIREMENTS',len(pairs))
print('VERTICAL_CHECK_FIBERS',sorted('0' if x==0 else f'theta^{LOG[x]}' for x in T))
print('AFFINE_W_COSETS',len(cosets),'LOWER_BOUND',LOWER_BOUND)
print('SELECTED_MAPS',len(selected),'MIN_PAIR_COVERAGE',min(selected_count.values()))
print('VERIFY_OK')
