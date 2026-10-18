"""Supplementary arithmetic and numerical checks of a rational two-step slow limit.

Python 3 standard library only. Numerical tests are not proof of an asymptotic theorem.
"""
from fractions import Fraction as F
from math import log


def Q(u, v, e):
    return u*u/(e*v*v + u*v + (1 + 3*e)*u*u)


def two(u, v, e):
    q = Q(u, v, e)
    return q, Q(v, q, e)


def slow(u):
    return (2*u-1)**3/(u*u-u+1)


def t_clock(u0, u1):
    d0, d1 = 2*u0-1, 2*u1-1
    return F(3,16)*(1/(d0*d0)-1/(d1*d1)) + F(1,8)*log(abs(d1/d0))


def check_exact():
    for u in (F(1,7), F(1,3), F(1,2), F(3,5), F(4,5), F(11,12)):
        v = 1-u
        # Differentiate each actual rational application at epsilon=0,
        # including the epsilon-dependence of the first intermediate state.
        dq = -(v*v+3*u*u)/(u+v)**2
        q0 = u/(u+v)
        dr = -(q0*q0+3*v*v)/(v+q0)**2 - v/(v+q0)**2*dq
        H1 = -(v*v+3*u*u)
        Hs = -u*(v*v+3*u*u)-u*u-3*v*v
        assert dq == H1 and dq+dr == Hs
        lam = u*v
        assert (H1 - u*Hs/(1-lam)) == slow(u)
        assert (1-lam)*(H1 - u*Hs/(1-lam)) == (2*u-1)**3
    # Analytic transverse eigenvalue from the displayed Jacobian.
    for u in (F(1,3), F(3,5), F(9,10)):
        v=1-u
        trace=v+u*(1+v)
        det=v*u*(1+v)-u*v*v
        assert trace == 1+u*v and det == u*v


def check_numerical():
    u0, u1=0.75,0.8
    target=t_clock(u0,u1)
    assert abs(target-0.251956861265911) < 1e-13
    residuals=[]
    for e in (0.002,0.0005,0.0001):
        u,v=u0,1-u0
        for j in range(50000):
            if u >= u1: break
            u,v=two(u,v,e)
        else: raise AssertionError('no crossing')
        residuals.append(abs(e*j-target))
    assert residuals[2]<0.002
    assert residuals[2]<residuals[1]<residuals[0]
    # Verify the equally important outward branch on the other side.
    u0,u1=0.25,0.20
    target_left=t_clock(u0,u1)
    errors=[]
    for e in (0.002,0.0005,0.0001):
        u,v=u0,1-u0
        for j in range(50000):
            if u <= u1: break
            u,v=two(u,v,e)
        else: raise AssertionError('left-side crossing absent')
        errors.append(abs(e*j-target_left))
    assert errors[-1]<errors[0] and errors[-1]<0.003
    print('left first-crossing residuals:', [round(z,8) for z in errors])
    print('first-crossing residuals:', [round(z,8) for z in residuals])
    print('target:',format(target,'.15f'))


if __name__=='__main__':
    check_exact()
    check_numerical()
    print('VERIFY_OK')
