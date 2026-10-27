"""Independent 15-dimensional generating set using the rational-point ideal."""
import importlib.util,json
from collections import Counter
# Coordinates x0,x1; y0,y1. The ideal of 9 rational points is (x0^2*x1+x0*x1^2, y0^2*y1+y0*y1^2).
A,B=3,5;terms=[(i,j) for i in range(4) for j in range(6)]
def bit(i,j):return 1<<terms.index((i,j))
vec=[]
# sx times degree-(0,5) binary quintics
for j in range(6):vec.append(bit(1,j)^bit(2,j))
# sy times degree-(3,2) polynomials; omit x1-exponent i=2, because of the syzygy
for i in (0,1,3):
 for j in range(3):vec.append(bit(i,j+1)^bit(i,j+2))
assert len(vec)==15 and len(set(vec))==15
allforms={0}
for b in vec:allforms|={w^b for w in tuple(allforms)}
assert len(allforms)==32768
points=((1,0),(1,1),(0,1))
def eval_(mask,x,y,delta):
 val=0
 for k,(i,j) in enumerate(terms):
  if not mask>>k&1:continue
  if delta==0:c=x[0]**(3-i)*x[1]**i*y[0]**(5-j)*y[1]**j
  elif delta==1:
   if x==(0,1):c=((3-i)&1)*x[0]**(2-i)*x[1]**i*y[0]**(5-j)*y[1]**j if i<3 else 0
   else:c=(i&1)*x[0]**(3-i)*x[1]**(i-1)*y[0]**(5-j)*y[1]**j if i else 0
  elif delta==2:
   if y==(0,1):c=((5-j)&1)*x[0]**(3-i)*x[1]**i*y[0]**(4-j)*y[1]**j if j<5 else 0
   else:c=(j&1)*x[0]**(3-i)*x[1]**i*y[0]**(5-j)*y[1]**(j-1) if j else 0
  val^=c&1
 return val
smooth=[]
for v in allforms:
 if all(eval_(v,x,y,0)==0 for x in points for y in points):
  if all(eval_(v,x,y,1) or eval_(v,x,y,2) for x in points for y in points):smooth.append(v)
 else:raise AssertionError('not a filling equation')
assert len(smooth)==5832
D=json.load(open('orbits.json'))
# orbit sizes and representatives must agree with primary independent kernel-method
print('Independent filling form basis dimension',len(vec),'exact forms',len(allforms),'rationally-smooth',len(smooth))
print('Minimum/maximum 24-bit masks',min(smooth),max(smooth))
json.dump({'basis_masks':vec,'total':len(allforms),'rationally_smooth_count':len(smooth)},open('independent_basis_counts.json','w'))
