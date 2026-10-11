#!/usr/bin/env python3
import json
from collections import Counter

P=19
RES={pow(a,2,P) for a in range(1,P)}
OUT=[]
for x in range(P):
    m=0
    for y in range(P):
        if x!=y and ((y-x)%P) in RES:
            m |= 1<<y
    OUT.append(m)

assert all(m.bit_count()==9 for m in OUT)
assert all((OUT[x]&OUT[y]).bit_count()==4 for x in range(P) for y in range(x+1,P))

simp=[[] for _ in range(6)]
for mask in range(1,1<<P):
    k=mask.bit_count()
    if k>5:
        continue
    deg=[]
    mm=mask
    while mm:
        bit=mm & -mm
        v=bit.bit_length()-1
        mm-=bit
        deg.append((OUT[v]&mask).bit_count())
    # A finite tournament is transitive iff its score multiset is {0,...,k-1}.
    if len(set(deg))==k and min(deg)==0 and max(deg)==k-1:
        simp[k].append(mask)

face_vector=[len(simp[k]) for k in range(1,6)]
assert face_vector == [19,171,684,1026,342]
chi=sum(((-1)**(k-1))*len(simp[k]) for k in range(1,6))
assert chi == -152

# Simplicial boundary ranks over finite fields; C_q is indexed by (q+1)-vertex faces.
def rank_boundary(cardinality, prime):
    cols=simp[cardinality]
    rows=simp[cardinality-1]
    row_index={m:i for i,m in enumerate(rows)}
    piv={}
    for mask in cols:
        verts=[i for i in range(P) if (mask>>i)&1]
        col={}
        for j,v in enumerate(verts):
            r=row_index[mask^(1<<v)]
            col[r]=(1 if j%2==0 else prime-1)
        while col:
            r=max(col)
            if r not in piv:
                inv=pow(col[r],-1,prime)
                col={i:(a*inv)%prime for i,a in col.items() if (a*inv)%prime}
                piv[r]=col
                break
            factor=col[r]
            for i,a in piv[r].items():
                nv=(col.get(i,0)-factor*a)%prime
                if nv:
                    col[i]=nv
                else:
                    col.pop(i,None)
    return len(piv)

field_checks={}
for prime in (2,3,5,7,19):
    ranks=[rank_boundary(k,prime) for k in range(2,6)]
    dims=face_vector
    betti=[dims[0]-ranks[0]]
    for q in range(1,4):
        betti.append(dims[q]-ranks[q-1]-ranks[q])
    betti.append(dims[4]-ranks[3])
    assert ranks == [18,153,531,341]
    assert betti == [1,0,0,154,1]
    field_checks[str(prime)]={"boundary_ranks":ranks,"betti":betti}

# Affine Paley subgroup A={x -> a x+b : a quadratic residue, b arbitrary}.
def image_mask(mask, perm):
    z=0
    mm=mask
    while mm:
        bit=mm & -mm
        v=bit.bit_length()-1
        mm-=bit
        z |= 1<<perm[v]
    return z

def orientation_sign(mask, perm):
    verts=[i for i in range(P) if (mask>>i)&1]
    images=[perm[i] for i in verts]
    inv=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
    return -1 if inv%2 else 1

def affine_order(a,b):
    aa,bb=1,0
    for n in range(1,172):
        aa=(a*aa)%P
        bb=(a*bb+b)%P
        if aa==1 and bb==0:
            return n
    raise AssertionError

all_faces=[m for k in range(1,6) for m in simp[k]]
character_rows=[]
for a in sorted(RES):
    for b in range(P):
        perm=[(a*x+b)%P for x in range(P)]
        # Verify it preserves every directed edge.
        for x in range(P):
            for y in range(P):
                if x!=y:
                    assert (((OUT[x]>>y)&1) == ((OUT[perm[x]]>>perm[y])&1))
        lefschetz=0
        fixed_by_cardinality=Counter()
        signed_trace_by_cardinality=Counter()
        for mask in all_faces:
            if image_mask(mask,perm)==mask:
                k=mask.bit_count()
                s=orientation_sign(mask,perm)
                fixed_by_cardinality[k]+=1
                signed_trace_by_cardinality[k]+=s
                lefschetz += ((-1)**(k-1))*s
        # Published homotopy type determined below gives H0=Q, H3=Q^154,H4=Q.
        # A has odd order, hence the 1-dimensional rational H4 character is trivial.
        h3_trace=2-lefschetz
        character_rows.append({
            "a":a,"b":b,"order":affine_order(a,b),
            "lefschetz":lefschetz,"h3_trace":h3_trace,
            "fixed_faces":dict(sorted(fixed_by_cardinality.items())),
            "signed_chain_trace":dict(sorted(signed_trace_by_cardinality.items()))
        })

assert len(character_rows)==171
char_hist=Counter()
for r in character_rows:
    if r["a"]==1 and r["b"]==0:
        cls="identity"
    elif r["a"]==1:
        cls="nonidentity_translation"
    else:
        cls="nontranslation_affine"
    char_hist[(cls,r["h3_trace"],r["lefschetz"])]+=1
assert char_hist == Counter({
    ("identity",154,-152):1,
    ("nonidentity_translation",2,0):18,
    ("nontranslation_affine",1,1):152,
})

# Restriction to C_19: a copies of the trivial rational representation and
# b copies of Q(zeta_19), whose character is 18 at identity and -1 otherwise.
b=(154-2)//19
a=2+b
assert (a,b)==(10,8)

result={
    "definition":{"prime":19,"quadratic_residues":sorted(RES)},
    "doubly_regular":{"outdegree":9,"common_outneighbors_for_each_pair":4},
    "face_vector":face_vector,
    "euler_characteristic":chi,
    "field_checks":field_checks,
    "affine_group_order":171,
    "h3_character_histogram":[
        {"class":k[0],"h3_trace":k[1],"lefschetz":k[2],"count":n}
        for k,n in sorted(char_hist.items())
    ],
    "c19_rational_decomposition":{"trivial_multiplicity":a,"cyclotomic_18d_multiplicity":b},
    "status":"VERIFY_OK"
}
print(json.dumps(result,sort_keys=True,separators=(",",":")))
