#!/usr/bin/env python3
import sympy as sp

x,y,t,z=sp.symbols('x y t z')
g=x**2+x*y-y**2+x-y
h=sp.expand(x*y*(x-y)*g)
assert sp.diff(g,x).subs({x:0,y:0})==1
assert sp.diff(g,y).subs({x:0,y:0})==-1

# Intersection multiplicities at the origin for the three line branches against g.
def ord0(poly,var):
    P=sp.Poly(sp.expand(poly),var,domain=sp.QQ)
    return min(k[0] for k,c in P.terms() if c)
assert ord0(g.subs(x,0),y)==1
assert ord0(g.subs(y,0),x)==1
assert ord0(g.subs(y,x),x)==2
contacts=[1,1,1,1,1,2]
delta=sum(contacts)
mu=2*delta-4+1
assert delta==7 and mu==11

# The reduced curve h=0 has only (0,0),(-1,0),(0,-1) as singular component intersections.
# q vanishes at the latter two and is a unit at the origin.
q=(x+1)*(y+1)
assert q.subs({x:0,y:0})==1
assert q.subs({x:-1,y:0})==0
assert q.subs({x:0,y:-1})==0

hx,hy=sp.diff(h,x),sp.diff(h,y)
G=sp.groebner([h,hx,hy,1-t*q],t,x,y,order='lex',domain=sp.QQ)
elim=[sp.Poly(p.as_expr(),x,y,domain=sp.QQ) for p in G.polys if not p.as_expr().has(t)]
# Recompute reduced lex GB in x>y after elimination.
L=sp.groebner([p.as_expr() for p in elim],x,y,order='lex',domain=sp.QQ)
LM=[p.LM(order=L.order).exponents for p in L.polys]
assert LM==[(3,0),(2,1),(1,3),(0,6)], LM
std=[]
for a in range(6):
    for b in range(6):
        if not any(a>=i and b>=j for i,j in LM):
            std.append((a,b))
expected={(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,0),(1,1),(1,2),(2,0)}
assert set(std)==expected, std
assert len(std)==10

# Resolution data and A'Campo polynomial consistency.
N1=4
N2=N1+1+1
assert N2==6
T=sp.symbols('T')
Delta=sp.expand((T-1)*(T**4-1)*(T**6-1))
assert sp.Poly(Delta,T).degree()==11
# (T-1)^3 divides, but fourth power does not: four branches => multiplicity r-1=3.
assert sp.rem(Delta,(T-1)**3,T)==0
assert sp.rem(Delta,(T-1)**4,T)!=0
print('VERIFY_OK')
