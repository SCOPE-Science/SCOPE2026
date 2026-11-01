"""Exact spherical fan for the central-section type of a regular truncated cube."""
import itertools, math
import sympy as s
T=s.sqrt(2)-1
# clipping normalized normals (a,b,c)=(1,y,z), a>=b>=c>=0
# Each inequality L_i>=0 has a fixed sign in the cell.
LINE=[(-1,1,T),(1,-T,-1),(-T,1,1),(-T,1,-1)]
TRI=[(s.S(0),s.S(0)),(s.S(1),s.S(0)),(s.S(1),s.S(1))]
def eval_line(pt,L):
 A,B,C=L; return s.simplify(A+B*pt[0]+C*pt[1])
def clip(poly,L,positive=True):
 if not positive: L=tuple(-q for q in L)
 out=[]
 if not poly: return out
 for old,new in zip(poly,poly[1:]+poly[:1]):
  f=eval_line(old,L);g=eval_line(new,L)
  inside_f=float(f)>=-1e-10;inside_g=float(g)>=-1e-10
  if inside_f!=inside_g:
   v=s.simplify(f/(f-g)); out.append(tuple(s.simplify(old[k]+v*(new[k]-old[k])) for k in range(2)))
  if inside_g:out.append(new)
 clean=[]
 for p in out:
  if not clean or any(s.simplify(p[k]-clean[-1][k])!=0 for k in range(2)): clean.append(p)
 if len(clean)>1 and all(s.simplify(clean[0][k]-clean[-1][k])==0 for k in range(2)): clean.pop()
 return clean
def vector(pt): return s.Matrix([s.Integer(1),pt[0],pt[1]])
def omega_triangle(P,Q,R):
 p,q,r=map(vector,[P,Q,R]); norms=[s.sqrt(v.dot(v)) for v in [p,q,r]]
 det=abs(s.det(s.Matrix.hstack(p,q,r)))
 denom=s.prod(norms)+p.dot(q)*norms[2]+q.dot(r)*norms[0]+r.dot(p)*norms[1]
 return 2*s.atan(s.simplify(det/denom))
def omega(poly):
 return sum((omega_triangle(poly[0],poly[i],poly[i+1]) for i in range(1,len(poly)-1)),s.S(0))
if __name__=='__main__':
 total={4:s.S(0),6:s.S(0),8:s.S(0),10:s.S(0)}
 for mask in itertools.product([0,1],repeat=4):
  poly=TRI
  for bit,L in zip(mask,LINE):poly=clip(poly,L,bool(bit))
  if len(poly)<3: continue
  ar=s.simplify(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly)))/2)
  if float(ar)<1e-10: continue
  k=4+2*(mask[0]+int(mask[1] and mask[2])+mask[3]); O=omega(poly); total[k]+=O
  print('mask',mask,'N',k,'poly',str(poly),'omega',s.N(O,13))
 print('results')
 for k,v in total.items():print(k,s.N(12*v/s.pi,14),'solid angle',s.N(v,14))
 print('sum',s.N(sum(total.values())), 'pi/12',s.N(s.pi/12))
