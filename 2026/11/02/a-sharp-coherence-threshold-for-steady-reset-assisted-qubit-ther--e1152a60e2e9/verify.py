"""Reproduce algebraic and numerical checks for the coherent-reset qubit theorem.

Only Python's standard library is needed. Finite tests are not the analytic proof.
"""
from fractions import Fraction as Q
from math import exp, log, sqrt, isclose
from random import Random


def exact_qfi(x, s, kappa, a, t):
    """QFI at omega=1; all arguments may be rational Fractions.

    t is squared transverse Bloch length, not elapsed time.
    """
    A = s*a-Q(1)
    B = Q(1)+s
    den_z = Q(2)+B*x
    z = A*x/den_z
    dz = Q(2)*(Q(1)+x)*A/den_z**2
    u = Q(1)+(s+Q(1, 2))*x
    den_w = u*u+(kappa*x)**2
    w2 = s*s*t*x*x/den_w
    dw2 = s*s*t*(Q(1)+x)**2/den_w**2
    cross = s*s*t*x*(Q(1)+x)*u/den_w**2
    return dz*dz+dw2+(z*dz+cross)**2/(Q(1)-z*z-w2)


def state(beta, s, kappa, a, wc):
    x = exp(beta)-1.0  # omega=gamma=1, so s=r and kappa=1 in beta tests
    A=s*a-1.0
    z=A*x/(2.0+(1+s)*x)
    w=s*wc*x/(1.0+(s+0.5+1j*kappa)*x)
    return z,w


def analytic_derivative(beta, s, kappa, a, wc):
    x=exp(beta)-1.0
    A=s*a-1.0
    dz=2.0*(1+x)*A/(2.0+(1+s)*x)**2
    dw=s*wc*(1+x)/(1.0+(s+0.5+1j*kappa)*x)**2
    return dz,dw


def float_qfi(beta, s, kappa, a, wc):
    z,w=state(beta,s,kappa,a,wc)
    dz,dw=analytic_derivative(beta,s,kappa,a,wc)
    dot=z*dz+(w.conjugate()*dw).real
    return dz*dz+abs(dw)**2+dot*dot/(1-z*z-abs(w)**2)


def opta(beta,s,kappa):
    lo,hi=-1.0,1.0
    for _ in range(110):
        a=lo+(hi-lo)/3
        b=hi-(hi-lo)/3
        va=float_qfi(beta,s,kappa,a,sqrt(max(0,1-a*a)))
        vb=float_qfi(beta,s,kappa,b,sqrt(max(0,1-b*b)))
        if va<vb: lo=a
        else: hi=b
    return (lo+hi)/2


def run():
    count=0
    x=Q(1,5); s=Q(2); k=Q(1)
    fg=exact_qfi(x,s,k,Q(-1),Q(0)); fe=exact_qfi(x,s,k,Q(1),Q(0))
    fc=exact_qfi(x,s,k,Q(-1,2),Q(3,4))
    assert fg==Q(405,338); count+=1
    assert fe==Q(150,1183); count+=1
    assert fc==Q(11574741702400,8063279547193); count+=1
    assert fc-fg==Q(3826239519515,16126559094386)>0; count+=1
    assert fg>fe; count+=1

    rng=Random(28072026)
    for j in range(1200):
        beta=rng.uniform(.04,2.0)
        r=rng.uniform(.02,8.0)
        a=rng.uniform(-1,1)
        wlen=sqrt(max(0,1-a*a))*rng.uniform(0,1)
        phi=rng.uniform(-3.14,3.14)
        wc=complex(wlen*__import__('math').cos(phi),wlen*__import__('math').sin(phi))
        z,w=state(beta,r,1.0,a,wc)
        Gamma=(exp(beta)+1)/(exp(beta)-1)
        # Direct stationary population/coherence equations.
        assert abs((Gamma+r)*z-r*a+1)<4e-12; count+=1
        assert abs((Gamma/2+r+1j)*w-r*wc)<4e-12; count+=1
        assert z*z+abs(w)**2<1; count+=1
        h=1e-5
        zp,wp=state(beta+h,r,1.,a,wc)
        zm,wm=state(beta-h,r,1.,a,wc)
        dz,dw=analytic_derivative(beta,r,1.,a,wc)
        assert abs((zp-zm)/(2*h)-dz)<4e-7; count+=1
        assert abs((wp-wm)/(2*h)-dw)<4e-7; count+=1
        qfi=float_qfi(beta,r,1.,a,wc)
        assert qfi>=0; count+=1
    # Uniform small-beta boundary optimizer and first correction to transition.
    for r in [0.15,0.25,0.4,0.7,1.5,4.0]:
        a=opta(1e-6,r,1.0)
        target=-1.0 if r<=1.0/3 else -1/(3*r)
        assert abs(a-target)<1e-3,(r,a,target)
        count+=1
        fa=float_qfi(1e-6,r,1.,a,sqrt(max(0,1-a*a)))
        expect=(1+r)**2/4 if r<=1/3 else r*r+1/3
        assert abs(fa-expect)<1e-3,(r,fa,expect)
        count+=1
    for delta in [.003,.005,.01]:
        from math import log
        # Find the sign boundary of the derivative of the pure-target objective at a=-1.
        beta=log(1+delta)
        def d_boundary(r):
            h=2e-5
            return (float_qfi(beta,r,1.0,-1+h,sqrt(1-(-1+h)**2))
                    -float_qfi(beta,r,1.0,-1.0,0.0))/h
        lo,hi=.30,.40
        for _ in range(36):
            m=(lo+hi)/2
            if d_boundary(m)>0: hi=m
            else: lo=m
        critical=(lo+hi)/2
        predicted=1/3+8*delta/27
        assert abs(critical-predicted)<.00015,(delta,critical,predicted)
        count+=1
    print('PASS',count,'finite assertions; exact witness and asymptotic phase law corroborated')


if __name__=='__main__':
    run()
