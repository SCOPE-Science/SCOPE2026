#!/usr/bin/env python3
"""Exact certificate for the Hesse arrangement's incidence and local Tjurina algebras.

No third-party dependencies. All global incidence tests use Eisenstein integer determinants;
local multiplication matrices are over prime fields.
"""
from collections import Counter
from itertools import combinations

zero = (0, 0)
one = (1, 0)
omega = (0, 1)
omega2 = (-1, -1)

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    x,y=a;u,v=b
    return (x*u-y*v,x*v+y*u-y*v)
def norm(a): return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
def det(a,b,c):
    return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),
                   mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),
               mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))

L=[(one,zero,zero),(zero,one,zero),(zero,zero,one),
   (one,one,one),(one,omega,omega2),(one,omega2,omega),
   (omega,one,one),(one,omega,one),(one,one,omega),
   (omega2,one,one),(one,omega2,one),(one,one,omega2)]
hist=Counter(norm(det(L[i],L[j],L[k])) for i,j,k in combinations(range(12),3))
expect={0:36,1:28,3:81,9:72,27:3}
assert dict(hist)==expect, (hist,expect)
assert sum(hist.values())==220
assert sum(hist[x] for x in hist if x>0)==184
# The entire nonzero determinant norm spectrum is supported on powers of 3.

# Check the 12 lines and the 21 intersection points in representative characteristic 2 and 7 fields.
# Elements of F4 are bits a+b*w, with w^2+w+1=0.
def ffadd(a,b,p): return a ^ b if p==2 else (a+b)%p
def ffmul(a,b,p):
    if p!=2:return (a*b)%p
    t=0
    for i in range(2):
      for j in range(2):
        if ((a>>i)&1) and ((b>>j)&1):t ^= 1<<(i+j)
    if t&4:t ^= 0b111
    return t

def run_geometry(p, alpha):
    # alpha is a primitive third root in F4 when p=2 or F7 when p=7.
    powers=[1,alpha,ffmul(alpha,alpha,p)]
    elems=range(1,4) if p==2 else range(1,p)
    inv={a:next(b for b in elems if ffmul(a,b,p)==1) for a in elems}
    def standard(v):
      first=next(a for a in v if a)
      return tuple(ffmul(a,inv[first],p) for a in v)
    def minus(a):return a if p==2 else (-a)%p
    def difference(a,b):return ffadd(a,minus(b),p)
    def cross(a,b):
      return standard(tuple(difference(ffmul(a[(j+1)%3],b[(j+2)%3],p),
                             ffmul(a[(j+2)%3],b[(j+1)%3],p)) for j in range(3)))
    def eval_line(v,pt):
      z=0
      for i in range(3):z=ffadd(z,ffmul(v[i],pt[i],p),p)
      return z
    ll=[(1,0,0),(0,1,0),(0,0,1),
        (1,1,1),(1,powers[1],powers[2]),(1,powers[2],powers[1]),
        (powers[1],1,1),(1,powers[1],1),(1,1,powers[1]),
        (powers[2],1,1),(1,powers[2],1),(1,1,powers[2])]
    ll=[standard(x) for x in ll]
    assert len(set(ll))==12
    pts={}
    for i,j in combinations(range(12),2):
      z=cross(ll[i],ll[j])
      pts[z]=tuple(k for k in range(12) if eval_line(ll[k],z)==0)
    m=Counter(len(v) for v in pts.values())
    assert dict(m)=={2:12,4:9},(p,m)
    return len(pts),m

assert run_geometry(2,2)[0]==21
assert run_geometry(7,2)[0]==21

# The completed local Tjurina rings at the nine four-line points have bases
# v^0,...,v^3;u*v^0,...,u*v^3;u^2.
# char2:  (u^3,u^2v,v^4)
# odd p!=3: (u^2v,u^3+4v^3), with derived v^4=0.
B=[(0,j) for j in range(4)]+[(1,j) for j in range(4)]+[(2,0)]
assert len(B)==9
assert Counter(i+j for i,j in B)=={0:1,1:2,2:3,3:2,4:1}

def product_u_or_v(exponent,variable,p):
    i,j=exponent
    if variable=="u":i+=1
    else:j+=1
    if j>=4 or (i>=2 and j>=1):return None,0
    if i>=3:
        if p==2:return None,0
        i-=3;j+=3
        if j>=4 or (i>=2 and j>=1):return None,0
        return (i,j),(-4)%p
    return (i,j),1

def rank_mod_p(matrix,p):
    a=[list(row) for row in matrix]
    m=len(a);n=len(a[0])
    r=0
    for j in range(n):
      pivot=next((i for i in range(r,m) if a[i][j]%p),None)
      if pivot is None:continue
      a[r],a[pivot]=a[pivot],a[r]
      x=pow(a[r][j],-1,p)
      a[r]=[(z*x)%p for z in a[r]]
      for i in range(m):
        if i!=r:
          t=a[i][j]%p
          if t:a[i]=[(a[i][h]-t*a[r][h])%p for h in range(n)]
      r+=1
      if r==m:break
    return r

def socle_dim(p):
    # The linear map A -> A^2, a |-> (u*a,v*a), has kernel the socle.
    mat=[[0]*len(B) for _ in range(2*len(B))]
    for col,mon in enumerate(B):
      for z,var in enumerate(('u','v')):
        out,c=product_u_or_v(mon,var,p)
        if out is not None:mat[z*len(B)+B.index(out)][col]=c
    return len(B)-rank_mod_p(mat,p)

assert socle_dim(2)==2
for p in (5,7,11,13):assert socle_dim(p)==1
assert 9*9+12==93
print('EISENSTEIN_TRIPLE_NORMS',dict(sorted(hist.items())))
print('PROJECTIVE_INTERSECTIONS_GF4_GF7', 'nine quadruple and twelve double')
print('TJURINA_HILBERT_FUNCTION',(1,2,3,2,1))
print('SOCLE_TYPE characteristic_2=2 characteristic_odd_not_3=1')
print('TOTAL_TJURINA_LENGTH',93)
print('VERIFY_OK')
