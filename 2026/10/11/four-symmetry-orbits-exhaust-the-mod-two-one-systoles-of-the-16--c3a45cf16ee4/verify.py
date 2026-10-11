from itertools import combinations, permutations
from collections import Counter

LETTERS = 'ABCDEF'
NUMS = '0123456789'
VERTICES = list(LETTERS + NUMS)
EDGE_LABELS = {
    'AB':'0123','AC':'0456','BC':'0789','AD':'1489','BD':'1567',
    'CD':'2347','AE':'2579','BE':'2468','CE':'1358','DE':'0369',
    'AF':'3678','BF':'3459','CF':'1269','DF':'0258','EF':'0147'
}

def edge_key(a,b):
    return ''.join(sorted((a,b)))

facets=set()
for v in LETTERS:
    for u in LETTERS:
        if u != v:
            facets.add(frozenset([v, *EDGE_LABELS[edge_key(v,u)]]))
for v in LETTERS:
    for vp in LETTERS:
        if vp == v:
            continue
        for vpp in LETTERS:
            if vpp in (v,vp):
                continue
            nums=set(EDGE_LABELS[edge_key(v,vpp)]) - set(EDGE_LABELS[edge_key(v,vp)])
            assert len(nums) == 3
            facets.add(frozenset([v,vp,*nums]))
assert len(facets) == 150

faces=[set() for _ in range(5)]
for F in facets:
    for k in range(1,6):
        for s in combinations(F,k):
            faces[k-1].add(frozenset(s))
assert [len(x) for x in faces] == [16,120,330,375,150]
assert len(faces[1]) == 120
triangles=faces[2]
missing={frozenset(s) for s in combinations(VERTICES,3) if frozenset(s) not in triangles}
assert len(missing) == 230
assert Counter(sum(v in LETTERS for v in s) for s in missing) == Counter({3:20,2:60,1:90,0:60})

edges=sorted(faces[1], key=lambda e: tuple(sorted(e)))
edge_index={e:i for i,e in enumerate(edges)}
def triangle_boundary(t):
    x=0
    for e in combinations(sorted(t),2):
        x ^= 1 << edge_index[frozenset(e)]
    return x

def gf2_basis(vectors):
    basis={}
    for x in vectors:
        y=x
        while y:
            p=y.bit_length()-1
            if p in basis:
                y ^= basis[p]
            else:
                basis[p]=y
                break
    return basis

def reduce_with_basis(x,basis):
    y=x
    for p in sorted(basis, reverse=True):
        if (y >> p) & 1:
            y ^= basis[p]
    return y

b2=gf2_basis(triangle_boundary(t) for t in triangles)
assert len(b2) == 104
# The one-skeleton is K_16, so rank(d1)=15 and dim ker(d1)=120-15=105.
assert 120 - 15 - len(b2) == 1
residues={reduce_with_basis(triangle_boundary(t),b2) for t in missing}
assert len(residues) == 1 and 0 not in residues

# Gauge-fixed cocycle: w(Ax)=0 and w(xy)=1 exactly when Axy is a missing triangle.
w=set()
others=[v for v in VERTICES if v != 'A']
for x,y in combinations(others,2):
    if frozenset(['A',x,y]) in missing:
        w.add(frozenset([x,y]))
assert len(w) == 45
def w_eval(t):
    return sum(frozenset(e) in w for e in combinations(t,2)) & 1
assert all(w_eval(t) == 0 for t in triangles)
assert all(w_eval(t) == 1 for t in missing)

# Recover each numeric vertex as the unordered 3+3 bisection encoded by its K_6 edge incidences.
parts={}
for n in NUMS:
    adj={v:set() for v in LETTERS}
    for e,label in EDGE_LABELS.items():
        if n in label:
            a,b=e
            adj[a].add(b); adj[b].add(a)
    seen=set(); comps=[]
    for v in LETTERS:
        if v in seen:
            continue
        stack=[v]; seen.add(v); comp=set()
        while stack:
            z=stack.pop(); comp.add(z)
            for q in adj[z]:
                if q not in seen:
                    seen.add(q); stack.append(q)
        comps.append(frozenset(comp))
    assert sorted(map(len,comps)) == [3,3]
    parts[n]=next(c for c in comps if 'A' in c)

bisection_to_num={}
for n,p in parts.items():
    key=frozenset([p, frozenset(set(LETTERS)-set(p))])
    bisection_to_num[key]=n
assert len(bisection_to_num) == 10

def act(p,t):
    mp={LETTERS[i]:p[i] for i in range(6)}
    out=[]
    for x in t:
        if x in LETTERS:
            out.append(mp[x])
        else:
            pp=frozenset(mp[a] for a in parts[x])
            key=frozenset([pp, frozenset(set(LETTERS)-set(pp))])
            out.append(bisection_to_num[key])
    return frozenset(out)

perms=list(permutations(LETTERS))
assert len(perms) == 720
for p in perms:
    assert all(act(p,F) in facets for F in facets)

remaining=set(missing); orbit_sizes=[]; orbit_types=[]
while remaining:
    r=next(iter(remaining))
    orb={act(p,r) for p in perms}
    assert orb <= missing
    orbit_sizes.append(len(orb))
    orbit_types.append(sum(v in LETTERS for v in r))
    remaining -= orb
assert sorted(orbit_sizes) == [20,60,60,90]
assert sorted(orbit_types) == [0,1,2,3]
for rep,size in [
    (frozenset(['A','B','D']),20),
    (frozenset(['C','E','3']),60),
    (frozenset(['D','3','8']),90),
    (frozenset(['1','4','5']),60),
]:
    assert rep in missing
    assert len({act(p,rep) for p in perms}) == size

print('VERIFY_OK f=16,120,330,375,150 H1_F2=1 missing3=230 essential3=230 cocycle_weight=45 systole=3 orbit_sizes=20,60,90,60 reps=ABD,CE3,D38,145')
