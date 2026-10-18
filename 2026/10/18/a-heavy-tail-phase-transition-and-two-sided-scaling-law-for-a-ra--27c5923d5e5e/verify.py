#!/usr/bin/env python3
"""Exact algebra and diagnostic checks for an invariant-law tail transition.
Requires sympy; numerical diagnostics use Python standard library.
"""
import math
import sympy as sp

P,u,v=sp.symbols('P u v',real=True)
q=sp.sqrt(15)
c=sp.Rational(1,4);s=q/4
D=P+2*u
X=(10*P+5*u-q*v)/(4*D)
Y=(2*P+u-q*v)/(2*D)
u1=c*u-s*v;v1=s*u+c*v
D1=P+2*u1
X1=(10*P+5*u1-q*v1)/(4*D1)
Y1=(2*P+u1-q*v1)/(2*D1)
FX=(sp.Rational(3,2)*X-sp.Rational(5,4))/Y
FY=(X-sp.Rational(3,2))/Y
assert sp.simplify(FX-X1)==0
assert sp.simplify(FY-Y1)==0
H=sp.Matrix([[1,sp.Rational(-7,4),-q/4],[1,sp.Rational(1,2),-q/2],[1,2,0]])
assert sp.simplify(H.det())!=0
assert sp.expand(u1**2+v1**2-(u**2+v**2)).simplify()==0
# Pole vectors: N=(D*X,D*Y), at cos t=-P/2, sin t=v.
Np=(sp.simplify(D*X),sp.simplify(D*Y))
Npole=(sp.simplify(Np[0].subs(u,-P/2)),sp.simplify(Np[1].subs(u,-P/2)))
assert Npole == (sp.Rational(15,8)*P-q*v/4, sp.Rational(3,4)*P-q*v/2)
A2=sp.simplify((Npole[0]**2+Npole[1]**2).subs({P:2,v:0}))
assert A2==sp.Rational(261,16)
# At P=0 the image is an invariant straight line, with exact Cauchy law.
assert sp.simplify((Y-2*X+1).subs(P,0))==0
# Small delta expansion at the critical pole t=pi+sqrt(delta)*z.
e,z=sp.symbols('e z',real=True,positive=True)
for sign in [-1,1]:
    pp=2+sign*e
    # cos(pi+sqrt(e)*z)=-cos(sqrt(e)*z)
    ds=pp-2*sp.cos(sp.sqrt(e)*z)
    assert sp.simplify(sp.limit(ds/e,e,0)-(sign+z**2))==0
print('EXACT_IDENTITY_OK; H_det=',H.det(),'critical_pole_squared_norm=',A2)

# Independent numerical checks of the high-radius exceedance probability.
# At fixed P and R, angle intervals are determined by roots of
# ||numerator(t)||^2 - R^2*denominator(t)^2, so measure is computed by
# high-resolution sign-bracket scanning plus bisection (no random sampling).
def components_mass(P0,R,mesh=30000):
    def g(t):
        d=P0+2*math.cos(t)
        nx=(10*P0+5*math.cos(t)-math.sqrt(15)*math.sin(t))/4
        ny=(2*P0+math.cos(t)-math.sqrt(15)*math.sin(t))/2
        return (nx*nx+ny*ny)-(R*d)**2
    n=mesh
    roots=[]
    a=0.0;fa=g(a)
    for j in range(1,n+1):
        b=2*math.pi*j/n;fb=g(b)
        if (fa>0)!=(fb>0):
            l=a;rr=b
            for _ in range(60):
                m=(l+rr)/2
                if (g(m)>0)==(fa>0):l=m
                else:rr=m
            roots.append((l+rr)/2)
        a=b;fa=fb
    points=[0]+roots+[2*math.pi]
    total=sum(bb-aa for aa,bb in zip(points,points[1:]) if g((aa+bb)/2)>0)
    return total/(2*math.pi),len(roots)

A=math.sqrt(261)/4
for xi in [0.4,1.7,4.0]:
    for sign in [-1,1]:
        delta=1e-3; p=2+sign*delta;R=A*xi/delta
        prob,k=components_mass(p,R)
        if sign==-1:
            pred=math.sqrt(delta)/math.pi*(math.sqrt(1+1/xi)-math.sqrt(max(0,1-1/xi)))
        else:
            pred=math.sqrt(delta)/math.pi*math.sqrt(max(0,1/xi-1))
        # 1e-3 is not asymptotic infinitesimal; allow <= 5% relative errors.
        if pred>0: assert abs(prob/pred-1)<0.06,(p,xi,prob,pred,k)
        else:assert prob<0.0005,(p,xi,prob,pred,k)
        print(f'CROSSOVER_TEST p={p:.3f} xi={xi:g} measured={prob:.8g} approx={pred:.8g} roots={k}')
print('VERIFY_OK')
