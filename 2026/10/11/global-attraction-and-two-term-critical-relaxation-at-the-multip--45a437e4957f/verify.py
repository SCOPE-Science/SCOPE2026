import sympy as sp
A,d,rho=sp.symbols('A d rho', positive=True)
x,y=sp.symbols('x y')
b1=d*rho/A
b0=d*rho**2/A**2
S=A/d+x
F=sp.expand(A-d*S-(b1+b0*y)*S*y)
G=sp.expand((b1+b0*y)*S*y-rho*y)
assert sp.expand(F-(-d*x-rho*y-d*rho*x*y/A-rho**2*y**2/A-d*rho**2*x*y**2/A**2))==0
assert sp.expand(G-(d*rho*x*y/A+rho**2*y**2/A+d*rho**2*x*y**2/A**2))==0

a1,a2,a3=sp.symbols('a1 a2 a3')
h=a1*y+a2*y**2+a3*y**3
red=sp.series(G.subs(x,h),y,0,5).removeO()
inv=sp.series(F.subs(x,h)-sp.diff(h,y)*red,y,0,5).removeO()
sol1=sp.solve(sp.expand(inv).coeff(y,1),a1)[0]
assert sp.simplify(sol1+rho/d)==0
sol2=sp.solve(sp.expand(inv.subs(a1,sol1)).coeff(y,2),a2)[0]
assert sp.simplify(sol2)==0
sol3=sp.solve(sp.expand(inv.subs({a1:sol1,a2:sol2})).coeff(y,3),a3)[0]
assert sp.simplify(sol3-rho**3*(d-rho)/(A**2*d**2))==0
rred=sp.expand(red.subs({a1:sol1,a2:sol2,a3:sol3}))
c3=sp.factor(rred.coeff(y,3))
c4=sp.factor(rred.coeff(y,4))
assert sp.simplify(c3+rho**3/A**2)==0
assert sp.simplify(c4-rho**4*(d-rho)/(A**3*d))==0

I=sp.symbols('I')
poly=sp.expand(rho*b0*I**2+(rho*b1-A*b0)*I+(d*rho-A*b1))
assert sp.factor(poly-rho*b0*I**2)==0

c=rho**3/A**2
q=rho**4*(d-rho)/(A**3*d)
lead=sp.simplify(1/sp.sqrt(2*c))
sub=sp.simplify(q/(2*c**2))
assert sp.simplify(lead-A/(sp.sqrt(2)*rho**sp.Rational(3,2)))==0
assert sp.simplify(sub-A*(d-rho)/(2*d*rho**2))==0
Slead=sp.simplify(-rho*lead/d)
Ssub=sp.simplify(-rho*sub/d)
assert sp.simplify(Slead+A/(d*sp.sqrt(2*rho)))==0
assert sp.simplify(Ssub-A*(rho-d)/(2*d**2*rho))==0

u,v,R=sp.symbols('u v R', positive=True)
Fu=1-u-u*v*(1+v)
Gv=R*v*(u*(1+v)-1)
# Interior equilibrium equations force u=1/(1+v), after which Fu=-v**2/(1+v).
assert sp.factor(Fu.subs(u,1/(1+v))) == -v**2/(v+1)
print('VERIFY_OK')
