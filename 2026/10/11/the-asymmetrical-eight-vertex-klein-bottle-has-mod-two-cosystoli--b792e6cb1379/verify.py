from itertools import combinations, permutations

V = list('ABCDEFGH')
FACETS = [tuple(sorted(x)) for x in [
    'ABD','ABH','ACG','ACH','ADF','AEF','AEG','BCE',
    'BCG','BDG','BEF','BFH','CDE','CDF','CFH','DEG'
]]
FSET = set(FACETS)
EDGES = sorted({tuple(sorted(e)) for f in FACETS for e in combinations(f,2)})
EIDX = {e:i for i,e in enumerate(EDGES)}
assert (len(V), len(EDGES), len(FACETS)) == (8,24,16)

# Closed connected surface checks.
EDGE_FACES = {e:[] for e in EDGES}
for fi,f in enumerate(FACETS):
    for e in combinations(f,2):
        EDGE_FACES[tuple(sorted(e))].append(fi)
assert all(len(x)==2 for x in EDGE_FACES.values())
assert len(V)-len(EDGES)+len(FACETS) == 0
adj = {v:set() for v in V}
for a,b in EDGES:
    adj[a].add(b); adj[b].add(a)
seen={'A'}; stack=['A']
while stack:
    u=stack.pop()
    for w in adj[u]-seen:
        seen.add(w); stack.append(w)
assert seen == set(V)

# Cervone's 1133 model has degree multiset 4,5,6,6,6,7,7,7.
DEG = {v:len(adj[v]) for v in V}
assert sorted(DEG.values()) == [4,5,6,6,6,7,7,7]

# Independently exhaust all degree-preserving vertex permutations: only identity is simplicial.
parts={}
for v,d in DEG.items(): parts.setdefault(d,[]).append(v)
auts=[]
for p7 in permutations(parts[7]):
    m7=dict(zip(parts[7],p7))
    for p6 in permutations(parts[6]):
        mp={**m7, **dict(zip(parts[6],p6)), parts[5][0]:parts[5][0], parts[4][0]:parts[4][0]}
        image={tuple(sorted(mp[x] for x in f)) for f in FACETS}
        if image == FSET:
            auts.append(mp)
assert len(auts) == 1 and all(auts[0][v] == v for v in V)

# Bit linear algebra over F_2.
def rref_bits(rows, ncols):
    rows=list(rows)
    piv=[]; r=0
    for c in range(ncols):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>c)&1), None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i]>>c)&1): rows[i] ^= rows[r]
        piv.append(c); r += 1
    return rows[:r],piv

# A one-cochain is a cocycle iff its edge values sum to zero on every face.
face_rows=[]
for f in FACETS:
    x=0
    for e in combinations(f,2): x |= 1 << EIDX[tuple(sorted(e))]
    face_rows.append(x)
ZR,ZP = rref_bits(face_rows,len(EDGES))
assert len(ZP) == 15
free=[c for c in range(len(EDGES)) if c not in ZP]
assert len(free) == 9

def all_cocycles():
    out=[]
    for mask in range(1<<len(free)):
        x=0
        for j,c in enumerate(free):
            if (mask>>j)&1: x |= 1<<c
        for row,p in zip(ZR,ZP):
            if (row & x).bit_count() & 1: x |= 1<<p
        assert all(((r & x).bit_count() & 1)==0 for r in face_rows)
        out.append(x)
    return out
Z1=all_cocycles()
assert len(Z1) == 512

# Vertex coboundaries.  The connected eight-vertex graph gives rank 7.
cob=[]
for v in V:
    x=0
    for e,i in EIDX.items():
        if v in e: x |= 1<<i
    cob.append(x)
BR,BP=rref_bits(cob,len(EDGES))
assert len(BR) == 7
B={0}
for b in BR:
    B |= {x^b for x in list(B)}
assert len(B) == 128

def reduce_mod_B(x):
    for row,p in zip(BR,BP):
        if (x>>p)&1: x ^= row
    return x

