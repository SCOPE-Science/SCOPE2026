import sympy as S
x,y,z=S.symbols('X Y Z');vs=[x,y,z]
mon=[x**3,y**3,z**3,x*x*y,x*x*z,x*y*y,y*y*z,x*z*z,y*z*z,x*y*z]
reps=[[0,1,4,1,1,0,0,0,0,0],[1,0,4,2,1,1,0,0,0,0]]
pts=[]
for a in range(5):
 for b in range(5):
  for c in range(5):
   if next((v for v in (a,b,c) if v),0)==1:pts.append((a,b,c))
assert len(pts)==31
norm=lambda v: tuple((int(k)*pow(next((int(a) for a in v if a),1),-1,5))%5 for k in v)
P=set(pts)
for coeff in reps:
 F=S.expand(sum(c*m for c,m in zip(coeff,mon)))
 grad=[S.diff(F,t) for t in vs]
 print('F=',F)
 for var in vs:
  rest=[w for w in vs if w!=var]
  g=S.groebner([p.subs({var:1}) for p in grad],*rest,modulus=5)
  print(' chart',var,' GB',g.polys)
 rational=[]; tangents=set();missing=[]
 for p in pts:
  if int(F.subs(dict(zip(vs,p))))%5:continue
  d=tuple(int(f.subs(dict(zip(vs,p))))%5 for f in grad)
  rational.append((p,d)); assert any(d)
  tangents.add(norm(d))
 for p in pts:
  if not any(sum(p[i]*line[i] for i in range(3))%5==0 for line in tangents):missing.append(p)
 print('point count',len(rational),'tangent lines',len(tangents),'covered',31-len(missing),'uncovered',missing)
 print('points',rational)
 print('tangent normals',sorted(tangents))
