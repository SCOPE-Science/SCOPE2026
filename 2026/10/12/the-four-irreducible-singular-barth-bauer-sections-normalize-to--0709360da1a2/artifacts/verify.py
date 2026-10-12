import sympy as sp
a,z0,z1,z3,x=sp.symbols("a z0 z1 z3 x")
g1=sp.expand((a**2-2*a-1)*(a**2+2*a-1))
assert sp.expand(g1-(a**4-6*a**2+1))==0
assert sp.gcd(sp.Poly(g1,a),sp.Poly(a**2+1,a)).degree()==0
sext=sp.expand((x**2+1)*(x**4-6*x**2+1))
assert sext==x**6-5*x**4-5*x**2+1
assert sp.gcd(sp.Poly(sext,x),sp.Poly(sp.diff(sext,x),x)).degree()==0
assert sp.gcd(sp.Poly(g1,a),sp.Poly(sp.diff(g1,a),a)).degree()==0
Fnode=z0**4+z1**4-6*z0**2*z1**2-6*(a**2+1)*(z0**2+z1**2)
H=sp.hessian(Fnode,(z0,z1)).subs({z0:0,z1:0})
hdet=sp.factor(H.det())
assert hdet==144*(a**2+1)**2
assert sp.gcd(sp.Poly(g1,a),sp.Poly(hdet,a)).degree()==0
r=sp.sqrt(2)
roots=[1+r,1-r,-1+r,-1-r]
assert len({str(sp.simplify(t)) for t in roots})==4
assert all(sp.simplify(g1.subs(a,t))==0 for t in roots)
print("g1 =",g1)
print("normalization_sextic =",sext)
print("node_hessian_det =",hdet)
print("VERIFY_OK")
