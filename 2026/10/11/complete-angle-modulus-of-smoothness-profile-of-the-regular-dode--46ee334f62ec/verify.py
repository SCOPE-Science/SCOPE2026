import sympy as sp
rt=sp.sqrt(3); a,b,e=sp.symbols('a b e', real=True)
r=2-rt
V=[sp.simplify(sp.Matrix([sp.cos(sp.pi/12+k*sp.pi/6)/sp.cos(sp.pi/12),sp.sin(sp.pi/12+k*sp.pi/6)/sp.cos(sp.pi/12)])) for k in range(12)]
def E(j,t): return sp.simplify(V[j]+t*(V[(j+1)%12]-V[j]))
base=[lambda z:z[0],lambda z:z[1],lambda z:(rt*z[0]+z[1])/2,lambda z:(z[0]+rt*z[1])/2,lambda z:(-z[0]+rt*z[1])/2,lambda z:(-rt*z[0]+z[1])/2]
def vals(z):
 q=[sp.simplify(f(z)) for f in base]; return q+[-u for u in q]
def nonneg_aff(expr,var,lo,hi):
 x0=sp.simplify(expr.subs(var,lo)); x1=sp.simplify(expr.subs(var,hi))
 assert float(sp.N(x0,60))>=-1e-45,(expr,lo,x0)
 assert float(sp.N(x1,60))>=-1e-45,(expr,hi,x1)
def norm_affine(z,cand,var,lo,hi):
 vv=vals(z)
 for u in vv:
  nonneg_aff(cand-u,var,lo,hi)
 assert any(sp.simplify(cand-u)==0 for u in vv)
# Edge certificates j=0,...,5.
x=E(0,a)
cert=[]
# j0
sv=vals(x+E(0,b)); assert sp.simplify(sv[2]-2)==0; cert.append('E0')
# j1 split
y=E(1,b); sv=vals(x+y); dv=vals(x-y)
A=sp.factor(sv[2]+r*dv[10]-2,extension=rt); B=sp.factor(sv[3]+r*dv[11]-2,extension=rt)
assert sp.simplify(A-2*(4*rt-7)*(a+b-1))==0
assert sp.simplify(B-(14-8*rt)*(a+b-1))==0
assert float(sp.N(4*rt-7))<0 and float(sp.N(14-8*rt))>0; cert.append('E1')
# j2 identity
y=E(2,b); sv=vals(x+y); dv=vals(x-y); assert sp.simplify(sv[3]+dv[11]/rt-4/rt)==0; cert.append('E2')
# j3 identity
y=E(3,b); sv=vals(x+y); dv=vals(x-y); assert sp.simplify(sv[1]+dv[11]-(1+rt))==0; cert.append('E3')
# j4 identity
y=E(4,b); sv=vals(x+y); dv=vals(x-y); assert sp.simplify(sv[1]+rt*dv[0]-4)==0; cert.append('E4')
# j5 split
y=E(5,b); sv=vals(x+y); dv=vals(x-y)
A=sp.factor(sv[1]+(2+rt)*dv[0]-2*(2+rt),extension=rt)
B=sp.factor(sv[4]+(2+rt)*dv[2]-2*(2+rt),extension=rt)
assert sp.simplify(A-2*(rt-2)*(a+b-1))==0
assert sp.simplify(B-(4-2*rt)*(a+b-1))==0
assert float(sp.N(rt-2))<0 and float(sp.N(4-2*rt))>0; cert.append('E5')
# j6 has distance exactly 2.
y=E(6,b); dv=vals(x-y); assert sp.simplify(dv[2]-2)==0; cert.append('E6')
# Lower envelope line comparisons.
d=sp.symbols('d', real=True)
Ls=[sp.Integer(2),2-r*d,(4-d)/rt,1+rt-d,4-rt*d,(2+rt)*(2-d)]
Ms=[(2-r*d,0,1),(1+rt-d,1,rt),((2+rt)*(2-d),rt,2)]
for M,lo,hi in Ms:
 for L in Ls: nonneg_aff(sp.simplify(L-M),d,lo,hi)
# Involution.
M1=2-r*d; M2=1+rt-d; M3=(2+rt)*(2-d)
assert sp.simplify(M3.subs(d,M1)-d)==0
assert sp.simplify(M2.subs(d,M2)-d)==0
assert sp.simplify(M1.subs(d,M3)-d)==0
# Sharp witness families.
def check_family(xf,yf,cand,lo,hi):
 norm_affine(xf,sp.Integer(1),e,lo,hi); norm_affine(yf,sp.Integer(1),e,lo,hi)
 norm_affine(sp.simplify(xf-yf),e,e,lo,hi); norm_affine(sp.simplify(xf+yf),cand,e,lo,hi)
check_family(E(0,1-e),E(1,e),2-r*e,0,1)
t=(e-1)/(rt-1); check_family(E(0,1-t),E(3,t),1+rt-e,1,rt)
t=(e-rt)/(2-rt); check_family(E(0,1-t),E(5,t),(2+rt)*(2-e),rt,2)
print('VERIFY_OK facets=12 edge_certificates=7 envelope_lines=6 witness_families=3 transitions=1,sqrt3')
