import sympy as s
x,y,z,a,c,t=s.symbols("x y z a c t", real=True)
L=s.symbols("L", positive=True)
F=s.Matrix([a*z,z,-x+y+y*y])
C=x-a*y
H=z*z/s.Integer(2)+x*y-(a+1)*y*y/2-y**3/3
assert s.simplify(s.Matrix([s.diff(C,i) for i in (x,y,z)]).dot(F)) == 0
assert s.simplify(s.Matrix([s.diff(H,i) for i in (x,y,z)]).dot(F)) == 0
assert s.simplify(s.Matrix([s.diff(H,i) for i in (x,y,z)]).cross(s.Matrix([s.diff(C,i) for i in (x,y,z)]))-F)==s.zeros(3,1)
assert s.simplify(s.trace(F.jacobian((x,y,z))))==0
V=(a-1)*y*y/2+c*y-y**3/3
assert s.simplify(-s.diff(V,y)-(y*y-(a-1)*y-c))==0
assert s.simplify(s.diff(V,y).subs(c,(L*L-(a-1)**2)/4)+(y-(a-1-L)/2)*(y-(a-1+L)/2))==0
lo=(a-1-L)/2; hi=(a-1+L)/2
assert s.simplify((V.subs(y,hi)-V.subs(y,lo)).subs(c,(L*L-(a-1)**2)/4)-L**3/6)==0
q=hi-s.Rational(3,2)*L*s.sech(s.sqrt(L)*t/2)**2
zq=s.diff(q,t)
force=(y*y-(a-1)*y-c).subs({y:q,c:(L*L-(a-1)**2)/4})
assert s.simplify(s.expand_trig(s.diff(q,t,2)-force))==0
assert s.simplify(q.subs(t,0)-(lo-L/2))==0
assert s.simplify(zq.subs(t,0))==0
assert s.simplify(s.limit(q,t,s.oo)-hi)==0
assert s.simplify((V.subs(y,hi)-V-(y-(hi-s.Rational(3,2)*L))*(y-hi)**2/3).subs(c,(L**2-(a-1)**2)/4))==0
assert s.simplify(4**4/(4*s.sqrt(2)/3)**2-72)==0
print('PASS: two polynomial integrals, Nambu form, divergence, leaf reduction, energy gap, explicit separatrix')
