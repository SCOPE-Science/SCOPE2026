#!/usr/bin/env python3
import sympy as sp

x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3')
i=sp.I
M=sp.Matrix([
    [x0+x3,0,x2,0],
    [0,2*x0+x3,i*x2,-i*x1],
    [x2,-i*x2,x2+x3,x1],
    [0,i*x1,x1,x3],
])
F=sp.expand(M.det())
expected=sp.expand(-2*x0**2*x1**2 + 2*x0**2*x2*x3 + 2*x0**2*x3**2
 -3*x0*x1**2*x2 -4*x0*x1**2*x3 -3*x0*x2**2*x3 +3*x0*x2*x3**2
 +3*x0*x3**3 +x1**2*x2**2 -3*x1**2*x2*x3 -2*x1**2*x3**2
 -2*x2**2*x3**2 +x2*x3**3 +x3**4)
assert sp.expand(F-expected)==0
partials=[sp.diff(F,v) for v in (x0,x1,x2,x3)]
G=sp.groebner([g.subs(x3,1) for g in partials],x0,x1,x2,order='lex')
assert list(G.polys)==[sp.Poly(2*x0+x2+1,x0,x1,x2),sp.Poly(x1**2+x2,x0,x1,x2),sp.Poly(4*x2**2-x2-1,x0,x1,x2)]

# At infinity the first, second and third gradient equations force either x1=0
# or the single point D.  In the x1=0 case the fourth equation factors as below.
inf=[sp.factor(g.subs(x3,0)) for g in partials]
assert inf[0]==-x1**2*(4*x0+3*x2)
assert inf[1]==-2*x1*(2*x0**2+3*x0*x2-x2**2)
assert inf[2]==-x1**2*(3*x0-2*x2)
assert sp.factor(inf[3].subs(x1,0))==x0*x2*(2*x0-3*x2)

s=sp.sqrt(17)
tm=(1-s)/8
tp=(1+s)/8
a=sp.sqrt((s-1)/8)
b=sp.sqrt((s+1)/8)
pts={
 'A':(1,0,0,0),
 'B':(0,0,1,0),
 'C':(3,0,2,0),
 'D':(0,1,0,0),
 'E+':(-(1+tm)/2,a,tm,1),
 'E-':(-(1+tm)/2,-a,tm,1),
 'F+':(-(1+tp)/2,sp.I*b,tp,1),
 'F-':(-(1+tp)/2,-sp.I*b,tp,1),
}
for P in pts.values():
    sub=dict(zip((x0,x1,x2,x3),P))
    assert all(sp.simplify(g.subs(sub))==0 for g in partials)
    assert M.subs(sub).rank()==2

# Seven singularities are ordinary nodes: local Hessian determinant is nonzero.
def local_hessian_det(P,chart):
    vs=(x0,x1,x2,x3)
    scale=P[chart]
    P=tuple(sp.simplify(z/scale) for z in P)
    local=[v for j,v in enumerate(vs) if j!=chart]
    H=sp.hessian(F.subs(vs[chart],1),local)
    return sp.simplify(H.det().subs({vs[j]:P[j] for j in range(4) if j!=chart}))
node_charts={'A':0,'B':2,'C':0,'E+':3,'E-':3,'F+':3,'F-':3}
for name,chart in node_charts.items():
    assert sp.simplify(local_hessian_det(pts[name],chart))!=0
assert sp.simplify(local_hessian_det(pts['D'],1))==0

# At D, use x1=1 and p=x0+x3, q=x2, w=x3.  The p,q quadratic block is nondegenerate.
p,q,w=sp.symbols('p q w')
GD=sp.expand(F.subs({x0:p-w,x1:1,x2:q,x3:w}))
expected_G=sp.expand(-2*p**2-3*p*q+q**2 + w*(2*p**2*q+2*p**2*w-3*p*q**2-p*q*w-p*w**2+q**2*w))
assert sp.expand(GD-expected_G)==0
Q=sp.hessian((-2*p**2-3*p*q+q**2),(p,q))
assert Q.det()==-17
# Formal critical section p(w),q(w), enough to determine the first nonzero split term.
p3,p4,p5,p6,p7,q3,q4,q5,q6,q7=sp.symbols('p3 p4 p5 p6 p7 q3 q4 q5 q6 q7')
ps=p3*w**3+p4*w**4+p5*w**5+p6*w**6+p7*w**7
qs=q3*w**3+q4*w**4+q5*w**5+q6*w**6+q7*w**7
dp=sp.expand(sp.diff(GD,p).subs({p:ps,q:qs}))
dq=sp.expand(sp.diff(GD,q).subs({p:ps,q:qs}))
eq=[]
for k in range(3,8):
    eq.extend([sp.Eq(dp.coeff(w,k),0),sp.Eq(dq.coeff(w,k),0)])
sol=sp.solve(eq,[p3,p4,p5,p6,p7,q3,q4,q5,q6,q7],dict=True)[0]
assert sol[p3]==sp.Rational(-2,17) and sol[q3]==sp.Rational(-3,17)
h=sp.expand(GD.subs({p:ps.subs(sol),q:qs.subs(sol)}))
assert all(sp.simplify(h.coeff(w,k))==0 for k in range(0,6))
assert sp.simplify(h.coeff(w,6)-sp.Rational(1,17))==0

# Real semidefinite rank-two points.  The characteristic polynomials decide signs.
lam=sp.symbols('lam')
expected_cp={
 'A':lam**2*(lam-2)*(lam-1),
 'B':lam**2*(lam-2)*(lam+1),
 'C':lam**2*(lam-7)*(lam-4),
 'D':lam**2*(lam**2-2),
 'E+':lam**2*(lam**2-(39+s)*lam/16+(37+3*s)/32),
 'E-':lam**2*(lam**2-(39+s)*lam/16+(37+3*s)/32),
}
for name,cp in expected_cp.items():
    P=pts[name]
    got=M.subs(dict(zip((x0,x1,x2,x3),P))).charpoly(lam).as_expr()
    assert sp.simplify(sp.expand(got-cp))==0
# A,C,E± have two positive nonzero eigenvalues; B,D are indefinite.
assert (39+s)>0 and (37+3*s)>0

# Three explicit singular trisecant lines lie on the quartic.
assert sp.expand(F.subs({x1:0,x3:0}))==0
t,u,v=sp.symbols('t u v')
line_restr=sp.factor(F.subs({x0:-(1+t)*v/2,x1:u,x2:t*v,x3:v}))
assert sp.expand(line_restr-v**2*(t*v**2+u**2)*(4*t**2-t-1)/2)==0
assert sp.simplify(4*tm**2-tm-1)==0 and sp.simplify(4*tp**2-tp-1)==0

print('VERIFY_OK')
