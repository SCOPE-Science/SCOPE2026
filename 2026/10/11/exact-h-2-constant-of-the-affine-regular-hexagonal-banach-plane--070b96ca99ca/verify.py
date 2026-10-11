from fractions import Fraction as F
import sympy as s

facets=[(F(1),F(0)),(F(0),F(1)),(F(1),F(-1)),(F(-1),F(0)),(F(0),F(-1)),(F(-1),F(1))]
verts=[(F(1),F(0)),(F(1),F(1)),(F(0),F(1)),(F(-1),F(0)),(F(-1),F(-1)),(F(0),F(-1))]
def edge_aff(j):
    a=verts[j]; b=verts[(j+1)%6]
    return a,(b[0]-a[0],b[1]-a[1])
def edgept(j,v):
    p,d=edge_aff(j); return (p[0]+d[0]*v,p[1]+d[1]*v)
x0,xd=edge_aff(0)
segments=set()
for j in range(6):
    y0,yd=edge_aff(j)
    def expr(f,sy):
        return [f[0]*(x0[0]+sy*y0[0])+f[1]*(x0[1]+sy*y0[1]),
                f[0]*xd[0]+f[1]*xd[1],
                sy*(f[0]*yd[0]+f[1]*yd[1])]
    for fp in facets:
      for fm in facets:
        ep,em=expr(fp,1),expr(fm,-1)
        E=[ep[k]-em[k] for k in range(3)]
        if E[1]==0 and E[2]==0:
            continue
        if E[2]!=0:
            u0,ut=F(0),F(1); v0,vt=-E[0]/E[2],-E[1]/E[2]
        else:
            v0,vt=F(0),F(1); u0,ut=-E[0]/E[1],-E[2]/E[1]
        ineq=[]
        def add(c,d):ineq.append((c,d))
        add(-u0,-ut);add(u0-1,ut);add(-v0,-vt);add(v0-1,vt)
        for h in facets:
            eh=expr(h,1); D=[eh[k]-ep[k] for k in range(3)]
            add(D[0]+D[1]*u0+D[2]*v0,D[1]*ut+D[2]*vt)
        for h in facets:
            eh=expr(h,-1); D=[eh[k]-em[k] for k in range(3)]
            add(D[0]+D[1]*u0+D[2]*v0,D[1]*ut+D[2]*vt)
        lo,hi=F(-10**6),F(10**6); ok=True
        for c,d in ineq:
            if d==0:
                if c>0:ok=False;break
            elif d>0:hi=min(hi,-c/d)
            else:lo=max(lo,-c/d)
        if not ok or lo>hi:continue
        p1=(u0+ut*lo,v0+vt*lo);p2=(u0+ut*hi,v0+vt*hi)
        segments.add((j,tuple(sorted((p1,p2)))))
expected={
(1,((F(0),F(1,2)),(F(1,3),F(2,3)))),(1,((F(1,3),F(2,3)),(F(1,2),F(1)))),
(2,((F(1,2),F(0)),(F(2,3),F(1,3)))),(2,((F(2,3),F(1,3)),(F(1),F(1,2)))),
(4,((F(0),F(1,2)),(F(1,3),F(2,3)))),(4,((F(1,3),F(2,3)),(F(1,2),F(1)))),
(5,((F(1,2),F(0)),(F(2,3),F(1,3)))),(5,((F(2,3),F(1,3)),(F(1),F(1,2))))}
assert segments==expected

def mm(A,B):
    a,b,c,d=A;e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def ap(M,p):
    a,b,c,d=M;return(a*p[0]+b*p[1],c*p[0]+d*p[1])
I=(F(1),F(0),F(0),F(1));gens=[(F(0),F(1),F(1),F(0)),(F(1),F(0),F(1),F(-1)),(F(-1),F(0),F(0),F(-1))]
G={I}
while True:
    old=set(G)
    for A in list(G):
        for B in gens:G.add(mm(A,B))
    if G==old:break
assert len(G)==12
canon={sgn:{((F(1),F(0)),(sgn*F(1,2),sgn*F(1))),((F(1),F(1,3)),(sgn*F(1,3),sgn*F(1)))} for sgn in (1,-1)}
for j,ends in segments:
    cfg=[]
    for u,v in ends:cfg.append(((F(1),u),edgept(j,v)))
    found=False
    for M in G:
      for swap in (False,True):
        tr=[]
        for x,y in cfg:
            x,y=ap(M,x),ap(M,y)
            if swap:x,y=y,x
            tr.append((x,y))
        if any(set(tr)==C for C in canon.values()):found=True
    assert found

u=s.symbols('u', real=True)
c2=s.Rational(32,45)
# plus family crossing value
Rp2=(u**2-u+2)**2/(5*u**2-6*u+5)
Dp=s.expand(45*(u**2-u+2)**2-32*(5*u**2-6*u+5))
assert s.expand(Dp-(45*u**4-90*u**3+65*u**2+12*u+20))==0
# minus family sharp factorization
Rm2=(u**2-u+2)**2/(u**2-2*u+5)
Dm=s.factor(45*(u**2-u+2)**2-32*(u**2-2*u+5))
assert Dm==(3*u-1)*(15*u**3-25*u**2+56*u-20)
q=15*u**3-25*u**2+56*u-20
assert s.discriminant(s.diff(q,u),u)<0
assert s.simplify(q.subs(u,s.Rational(1,3))+s.Rational(32,9))==0
# equality pair and exact quotient squared
x=(s.Rational(1),s.Rational(1,3));y=(-s.Rational(1,3),-s.Rational(1));lam=s.Rational(3)
def N(v):return max(abs(v[0]),abs(v[1]),abs(v[0]-v[1]))
assert N(x)==1 and N(y)==1
assert N((x[0]+y[0],x[1]+y[1]))==s.Rational(4,3)
assert N((x[0]-y[0],x[1]-y[1]))==s.Rational(4,3)
assert N((x[0]+lam*y[0],x[1]+lam*y[1]))==s.Rational(8,3)
assert s.simplify((1+lam**2)/N((x[0]+lam*y[0],x[1]+lam*y[1]))**2-s.Rational(90,64))==0
print('VERIFY_OK segments=8 canonical_families=2 sharp_H2=3sqrt10/8')
