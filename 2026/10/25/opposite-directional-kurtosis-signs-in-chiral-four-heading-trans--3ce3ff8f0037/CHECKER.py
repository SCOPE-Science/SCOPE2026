#!/usr/bin/env python3
"""Exact independent checks for biased right-angle velocity-jump motion.

Four cardinal velocities, clockwise and counterclockwise Poisson turns.
Requires sympy. No randomized tests or asymptotic-fit assumptions.
"""
import sympy as S
N=0
def check(expr,label):
    global N
    if not expr: raise AssertionError(label)
    N+=1

def equal(x,y,label):
    check(S.cancel(x-y)==0,label)

a,b,v,x,y=S.symbols('a b v x y')
s=a+b; d=a-b; R=s*s+d*d
c2=v*v*s*(x*x+y*y)/(2*R)
c4=v**4*(s*(3*d*d-s*s)*(x*x+y*y)**2/R**3-4*x*x*y*y/(s*R))/8
# Angular / radial contractions from the complete homogeneous quartic.
Kx=24*c4.subs({x:1,y:0})
Ky=24*c4.subs({x:0,y:1})
Kxy=4*S.Poly(c4,x,y).coeff_monomial(x*x*y*y)
kr=Kx+Ky+2*Kxy
kr_expected=4*v**4*(4*s*s*d*d-3*s**4-d**4)/(s*R**3)
equal(Kx,Ky,'square axes symmetry')
equal(kr,kr_expected,'radial fourth-cumulant expression')
equal(24*c4.subs({x:1/S.sqrt(2),y:1/S.sqrt(2)}),3*v**4*(s*(3*d*d-s*s)/R**3-1/(s*R)),'diagonal projection')
ss,chi=S.symbols('ss chi')
rad_chi=4*v**4*(4*ss**2*(chi*ss)**2-3*ss**4-(chi*ss)**4)/(ss*(ss**2+(chi*ss)**2)**3)
equal(rad_chi,-4*v**4*(1-chi**2)*(3-chi**2)/(ss**3*(1+chi**2)**3),'negative radial factorization')

# Independently reconstruct the cumulant coefficients from the tilted
# eigenvector Poisson recursion, not from the characteristic determinant.
for aa,bb in [(1,1),(3,1),(4,1),(1,4),(9,1),(2,7)]:
    A,B=S.Integer(aa),S.Integer(bb)
    Q=S.zeros(4)
    for j in range(4):
        Q[j,j]=-(A+B)
        Q[j,(j+1)%4]+=A
        Q[j,(j-1)%4]+=B
    pi=S.ones(1,4)/4
    proj=S.ones(4,1)*pi
    inverse=(Q+proj).inv()
    for X,Y in [(S.Integer(1),S.Integer(0)),(S.Integer(1),S.Integer(1)),(S.Rational(3,5),S.Rational(4,5))]:
        vv=S.Rational(5,3)
        V=S.diag(vv*X,vv*Y,-vv*X,-vv*Y)
        rs=[S.ones(4,1)]
        ls=[S.Integer(0)]
        for n in range(1,5):
            ln=(pi*V*rs[n-1])[0]
            ls.append(ln)
            rhs=ln*rs[0]-V*rs[n-1]
            for j in range(1,n): rhs+=ls[j]*rs[n-j]
            rn=inverse*rhs
            equal((pi*rn)[0],0,'mean-zero Poisson solution')
            check(Q*rn==rhs,'Poisson equation')
            rs.append(rn)
        equal(ls[1],0,'first odd coefficient')
        equal(ls[3],0,'third odd coefficient')
        params={a:A,b:B,v:vv,x:X,y:Y}
        equal(ls[2],c2.subs(params),'quadratic cumulant rate')
        equal(ls[4],c4.subs(params),'quartic cumulant rate')

# Exact sign boundaries and coexistence, not used to infer the infinite claim.
for aa,bb,positive in [(1,1,False),(3,1,False),(4,1,True),(9,1,True),(1,9,True)]:
    params={a:aa,b:bb,v:1}
    check(bool((Kx.subs(params)>0))==positive,'coordinate rate sign')
    check(bool((24*c4.subs({**params,x:1/S.sqrt(2),y:1/S.sqrt(2)})<0)),'diagonal negative')
    check(bool(kr.subs(params)<0),'radial negative')

critical=2+S.sqrt(3)
check(S.simplify(Kx.subs({a:critical,b:1,v:1}))==0,'sharp threshold')
print(f'PASS: {N} exact algebraic and independent Poisson-recursion checks')
