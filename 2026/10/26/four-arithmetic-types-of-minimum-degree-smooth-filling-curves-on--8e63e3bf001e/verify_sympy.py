"""Independent exact scan for smooth (3,4) binary filling curves."""
from itertools import product
from sympy import symbols,Poly,groebner
from pathlib import Path
A=3;B=4
monomials=list(product(range(A+1),range(B+1)))
pts=[(1,0),(1,1),(0,1)]

def evterm(i,j,p,q):
    return (p[0]**(A-i))*(p[1]**i)*(q[0]**(B-j))*(q[1]**j)
checks=[sum(evterm(i,j,p,q)<<t for t,(i,j) in enumerate(monomials)) for p in pts for q in pts]
# canonical RREF via eliminating highest pivots
rows=checks[:]; pivots={}
for col in range(len(monomials)):
    ix=next((t for t in range(len(rows)) if rows[t]>>col&1),None)
    if ix is None:continue
    pivot=rows.pop(ix)
    for t in range(len(rows)):
        if rows[t]>>col&1:rows[t]^=pivot
    for p in pivots:
        if pivots[p]>>col&1:pivots[p]^=pivot
    pivots[col]=pivot
free=[j for j in range(len(monomials)) if j not in pivots]
assert len(free)==11
base=[]
for j in free:
 v=1<<j
 for col,p in pivots.items():
  if p>>j&1:v|=1<<col
 assert all((v&c).bit_count()%2==0 for c in checks)
 base.append(v)
assert len(set(base))==11
x,y=symbols('x y')
monpoly=[]
for c1,c2 in product(range(2),repeat=2):
 monpoly.append([x**(i if c1==0 else A-i)*y**(j if c2==0 else B-j) for i,j in monomials])

def chartpoly(mask,ch):
 p=0
 for k,term in enumerate(monpoly[ch]):
  if mask>>k&1:p+=term
 return Poly(p,x,y,modulus=2).as_expr()
def smooth(mask):
 for c1,c2 in product(range(2),repeat=2):
  ch=2*c1+c2
  f=chartpoly(mask,ch)
  # sympy g.basis unit ideal iff contains a constant 1
  g=groebner([f,f.diff(x),f.diff(y)],x,y,order='lex',modulus=2)
  if len(g.polys)!=1 or g.polys[0].total_degree()!=0:return False
 return True
results=[]
for bits in range(1,1<<len(base)):
 v=0
 for k,b in enumerate(base):
  if bits>>k&1:v^=b
 # only rational smooth candidates
 good=True
 for p in pts:
  c1=1 if p[0]==0 else 0;xx=0 if p!=(1,1) else 1
  for q in pts:
   c2=1 if q[0]==0 else 0;yy=0 if q!=(1,1) else 1
   f=chartpoly(v,2*c1+c2)
   if int(f.diff(x).subs({x:xx,y:yy}))%2==0 and int(f.diff(y).subs({x:xx,y:yy}))%2==0:
    good=False;break
  if not good:break
 if good and smooth(v):results.append(v)
print('independent sympy count',len(results),'match',set(results)==set(map(int,Path(str(Path(__file__).with_name('smooth_masks.txt'))).read_text().split())))
if set(results)!=set(map(int,Path(str(Path(__file__).with_name('smooth_masks.txt'))).read_text().split())):
 print('diff',set(results)^set(map(int,Path(str(Path(__file__).with_name('smooth_masks.txt'))).read_text().split())))
Path(str(Path(__file__).with_name('independent_output.txt'))).write_text('sympy smooth count '+str(len(results))+'\n')
