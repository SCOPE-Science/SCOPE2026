from itertools import product, combinations
from collections import Counter
from pathlib import Path
import json

N=5
words=[''.join(p) for p in product('01', repeat=N)]

def rots(w):
    return [w[i:]+w[:i] for i in range(N)]

def primitive(w):
    return len(set(rots(w)))==N

prim=sorted(w for w in words if primitive(w))
assert len(prim)==30
seen=set(); necklaces=[]
for w in prim:
    if w in seen: continue
    orb=sorted(set(rots(w)))
    necklaces.append(orb); seen.update(orb)
necklaces=sorted(necklaces)
assert len(necklaces)==6 and all(len(x)==5 for x in necklaces)

def overlap(u,v,s):
    return u[s:]+v[:s]

def comma_free(code):
    C=set(code)
    for u in code:
        for v in code:
            for s in range(1,N):
                if overlap(u,v,s) in C:
                    return False
    return True

# Method A: every equality case is a transversal of the six primitive necklaces.
A=[]
for choice in product(range(5), repeat=6):
    C=tuple(sorted(necklaces[i][choice[i]] for i in range(6)))
    if comma_free(C): A.append(C)
Aset=set(A)
assert len(Aset)==86

# Method B: enumerate all 6-subsets of the 30 primitive words directly.
# Precompute every ordered-pair/shift overlap as a 32-word ambient index, then
# reject a subset iff any such target is another member of that same subset.
allidx={w:i for i,w in enumerate(words)}
prim_bits=[1<<allidx[w] for w in prim]
ovtarget=[[[allidx[overlap(u,v,s)] for s in range(1,N)] for v in prim] for u in prim]
B=[]
for comb in combinations(range(30),6):
    mask=0
    for a in comb: mask |= prim_bits[a]
    ok=True
    for a in comb:
        if not ok: break
        for b in comb:
            for t in ovtarget[a][b]:
                if mask & (1<<t):
                    ok=False; break
            if not ok: break
    if ok:
        C=tuple(prim[i] for i in comb)
        assert comma_free(C)
        B.append(C)
Bset=set(B)
assert len(Bset)==86 and Aset==Bset

# Every maximum is one representative per necklace.
for C in Aset:
    for orb in necklaces:
        assert sum(w in C for w in orb)==1
    assert tuple(sorted(w.count('1') for w in C))==(1,2,2,3,3,4)

def compword(w): return ''.join('1' if c=='0' else '0' for c in w)
def revword(w): return w[::-1]
def trans(C,kind):
    if kind=='I': f=lambda w:w
    elif kind=='C': f=compword
    elif kind=='R': f=revword
    elif kind=='CR': f=lambda w:compword(revword(w))
    return tuple(sorted(f(w) for w in C))
G=['I','C','R','CR']
for C in Aset:
    for g in G: assert trans(C,g) in Aset
fixed={g:sum(trans(C,g)==C for C in Aset) for g in G}
assert fixed=={'I':86,'C':10,'R':0,'CR':4}

unseen=set(Aset); orbits=[]
while unseen:
    C=min(unseen)
    O={trans(C,g) for g in G}
    assert O <= Aset
    orbits.append(O); unseen-=O
sizes=Counter(map(len,orbits))
assert len(orbits)==25 and sizes==Counter({4:18,2:7})
stab_orbits=Counter()
for O in orbits:
    C=min(O)
    stab=tuple(g for g in G if trans(C,g)==C)
    if len(O)==4: assert stab==('I',); stab_orbits['identity_only']+=1
    elif stab==('I','C'): stab_orbits['complement']+=1
    elif stab==('I','CR'): stab_orbits['reverse_complement']+=1
    else: raise AssertionError(stab)
assert stab_orbits==Counter({'identity_only':18,'complement':5,'reverse_complement':2})

expected=json.loads(Path('census.json').read_text())
actual={
 'alphabet':'binary','length':5,'maximum_size':6,'primitive_words':30,
 'primitive_necklaces':6,'labeled_maxima':86,'natural_group_order':4,
 'fixed_by_complement':10,'fixed_by_reversal':0,'fixed_by_reverse_complement':4,
 'orbit_count':25,'orbit_size_distribution':{'2':7,'4':18},
 'stabilizer_orbit_distribution':{'identity_only':18,'complement':5,'reverse_complement':2},
 'weight_profile':[1,2,2,3,3,4]
}
assert actual==expected
file_codes=[]
for line in Path('maxima.txt').read_text().splitlines():
    if line.strip(): file_codes.append(tuple(line.split()))
assert set(file_codes)==Aset and len(file_codes)==86
print('VERIFY_OK primitive_words=30 primitive_necklaces=6 maximum=6 labeled_maxima=86 orientation_cases=15625 subset_cases=593775 fixed=C10,R0,CR4 orbits=25 orbit_sizes=2x7,4x18 stabilizer_orbits=Cx5,CRx2 weight_profile=1,2,2,3,3,4')
