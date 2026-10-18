#!/usr/bin/env python3
"""Exact rational certificate for the cubic cardinal spline Zak nonvanishing lemma.
Scientific-only dependency: Python 3 standard library. No sampling is used.

T=2/lambda-2 in [0,2], X=x in [0,1/2]. For j=1..4, define
D_j=6 lambda^(-3) [B4(lambda(j-X))-B4(lambda(j+X))].
The four degree-three Bernstein coefficients of the sine quotient are
D1-2D2+3D3-4D4, D1-2D2/3-7D3/3+28D4/3,
D1+2D2/3-7D3/3-28D4/3, D1+2D2+3D3+4D4.
They are nonnegative throughout the rectangle, certified by rational
Bernstein coefficients on its 10-triangle affine-linear subdivision.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

ZERO={}
ONE={(0,0):Q(1)}
def const(c):
 c=Q(c)
 return {(0,0):c} if c else {}
TT={(1,0):Q(1)}
XX={(0,1):Q(1)}
def add(*poly):
 out={}
 for p in poly:
  for k,v in p.items(): out[k]=out.get(k,Q(0))+v
 return {k:v for k,v in out.items() if v}
def neg(p):return {k:-v for k,v in p.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 out={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),Q(0))+v*w
 return {k:v for k,v in out.items() if v}
def scale(a,c):return mul(a,const(c))
def power(a,n):
 out=ONE
 for _ in range(n):out=mul(out,a)
 return out
def lin(c,a,b):return add(const(c),scale(TT,a),scale(XX,b))
def eval_poly(poly,t,x):return sum(v*t**i*x**j for (i,j),v in poly.items())

# Each affine line is c + a*T+b*X=0.
lines=[(0,1,-1),(-1,1,1),(-1,1,-1),(-2,1,1),(-1,Q(1,2),1),(0,Q(1,2),-1)]
base=[(Q(0),Q(0)),(Q(2),Q(0)),(Q(2),Q(1,2)),(Q(0),Q(1,2))]
def cut(poly,form,positive):
 c,a,b=form
 def value(p):return (c+a*p[0]+b*p[1])*(1 if positive else -1)
 out=[]
 for p,q in zip(poly,poly[1:]+poly[:1]):
  v,w=value(p),value(q)
  if v>=0:out.append(p)
  if v*w<0:
   h=v/(v-w)
   out.append((p[0]+h*(q[0]-p[0]),p[1]+h*(q[1]-p[1])))
 ans=[]
 for p in out:
  if p not in ans:ans.append(p)
 return ans

def area(poly):return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2

def active_poly(bits):
 # These are the normalized differences D_j, obtained from
 # B4(t)=[(2-|t|)_+^3 - 4(1-|t|)_+^3]/6.
 d1=sub(sub(power(lin(1,1,1),3),power(lin(1,1,-1),3)),
        scale(sub(power(lin(0,Q(1,2),1),3), power(lin(0,Q(1,2),-1),3) if bits[5] else ZERO),4))
 d2=sub(sub(power(lin(0,1,1),3),power(lin(0,1,-1),3) if bits[0] else ZERO),
        scale(power(lin(-1,Q(1,2),1),3) if bits[4] else ZERO,4))
 d3=sub(power(lin(-1,1,1),3) if bits[1] else ZERO,
        power(lin(-1,1,-1),3) if bits[2] else ZERO)
 d4=power(lin(-2,1,1),3) if bits[3] else ZERO
 return [add(d1,scale(d2,-2),scale(d3,3),scale(d4,-4)),
         add(d1,scale(d2,Q(-2,3)),scale(d3,Q(-7,3)),scale(d4,Q(28,3))),
         add(d1,scale(d2,Q(2,3)),scale(d3,Q(-7,3)),scale(d4,Q(-28,3))),
         add(d1,scale(d2,2),scale(d3,3),scale(d4,4))]

def compose(poly,tri):
 a,b,c=tri
 t=lin(a[0],b[0]-a[0],c[0]-a[0]);x=lin(a[1],b[1]-a[1],c[1]-a[1])
 out=ZERO
 for (i,j),v in poly.items():out=add(out,scale(mul(power(t,i),power(x,j)),v))
 return out

def fall(n,k):
 z=1
 for j in range(k):z*=n-j
 return z

def bernstein_coeffs_on_triangle(poly,tri):
 p=compose(poly,tri)
 for i in range(4):
  for j in range(4-i):
   b=sum(v*Q(fall(i,a)*fall(j,c),fall(3,a+c))
         for (a,c),v in p.items() if a<=i and c<=j)
   yield (i,j,b)

def main():
 cells=0;triangles=0;tests=0;whole_area=Q(0);zeros=0
 for bits in product((False,True),repeat=6):
  poly=base
  for line,pos in zip(lines,bits):poly=cut(poly,line,pos)
  if len(poly)<3 or not area(poly):continue
  cells+=1;whole_area+=area(poly)
  polys=active_poly(bits)
  for j in range(1,len(poly)-1):
   tri=[poly[0],poly[j],poly[j+1]]
   triangles+=1
   assert area(tri)>0
   for k,f in enumerate(polys):
    for i,h,b in bernstein_coeffs_on_triangle(f,tri):
     assert b>=0,(bits,tri,k,i,h,b)
     zeros+=(b==0);tests+=1
 assert whole_area==1,(whole_area,cells)
 assert (cells,triangles,tests)==(9,10,400),(cells,triangles,tests)
 print('VERIFY_OK exact rational Bernstein certificate: 9 cells, 10 triangles, 400 nonnegative controls; total area 1; zero controls',zeros)

if __name__=='__main__':main()
