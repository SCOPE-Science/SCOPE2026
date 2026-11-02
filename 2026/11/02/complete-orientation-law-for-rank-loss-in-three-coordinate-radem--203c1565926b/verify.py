from itertools import product
from fractions import Fraction
from collections import Counter

def cross(u,v):return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def dot(u,v):return sum(x*y for x,y in zip(u,v))
S=list(product((-1,1),repeat=3))

def rank_of_sketch(normal, cols):
  # Any two projected images are independent iff their cross product
  # has a nonzero component in the normal direction.
  nonzero=[s for s in cols if cross(s,normal)!=(0,0,0)]
  if len(nonzero)<2:return len(nonzero)
  for i in range(len(nonzero)):
    for j in range(i+1,len(nonzero)):
      if dot(normal,cross(nonzero[i],nonzero[j])):return 2
  return 1

def theoretical(normal,L):
 a,b,c=map(abs,normal)
 if a==b==c and a>0: return (3*Fraction(1,2)**L-2*Fraction(1,4)**L,Fraction(1,4)**L,'diagonal')
 if sum(t==0 for t in (a,b,c))==2:return (2*Fraction(1,2)**L,Fraction(0),'axis')
 if a==b or b==c or a==c:return (Fraction(1,2)**L+2*Fraction(1,4)**L,Fraction(0),'pair')
 return (4*Fraction(1,4)**L,Fraction(0),'generic')

N=0
for norm in product(range(-2,3),repeat=3):
 if norm==(0,0,0):continue
 for L in range(2,5):
  counts=Counter(rank_of_sketch(norm,cols) for cols in product(S,repeat=L))
  failure=Fraction(counts[0]+counts[1],8**L)
  zero=Fraction(counts[0],8**L)
  f,z,case=theoretical(norm,L)
  expected_loss=Fraction(counts[1]+2*counts[0],8**L)
  assert (failure,zero,expected_loss)==(f,z,f+z),(norm,L,case,counts,f,z)
  N+=1
print('VERIFIED',N,'normal-length cases: rank and zero probabilities exact')
for norm in ((1,2,3),(1,1,2),(1,0,0),(1,1,1)):
 for L in (2,3,4,5,6):
  f,z,case=theoretical(norm,L)
  print('case',case,'L',L,'rankdef',f,'zero',z,'expected squared Frobenius loss for partial isometry',f+z)
