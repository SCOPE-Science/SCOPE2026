import sympy as sp

I=sp.I
sqrt2=sp.sqrt(2); sqrt3=sp.sqrt(3)
alpha=(1+I)/sqrt2  # alpha^4=-1
zeta6=sp.Rational(1,2)+I*sqrt3/2
xi=-sp.Rational(1,2)+I*sqrt3/2
assert sp.simplify(alpha**4 + 1)==0
assert sp.simplify(zeta6**2-zeta6+1)==0
assert sp.simplify(xi**2+xi+1)==0

X,Y,Z,W=sp.symbols('X Y Z W')
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3')
F8=X**4+X*Y**3+Z**4+Z*W**3
Fschur=x0**4-x0*x1**3-x2**4+x2*x3**3
pull=sp.expand(Fschur.subs({x0:X,x1:-Y,x2:alpha*Z,x3:-alpha*W}))
assert sp.simplify(pull-F8)==0

def canon(v):
    v=[sp.simplify(a) for a in v]
    for a in v:
        if sp.simplify(a)!=0:
            return tuple(sp.simplify(sp.radsimp(b/a)) for b in v)
    raise ValueError

def T(v):
    X,Y,Z,W=v
    return canon([X,-Y,alpha*Z,-alpha*W])

Gs=[(0,0,0,1)]
for i in (1,3,5): Gs.append((0,0,sp.simplify(zeta6**i),1))
Gs.append((0,1,0,0))
for i in (1,3,5): Gs.append((sp.simplify(zeta6**i),1,0,0))
trans={T(v) for v in Gs}
ps={canon(v) for v in [(0,0,0,1),(0,0,1,1),(0,0,xi,1),(0,0,xi**2,1)]}
qs={canon(v) for v in [(0,1,0,0),(1,1,0,0),(xi,1,0,0),(xi**2,1,0,0)]}
assert trans == ps|qs and len(trans)==8

s,t=sp.symbols('s t')
ps_list=[(0,0,0,1),(0,0,1,1),(0,0,xi,1),(0,0,xi**2,1)]
qs_list=[(0,1,0,0),(1,1,0,0),(xi,1,0,0),(xi**2,1,0,0)]

def reduce_xi(expr):
    expr=sp.expand(expr)
    # exact simplify using xi definition
    return sp.simplify(expr)

def plucker(p,q):
    vals=[]
    for i in range(4):
        for j in range(i+1,4): vals.append(sp.simplify(p[i]*q[j]-p[j]*q[i]))
    return canon(vals)

lines=[]
for i,p in enumerate(ps_list):
  for j,q in enumerate(qs_list):
    pt=[s*p[k]+t*q[k] for k in range(4)]
    val=sp.expand(Fschur.subs(dict(zip((x0,x1,x2,x3),pt))))
    assert sp.simplify(val)==0, (i,j,sp.factor(val))
    lines.append((i,j,plucker(p,q)))
assert len({L[2] for L in lines})==16
for i in range(4): assert sum(1 for a,b,_ in lines if a==i)==4
for j in range(4): assert sum(1 for a,b,_ in lines if b==j)==4

print('VERIFY_OK transform=S8_to_Schur galois_points=8 join_lines=16 incidence=K4,4 each_galois_point_on_join_lines=4')
