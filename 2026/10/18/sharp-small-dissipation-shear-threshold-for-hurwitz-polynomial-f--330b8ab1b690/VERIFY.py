# Exact symbolic checks for the named polynomial vector field.
# Requires SymPy; no external files.
import sympy as s
x,y,z,mu,e,k,u=s.symbols('x y z mu e k u',real=True)
U=x*x+y*y
S=(U-5)*(s.Rational(20,21)-U)-s.Rational(400,21)*z*z
Om=1+e*(z+U/10)
F=s.Matrix([mu*x*S-Om*y,mu*y*S+Om*x,-z-U/10]); J=F.jacobian((x,y,z)).subs(y,0)
t=s.symbols('t'); C=s.Poly(J.charpoly(t).as_expr(),t)
fs=[126*u**2-160*u*z-500*u+800*z**2+200,21*u**2-75*u+80*z**2+20,21*u**2-125*u+400*z**2+100,21*u**2-32*u*z-75*u+80*z**2+20]; f1,f2,f3,f4=fs
g=10+e*(u+10*z)
c2=1+mu*(6*(u-s.Rational(125,63))**2+s.Rational(800,21)*z**2-s.Rational(18650,1323))
c1=g*(g+2*e*u)/100+mu*f1/21+5*mu**2*f2*f3/441
c0=g**2/100+5*mu**2*f3*f4/441
for n,c in [(2,c2),(1,c1),(0,c0)]:
 v=s.factor(C.coeff_monomial(t**n)-c.subs(u,x**2))
 assert v==0
H=s.Poly(s.expand((c2*c1-c0).subs(e,k*mu)),mu)
assert s.factor(H.coeff_monomial(mu)-s.expand((1600*(z-u/20)**2+248*u**2-1000*u+400)/21+k*u/5))==0
for p,d,formula in [(2,4,(15876*u**4-16800*u**3*z+201600*u**2*z**2-64000*u*z**3+640000*z**4)/441),(3,6,10*(21*u*u+80*z*z)*(21*u*u+400*z*z)*(63*u*u+400*z*z)/9261)]:
 poly=s.Poly(H.coeff_monomial(mu**p),u,z)
 hom=sum(c*u**ij[0]*z**ij[1] for ij,c in poly.terms() if sum(ij)==d)
 v=s.factor(hom-formula); assert v==0
u0=10/s.sqrt(62); z0=u0/20; k0=(5000-400*s.sqrt(62))/21
p2=s.simplify(H.coeff_monomial(mu**2).subs({u:u0,z:z0,k:k0})); k1=s.simplify(-5*p2/u0)
assert s.simplify(H.coeff_monomial(mu).subs({u:u0,z:z0,k:k0}))==0
assert s.simplify(s.diff(H.coeff_monomial(mu),u).subs({u:u0,z:z0,k:k0}))==0
assert s.simplify(s.diff(H.coeff_monomial(mu),z).subs({u:u0,z:z0,k:k0}))==0
assert p2<0
assert k1>0
assert s.simplify((15876*u**4-16800*u**3*z+201600*u**2*z**2-64000*u*z**3+640000*z**4)-(7476*u**4+161200*u**2*z**2+608000*z**4)-(8400*(u**2-u*z)**2+32000*(u*z-z**2)**2))==0
assert s.simplify(k1-(-s.Rational(64250000,13671)+s.Rational(39430000,60543)*s.sqrt(62)))==0
print('PASS')
