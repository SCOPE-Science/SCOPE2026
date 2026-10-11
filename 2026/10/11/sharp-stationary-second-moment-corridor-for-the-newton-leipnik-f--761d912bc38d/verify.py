import sympy as s
x,y,z,lam,t=s.symbols('x y z lam t', real=True)
a=s.Rational(2,5); b=s.Rational(7,40)
fx=-a*x+y+10*y*z
fy=-x-a*y+5*x*z
fz=b*z-5*x*y
F1=x**2/s.Integer(2)+z**2
F2=(y**2+z**2)/2
D1=s.expand(s.diff(F1,x)*fx+s.diff(F1,y)*fy+s.diff(F1,z)*fz)
D2=s.expand(s.diff(F2,x)*fx+s.diff(F2,y)*fy+s.diff(F2,z)*fz)
assert s.expand(D1-(-a*x**2+x*y+2*b*z**2))==0
assert s.expand(D2-(-x*y-a*y**2+b*z**2))==0
poly=s.factor((a*t-2*b)**2-t*(s.Rational(21,16)-t))
assert poly==s.factor((464*t**2-637*t+49)/400)
roots=s.solve(464*t**2-637*t+49,t)
expected=[s.Rational(637,928)-s.Rational(35,928)*s.sqrt(257),s.Rational(637,928)+s.Rational(35,928)*s.sqrt(257)]
assert all(s.simplify(r-e)==0 for r,e in zip(roots,expected))
zroots=[s.Rational(1,20)-s.sqrt(257)/100,s.Rational(1,20)+s.sqrt(257)/100]
for zz,tt in zip(zroots,expected):
    ll=s.simplify(a/(1+10*zz))
    xx2=s.simplify(b*zz/(5*ll))
    assert s.simplify(tt-xx2/zz**2)==0
    assert s.simplify(fx.subs({y:ll*x,z:zz})/x)==0
    assert s.simplify(fy.subs({y:ll*x,z:zz})/x)==0
    assert s.simplify((b*zz-5*ll*xx2))==0
print('VERIFY_OK')
print('roots=',[s.sstr(r) for r in roots])
print('approx=',[float(r.evalf()) for r in roots])
