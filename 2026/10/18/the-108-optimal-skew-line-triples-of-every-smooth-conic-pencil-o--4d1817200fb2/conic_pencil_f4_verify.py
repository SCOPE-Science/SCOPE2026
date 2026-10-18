#!/usr/bin/env python3
"""Exact GF(4) certificate for smooth conic pencils and their skew-line witnesses.

Use python3 conic_pencil_f4_verify.py. No nonstandard dependencies.
"""
from itertools import product, combinations
from collections import Counter

# GF(4) = GF(2)[w]/(w*w+w+1), encoded 0,1,w,w+1 by 0,1,2,3.
M = ((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
INV=(None,1,3,2)
def mul(a,b): return M[a][b]
def add_vec(a,b): return tuple(x^y for x,y in zip(a,b))
def scale(t,a): return tuple(M[t][x] for x in a)
def normal(a):
    last=next(x for x in reversed(a) if x)
    return scale(INV[last],a)

def p2():
    return [(x,y,1) for x in range(4) for y in range(4)] + [(x,1,0) for x in range(4)] + [(1,0,0)]
P=p2(); L=P
monomials=lambda p: (M[p[0]][p[0]],M[p[1]][p[1]],M[p[2]][p[2]], M[p[0]][p[1]],M[p[0]][p[2]],M[p[1]][p[2]])
MON=[monomials(p) for p in P]
def evaluate(form,mon): return M[form[0]][mon[0]]^M[form[1]][mon[1]]^M[form[2]][mon[2]]^M[form[3]][mon[3]]^M[form[4]][mon[4]]^M[form[5]][mon[5]]

def is_geometrically_smooth(c):
    a,b,z,d,e,f = c
    if not (d or e or f): return False
    r=(f,e,d)  # unique projective critical point of polar derivatives
    return evaluate(c,monomials(r))!=0

LINEPOINTS=[tuple(j for j,p in enumerate(P) if M[l[0]][p[0]]^M[l[1]][p[1]]^M[l[2]][p[2]]==0) for l in L]
assert len(P)==21 and len(LINEPOINTS)==21 and all(len(x)==5 for x in LINEPOINTS)
forms=sorted({normal(v) for v in product(range(4),repeat=6) if any(v)})
assert len(forms)==1365
form_id={v:i for i,v in enumerate(forms)}
smooth=tuple(is_geometrically_smooth(v) for v in forms)
assert sum(smooth)==1008
masks=[]
for v in forms:
    vals=tuple(evaluate(v,mon) for mon in MON)
    masks.append(sum(1<<i for i,ln in enumerate(LINEPOINTS) if all(vals[j]!=0 for j in ln)))

# Explicit canonical pencil C_[s:t] = s(XZ+Y^2) + t(XY+w Z^2).
Q=(0,1,0,0,1,0)
R=(0,0,2,1,0,0)
CAN=sorted(form_id[normal(v)] for v in [Q,R,add_vec(Q,R),add_vec(Q,scale(2,R)),add_vec(Q,scale(3,R))])
assert all(smooth[i] for i in CAN)
FAMILY=(form_id[normal(R)], form_id[normal(Q)], form_id[normal(add_vec(Q,R))],form_id[normal(add_vec(Q,scale(2,R)))],form_id[normal(add_vec(Q,scale(3,R)))])
line_member_masks=[]
for j in range(21):
    line_member_masks.append(sum(1<<i for i,ci in enumerate(FAMILY) if (masks[ci]>>j)&1))
ALL=31
covers3=[tr for tr in combinations(range(21),3) if line_member_masks[tr[0]]|line_member_masks[tr[1]]|line_member_masks[tr[2]]==ALL]
assert len(covers3)==108
assert sum(bool(v) for v in line_member_masks)==15
assert not any(line_member_masks[i]|line_member_masks[j]==ALL for i,j in combinations(range(21),2))

# Independent complete enumeration of all 2-dimensional subspaces in GF(4)^6.
# Every such pencil consists of five projective quadratic forms; each appears C(5,2)=10 times
# among the C(1365,2) pairs of projective forms. Canonicalize by the sorted set of five IDs.
pencils=set()
all_smooth_count=0
smooth_pencils=set()
for ia,a in enumerate(forms):
    for ib in range(ia+1,len(forms)):
        b=forms[ib]
        key=tuple(sorted((ia,ib,form_id[normal(add_vec(a,b))],
                               form_id[normal(add_vec(a,scale(2,b)))],
                               form_id[normal(add_vec(a,scale(3,b)))])))
        if key in pencils: continue
        assert len(set(key))==5
        pencils.add(key)
        if all(smooth[i] for i in key):
            smooth_pencils.add(key)
assert len(pencils)==93093,(len(pencils))
assert len(smooth_pencils)==20160,len(smooth_pencils)
assert tuple(CAN) in smooth_pencils

# Group-theoretic check: |PGL_3(F4)|/3 = 20160, and all smooth pencils form one orbit.
assert 4**3*(4**3-1)*(4**2-1)//3==20160

# Over all 20,160 smooth pencils, enumerate minimal witness number and count optimal triples.
# The first-named pencil isomorphic to every other via the frame/Frobenius argument in RESULT.md,
# but we also check the incidence property independently over the whole pencil census.
min_witness_hist=Counter()
triple_hist=Counter()
line_hist=Counter()
for key in smooth_pencils:
    im=[sum(1<<j for j,ci in enumerate(key) if (masks[ci]>>line)&1) for line in range(21)]
    line_hist[sum(bool(v) for v in im)]+=1
    assert all(any((masks[ci]>>line)&1 for line in range(21)) for ci in key)
    assert all((im[i]|im[j])!=ALL for i,j in combinations(range(21),2))
    num3=sum((im[i]|im[j]|im[k])==ALL for i,j,k in combinations(range(21),3))
    triple_hist[num3]+=1
    if num3:min_witness_hist[3]+=1
    else:min_witness_hist['>3']+=1
assert min_witness_hist=={3:20160},min_witness_hist
assert triple_hist=={108:20160},triple_hist
assert line_hist=={15:20160},line_hist
assert (4,5,10) in covers3, covers3[:2]
print('VERIFY_OK')
print('field=GF(4), w^2+w+1=0; projective_points=21; projective_lines=21')
print('projective_conics=1365, smooth_conics=1008')
print('all_pencils=93093, smooth_rational_pencils=20160')
print('smooth_pencil_3_witness_min=20160; other=0')
print('optimal_unordered_witness_triples_per_pencil=108')
print('lines_skew_to_at_least_one_member_per_pencil=15; others=6')
print('canonical_conics=Q:XZ+Y^2, R:XY+w Z^2')
print('explicit_witness_lines=',L[4],L[5],L[10])
print('explicit_witness_incidence_masks=',[bin(line_member_masks[i]) for i in (4,5,10)])
