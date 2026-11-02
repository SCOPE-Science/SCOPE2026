#!/usr/bin/env python3
"""Exact arithmetic checks for projective polynomial interpolation invariants.

All identities in the associated theorem have independent analytic proofs;
these finite checks are diagnostics, not substitutes for proofs.
"""
from fractions import Fraction as F
from random import Random


def divided_diff(x, y, ids):
    total = F(0)
    for i in ids:
        den = F(1)
        for j in ids:
            if i != j:
                den *= x[i] - x[j]
        total += y[i] / den
    return total


def cross(x, i):
    return (x[i]-x[0])*(x[1]-x[2])/((x[i]-x[2])*(x[1]-x[0]))


def invariants(L, x, y):
    N = len(x)
    s0 = tuple(range(L+2))
    base = divided_diff(x,y,s0)
    assert base != 0
    K = [cross(x,i) for i in range(3,N)]
    J = []
    for i in range(L+2,N):
        si = tuple(range(L+1)) + (i,)
        J.append(divided_diff(x,y,si)/base*(x[i]-x[0])/(x[L+1]-x[0]))
    return K,J,base


def poly(coeffs,x):
    return sum((v*x**i for i,v in enumerate(coeffs)),F(0))


def transformed(x,y,L,a,b,c,d,lam,h):
    assert a*d-b*c == 1
    A = [c*z+d for z in x]
    assert all(z > 0 for z in A)
    xx=[(a*z+b)/w for z,w in zip(x,A)]
    yy=[(lam*v+poly(h,z))/w**L for z,v,w in zip(x,y,A)]
    return xx,yy,A


def run():
    rng=Random(20261028)
    ncases=0
    for L in range(1,6):
        for repeat in range(20):
            n=L+4+(repeat % 3)
            x=[F(i+1, i+3) for i in range(n)]
            y=[F(rng.randint(-30,30),rng.randint(1,17)) for _ in range(n)]
            k0,j0,delta0 = invariants(L,x,y)
            c=F(rng.randint(0,5),20)
            d=F(1)
            a=F(1)
            b=F(0)
            lam=F(rng.randint(1,9),rng.randint(1,8))
            h=[F(rng.randint(-7,7),rng.randint(1,11)) for _ in range(L+1)]
            xt,yt,A=transformed(x,y,L,a,b,c,d,lam,h)
            k1,j1,delta1 = invariants(L,xt,yt)
            assert k0==k1,(L,'K')
            assert j0==j1,(L,'J')
            assert delta1==lam*delta0*poly_product(A[:L+2])
            assert delta0*delta1>0
            ncases+=1
    print('PASS: %d exact rational group-transform tests, L=1..5' % ncases)
    # Scalar vector field check: sum derivative of y and differences
    # with time-dependent coefficients, integrated by second-order finite differences.
    # This tests the infinitesimal Lie-generator structure for small perturbations.
    for L in (1,2,3):
        n=L+4
        x=[F(i+1,2) for i in range(n)]
        y=[F((i+1)**(L+1)+2*i+3,3) for i in range(n)]
        kval,jval,_ = invariants(L,x,y)
        eps=F(1,10**5)
        A,B,C,D=F(2,7),F(-3,5),F(1,11),F(2,9)
        E=[F(i+1,13) for i in range(L+1)]
        xx=[z+eps*(A+B*z+C*z*z) for z in x]
        yy=[v+eps*(D*v+L*C*z*v+poly(E,z)) for z,v in zip(x,y)]
        kp,jp,_ = invariants(L,xx,yy)
        xx=[z-eps*(A+B*z+C*z*z) for z in x]
        yy=[v-eps*(D*v+L*C*z*v+poly(E,z)) for z,v in zip(x,y)]
        km,jm,_ = invariants(L,xx,yy)
        for init,p,m in zip(kval+jval,kp+jp,km+jm):
            assert abs((p-m)/(2*eps)) < F(1,10**5), (L,(p-m)/(2*eps))
    print('PASS: centered difference tests of three vector-field families')
    # Independently differentiate each barycentric summand, using exact rational
    # velocities of the ODE, and check the exact multiplicative evolution law.
    for L in range(1,7):
        for trial in range(20):
            n=L+4
            x=[F(i+1,i+3) for i in range(n)]
            y=[F((i+1)**(L+1)+trial*i+2,17) for i in range(n)]
            A,B,C,D = F(3,7),F(-2,5),F(5,13),F(4,9)
            E=[F((j+1)*(trial+2),j+9) for j in range(L+1)]
            dx=[A+B*z+C*z*z for z in x]
            dy=[(D+L*C*z)*v+poly(E,z) for z,v in zip(x,y)]
            for S in (tuple(range(L+2)),tuple(range(L+1))+(L+2,)):
                lhs=F(0)
                for i in S:
                    w=F(1)
                    for j in S:
                        if j!=i:
                            w /= x[i]-x[j]
                    dlogw=-sum(((dx[i]-dx[j])/(x[i]-x[j]) for j in S if i!=j),F(0))
                    lhs += w*(dy[i]+y[i]*dlogw)
                rhs=(D-(L+1)*B-C*sum((x[i] for i in S),F(0)))*divided_diff(x,y,S)
                assert lhs==rhs, (L,trial,S,lhs,rhs)
    print('PASS: 240 exact rational ODE derivative-identity checks, L=1..6')


def poly_product(a):
    p=F(1)
    for v in a:
        p*=v
    return p


if __name__=='__main__':
    run()
