"""Standalone checks for the critical two-group SIQS endemic asymptotics.

Requires only Python 3 standard library. All scientific assertions are checked
against the explicit stationary equations; finite checks do not prove the limit.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext

for k in (3, 7, 64, 512, 4096, 65536, 10**6):
    e = F(1, k)
    m11, m12 = 1 + 2*e, 2*(1-e)
    m21, m22 = F(2,3)*e, 1-F(2,3)*e
    assert m11*m22 - m12*m21 == 1
    assert m11 + m22 == 2 + F(4,3)*e

with localcontext() as ctx:
    ctx.prec = 75
    one = D(1)
    third = one / D(3)
    R, s = D(3), one/D(3)
    B, C, delta = D(2), D(2)/D(3), D(2)/D(3)
    U0 = (B*B*C) ** third
    W0 = (B*C*C) ** third
    assert abs(U0*U0-B*W0) < D('1e-65')
    assert abs(W0*W0-C*U0) < D('1e-65')
    for k in (64,512,4096,65536,10**6):
        e = one/D(k)
        t = e**third
        u,w = U0*t,W0*t*t
        for iteration in range(40):
            f1 = u*u/(1-u)-D(2)*e*u-B*(1-e)*w
            f2 = w*w/(1-w)+delta*e*w-C*e*u
            a = (D(2)*u-u*u)/(1-u)**2-D(2)*e
            b = -B*(1-e)
            c = -C*e
            d = (D(2)*w-w*w)/(1-w)**2+delta*e
            jac = a*d-b*c
            du = (f1*d-b*f2)/jac
            dw = (a*f2-c*f1)/jac
            u,w = u-du,w-dw
            assert 0<u<1 and 0<w<1
            if max(abs(du),abs(dw))<D('1e-65'):
                break
        else:
            raise AssertionError('Newton iteration did not converge')
        # Check the *original six differential stationarity residuals*.
        hn=hv=D(3)/D(4)
        lam=one; beta=tau=one/D(4)
        theta=one/D(3)
        xn=e*u; xv=(1-e)*w
        in_=hn*beta/(beta+tau)*xn
        iv=hv*beta/(beta+tau)*xv
        qn=xn-in_; qv=xv-iv
        sn=e-xn; sv=(1-e)-xv
        hazard_n=D(2)*lam*((theta/e+1-theta)*in_+(1-theta)*iv)
        hazard_v=D(2)*lam*s*((1-theta)*in_+(theta/(1-e)+1-theta)*iv)
        res=[-hazard_n*sn+beta*xn,
             hn*hazard_n*sn-(beta+tau)*in_,
             (1-hn)*hazard_n*sn+tau*in_-beta*qn,
             -hazard_v*sv+beta*xv,
             hv*hazard_v*sv-(beta+tau)*iv,
             (1-hv)*hazard_v*sv+tau*iv-beta*qv]
        assert max(abs(x) for x in res)<D('1e-60')
        rho=(D(2)+D(4)*e/D(3)+((D(2)+D(4)*e/D(3))**2-D(4)).sqrt())/D(2)
        assert rho>1
        print('epsilon=',str(e),'scaled_nonvacc=',str(u/t),
              'scaled_vacc=',str(w/(t*t)), 'max_six_ODE_residual=',
              str(max(abs(x) for x in res)))
    print('limiting_constants=',str(U0),str(W0))
print('CHECK_OK')
