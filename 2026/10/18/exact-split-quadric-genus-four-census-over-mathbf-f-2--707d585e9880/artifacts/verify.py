from pathlib import Path
ROOT=Path(__file__).resolve().parent
"""Separate exact smoothness check on projective orbit representatives."""
import sympy as sp,time
x,y=sp.symbols('x y')

def check(mask):
 for xinfty in (False,True):
  for yinfty in (False,True):
   f=sum((x**(3-i if xinfty else i))*(y**(3-j if yinfty else j)) for i in range(4) for j in range(4) if mask>>(4*i+j)&1)
   P=sp.Poly(f,x,y,modulus=2)
   GB=sp.groebner([P.as_expr(),P.diff(x).as_expr(),P.diff(y).as_expr()],x,y,modulus=2)
   if not (len(GB.polys)==1 and GB.polys[0].as_expr()==1):
    return False,(xinfty,yinfty,str(GB))
 return True,None

rows=[tuple(map(int,line.split())) for line in open(ROOT / "orbit_representatives.tsv")]
st=time.time()
for idx,(mask,r,orb,stab) in enumerate(rows,1):
 ok,err=check(mask)
 if not ok:raise AssertionError((idx,mask,err))
print('PASS',len(rows),'projective orbit representatives smooth on 4 exact polynomial Groebner charts; time %.3f s'%(time.time()-st))
