#!/usr/bin/env python3
"""Exact finite checker for the integral layer-involution homology module.

Only the Python standard library is required. Incidence pairs are oriented
from the matched graph vertex toward the opposite endpoint.
"""
from collections import Counter
from itertools import permutations, product

V = tuple(range(6))
E = sorted({tuple(sorted((3*t+i, 3*t+(i+1)%3)))
            for t in (0,1) for i in range(3)} | {(i,i+3) for i in range(3)})
INC = sorted((v,e) for e in E for v in e)
idx = {a:j for j,a in enumerate(INC)}
outs = [[idx[(v,e)] for e in E if v in e] for v in V]
head = [next(w for w in e if w!=v) for v,e in INC]

# Enumerate every acyclic incidence matching, including the empty face.
F = []
for choices in product(*([None]+outs[v] for v in V)):
    face = tuple(sorted(k for k in choices if k is not None))
    if len({INC[k][1] for k in face}) != len(face):
        continue
    nxt = {INC[k][0]:head[k] for k in face}
    acyclic = True
    for v in nxt:
        seen=set(); x=v
        while x in nxt and x not in seen:
            seen.add(x); x=nxt[x]
        if x in seen:
            acyclic=False; break
    if acyclic:
        F.append(face)
assert len(F)==1728 and len(set(F))==1728
faces = {k: sorted(face for face in F if len(face)==k) for k in range(1,6)}
assert tuple(len(faces[k]) for k in range(1,6)) == (18,126,428,705,450)

# Exact F_2 ranks of all integral simplicial boundary matrices.
def rank2(columns):
    pivots={}
    for column in columns:
        while column:
            p=column.bit_length()-1
            if p in pivots:
                column ^= pivots[p]
            else:
                pivots[p]=column
                break
    return len(pivots)

ranks={}
for k in range(2,6):
    lower={f:j for j,f in enumerate(faces[k-1])}
    cols=[]
    for f in faces[k]:
        bits=0
        for i in range(k):bits ^= 1 << lower[f[:i]+f[i+1:]]
        cols.append(bits)
    ranks[k-1]=rank2(cols)
assert tuple(ranks[k] for k in (1,2,3,4)) == (17,109,319,386)

# The full group of automorphisms of the triangular-prism graph is S_3 x C_2.
def incidence_action(sigma,layer_switch):
    vm={i+3*t:sigma[i]+3*(t^layer_switch) for t in (0,1) for i in range(3)}
    return [idx[(vm[v],tuple(sorted(vm[w] for w in e)))] for v,e in INC]

def face_action(face,inc_perm):
    return tuple(sorted(inc_perm[i] for i in face))

def perm_sign(images):
    inversions=sum(images[i]>images[j] for i in range(len(images))
                   for j in range(i+1,len(images)))
    return (-1)**inversions

def cycletype3(sigma):
    seen=set();res=[]
    for v in range(3):
        if v in seen:continue
        n=0;u=v
        while u not in seen:
            seen.add(u); n+=1; u=sigma[u]
        res.append(n)
    return tuple(sorted(res,reverse=True))

fixed_char={}
setF = set(F)
for sigma in permutations(range(3)):
    for swap in (0,1):
        perm=incidence_action(sigma,swap)
        traces=Counter()
        for f in F:
            gf=face_action(f,perm)
            assert gf in setF
            if f: 
                images=[perm[i] for i in f]
                if gf==f:
                    traces[len(f)-1] += perm_sign(images)
        # Euler-Lefschetz and rational concentration at degree 4.
        char=sum((-1)**k*trace for k,trace in traces.items()) - 1
        key=(cycletype3(sigma),swap)
        if key in fixed_char:assert fixed_char[key] == char
        fixed_char[key]=char
assert fixed_char == {
    ((1,1,1),0):64, ((1,1,1),1):-4,
    ((2,1),0):0, ((2,1),1):-8,
    ((3,),0):1, ((3,),1):-1}

# Full top-dimensional cycle space over F_2 (no top boundaries).
top=faces[5]
topidx={f:j for j,f in enumerate(top)}
lowidx={f:j for j,f in enumerate(faces[4])}
col_piv={}; kernel=[]
for j,f in enumerate(top):
    boundary=0
    for i in range(5): boundary ^= 1 << lowidx[f[:i]+f[i+1:]]
    witness=1<<j
    while boundary:
        p=boundary.bit_length()-1
        if p in col_piv:
            b,c = col_piv[p]
            boundary ^= b
            witness ^= c
        else:
            col_piv[p]=(boundary,witness)
            break
    else:
        kernel.append(witness)
assert len(col_piv)==386 and len(kernel)==64

# Layer-interchange acts on 5-element incidence faces in 225 pairs.
inc_perm=incidence_action((0,1,2),1)
perm=[topidx[face_action(f,inc_perm)] for f in top]
assert all(perm[perm[j]]==j and perm[j]!=j for j in range(450))

def apply_perm(bits):
    out=0
    while bits:
        least=bits&-bits
        j=least.bit_length()-1
        out ^= 1<<perm[j]
        bits ^= least
    return out

# Method A: direct rank on a basis of the mod-two cycle space.
modular_rank=rank2([z^apply_perm(z) for z in kernel])
assert modular_rank==30

# Method B: independent matrix-stack rank, 450 columns, 1155 rows.
rows=[0]*len(faces[4])
for j,f in enumerate(top):
    for i in range(5): rows[lowidx[f[:i]+f[i+1:]]] ^= 1<<j
constraint=[1<<j for j in range(450)]
for j,k in enumerate(perm):constraint[k] ^= 1<<j
stacked_rank=rank2(rows+constraint)
assert stacked_rank==416 == ranks[4]+modular_rank

# Rational +/- dimensions follow from involution trace -4.
p=(64+fixed_char[((1,1,1),1)])//2
q=(64-fixed_char[((1,1,1),1)])//2
assert (p,q)==(30,34)
assert (p-modular_rank,q-modular_rank,modular_rank)==(0,4,30)
print('VERIFY_OK')
print('face_vector: (18,126,428,705,450)')
print('mod2_boundary_ranks: (17,109,319,386)')
print('degree4_rational_rank: 64')
print('layer_swap_degree4_trace: -4')
print('layer_swap_F2_rank_I_plus_t: 30')
print('independent_stacked_rank: 416')
print('integral_C2_lattice: 30 regular plus 4 sign')
