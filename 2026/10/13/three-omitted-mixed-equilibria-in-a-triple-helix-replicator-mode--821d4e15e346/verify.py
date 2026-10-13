from fractions import Fraction as F
import itertools
import sympy as sp

x,y,z=sp.symbols('x y z')
A,D,B,E,C,U,R=sp.symbols('A D B E C U R', positive=True)
# R denotes F_c+F_u in this checker.
sol=sp.solve([
    sp.Eq(A*y+B*z,C),
    sp.Eq(D*x+E*z,U),
    sp.Eq(B*x+E*y,R)
],[x,y,z], dict=True)[0]
assert sp.simplify(sol[x]-(A*R+B*U-C*E)/(B*(A+D)))==0
assert sp.simplify(sol[y]-(-B*U+C*E+D*R)/(E*(A+D)))==0
assert sp.simplify(sol[z]-(A*B*U-A*D*R+C*D*E)/(B*E*(A+D)))==0

sx,sy,sz=sp.symbols('sx sy sz', positive=True)
J=sp.Matrix([[0,sx*A,sx*B],[sy*D,0,sy*E],[-sz*B,-sz*E,0]])
assert sp.trace(J)==0
assert sp.factor(J.det()) == -B*E*sx*sy*sz*(A+D)

# Baseline exact equilibrium census.
AA,DD,BB,EE,CC,UU,RR=41,37,32,28,40,34,26
f1=AA*y+BB*z-CC
f2=DD*x+EE*z-UU
f3=RR-BB*x-EE*y
factors=[f1,f2,f3]
vars_=[x,y,z]
points=set()
for status in itertools.product([0,1,'I'], repeat=3):
    subs={}
    eqs=[]
    for v,s,f in zip(vars_,status,factors):
        if s in (0,1): subs[v]=sp.Rational(s)
        else: eqs.append(sp.expand(f.subs(subs)))
    # Substitute all fixed coordinates after they have been collected.
    eqs=[sp.expand(f.subs(subs)) for f,s in zip(factors,status) if s=='I']
    iv=[v for v,s in zip(vars_,status) if s=='I']
    sols=sp.solve(eqs,iv,dict=True) if iv else ([{}] if all(sp.expand(f.subs(subs))==0 for f,s in zip(factors,status) if s=='I') else [])
    for so in sols:
        p={**subs,**so}
        if set(p)!=set(vars_):
            continue
        vals=tuple(sp.simplify(p[v]) for v in vars_)
        ok=True
        for val,s in zip(vals,status):
            if not (0 <= val <= 1): ok=False
            if s=='I' and not (0 < val < 1): ok=False
        if ok: points.add(vals)
expected={(sp.Rational(i),sp.Rational(j),sp.Rational(k)) for i in (0,1) for j in (0,1) for k in (0,1)}
expected |= {
    (sp.Rational(34,37),sp.Rational(40,41),sp.Rational(0)),
    (sp.Rational(6,37),sp.Rational(8,41),sp.Rational(1)),
    (sp.Rational(517,1248),sp.Rational(71,156),sp.Rational(3329,4992)),
}
assert points==expected, (points ^ expected)
assert len(points)==11

# Verify baseline interior equilibrium by direct substitution.
p=(sp.Rational(517,1248),sp.Rational(71,156),sp.Rational(3329,4992))
assert all(sp.expand(f.subs({x:p[0],y:p[1],z:p[2]}))==0 for f in factors)

# Face transverse signs.
p0=(sp.Rational(34,37),sp.Rational(40,41),sp.Rational(0))
p1=(sp.Rational(6,37),sp.Rational(8,41),sp.Rational(1))
br=lambda P: sp.simplify(RR-BB*P[0]-EE*P[1])
assert br(p0)==-sp.Rational(46606,1517)
assert -br(p1)==-sp.Rational(23282,1517)

print('VERIFY_OK')
