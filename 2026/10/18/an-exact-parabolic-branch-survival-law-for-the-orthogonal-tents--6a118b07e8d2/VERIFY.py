from fractions import Fraction as F
from itertools import product
A=(0,0);B=(1,1);C=(0,1);D=(1,0)
labels={'A':A,'B':B,'C':C,'D':D}

def lin_add(L1,L2):return tuple(a+b for a,b in zip(L1,L2))
def lin_sub(L1,L2):return tuple(a-b for a,b in zip(L1,L2))
def lin_mul(k,L):return tuple(k*a for a in L)
# affine linear form as (x coeff,y coeff,constant)
def eval_lin(L,p):return L[0]*p[0]+L[1]*p[1]+L[2]
def clip(poly,L,low=True):
 def v(p):return eval_lin(L,p)
 out=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  vp,vq=v(p),v(q); a=(vp>=0 if low else vp<=0); b=(vq>=0 if low else vq<=0)
  if a:out.append(p)
  if a!=b:
   t=vp/(vp-vq)
   out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
 # remove adjacent duplicates, and degeneracies
 r=[]
 for p in out:
  if not r or p!=r[-1]:r.append(p)
 if r and r[0]==r[-1]:r.pop()
 return r

def polygon(path):
 poly=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
 x,y=(F(1),F(0),F(0)),(F(0),F(1),F(0))
 for f,g in path:
  t=lin_add(x,lin_mul(2,y))
  pre=lin_sub(lin_add(y,(F(0),F(0),F(2+2*f))),lin_mul(2,t))
  # y in [0,.5]; t in [f+.5,f+1]; pre in [g,g+1]
  constraints=[(y,F(0),True),(y,F(1,2),False),(t,F(f)+F(1,2),True),(t,F(f+1),False),(pre,F(g),True),(pre,F(g+1),False)]
  for form,bound,lower in constraints:
   poly=clip(poly,lin_sub(form,(F(0),F(0),bound)),lower)
   if not poly:return []
  x,y=lin_sub(t,(F(0),F(0),F(f))),lin_sub(pre,(F(0),F(0),F(g)))
 return poly

def area(poly):
 if not poly:return F(0)
 return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2


if __name__ == '__main__':
    for m in range(1,61):
        paths=[([A,B]*m,F(1,16*(4*m-1))),([B,A]*m,F(1,16*(4*m-1))),([C,A]+[B,A]*(m-1),F(1,16*(4*m-1)*(4*m-3))),([A,B]*(m-1)+[A,D],F(1,16*(4*m-1)*(4*m-3)))]
        for path,expected in paths:
            assert area(polygon(path))==expected,(m,path)
    print('PASS: 240 exact rational polygon-area checks.')
