from itertools import combinations,permutations
from collections import Counter
P=list(range(9)); C=list(combinations(P,4));
d=lambda a:(a//3,a%3)
def expo(a,b):
 x,y=d(a);u,v=d(b)
 return (x*u+y*v)%3
omega=[(1,0),(0,1),(-1,-1)]
M=[[omega[expo(a,b)] for b in P] for a in P]
perms=[]
for v in permutations(range(4)):
 inv=sum(v[i]>v[j] for i in range(4) for j in range(i+1,4))
 perms.append((v,-1 if inv%2 else 1))
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def det(A,B):
 Z=(0,0)
 for perm,sign in perms:
  v=(sign,0)
  for i,k in enumerate(perm):v=mul(v,M[A[i]][B[k]])
  Z=(Z[0]+v[0],Z[1]+v[1])
 return Z
def cap(A):
 for a,b,c in combinations(A,3):
  x,y=d(a);u,v=d(b);w,z=d(c)
  if ((u-x)*(z-y)-(w-x)*(v-y))%3==0:return 0
 return 1
classes={A:cap(A) for A in C}
counts=Counter()
for A in C:
 for B in C:
  counts[(classes[A],classes[B],det(A,B)==(0,0))]+=1
print(counts)
# Full 126-by-126 rank incidence and its two affine-set strata.
expected={(0,0,True):1296,(0,0,False):3888,
          (0,1,True):1944,(0,1,False):1944,
          (1,0,True):1944,(1,0,False):1944,
          (1,1,True):486,(1,1,False):2430}
assert dict(counts)==expected
assert Counter(classes.values())=={0:72,1:54}
for A in C:
    assert sum(det(A,B)==(0,0) for B in C)==45
for A,targets in [((0,1,3,6),{0:18,1:27}),((0,1,3,4),{0:36,1:9})]:
    assert {j:sum(det(A,B)==(0,0) for B in C if classes[B]==j) for j in (0,1)}==targets
print('CHECK_PASS 126x126 exact Eisenstein determinants, 45 per support, quotient=18,27;36,9')
