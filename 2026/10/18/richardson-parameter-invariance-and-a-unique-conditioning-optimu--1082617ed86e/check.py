"""Exact arithmetic and condition-number checks for a two-column residual coarse space.

Run with Python 3.9 or newer: python check.py
Uses only the standard library.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def mm(A,v):
    return [dot(row,v) for row in A]


def add(u,v,c=1):
    return [x+c*y for x,y in zip(u,v)]


def scale(c,u):
    return [c*x for x in u]


def solve2(M,v):
    (a,b),(c,d)=M
    t=a*d-b*c
    if not t:
        raise ValueError('Dependent columns')
    return [(d*v[0]-b*v[1])/t, (a*v[1]-c*v[0])/t]


def condition2(trace, det):
    tr=float(trace); de=float(det)
    disc=max(0.0,tr*tr-4*de)
    return (tr+sqrt(disc))**2/(4*de)


def run_case(A,r,omegas):
    a=mm(A,r); b=mm(A,a)
    u=dot(a,a); v=dot(a,b); w=dot(b,b)
    delta=u*w-v*v
    assert delta>0
    gr=solve2(((u,v),(v,w)),(dot(a,r),dot(b,r)))
    gm=add(scale(gr[0],r),scale(gr[1],a))
    cnt=0
    for omega in omegas:
        p=scale(omega,r)
        q=add(p, a, -omega*omega)
        Ap=mm(A,p); Aq=mm(A,q)
        pre=add(r,a,-omega)
        # pre above is r - omega*A*r, the presmoothed residual
        M=((dot(Ap,Ap),dot(Ap,Aq)),(dot(Ap,Aq),dot(Aq,Aq)))
        rhs=(dot(Ap,pre),dot(Aq,pre))
        t1,t2=solve2(M,rhs)
        new=add(add(scale(omega,r),scale(t1,p)),scale(t2,q))
        assert new==gm, (A,r,omega,new,gm)
        assert M[0][0]==omega**2*u
        assert M[0][1]==omega**2*(u-omega*v)
        assert M[1][1]==omega**2*(u-2*omega*v+omega*omega*w)
        determinant=M[0][0]*M[1][1]-M[0][1]**2
        assert determinant==omega**6*delta
        assert (M[0][0]+M[1][1])==omega**2*(2*u-2*omega*v+omega**2*w)
        cnt+=6
    optimal=sqrt(float(2*u/w))
    s=lambda z: (2*float(u)/z-2*float(v)+z*float(w))/sqrt(float(delta))
    assert s(optimal)<s(0.999*optimal)
    assert s(optimal)<s(1.001*optimal)
    assert isclose(s(optimal),2*(sqrt(float(2*u*w))-float(v))/sqrt(float(delta)),rel_tol=1e-12)
    for small in (F(1,100), F(1,1000), F(1,10000)):
        om=float(small)
        # Avoid catastrophic floating point cancellation in determinant: use exact identity.
        tr=small**2*(2*u-2*small*v+small**2*w)
        det=small**6*delta
        calculated=condition2(tr,det)
        expected=float(4*u*u/delta)/om**2
        assert abs(calculated/expected-1)<10*om*float(abs(v/u)+1)
    cnt+=6
    return cnt


def main():
    cases=[
      ([[F(1),F(0),F(0)],[F(0),F(2),F(0)],[F(0),F(0),F(4)]],[F(1),F(1),F(1)]),
      ([[F(2),F(1),F(0)],[F(0),F(3),F(1)],[F(0),F(0),F(5)]],[F(1),F(-1),F(2)]),
      ([[F(1),F(1),F(0)],[F(0),F(2),F(2)],[F(1),F(0),F(5)]],[F(3),F(2),F(-1)])
    ]
    for p in range(1,21):
        A=[[F(1+p),F(1),F(0)],[F(0),F(2+p),F(1)],[F(0),F(0),F(4+p)]]
        r=[F(p),F(-1),F(1)]
        cases.append((A,r))
    test_steps=(F(1,20),F(1,10),F(1,5),F(1,4),F(1,3),F(2,5),F(1,2),F(3,4))
    checks=sum(run_case(A,r,test_steps) for A,r in cases)
    print(f'PASS: {checks} rational identity and numerical conditioning assertions across {len(cases)} matrices')
    u,v,w=F(21),F(73),F(273)
    assert u*w-v*v==404
    assert 2*u/w==F(2,13)
    print('Diagnostic: A=diag(1,2,4), r=(1,1,1): u=21, v=73, w=273, Delta=404, omega_star=sqrt(2/13).')

if __name__=='__main__':
    main()
