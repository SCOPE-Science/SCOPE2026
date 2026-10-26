#!/usr/bin/env python3
"""Algebra and numerical branch-count checks for a saturable lossy dimer."""
import math
import random


def branch(s, j, loss, g, sign):
    return s * (2*g/(9-s*s) + sign*math.sqrt(j*j/(1-s*s)-loss*loss))


def deriv_minus(s, j, loss, g):
    x=s*s
    d=j*j-loss*loss
    b=(d + loss*loss*x*(2-x))/((1-x)**1.5*math.sqrt(d+loss*loss*x))
    return 2*g*(9+x)/(9-x)**2 - b


def root_monotone(f,lo,hi):
    a=f(lo); b=f(hi)
    assert a*b<=0,(lo,hi,a,b)
    for _ in range(90):
        mid=(lo+hi)*.5
        if f(mid)*a>0:
            lo=mid; a=f(mid)
        else: hi=mid
    return (lo+hi)*.5


def intervals_roots(func, value, grid=1800):
    out=[]
    pts=[-0.999999 + 1.999998*i/grid for i in range(grid+1)]
    fa=func(pts[0])-value
    for a,b in zip(pts[:-1],pts[1:]):
        fb=func(b)-value
        if abs(fa)<1e-12 and not any(abs(t-a)<1e-7 for t in out): out.append(a)
        if fa*fb<0:
            r=root_monotone(lambda s:func(s)-value,a,b)
            if not any(abs(t-r)<1e-7 for t in out):out.append(r)
        fa=fb
    return out


def numerical():
    random.seed(7)
    for _ in range(100):
        J=random.uniform(.6,3.3)
        Gamma=J*random.uniform(.02,.94)
        Delta=math.sqrt(J*J-Gamma*Gamma)
        gcrit=4.5*Delta
        g=gcrit*random.uniform(.2,2.5)
        D=random.uniform(-1,1)*2*J
        sp=intervals_roots(lambda s:branch(s,J,Gamma,g,1),D)
        sm=intervals_roots(lambda s:branch(s,J,Gamma,g,-1),D)
        assert len(sp)==1 and len(sm) in (1,3), (J,Gamma,g,D,len(sp),len(sm))
        if g<=gcrit: assert len(sm)==1
        for sign,roots in ((1,sp),(-1,sm)):
            for s in roots:
                ss=math.sqrt(1-s*s)
                sn=Gamma*ss/J
                cs=sign*math.sqrt(1-sn*sn)
                # gauge psi1 positive; reconstruct eigensystem directly
                z1=math.sqrt((1+s)/2)
                z2=math.sqrt((1-s)/2)*complex(cs,sn)
                mu=D-2j*Gamma+2*g/(3+s)+J*z2/z1
                other=J*z1/z2-D+2*g/(3-s)
                assert abs(mu-other)<1e-8,(mu,other)
                assert abs((abs(z1)**2+abs(z2)**2)-1)<1e-10
    print('PASS: 100 random parameter/detuning samples; nonlinear eigensystem reconstructed.')
    for J,Gamma in ((1,.4), (2,1.7), (.8,.3)):
        Delta=math.sqrt(J*J-Gamma*Gamma)
        gc=4.5*Delta
        c=8/(27*math.sqrt(3))*math.sqrt(Delta/(7*J*J+2*Gamma*Gamma))
        for eps in (1e-2,1e-3,1e-4):
            g=gc+eps
            sstar=root_monotone(lambda s:deriv_minus(s,J,Gamma,g),0,0.9999)
            fold=branch(sstar,J,Gamma,g,-1)
            assert abs(fold/(c*eps**1.5)-1)<.02,(J,Gamma,eps,fold,c*eps**1.5)
        for g in (gc*.6, gc, gc*1.5):
            roots=intervals_roots(lambda s:branch(s,J,Gamma,g,-1),0)
            assert len(roots)== (3 if g>gc else 1)
    print('PASS: fold uniqueness, cusp 3/2 law, and threshold mode counts.')


def symbolic():
    import sympy as S
    x,u=S.symbols('x u',positive=True)
    B=(1+u*x*(2-x))/((1-x)**S.Rational(3,2)*S.sqrt(1+u*x))
    L=(u+1)*(u*x*x+2*u*x+3)/(2*(1-x)*(1+u*x)*(1+u*x*(2-x)))
    assert S.simplify(S.diff(S.log(B),x)-L)==0
    positivity=S.expand((u+1)*(u*x*x+2*u*x+3)-(1+u*x)*(1+u*x*(2-x)))
    assert S.simplify(positivity-(u*u*x*(x*x-x+2)+u*(2*x*x-x+3)+2))==0
    s,J,G,g=S.symbols('s J G g',positive=True)
    Delta=S.symbols('Delta',positive=True)
    expr=s*(2*g/(9-s*s)-S.sqrt(J*J/(1-s*s)-G*G))
    gcrit=S.Rational(9,2)*Delta
    ex=S.series(expr.subs(g,gcrit).subs(J*J,G*G+Delta*Delta),s,0,6).removeO().expand()
    assert S.simplify(ex.coeff(s,1))==0
    assert S.simplify(ex.coeff(s,3)+(7*J*J+2*G*G)/(18*Delta)).subs(J*J,G*G+Delta*Delta)==0
    print('PASS: exact derivative monotonicity identity and cubic normal form.')

if __name__=='__main__':
    symbolic()
    numerical()
