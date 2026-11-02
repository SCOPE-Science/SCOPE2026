"""Complete exact census of balanced three-container layouts of the binary [15,4] simplex code.
This is a standalone scientific checker; standard Python only.
"""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
from math import lcm

V=tuple(range(1,16));ALL=(1<<15)-1

def mask(items):return sum(1<<(v-1) for v in items)

def vectors(m):return tuple(v for v in V if (m>>(v-1))&1)

# The 15 projective hyperplanes and 35 projective lines of F_2^4.
H=tuple(mask(v for v in V if (normal&v).bit_count()%2==0) for normal in V)
L=tuple(sorted({mask((a,b,a^b)) for a,b in combinations(V,2)}))
assert len(H)==15 and len(set(H))==15 and all(h.bit_count()==7 for h in H)
assert len(L)==35 and all(x.bit_count()==3 for x in L)

PRODUCTS=(5,8,9,12)
DEN=lcm(62,*[125-p for p in PRODUCTS])
WEIGHT={p:DEN*p//(125-p) for p in PRODUCTS}
RAINBOW_WEIGHT=DEN//62
assert DEN==475427160

def layout_score(A,B,C):
 score=0;profile=Counter()
 for h in H:
  a=(A&h).bit_count();b=(B&h).bit_count();c=(C&h).bit_count()
  assert a+b+c==7
  p=a*b*c
  assert p in (0,)+PRODUCTS
  profile[p]+=1
  if p:score+=WEIGHT[p]
 rain=sum(1 for l in L if (l&A).bit_count()==(l&B).bit_count()==(l&C).bit_count()==1)
 score-=RAINBOW_WEIGHT*rain
 return score,tuple(profile[p] for p in (0,)+PRODUCTS),rain

# Every unlabeled balanced partition is represented exactly once by:
# (i) choosing the block A containing vector 1; (ii) choosing B to contain
# the smallest remaining vector; (iii) taking C as the complement.
best=None;winners=set();hist=Counter();tested=0;profiles=Counter()
for four in combinations(range(2,16),4):
 A=mask((1,)+four)
 rem=[v for v in V if not (A>>(v-1))&1]
 anchor=rem[0]
 for others in combinations(rem[1:],4):
  B=mask((anchor,)+others)
  C=ALL^A^B
  assert A.bit_count()==B.bit_count()==C.bit_count()==5
  tested+=1
  score,prof,rain=layout_score(A,B,C)
  hist[score]+=1
  if best is None or score<best:best=score;winners={tuple(sorted((A,B,C)))}
  elif score==best:winners.add(tuple(sorted((A,B,C))))
assert tested==126126==sum(hist.values())
assert len(hist)==13
assert len(winners)==336
expect=Fraction(DEN+best,DEN)
assert expect==Fraction(7491,3596)
second=Fraction(DEN+sorted(hist)[1],DEN)
assert second==Fraction(99660239,47542716)

# 5-cap = no projective line lies entirely in the set.
def is_cap(A):return A.bit_count()==5 and all((A&l)!=l for l in L)
CAPS={mask(c) for c in combinations(V,5) if is_cap(mask(c))}
assert len(CAPS)==1008
cap_parts=set()
for A in CAPS:
 if not A&1:continue
 for B in CAPS:
  if A&B:continue
  C=ALL^A^B
  if C in CAPS:cap_parts.add(tuple(sorted((A,B,C))))
assert len(cap_parts)==336 and winners==cap_parts
for A,B,C in winners:
 assert layout_score(A,B,C)[1]==(0,0,0,15,0)
 assert layout_score(A,B,C)[2]==5

# Orbit of the explicit witness under all 20160 invertible F_2-linear maps.
# Enumerate ordered independent images of the four standard basis vectors.
base=tuple(sorted((mask((1,2,4,8,15)),mask((3,5,7,10,11)),mask((6,9,12,13,14)))))
assert base in winners

def span(values):
 ans={0}
 for v in values:ans|={z^v for z in tuple(ans)}
 return ans

def transform(m,tab):return mask(tab[v] for v in vectors(m))

orbit=set();matrix_count=0
for images in product(V,repeat=4):
 if len(span(images))<16:continue
 matrix_count+=1
 tab={v:0 for v in V}
 for v in V:
  z=0
  for i in range(4):
   if v&(1<<i):z^=images[i]
  tab[v]=z
 orbit.add(tuple(sorted(transform(m,tab) for m in base)))
assert matrix_count==20160
assert len(orbit)==336 and orbit==winners

print('VERIFY_OK')
print('projective_hyperplanes',len(H),'projective_lines',len(L))
print('unlabeled_balanced_partitions',tested)
print('distinct_exact_expectations',len(hist))
print('minimum_expected_rounds',str(expect))
print('second_smallest_expected_rounds',str(second))
print('number_of_unlabeled_minimizers',len(winners))
print('five_caps',len(CAPS),'three_cap_partitions',len(cap_parts))
print('GL4_2_order',matrix_count,'optimizer_orbit_size',len(orbit))
print('witness',tuple(vectors(m) for m in base))
print('optimizer_hyperplane_products',{'9':15},'rainbow_lines',5)
print('entire_census_histogram',[(str(Fraction(DEN+s,DEN)),hist[s]) for s in sorted(hist)])
