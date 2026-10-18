"""Independent Fraction-based check of seasonal permutations and persistence witness.
Run: python3 leslie_fraction.py  (Python standard library only)
"""
from fractions import Fraction as F
from itertools import permutations, product

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)) for i in (0,1))

def prodm(mats):
    P=((F(1),F(0)),(F(0),F(1)))
    for M in mats:
        P=mm(P,M)
    return P

def trace(P):return P[0][0]+P[1][1]
def det(P):return P[0][0]*P[1][1]-P[0][1]*P[1][0]
def mat(b,s,a):return ((F(0),F(b)),(F(s),F(a)))
def signed_area(a,s):
    return (a[0]*(s[1]-s[2])+a[1]*(s[2]-s[0])+a[2]*(s[0]-s[1]))

one=F(1)
a=(F(1,4),F(1,2),F(3,4)); s=(F(1,4),F(3,4),F(1,4));b=F(4,3)
M=[mat(b,s[i],a[i]) for i in range(3)]
C=prodm(M); R=prodm([M[0],M[2],M[1]])
assert trace(C)==F(73,96) and trace(R)==F(35,32)
assert det(C)==det(R)==-F(1,9)
assert one-trace(C)+det(C)==F(37,288)>0
assert one-trace(R)+det(R)==-F(59,288)<0
assert trace(C)-trace(R)==b*signed_area(a,s)==-F(1,3)
# Independent integer-grid sampling; the symbolic identity in the proof covers all parameters.
count=0
for aa in product((F(1,5),F(2,5),F(3,5),F(4,5)),repeat=3):
 for ss in product((F(1,4),F(1,2),F(3,4)),repeat=3):
  bb=F(7,5)
  L=[mat(bb,ss[i],aa[i]) for i in range(3)]
  x=prodm(L);y=prodm([L[0],L[2],L[1]])
  assert trace(x)-trace(y)==bb*signed_area(aa,ss)
  assert det(x)==det(y)==-bb**3*ss[0]*ss[1]*ss[2]
  vals=[trace(prodm([L[i] for i in p])) for p in permutations(range(3))]
  assert set(vals)=={trace(x),trace(y)}
  count+=1
print('PASS: rational reversal and persistence example; %d exact parameter triples verified.' % count)
