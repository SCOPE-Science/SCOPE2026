#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

# Exact arithmetic model for the Leech-lattice construction in arXiv:2102.08163.
# Coordinates below are integer numerators for the standard normalization in which
# the bilinear form is ordinary coordinate dot product divided by 8.

def dot8(x,y):
    return sum(a*b for a,b in zip(x,y))

def v24(entries):
    v=[0]*24
    for k,a in entries.items():
        v[k-1]=a
    return tuple(v)

# Extended binary Golay code from the standard cyclic [23,12,7] generator.
g=sum(1<<e for e in (11,10,6,5,4,2,0))
code=[]
for m in range(1<<12):
    c=0
    for j in range(12):
        if (m>>j)&1:
            c ^= g<<j
    c |= ((c.bit_count()&1)<<23)
    code.append(c)
assert Counter(c.bit_count() for c in code)==Counter({0:1,8:759,12:2576,16:759,24:1})

# Relabel coordinates so one octad is O={1,2,4,5,6,7,8,9}, as in the source.
octad=next(c for c in code if c.bit_count()==8)
supp=[i for i in range(24) if (octad>>i)&1]
nons=[i for i in range(24) if not ((octad>>i)&1)]
target_supp=[0,1,3,4,5,6,7,8]
target_nons=[2]+[i for i in range(24) if i not in target_supp and i!=2]
perm={old:new for old,new in zip(supp,target_supp)}
perm.update({old:new for old,new in zip(nons,target_nons)})
def pbits(c):
    d=0
    for old,new in perm.items():
        if (c>>old)&1:
            d |= 1<<new
    return d
code=[pbits(c) for c in code]
assert len(set(code))==4096

octads=[c for c in code if c.bit_count()==8]
assert len(octads)==759

hbar=v24({1:4,2:4})
a=v24({2:4,3:4})
u1=v24({3:4,4:4})
u2=v24({4:4,5:4})
u3=v24({1:-2,2:2,4:-2,5:2,6:2,7:2,8:2,9:2})
basis=[hbar,a,u1,u2,u3]
G=[[dot8(x,y)//8 for y in basis] for x in basis]
assert G==[[4,2,0,0,0],[2,4,2,0,1],[0,2,4,2,-1],[0,0,2,4,0],[0,1,-1,0,4]]

def is_conic(l):
    return (dot8(l,hbar)==16 and dot8(l,a)==8 and dot8(l,u1)==0
            and dot8(l,u2)==0 and dot8(l,u3)==0)

conics=[]
types=Counter()
# Minimal vectors of type (±4,±4,0^22)/sqrt(8).
for i,j in combinations(range(24),2):
    for si in (-4,4):
        for sj in (-4,4):
            l=[0]*24; l[i]=si; l[j]=sj; l=tuple(l)
            if is_conic(l): conics.append(l); types['C']+=1
# Minimal vectors of type (±2^8,0^16)/sqrt(8), octad support, even sign parity.
for c in octads:
    S=[i for i in range(24) if (c>>i)&1]
    for mask in range(128):
        ss=[-2 if (mask>>k)&1 else 2 for k in range(7)]
        ss.append(-2 if sum(x<0 for x in ss)%2 else 2)
        l=[0]*24
        for i,s in zip(S,ss): l[i]=s
        l=tuple(l)
        if is_conic(l): conics.append(l); types['B']+=1
# Minimal vectors of type (∓3,±1^23)/sqrt(8), signs indexed by Golay words.
for c in code:
    signs=[-1 if (c>>j)&1 else 1 for j in range(24)]
    for i in range(24):
        l=signs.copy(); l[i]*=-3; l=tuple(l)
        if is_conic(l): conics.append(l); types['A']+=1

assert len(conics)==800 and len(set(conics))==800
assert types==Counter({'B':608,'A':192})

# In the source's Néron-Severi realization, if l,m are Leech conic vectors then
# C_l.C_m = 2 - l.m. Integer coordinate dot products are divided by 8.
def intersection(l,m):
    q=dot8(l,m)
    assert q%8==0
    return 2-q//8

pair=Counter()
profiles=[]
for i,c in enumerate(conics):
    p=Counter()
    for j,d in enumerate(conics):
        if i==j: continue
        p[intersection(c,d)]+=1
    assert set(p)<=set((0,1,2,4))
    profiles.append(tuple(p[k] for k in (0,1,2,4)))
    for j in range(i+1,len(conics)):
        pair[intersection(c,conics[j])]+=1
assert pair==Counter({0:72240,1:174720,2:72240,4:400})
assert sum(pair.values())==800*799//2
pc=Counter(profiles)
P=(179,440,179,1); Q=(183,432,183,1)
assert pc==Counter({P:480,Q:320})

classes=[0 if p==P else 1 for p in profiles]
def split_profile(i):
    same=Counter(); cross=Counter()
    for j,d in enumerate(conics):
        if i==j: continue
        m=intersection(conics[i],d)
        (same if classes[i]==classes[j] else cross)[m]+=1
    return tuple(same[k] for k in (0,1,2,4)), tuple(cross[k] for k in (0,1,2,4))
for cls,expect_same,expect_cross in [
    (0,(115,248,115,1),(64,192,64,0)),
    (1,(87,144,87,1),(96,288,96,0))]:
    vals={split_profile(i) for i,x in enumerate(classes) if x==cls}
    assert vals=={(expect_same,expect_cross)}

# Multiplicity 4 gives a perfect matching, agreeing with residual plane-section pairing.
partners=[]
for i,c in enumerate(conics):
    js=[j for j,d in enumerate(conics) if i!=j and intersection(c,d)==4]
    assert len(js)==1
    partners.append(js[0])
assert all(partners[partners[i]]==i for i in range(800))
assert len({tuple(sorted((i,partners[i]))) for i in range(800)})==400

print('VERIFY_OK conics=800 types=A192+B608 pairs=0:72240,1:174720,2:72240,4:400 profiles=480x(179,440,179,1)+320x(183,432,183,1) quotient=A/A(115,248,115,1),A/B(64,192,64,0),B/B(87,144,87,1),B/A(96,288,96,0) residual_pairs=400')
