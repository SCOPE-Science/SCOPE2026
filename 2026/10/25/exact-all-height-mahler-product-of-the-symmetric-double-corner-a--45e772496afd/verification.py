import sympy as sp, numpy as np,itertools,math,sys,time
from scipy.spatial import ConvexHull
x=sp.symbols('t', positive=True)
sgn = np.array(list(itertools.product([-1,1],repeat=4)),dtype=float)
C = sp.Matrix([[int(a) for a in row] for row in sgn.tolist()]);
v=sp.Matrix([1,1,1+x,1]);w=sp.Matrix([1,1,1,1+x]);
vertsP = [C.row(i).T for i in range(16)] + [v,-v,w,-w]
ineq = vertsP.copy()

def sort_unique_numeric(t):
 a=np.asarray([np.asarray(z.subs(x,t), dtype=float).flatten() for z in ineq]);
 seen={}
 for ids in itertools.combinations(range(20),4):
  mat=a[list(ids)];
  try: zz=np.linalg.solve(mat,np.ones(4))
  except np.linalg.LinAlgError: continue
  if np.max(a@zz-1)>1e-7:continue
  key=tuple(np.round(zz,8))
  if key not in seen:seen[key]=ids
 keys=list(seen)
 return np.array(keys,dtype=float),list(seen.values())

for val in [sp.Rational(1,1),sp.Rational(3,1)]:
 t0=time.time()
 vertsP_num=np.asarray([np.asarray(z.subs(x,val),dtype=float).flatten() for z in vertsP])
 hP=ConvexHull(vertsP_num,qhull_options='Qx')
 vp=sp.Rational(0)
 for simplex in hP.simplices:
  mat=sp.Matrix.hstack(*[vertsP[int(i)] for i in simplex])
  expr=mat.det(method='domain-ge')
  sg=sp.sign(expr.subs(x,val));vp+=sg*expr/sp.factorial(4)
 vp=sp.factor(vp)
 print('primal',val,vp,'faces',len(hP.simplices),'seconds',time.time()-t0,flush=True)

 coords,active=sort_unique_numeric(val)
 vps=[]
 for ids in active:
  a=sp.Matrix.hstack(*[ineq[k] for k in ids]).T
  vps.append(a.inv()*sp.ones(4,1))
 hD=ConvexHull(coords,qhull_options='Qx')
 from sympy import Poly
 u=sp.symbols('u',nonnegative=True)
 def positive(expr):
  expr=sp.cancel(expr)
  shifted=sp.cancel(expr.subs(x,2*u/(1+u)) if val==1 else expr.subs(x,2+u))
  num,den=sp.fraction(shifted)
  a=sp.Poly(num,u);b=sp.Poly(den,u)
  ca=a.all_coeffs(); cb=b.all_coeffs()
  return all(c>=0 for c in ca) and all(c>0 for c in cb)
 violations=[]
 for k,vv in enumerate(vps):
  for j,rr in enumerate(ineq):
   expr=sp.factor(1-(rr.T*vv)[0]);
   if not positive(expr): violations.append(('ineq',k,j,str(expr)))
 assert not violations, ('candidate feasibility',violations)
 missing=[]
 for simplex in hD.simplices:
  jj=[int(i) for i in simplex]
  supporting=[k for k,rr in enumerate(ineq) if all(sp.factor((rr.T*vps[i])[0]-1)==0 for i in jj)]
  if not supporting:missing.append(jj)
 assert not missing, ('polar facet coverage',missing)
 vd=sp.Rational(0)
 for simplex in hD.simplices:
  mat=sp.Matrix.hstack(*[vps[int(i)] for i in simplex]);
  det=sp.factor(mat.det(method='domain-ge'))
  sg=sp.sign(det.subs(x,val))
  if not positive(sg*det): violations.append(('orient',str(simplex),str(sg*det)))
  vd+=sg*det/sp.factorial(4)
 vd=sp.factor(vd)
 missing_primal=[]
 for simplex in hP.simplices:
  jj=[int(i) for i in simplex]
  supporting=[k for k,zz in enumerate(vps) if all(sp.factor((zz.T*vertsP[i])[0]-1)==0 for i in jj)]
  if not supporting: missing_primal.append(jj)
 assert not missing_primal, ('primal facet coverage',missing_primal)
 assert not violations, ('polar orientations',violations)
 print('polar',val,vd,'vertices',len(vps),'faces',len(hD.simplices),'seconds',time.time()-t0,flush=True)
 prod=sp.factor(vd*vp)
 print('product',val,prod,flush=True)
 print('mah_stability',val,sp.factor(prod-sp.Rational(32,3)),flush=True)

 expected_primal=2*(x*x+12*x+24)/3 if val==1 else 4*(x*x+6*x+10)/3
 expected_polar=-(x**5+4*x**4-44*x**3-272*x**2-464*x-256)/(3*(x+2)**3*(x+4)**2) if val==1 else 8*(3*x**6+26*x**5+80*x**4+72*x**3-88*x**2-64*x+128)/(3*x**3*(x+2)**3*(x+4)**2)
 assert sp.factor(vp-expected_primal)==0
 assert sp.factor(vd-expected_polar)==0
 A=x**6+16*x**5+76*x**4-32*x**3-1136*x**2-2752*x-1920
 B=x**7+19*x**6+106*x**5+188*x**4-128*x**3-568*x**2+64*x+640
 assert sp.factor(prod-sp.Rational(32,3)-(-2*x*A/(9*(x+2)**3*(x+4)**2) if val==1 else 64*B/(9*x**3*(x+2)**3*(x+4)**2)))==0
 if val==1: assert positive(-A)
 else: assert positive(B)
 print('PASS: exact algebraic formulas, symbolic interval inequalities and facet certificates',val,flush=True)
