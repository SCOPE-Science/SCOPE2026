import sympy as s
T=s.symbols('T'); pts=[(0,(0,0)),(1,(1,0)),(2,(0,1)),(3,(1,1)),(4,(2,3))]
def interpolation(omit):
 a=s.symbols('a0:9');x=sum(a[j]*T**j for j in range(3));y=sum(a[j+3]*T**j for j in range(3));z=sum(a[j+6]*T**j for j in range(3))
 eq=[]
 for i,(t,(u,v)) in enumerate(pts):
  if i!=omit: eq.extend([x.subs(T,t)-u*z.subs(T,t),y.subs(T,t)-v*z.subs(T,t)])
 M=s.linear_eq_to_matrix(eq,a)[0]; ns=M.nullspace()
 if len(ns)!=1: raise Exception('not unique')
 v=ns[0]; den=s.ilcm(*[int(w.q) for w in v]);v=[int(w*den) for w in v]
 return [s.Poly(f.subs(dict(zip(a,v))),T).as_expr() for f in (x,y,z)]
bs=[interpolation(i) for i in range(5)]
for i,b in enumerate(bs):
 print('B',i,b)
 assert all(s.Poly(z,T).degree()<=2 for z in b)
 for j,(t,(u,v)) in enumerate(pts):
  if j!=i: assert b[0].subs(T,t)==u*b[2].subs(T,t) and b[1].subs(T,t)==v*b[2].subs(T,t) and b[2].subs(T,t)!=0
 assert s.Poly(s.gcd_list(b),T).degree()==0
for i in range(5):
 for j in range(i+1,5):
  a,b=bs[i],bs[j];cross=[s.expand(a[r]*b[q]-a[q]*b[r]) for r,q in [(0,1),(0,2),(1,2)]]
  g=s.Poly(s.gcd_list(cross),T); print('intersection B',i,j,' gcd=',s.factor(g.as_expr()),' degree=',g.degree())
  assert g.degree()==3 and s.Poly(g,T).is_sqf
for i,(t,(u,v)) in enumerate(pts):
 for j,b in enumerate(bs):
  gcd=s.Poly(s.gcd(b[0]-u*b[2],b[1]-v*b[2]),T)
  print('A',i,'B',j,'gcd',s.factor(gcd.as_expr()))
  assert gcd.degree()==(0 if i==j else 1)
print('VERIFY_OK')
# The surface is the blow-up of the plane in six general points.
# Classes are triples (degree, multiplicities at its six points).
def pairing(c,d):
 return c[0]*d[0]-sum(c[i]*d[i] for i in range(1,7))
conics=[]
for missing in range(6):
 c=(2,)+tuple(0 if j==missing else 1 for j in range(6))
 assert pairing(c,c)==-1
 assert pairing((5,2,2,2,2,2,2),c)==0
 assert pairing((2,1,1,1,1,1,1),c)==-1
 conics.append(c)
for i in range(6):
 for j in range(i+1,6): assert pairing(conics[i],conics[j])==0
for j in range(6):
 e=(0,)+tuple(-1 if i==j else 0 for i in range(6))
 assert pairing((5,2,2,2,2,2,2),e)==2
for i in range(6):
 for j in range(i+1,6):
  line=(1,)+tuple(1 if k in (i,j) else 0 for k in range(6))
  assert pairing((5,2,2,2,2,2,2),line)==1
# Curve coordinates (h1, h2, e1,...,e5), so blow-up exceptional
# classes have negative e_i coefficients by convention.
A=[];B=[]
for i in range(5):
 a=(1,0)+tuple(-1 if k==i else 0 for k in range(5))
 b=(1,2)+tuple(0 if k==i else -1 for k in range(5))
 A.append(a);B.append(b)
for a,b in zip(A,B):
 assert tuple(x+y for x,y in zip(a,b)) == (2,2,-1,-1,-1,-1,-1)
for c in A+B+[(2,2,-1,-1,-1,-1,-1)]:
 assert 2*c[0]+3*c[1]+2*sum(c[2:])==0
print('ELEVEN_CURVES_SIX_DISJOINT_CONICS_ONE_NONEXTREMAL_VERIFY_OK')
