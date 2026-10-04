import sympy as sp

u,s,b,d=sp.symbols('u s b d', positive=True)
A=-1/(b*(s+1)); C=1/b; F=1/(b*d); H=1/(2*b**2*d)
D=-(b*d+b*s+b-2*d*s)/(b**3*d*(s+1))
B=(-2*b*d*s+b*d+b*s**2+2*b*s+b-2*d*s**2-2*d*s)/(b**3*d*(s+1)**3)
G=(-b*d+b*s-2*b+2*d*s)/(b**3*d**2*(s+1))
p=s*A; q=s*B
y=u+A*u**3+B*u**5; z=C*u**2+D*u**4; y1=F*u**3+G*u**5; z1=H*u**4
f=p*u**3+q*u**5
R=[sp.expand(f-s*(y-u)),sp.expand(sp.diff(y,u)*f-(-u*z+u-y)),sp.expand(sp.diff(z,u)*f-(u*y-u*y1-b*z)),sp.expand(sp.diff(y1,u)*f-(u*z-2*u*z1-d*y1)),sp.expand(sp.diff(z1,u)*f-(2*u*y1-4*b*z1))]
required=[[],[3,5],[2,4],[3,5],[4]]
for residual,powers in zip(R,required):
    for k in powers: assert sp.simplify(residual.coeff(u,k))==0
assert sp.simplify(q-s*B)==0
vals={s:sp.Rational(10),b:sp.Rational(8,3),d:sp.Rational(19,3)}; c=-p
assert sp.simplify((2*c).subs(vals)-sp.Rational(15,22))==0
assert sp.simplify((-q/c).subs(vals)-sp.Rational(9393,36784))==0
assert sp.simplify(q.subs(vals)+sp.Rational(140895,1618496))==0
print('VERIFY_OK')
