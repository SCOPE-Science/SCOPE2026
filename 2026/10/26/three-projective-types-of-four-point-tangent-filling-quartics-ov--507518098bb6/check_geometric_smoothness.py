from pathlib import Path
BASE = Path(__file__).resolve().parent
import sympy as s,time
x,y,z=s.symbols('x y z')
V=(x,y,z)
MON=[(i,j,4-i-j) for i in range(5) for j in range(5-i)]
vecs=[tuple(map(int,line.strip().split(','))) for line in open(str(BASE/'candidate_vectors.csv')) if line.strip()]
fs=[];tt=time.time()
for idx,v in enumerate(vecs):
 F=s.Poly(sum(int(c)*x**i*y**j*z**k for c,(i,j,k) in zip(v,MON)),x,y,z,modulus=3)
 D=[F.diff(t).as_expr() for t in V]
 ok=True
 for k in range(3):
  W=[j for j in range(3) if j!=k];polys=[s.Poly(p.subs(V[k],1),V[W[0]],V[W[1]],modulus=3) for p in D]
  gb=s.groebner(polys,V[W[0]],V[W[1]],modulus=3)
  if not gb.is_zero_dimensional and tuple(gb.polys)!= (s.Poly(1,V[W[0]],V[W[1]],modulus=3),):
   ok=False;break
  if len(gb.polys)!=1 or gb.polys[0].as_expr()!=1:
   ok=False;break
 if ok:fs.append(v)
 if idx%50==0:print('tested',idx+1,'elapsed',round(time.time()-tt,2),'smooth',len(fs),flush=True)
print('DONE',len(fs),'elapsed',time.time()-tt,'examples',fs[:5]);open(str(BASE/'smooth_vectors.csv'),'w').write('\n'.join(','.join(map(str,v)) for v in fs)+'\n')
