import csv,time
import sympy as sp
from pathlib import Path
x,y,z=sp.symbols('x y z')
M=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
rows=list(csv.DictReader(open(Path(__file__).parent/'orbits.csv')))

def test(code):
 coef=[]
 for _ in range(15):coef.append(code%3);code//=3
 f=sp.Poly(sum(coef[i]*x**a*y**b*z**c for i,(a,b,c) in enumerate(M)),x,y,z,modulus=3)
 fs=[f.diff(t).as_expr() for t in (x,y,z)]
 for p,q in ((x,(y,z)),(y,(x,z)),(z,(x,y))):
  gb=sp.groebner([g.subs(p,1) for g in fs],*q,modulus=3,order='grevlex')
  if not any(g.is_ground for g in gb.polys):return False
 return True
if __name__=='__main__':
 t=time.time()
 for i,row in enumerate(rows):
  g=test(int(row['code']));assert g==(row['smooth']=='1'), (row,g)
 print(len(rows),'orbit representatives: affine-chart Groebner smoothness tests all match; seconds',round(time.time()-t,2))
