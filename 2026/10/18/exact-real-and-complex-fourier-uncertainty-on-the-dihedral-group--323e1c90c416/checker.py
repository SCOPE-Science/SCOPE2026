#!/usr/bin/env python3
"""Exact Gaussian-integer checks for the D8 uncertainty-profile theorem.

No external dependencies. Index order r^0,r^1,r^2,r^3,s,sr,sr^2,sr^3.
All coefficient pairs (a,b) mean a+b*i with integral a,b.
"""
from itertools import combinations

Z=(0,0)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sq(x):return mul(x,x)
def g(x):return (x,0) if isinstance(x,int) else x

def spectrum(f):
    f=[g(x) for x in f]
    assert len(f)==8
    a,b=f[:4],f[4:]
    A=sum((a[j][0] for j in range(4)))
    # Explicit four one-dimensional transforms, with no normalization.
    chars=[]
    for u in (1,-1):
        for v in (1,-1):
            z=Z
            for j in range(4):
                z=add(z,(u**j*a[j][0],u**j*a[j][1]))
                z=add(z,(v*u**j*b[j][0],v*u**j*b[j][1]))
            chars.append(z)
    x=sub(a[0],a[2]);y=sub(a[1],a[3]);z=sub(b[0],b[2]);w=sub(b[1],b[3])
    det=sub(add(sq(x),sq(y)),add(sq(z),sq(w)))
    rank2=0 if (x==y==z==w==Z) else (1 if det==Z else 2)
    return sum(v!=Z for v in chars)+2*rank2,chars,det,rank2

def support(f):return sum(g(x)!=Z for x in f)

W={
 ('C',1):[1,0,0,0,0,0,0,0],
 ('C',2):[1,0,1,0,0,0,0,0],
 ('C',3):[(1,1),2,(1,-1),0,0,0,0,0],
 ('C',4):[1,1,1,1,0,0,0,0],
 ('C',5):[-1,1,-1,-1,2,0,0,0],
 ('C',6):[3,4,-3,-4,5,0,-5,0],
 ('C',7):[-2,-3,8,-3,-7,6,1,0],
 ('C',8):[1,1,1,1,1,1,1,1],
}
for k in range(1,9):
 if k!=3:W['R',k]=W['C',k]
W['R',3]=[1,2,1,0,0,0,0,0]
TARGETS={'C':(8,4,4,2,4,2,3,1),'R':(8,4,6,2,4,2,3,1)}
for field in ('C','R'):
 for k,target in enumerate(TARGETS[field],1):
  f=W[field,k]
  assert support(f)==k,(field,k,'support')
  assert spectrum(f)[0]==target,(field,k,'Fourier rank')
  if field=='R':assert all(g(v)[1]==0 for v in f)
print('All 16 exact Gaussian-integer upper witnesses passed.')

# Independently verify that the three triple-support normal forms are exhaustive.
# automorphism r -> r^{eps}, s -> r^k s, and left translation by s^t r^a.
def auto(i,eps,k):return ((eps*i)%4 if i<4 else 4+(eps*(i-4)-k)%4)
def left(i,a,t):
 if not t: return ((i+a)%4 if i<4 else 4+(i-4-a)%4)
 return (4+(a+i)%4 if i<4 else (i-4-a)%4)
permutations={tuple(left(auto(i,eps,k),a,t) for i in range(8))
 for eps in (-1,1) for k in range(4) for t in (0,1) for a in range(4)}
orbit_reps=((0,1,2),(0,1,4),(0,2,4))
orbits=[]
for rep in orbit_reps:
 orbit={tuple(sorted(p[i] for i in rep)) for p in permutations}
 orbits.append(orbit)
assert all(not (orbits[i]&orbits[j]) for i in range(3) for j in range(i+1,3))
assert set().union(*orbits)==set(combinations(range(8),3))
assert [len(o) for o in orbits]==[8,32,16]
print('Three triple-support orbits exhaust all 56 subsets: sizes 8,32,16.')

# Algebraic singleton-pair obstruction in the one-scalar + rank-one case:
# if three of x^2,y^2,z^2,w^2 equal c^2 and Q=0,
# the fourth must equal c^2. This is an integer identity.
for missing in range(4):
 diag=[1,1,-1,-1]
 required=-sum(diag[i] for i in range(4) if i!=missing)/diag[missing]
 assert required==1
print('All four symbolic singleton-pair implications passed.')
print('The lower bounds are the analytic arguments in RESULT.md; this checker does not enumerate all complex amplitudes.')
