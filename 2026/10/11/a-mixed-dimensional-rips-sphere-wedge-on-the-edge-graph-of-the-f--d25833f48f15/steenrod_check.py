#!/usr/bin/env python3
"""GF2 cochain check of Sq^2:H^3 -> H^5 via classical cup-one formula."""
from verify import FACES
from collections import defaultdict
F=defaultdict(list)
for s in FACES:F[s.bit_count()-1].append(s)
ind3={s:i for i,s in enumerate(F[3])};ind5={s:i for i,s in enumerate(F[5])}

def echelon(vecs):
  piv={}
  for c in vecs:
    while c:
      bit=c.bit_length()-1
      if bit in piv:c^=piv[bit]
      else:piv[bit]=c;break
  return piv

def reduce_vec(c,piv):
 while c:
  bit=c.bit_length()-1
  if bit in piv:c^=piv[bit]
  else:return c
 return 0

def boundary(s):
 a=s
 while a:
  bit=a&-a;a-=bit
  yield s^bit

def coboundary_basis(k):
 low=F[k];lowset=set(low)
 highs=F[k+1];index={s:i for i,s in enumerate(highs)}
 incidence={s:0 for s in low}
 for high in highs:
  for face in boundary(high):
   incidence[face] |= (1<<index[high])
 return [incidence[s] for s in low]

# Linear equations imposing δ_3 α=0, one for each 4-simplex.
eqs=[]
for high in F[4]:
 eq=0
 for f in boundary(high): eq^=1<<ind3[f]
 eqs.append(eq)
P=echelon(eqs)
print('rank_equations',len(P),flush=True)
free=[i for i in range(len(F[3])) if i not in P]
print('free_vars',len(free),flush=True)
# coboundary space in C^3: image δ_2
R=echelon(coboundary_basis(2))
assert len(R)==1263
print('rank_coboundary3',len(R),flush=True)
alpha=None
for j in free:
   x=1<<j
   # equations with high pivot plus lower-index terms. Solve ascending pivot order.
   for i in sorted(P):
      e=P[i]
      if (e&x).bit_count()%2: x|=1<<i
   assert all((eq&x).bit_count()%2==0 for eq in eqs)
   if reduce_vec(x,R):
      alpha=x
      print('cohomology_generator_free_index',j,'support',x.bit_count(),flush=True)
      break
assert alpha is not None

# Classical simplicial cup-one: (α ∪_1 α)(v0...v5) = Σ_{j=0}^2 α(v0..vj,v(j+3)..v5) α(vj..v(j+3)).
Sq=0
for s in F[5]:
 vertices=[i for i in range(32) if s>>i&1]
 z=0
 for j in range(3):
  left=vertices[:j+1]+vertices[j+3:]
  right=vertices[j:j+4]
  lm=sum(1<<u for u in left)
  rm=sum(1<<u for u in right)
  z ^= ((alpha>>ind3[lm])&1) & ((alpha>>ind3[rm])&1)
 if z:Sq |=1<<ind5[s]
print('Sq_support',Sq.bit_count(),flush=True)
# Cocylicity of Sq in degree 5.
for s in F[6]:
    val=0
    for f in boundary(s):val^=Sq>>ind5[f]&1
    assert val==0
print('Sq_cocycle_yes',flush=True)
# Is Sq a boundary from C4? rank=rank ∂_5.
R5=echelon(coboundary_basis(4))
assert len(R5)==2104
res=reduce_vec(Sq,R5)
print('rank_coboundary5',len(R5),'Sq_nonzero_cohomology',bool(res),'residual_support',res.bit_count(),flush=True)
assert res == 0, 'Sq^2 unexpectedly nonzero'
print('STEENROD_OK Sq2_is_zero')
