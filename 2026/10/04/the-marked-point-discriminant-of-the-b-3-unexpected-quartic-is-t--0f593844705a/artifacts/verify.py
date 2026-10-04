import sympy as sp
from itertools import combinations

a,b,c,x,y,z,u,v=sp.symbols('a b c x y z u v')
Q=(3*a*(b**2-c**2)*x**2*y*z
   +3*b*(c**2-a**2)*x*y**2*z
   +3*c*(a**2-b**2)*x*y*z**2
   +a**3*y**3*z-a**3*y*z**3
   +b**3*x*z**3-b**3*x**3*z
   +c**3*x**3*y-c**3*x*y**3)

def hom_part(expr, vars_, deg):
    e=sp.Poly(sp.expand(expr), *vars_)
    return sp.expand(sum(coef*sp.prod(var**pow_ for var,pow_ in zip(vars_,mon))
                         for mon,coef in e.terms() if sum(mon)==deg))

# c=1 chart, R=[a:b:1], local x=a+u,y=b+v,z=1
E=sp.expand(Q.subs({c:1,x:a+u,y:b+v,z:1}))
for d in (0,1,2): assert hom_part(E,(u,v),d)==0
T3=sp.factor(hom_part(E,(u,v),3))
T4=sp.factor(hom_part(E,(u,v),4))
expected_T3=sp.expand(-(b*u-a*v)**3+b*u**3-a*v**3)
assert sp.expand(T3-expected_T3)==0
assert sp.expand(T4-u*v*(u-v)*(u+v))==0
P=sp.Poly(T3.subs(u,1),v)
D=sp.factor(sp.discriminant(P.as_expr(),v))
expectedD=-27*a**2*b**2*(a-b-1)*(a-b+1)*(a+b-1)*(a+b+1)
assert sp.expand(D-expectedD)==0

# check other affine charts and global reduced discriminant pieces
# a=1, local y=b+u,z=c+v,x=1
E_a=sp.expand(Q.subs({a:1,x:1,y:b+u,z:c+v}))
for d in (0,1,2): assert hom_part(E_a,(u,v),d)==0
D_a=sp.factor(sp.discriminant(hom_part(E_a,(u,v),3).subs(u,1),v))
assert sp.expand(D_a +27*b**2*c**2*(b-c-1)*(b-c+1)*(b+c-1)*(b+c+1))==0
# b=1, local x=a+u,z=c+v,y=1
E_b=sp.expand(Q.subs({b:1,x:a+u,y:1,z:c+v}))
for d in (0,1,2): assert hom_part(E_b,(u,v),d)==0
D_b=sp.factor(sp.discriminant(hom_part(E_b,(u,v),3).subs(u,1),v))
assert sp.expand(D_b +27*a**2*c**2*(a-c-1)*(a-c+1)*(a+c-1)*(a+c+1))==0

# Factor type along the 4 diagonal lines on c=1 and coordinate lines.
subs_lines={
    'a0':{a:0}, 'b0':{b:0},
    'a+b+1':{b:-a-1}, 'a+b-1':{b:1-a},
    'a-b+1':{b:a+1}, 'a-b-1':{b:a-1},
}
facts={name:sp.factor(T3.subs(s)) for name,s in subs_lines.items()}
assert sp.factor(facts['a0'] + b*(b-1)*(b+1)*u**3)==0
assert sp.factor(facts['b0'] - a*(a-1)*(a+1)*v**3)==0
for name in ['a+b+1','a+b-1']:
    assert sp.rem(sp.Poly(facts[name],u,v), sp.Poly((u+v)**2,u,v))==0
for name in ['a-b+1','a-b-1']:
    assert sp.rem(sp.Poly(facts[name],u,v), sp.Poly((u-v)**2,u,v))==0

# Projective 7-line arrangement: a=0,b=0,c=0, a+b+c=0,a+b-c=0,a-b+c=0,-a+b+c=0
lines=[(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]

def cross(p,q):
    return (p[1]*q[2]-p[2]*q[1], p[2]*q[0]-p[0]*q[2], p[0]*q[1]-p[1]*q[0])
def norm(pt):
    vals=[sp.Rational(t) for t in pt]
    for t in vals:
        if t!=0:
            vals=[sp.simplify(q/t) for q in vals]
            # canonical first nonzero=1
            return tuple(vals)
    raise ValueError
pts={}
for i,j in combinations(range(7),2):
    p=norm(cross(lines[i],lines[j]))
    pts.setdefault(p,set()).update([i,j])
# recompute all incidences for every point
for p in list(pts):
    inc={i for i,L in enumerate(lines) if sp.expand(L[0]*p[0]+L[1]*p[1]+L[2]*p[2])==0}
    pts[p]=inc
mult_counts={m:sum(1 for s in pts.values() if len(s)==m) for m in set(map(len,pts.values()))}
assert mult_counts=={2:3,3:6}
Z={(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)}
Z={norm(p) for p in Z}
assert set(pts)==Z

# At each of the nine base points, cubic initial term vanishes and the quartic initial term is squarefree product of four lines.
for R in Z:
    aa,bb,cc=R
    if cc!=0:
        aa,bb=sp.simplify(aa/cc),sp.simplify(bb/cc)
        E=sp.expand(Q.subs({a:aa,b:bb,c:1,x:aa+u,y:bb+v,z:1}))
    elif aa!=0:
        bb,cc=sp.simplify(bb/aa),sp.simplify(cc/aa)
        E=sp.expand(Q.subs({a:1,b:bb,c:cc,x:1,y:bb+u,z:cc+v}))
    else:
        aa,cc=sp.simplify(aa/bb),sp.simplify(cc/bb)
        E=sp.expand(Q.subs({a:aa,b:1,c:cc,x:aa+u,y:1,z:cc+v}))
    assert all(hom_part(E,(u,v),d)==0 for d in range(4))
    H4=sp.factor(hom_part(E,(u,v),4))
    coeff, facs=sp.factor_list(H4)
    assert sum(sp.Poly(f,u,v).total_degree()*e for f,e in facs)==4
    assert len(facs)==4 and all(sp.Poly(f,u,v).total_degree()==1 and e==1 for f,e in facs)

print('VERIFY_OK')
