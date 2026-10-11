import sympy as sp
a,b,c=sp.symbols('a b c', real=True); d=-a-b-c; v=[a,b,c,d]
lhs=sum((v[i]-v[j])**4 for i in range(4) for j in range(i+1,4))
rhs=4*sum(z**4 for z in v)+3*sum(z**2 for z in v)**2
assert sp.expand(lhs-rhs)==0
alpha=sp.root(3,4)**-1
pts=[(alpha,alpha,alpha),(alpha,-alpha,-alpha),(-alpha,alpha,-alpha),(-alpha,-alpha,alpha)]
for p in pts: assert sp.simplify(sum(z**4 for z in p)-1)==0
assert all(sp.simplify(sum(p[k] for p in pts))==0 for k in range(3))
d4=[]
for i in range(4):
  for j in range(i+1,4):
    q=sp.simplify(sum((pts[i][k]-pts[j][k])**4 for k in range(3)))
    assert sp.simplify(q-sp.Rational(32,3))==0; d4.append(q)
objective=sp.simplify(sum(sp.sqrt(q) for q in d4))
assert sp.simplify(objective-8*sp.sqrt(6))==0
assert sp.simplify(sum(d4)-64)==0
assert float(sp.N(8*sp.sqrt(6)-8*(1+sp.sqrt(2)),30))>0
print('VERIFY_OK scalar_identity=exact tetrahedron=exact fourth_power_total=64 objective=8*sqrt(6)')
