#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product, combinations

V=[(F(1),F(1)),(F(0),F(1)),(F(-1),F(0)),(F(-1),F(-1)),(F(0),F(-1)),(F(1),F(0))]
FORMS=[(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]
BASE=[(1,0),(0,1),(1,-1)]
EXPECTED_POLYS={
(F(0),F(9,4),F(-5,4)),(F(1,9),F(8,9),F(0)),(F(1,9),F(20,9),F(-4,3)),
(F(1,4),F(3,4),F(0)),(F(1,4),F(11,4),F(-2)),(F(4,9),F(0),F(0)),
(F(4,9),F(16,9),F(-16,9)),(F(1),F(-8,9),F(0)),(F(1),F(-3,4),F(0)),
(F(1),F(1,4),F(-5,4)),(F(1),F(4,9),F(-4,3)),(F(1),F(5,4),F(-2))}

def dot(f,z): return F(f[0])*z[0]+F(f[1])*z[1]
def norm(z): return max(abs(dot(f,z)) for f in BASE)
def edge(i):
    a=V[i]; b=V[(i+1)%6]
    return a,(b[0]-a[0],b[1]-a[1])
def expr(f,i,k,sgn):
    xc,xd=edge(i); yc,yd=edge(k)
    return (dot(f,(xc[0]+sgn*yc[0],xc[1]+sgn*yc[1])),dot(f,xd),sgn*dot(f,yd))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def val(e,t,u): return e[0]+e[1]*t+e[2]*u

def support_inequalities(i,k,p,m):
    ep=expr(FORMS[p],i,k,1); em=expr(FORMS[m],i,k,-1)
    q=[]
    for j in range(6):
        q += [sub(ep,expr(FORMS[j],i,k,1)),sub(em,expr(FORMS[j],i,k,-1))]
    q += [(F(0),F(1),F(0)),(F(1),F(-1),F(0)),(F(0),F(0),F(1)),(F(1),F(0),F(-1))]
    return ep,em,q

def feasible_vertices_2d(ineq):
    pts=set()
    for a,b in combinations(ineq,2):
        d,e,f=a; g,h,j=b
        det=e*j-f*h
        if det==0: continue
        t=(-d*j+f*g)/det
        u=(-e*g+d*h)/det
        if all(val(q,t,u)>=0 for q in ineq): pts.add((t,u))
    return pts

def enumerate_pairs():
    out=set(); degenerate_feasible=0
    for i,k,p,m in product(range(6),repeat=4):
        ep,em,ineq=support_inequalities(i,k,p,m)
        eq=sub(ep,em); a,b,c=eq
        if eq==(0,0,0):
            if feasible_vertices_2d(ineq): degenerate_feasible += 1
            continue
        for h in ineq:
            d,e,f=h; det=b*f-c*e
            if det==0: continue
            t=((-a)*f-c*(-d))/det
            u=(b*(-d)-(-a)*e)/det
            if val(eq,t,u)==0 and all(val(q,t,u)>=0 for q in ineq):
                xc,xd=edge(i); yc,yd=edge(k)
                x=(xc[0]+t*xd[0],xc[1]+t*xd[1]); y=(yc[0]+u*yd[0],yc[1]+u*yd[1])
                out.add((x,y))
    assert degenerate_feasible==0
    return out

def polys_from_pairs(P):
    S=set()
    for x,y in P:
        assert norm(x)==norm(y)==1
        xp=(x[0]+y[0],x[1]+y[1]); xm=(x[0]-y[0],x[1]-y[1])
        assert norm(xp)==norm(xm)
        r=norm(xm)
        d=(x[0]-y[0],x[1]-y[1])
        for f in BASE:
            a=dot(f,y); b=dot(f,d)
            S.add((a*a,2*a*b+r*r,b*b-r*r))
    return S

def qval(p,x): return p[0]+p[1]*x+p[2]*x*x
def min_quad(p,a,b):
    vals=[qval(p,a),qval(p,b)]
    A=p[2]; B=p[1]
    if A>0:
        x=-B/(2*A)
        if a<=x<=b: vals.append(qval(p,x))
    return min(vals)

def check_envelope(polys):
    E0=(F(1),F(5,4),F(-2)); E1=(F(1,4),F(11,4),F(-2))
    for p in polys:
        d0=tuple(E0[i]-p[i] for i in range(3)); d1=tuple(E1[i]-p[i] for i in range(3))
        assert min_quad(d0,F(0),F(1,2))>=0
        assert min_quad(d1,F(1,2),F(1))>=0
    assert E0 in polys and E1 in polys
    x=(F(1),F(1,2)); y=(F(0),F(1)); d=(F(1),F(-1,2))
    assert norm(x)==norm(y)==1
    assert norm((x[0]+y[0],x[1]+y[1]))==norm(d)==F(3,2)
    for l in [F(0),F(1,10),F(1,3),F(1,2)]:
        z=(l*x[0]+(1-l)*y[0],l*x[1]+(1-l)*y[1])
        obj=norm(z)**2+l*(1-l)*norm(d)**2
        assert obj==qval(E0,l)
    return E0,E1

P=enumerate_pairs()
assert len(P)==48
S=polys_from_pairs(P)
assert S==EXPECTED_POLYS
E0,E1=check_envelope(S)
print('VERIFY_OK')
print('orthogonal_partition_vertices=',len(P))
print('candidate_quadratics=',len(S))
print('left_envelope=',E0)
print('right_envelope=',E1)
