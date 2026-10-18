"""Standalone exact verification of the three-rational-hyperflex plane-quartic classification.

Uses integer arithmetic for all 32767 ternary quartics over F2, and SymPy
only for an independent geometric smoothness test of the representative.
Run: python verify_three_hyperflex.py
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json
import sympy as sp

mons=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
ind={m:i for i,m in enumerate(mons)}
points=tuple(range(1,8))

def dot(a,b):return (a&b).bit_count()&1

def eval_at_mono(m,P):return int(all(e==0 or P&(1<<i) for i,e in enumerate(m)))

def form_from_terms(terms):return sum(1<<ind[t] for t in terms)
F0=form_from_terms([(3,1,0),(2,2,0),(1,3,0),
                    (3,0,1),(2,0,2),(1,0,3),
                    (0,3,1),(0,2,2),(0,1,3)])
assert F0==15150

def eval_masks():
    fm={};gm={}
    for P in points:
      fm[P]=sum(eval_at_mono(m,P)<<i for i,m in enumerate(mons))
      gm[P]=tuple(sum(( (m[a]&1) and eval_at_mono(tuple(m[j]-(j==a) for j in range(3)),P) )<<i
                            for i,m in enumerate(mons)) for a in range(3))
    return fm,gm
FM,GM=eval_masks()

def restrict_masks(P,L):
    Q=next(Q for Q in points if Q!=P and dot(Q,L)==0)
    rows=[0]*5
    for i,m in enumerate(mons):
      c=[1,0,0,0,0]
      n=0
      for a in range(3):
        for rep in range(m[a]):
          v=[0]*5
          for k in range(n+1):
            if c[k]:
              if P&(1<<a):v[k]^=1
              if Q&(1<<a):v[k+1]^=1
          c=v;n+=1
      for k,v in enumerate(c):
        if v: rows[k]|=1<<i
    return tuple(rows)
RM={(P,L):restrict_masks(P,L) for P in points for L in points if dot(P,L)==0}
assert len(RM)==21

def hyperflexes(f):
    hits=[]
    for P in points:
        if dot(f,FM[P]):continue
        g=sum(dot(f,GM[P][a])<<a for a in range(3))
        if not g:continue
        assert dot(P,g)==0
        line=RM[P,g]
        # exact tangent intersection divisor 4P; exclude contained lines.
        if all(dot(f,line[k])==0 for k in range(4)) and dot(f,line[4])==1:
            hits.append(P)
    return tuple(hits)

triple_forms={}
count=Counter()
for f in range(1,1<<15):
    H=hyperflexes(f)
    count[len(H)]+=1
    if len(H)>=3:
        assert len(H)==3 and H[0]^H[1]^H[2]!=0, (f,H)
        assert H not in triple_forms, (f,H)
        triple_forms[H]=f
assert len(triple_forms)==28
all_noncollinear={p for p in __import__('itertools').combinations(points,3) if p[0]^p[1]^p[2]!=0}
assert set(triple_forms)==all_noncollinear
assert triple_forms[(1,2,4)]==F0

# Exact geometric check over algebraic closure, not finite-extension sampling.
x,y,z=sp.symbols('x y z')
F=sum(x**a*y**b*z**c for i,(a,b,c) in enumerate(mons) if F0>>i&1)
for chart_var in (x,y,z):
    affine=F.subs(chart_var,1)
    vs=[v for v in (x,y,z) if v!=chart_var]
    gb=sp.groebner([affine,sp.diff(affine,vs[0]),sp.diff(affine,vs[1])],*vs,modulus=2)
    assert gb.is_zero_dimensional or list(gb.polys)==[sp.Poly(1,*vs,modulus=2)]
    assert list(gb.polys)==[sp.Poly(1,*vs,modulus=2)],(chart_var,list(gb.polys))
assert hyperflexes(F0)==(1,2,4)
assert tuple(P for P in points if not dot(F0,FM[P]))==(1,2,4)

# Every noncollinear rational triple is the image of the coordinate triangle.
# Explicitly cross-check the full PGL3(F2) orbit with the direct enumeration.
def rank_rows(rows):
    piv={}
    for row in rows:
      while row:
        k=row.bit_length()-1
        if k in piv:row^=piv[k]
        else:piv[k]=row;break
    return len(piv)

def mul_poly(A,B):
    out={}
    for m,ca in A.items():
      for n,cb in B.items():
        j=tuple(m[i]+n[i] for i in range(3))
        out[j]=out.get(j,0)^ca*cb
    return {m:v for m,v in out.items() if v}

def apply_rows(f,rows):
    factors=[{tuple(int(j==i) for j in range(3)):1 for i in range(3) if rows[k]>>i&1} for k in range(3)]
    powers=[[{(0,0,0):1}] for _ in range(3)]
    for j in range(3):
      for k in range(4): powers[j].append(mul_poly(powers[j][-1],factors[j]))
    mask=0
    for i,(a,b,c) in enumerate(mons):
      if f>>i&1:
        for exp,v in mul_poly(mul_poly(powers[0][a],powers[1][b]),powers[2][c]).items():
          if v:mask^=1<<ind[exp]
    return mask
all_matrices=[a for a in product(points,repeat=3) if rank_rows(a)==3]
assert len(all_matrices)==168
images={apply_rows(F0,M) for M in all_matrices}
assert len(images)==28 and images==set(triple_forms.values())
assert sum(1 for M in all_matrices if apply_rows(F0,M)==F0)==6

cert={'representative_mask':F0,'total_polynomials_checked':32767,'representative_geometrically_smooth':True,
      'all_forms_with_at_least_three_smooth_rational_hyperflex_points':len(triple_forms),
      'image_of_pgl3_f2_orbit_equals_extremal_forms':True,
      'automorphism_group_order':6,
      'hyperflex_count_distribution_all_nonzero_forms':dict(sorted(count.items())),
      'extremal_forms':[
        {'rational_hyperflex_point_vectors':list(T),'form_bitmask':F} for T,F in sorted(triple_forms.items())]}
path=Path(__file__).with_name('three_hyperflex_certificate.json')
path.write_text(json.dumps(cert,indent=2)+'\n')
print('PASS: 32767 quartics checked, exactly 28 with three rational hyperflexes.')
print('PASS: representative smooth on all three affine charts over algebraic closure.')
print('PASS: one PGL3(F2) orbit of size 28, stabilizer order 6.')
print('Distribution across all forms:',dict(sorted(count.items())))