classes={}
for z in Z1:
    classes.setdefault(reduce_mod_B(z),[]).append(z)
assert len(classes) == 4 and all(len(c)==128 for c in classes.values())

# Alexander-Whitney cup-square evaluation on the mod-two fundamental cycle.
def cup_square(z):
    val=0
    for f in FACETS:
        a,b,c=sorted(f)
        ab=EIDX[tuple(sorted((a,b)))]
        bc=EIDX[tuple(sorted((b,c)))]
        val ^= ((z>>ab)&1) & ((z>>bc)&1)
    return val

class_data={}
for q,reps in classes.items():
    squares={cup_square(z) for z in reps}
    assert len(squares)==1
    weights=[z.bit_count() for z in reps]
    mw=min(weights)
    mins=[z for z in reps if z.bit_count()==mw]
    class_data[q]={'square':next(iter(squares)),'min_weight':mw,'mins':mins}

zero=[q for q in classes if q==0]
nonzero=[q for q in classes if q!=0]
assert len(zero)==1 and len(nonzero)==3
# Null class is not part of the cosystolic spectrum.
assert class_data[0]['min_weight']==0

sq0=[q for q in nonzero if class_data[q]['square']==0]
sq1=[q for q in nonzero if class_data[q]['square']==1]
assert len(sq0)==1 and len(sq1)==2
omega=sq0[0]
assert (class_data[omega]['min_weight'],len(class_data[omega]['mins'])) == (6,5)

# Alpha is the explicit unique weight-five nontrivial cocycle.
def mask_of(edge_names):
    x=0
    for name in edge_names:
        e=tuple(sorted(name))
        assert e in EIDX
        x |= 1<<EIDX[e]
    return x
alpha_rep=mask_of(['BC','BG','CE','DE','DG'])
assert alpha_rep in Z1
alpha=reduce_mod_B(alpha_rep)
assert alpha != 0 and class_data[alpha]['square']==1
assert (class_data[alpha]['min_weight'],len(class_data[alpha]['mins'])) == (5,1)
assert class_data[alpha]['mins'] == [alpha_rep]

third=alpha ^ omega
assert third in classes and third != 0 and third != alpha and third != omega
assert class_data[third]['square']==1
assert (class_data[third]['min_weight'],len(class_data[third]['mins'])) == (6,3)

# Every minimizing support is a single simple cycle in the dual graph.
def dual_cycle_length(z):
    dadj={i:[] for i in range(len(FACETS))}
    for e,ei in EIDX.items():
        if (z>>ei)&1:
            a,b=EDGE_FACES[e]
            dadj[a].append(b); dadj[b].append(a)
    active={u for u in dadj if dadj[u]}
    assert active
    assert all(len(dadj[u])==2 for u in active)
    seen={next(iter(active))}; stack=list(seen)
    while stack:
        u=stack.pop()
        for w in dadj[u]:
            if w not in seen: seen.add(w); stack.append(w)
    assert seen==active
    return len(active)

for q in nonzero:
    for z in class_data[q]['mins']:
        assert dual_cycle_length(z) == z.bit_count()

# Full coset weight enumerators are included as an extra replayable check.
def hist(reps):
    d={}
    for z in reps: d[z.bit_count()]=d.get(z.bit_count(),0)+1
    return ','.join(f'{w}:{d[w]}' for w in sorted(d))

print('VERIFY_OK f=8,24,16 H1_F2_dim=2 aut_order=1 '
      'nonzero_cosystolic_spectrum=5x1,6x5,6x3 '
      'unique_weight5_support=BC,BG,CE,DE,DG '
      'cup_square_zero_class=6x5 all_minimizers_single_dual_cycles=yes')
print('WEIGHT_ENUM_ALPHA',hist(classes[alpha]))
print('WEIGHT_ENUM_OMEGA',hist(classes[omega]))
print('WEIGHT_ENUM_ALPHA_PLUS_OMEGA',hist(classes[third]))
