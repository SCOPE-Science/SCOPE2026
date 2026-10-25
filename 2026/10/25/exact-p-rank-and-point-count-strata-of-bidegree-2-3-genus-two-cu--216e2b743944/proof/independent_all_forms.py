"""Independent direct scan of all 4095 nonzero bidegree(2,3) binary equations."""
import sympy as S
from collections import Counter
x,y=S.symbols('x y')
POLYS=[]
for iu in range(2):
 for iv in range(2):
  POLYS.append([x**(i if iu==0 else 2-i)*y**(j if iv==0 else 3-j) for i in range(3) for j in range(4)])

def smooth(mask):
 for terms in POLYS:
  f=sum(terms[i] for i in range(12) if (mask>>i)&1)
  g=S.groebner([f,S.diff(f,x),S.diff(f,y)],x,y,modulus=2)
  if 1 not in g.polys and not any(z.as_expr()==1 for z in g.polys):return False
 return True

# roots of binary cubic coefficient mask at index 4..7
roots_count={}
t=S.symbols('t')
for b in range(1,16):
 poly=sum(((b>>j)&1)*t**j for j in range(4))
 factors=S.factor_list(poly,modulus=2)[1]
 roots_count[b]=sum(S.degree(f,t) for f,e in factors)+ (1-((b>>3)&1))

def n1(mask):
 n=0
 pts=((1,0),(0,1),(1,1))
 for a,b in pts:
  for c,d in pts:
   v=0
   for i in range(3):
    for j in range(4):
     if (mask>>(4*i+j))&1:v^=a**(2-i)*b**i*c**(3-j)*d**j
   n+=(v==0)
 return n

C=Counter();smooth_total=0
for mask in range(1,4096):
 if smooth(mask):
  smooth_total+=1
  B=(mask>>4)&15
  assert B!=0
  C[(n1(mask), roots_count[B]-1)]+=1
print('INDEPENDENT',smooth_total,sorted(C.items()))
