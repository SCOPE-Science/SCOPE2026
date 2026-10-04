from itertools import product
from collections import Counter

MODS=(4,2,2)
ELEMS=list(product(*[range(m) for m in MODS]))
IDX={x:i for i,x in enumerate(ELEMS)}
N=len(ELEMS)
ZERO=IDX[(0,0,0)]

def addx(x,y):
    return tuple((x[j]+y[j])%MODS[j] for j in range(3))

def smul(a,x):
    return tuple((a*x[j])%MODS[j] for j in range(3))

NEG=[IDX[tuple((-x[j])%MODS[j] for j in range(3))] for x in ELEMS]
SUB=[[IDX[addx(ELEMS[i],ELEMS[NEG[j]])] for j in range(N)] for i in range(N)]


def fourier_zero_mask(A):
    # chi_k(x)=i^(k1*x1 + 2*k2*x2 + 2*k3*x3).
    # An integer combination n0+n1*i-n2-n3*i vanishes exactly when n0=n2 and n1=n3.
    out=0
    for ki,k in enumerate(ELEMS):
        counts=[0,0,0,0]
        for ai in A:
            x=ELEMS[ai]
            phase=(k[0]*x[0]+2*k[1]*x[1]+2*k[2]*x[2])%4
            counts[phase]+=1
        if counts[0]==counts[2] and counts[1]==counts[3]:
            out |= 1<<ki
    return out


def clique_exists(vertices_mask, need, compatible):
    if need==0:
        return True
    if vertices_mask.bit_count()<need:
        return False
    def rec(cands,k):
        if k==0:
            return True
        if cands.bit_count()<k:
            return False
        while cands:
            lsb=cands & -cands
            v=lsb.bit_length()-1
            cands ^= lsb
            if rec(cands & compatible[v], k-1):
                return True
            if cands.bit_count()<k:
                return False
        return False
    return rec(vertices_mask,need)


def spectral(A):
    m=len(A)
    if m==1:
        return True
    z=fourier_zero_mask(A)
    comp=[0]*N
    for i in range(N):
        cm=0
        for j in range(N):
            if i!=j and ((z>>SUB[i][j])&1):
                cm |= 1<<j
        comp[i]=cm
    # Translate any spectrum so that 0 belongs to it.
    return clique_exists(comp[ZERO] & ~(1<<ZERO),m-1,comp)


def tiles(A):
    m=len(A)
    if N%m:
        return False
    if m==N:
        return True
    diffA=0
    for a in A:
        for b in A:
            diffA |= 1<<SUB[a][b]
    comp=[0]*N
    for i in range(N):
        cm=0
        for j in range(N):
            if i!=j and not ((diffA>>SUB[i][j])&1):
                cm |= 1<<j
        comp[i]=cm
    # Translate any complement so that 0 belongs to it.
    return clique_exists(comp[ZERO] & ~(1<<ZERO),N//m-1,comp)


def automorphisms():
    ord2=[x for x in ELEMS if smul(2,x)==(0,0,0)]
    autos=[]
    for a in ELEMS:
        for b in ord2:
            for c in ord2:
                mp=[]
                for x in ELEMS:
                    y=addx(addx(smul(x[0],a),smul(x[1],b)),smul(x[2],c))
                    mp.append(IDX[y])
                if len(set(mp))==N:
                    autos.append(tuple(mp))
    return autos

accepted=[]
size_counts=Counter()
for mask in range(1,1<<N):
    A=[i for i in range(N) if (mask>>i)&1]
    s=spectral(A)
    t=tiles(A)
    assert s==t,(mask,s,t)
    if s:
        accepted.append(mask)
        size_counts[len(A)]+=1

expected={1:16,2:120,4:1436,8:1574,16:1}
assert dict(size_counts)==expected,(size_counts,expected)
assert len(accepted)==3147

autos=automorphisms()
assert len(autos)==192
transforms=[]
for au in autos:
    for t in range(N):
        transforms.append(tuple(IDX[addx(ELEMS[au[i]],ELEMS[t])] for i in range(N)))
assert len(transforms)==3072

seen=set()
orbit_counts=Counter()
accepted_set=set(accepted)
for mask in accepted:
    if mask in seen:
        continue
    orbit=set()
    for perm in transforms:
        image=0
        for i in range(N):
            if (mask>>i)&1:
                image |= 1<<perm[i]
        orbit.add(image)
    assert orbit <= accepted_set
    seen |= orbit
    orbit_counts[mask.bit_count()]+=1
assert seen==accepted_set
expected_orbits={1:1,2:3,4:10,8:12,16:1}
assert dict(orbit_counts)==expected_orbits,(orbit_counts,expected_orbits)

print('VERIFY_OK subsets=65535 accepted=3147 sizes=16,120,1436,1574,1 aut=192 affine=3072 orbits=1,3,10,12,1')
