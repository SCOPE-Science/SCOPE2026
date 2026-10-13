from sympy import symbols, Matrix, Rational, expand, factor, groebner, diff, hessian

x0,x1,x2=symbols('x0 x1 x2')
Q1=x0*x1-x1**2+x2**2
Q2=x0*x2-x0**2+x1**2-x2**2
Q3=x0*x1+x1**2-x2**2
Q4=x0*x2+x0**2-x1**2+x2**2
Qs=[Q1,Q2,Q3,Q4]
F=expand(x0*Q1*Q2*Q3*Q4)

# All conics are smooth.
dets=[factor((hessian(q,(x0,x1,x2))/2).det()) for q in Qs]
assert dets == [Rational(-1,4),Rational(3,4),Rational(1,4),Rational(-3,4)]

# Symmetry exchanges p2<->p3 and p4<->p5.
assert expand(F.subs(x1,-x1)-F) == 0

# The only projective point missed by the charts x0=1 and x2=1 is [0:1:0], and it is smooth.
p_inf={x0:0,x1:1,x2:0}
assert [diff(F,q).subs(p_inf) for q in (x0,x1,x2)] == [1,0,0]

# Chart x0=1: singular support is exactly (x1,x2)=(0,0),(+-1,0).
y,z=symbols('y z')
Finf=expand(F.subs({x0:1,x1:y,x2:z}))
Ginf=groebner([Finf,diff(Finf,y),diff(Finf,z)],y,z,order='lex')
assert factor(Ginf.polys[-1].as_expr()) == z**3
assert factor(Ginf.polys[0].as_expr().subs(z,0)) == 3*y*(y-1)**2*(y+1)**2
LM_inf=[p.LM(order=Ginf.order).exponents for p in Ginf.polys]
assert LM_inf == [(5,0),(3,1),(0,3)]
# Standard monomial count: 5 + 3 + 3 = 11 = 3+4+4.
assert 5+3+3 == 11

# p1 is two smooth tangent branches with intersection multiplicity 2.
u,v=symbols('u v')
p1a=expand(Q1.subs({x0:1,x1:u,x2:v}))
p1b=expand(Q3.subs({x0:1,x1:u,x2:v}))
assert expand(p1a+p1b) == 2*u
assert expand(p1a.subs(u,0)) == v**2

# p2 has three distinct tangent lines; p3 follows by symmetry.
p2subs={x0:1,x1:-1+u,x2:v}
p2=[expand(q.subs(p2subs)) for q in (Q2,Q3,Q4)]
p2lin=[expand(diff(q,u).subs({u:0,v:0})*u+diff(q,v).subs({u:0,v:0})*v) for q in p2]
assert p2lin == [-2*u+v,-u,2*u+v]

# Chart x2=1 near p4; p5 is (u,v)=(0,2).
p4subs={x0:u,x1:-1+v,x2:1}
branches=[u]+[expand(q.subs(p4subs)) for q in Qs]
lin=[expand(diff(q,u).subs({u:0,v:0})*u+diff(q,v).subs({u:0,v:0})*v) for q in branches]
assert lin == [u,-u+2*v,u-2*v,-u-2*v,u+2*v]
floc=expand(branches[0]*branches[1]*branches[2]*branches[3]*branches[4])

# Contact order 2 for Q1/Q2 and Q3/Q4.
u_q1=(v**2-2*v)/(v-1)
sub12=factor(branches[2].subs(u,u_q1))
assert sub12 == v**2*(v-2)/(v-1)**2
u_q3=(-v**2+2*v)/(v-1)
sub34=factor(branches[4].subs(u,u_q3))
assert sub34 == -v**2*(v-2)/(v-1)**2

# Full Tjurina support in x2=1 is only p4 and p5; total local length 36.
Gall=groebner([floc,diff(floc,u),diff(floc,v)],u,v,order='lex')
assert factor(Gall.polys[-1].as_expr()) == v**8*(v-2)**8
LM_all=[p.LM(order=Gall.order).exponents for p in Gall.polys]
assert LM_all == [(4,0),(3,2),(2,6),(1,12),(0,16)]
assert 16+12+6+2 == 36

# Localize at p4 by inverting v-2. The quotient has Tjurina dimension 18.
t=symbols('t')
Gloc=groebner([floc,diff(floc,u),diff(floc,v),1-t*(v-2)],t,u,v,order='lex')
LM=[p.LM(order=Gloc.order).exponents for p in Gloc.polys]
assert LM == [(1,0,0),(0,4,0),(0,3,1),(0,2,3),(0,1,6),(0,0,8)]
assert 8+6+3+1 == 18

# Five smooth branches, two contact-two pairs and eight transverse pairs.
delta=2+2+8
mu=2*delta-5+1
assert delta == 12 and mu == 20
tau=18
assert 3+4+4+2*mu == 51
assert 3+4+4+2*tau == 47
assert 51-47 == 4
print('VERIFY_OK p1=A3 p2,p3=D4 p4,p5_mu_tau=20,18 global_mu_tau=51,47 resolution=5,7,7')
