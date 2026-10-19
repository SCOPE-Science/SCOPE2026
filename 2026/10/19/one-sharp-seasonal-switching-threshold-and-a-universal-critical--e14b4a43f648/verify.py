"""Numerical consistency checks for a two-season two-patch model.

Run with Python 3 and the standard library: python verify.py.
Numerical checks supplement, but do not prove, the analytic theorem.
"""
import math


def multiply(a, b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]))


def act(a, v):
    return (a[0][0]*v[0]+a[0][1]*v[1], a[1][0]*v[0]+a[1][1]*v[1])


def mat_exp_phase(t, r, d, h, sign):
    q = math.exp(sign*h)
    scale = math.exp(-d*t)
    ch, sh = math.cosh(r*t), math.sinh(r*t)
    return ((scale*ch, scale*sh*q), (scale*sh/q, scale*ch))


def phi(t, period, r, d, h):
    half = period/2
    if t <= half:
        return mat_exp_phase(t, r, d, h, 1)
    return multiply(mat_exp_phase(t-half, r, d, h, -1),
                    mat_exp_phase(half, r, d, h, 1))


def monodromy(period, r, d, h):
    return phi(period, period, r, d, h)


def lam(period, r, d, h):
    return -d+2/period*math.asinh(math.cosh(h)*math.sinh(r*period/2))


def perron(P):
    tr=P[0][0]+P[1][1]
    det=P[0][0]*P[1][1]-P[0][1]*P[1][0]
    discr=tr*tr-4*det
    assert discr>0
    mu=(tr+math.sqrt(discr))/2
    v=(P[0][1],mu-P[0][0])
    v=(v[0]/sum(v),v[1]/sum(v))
    assert min(v)>0
    return mu,v


def simpson_integral(period, r, d, h, v, N=1200):
    assert N % 2 == 0
    step=period/N
    res=0.0
    for i in range(N+1):
        w=1 if i in (0,N) else (4 if i%2 else 2)
        res+=w*sum(act(phi(i*step,period,r,d,h),v))
    return res*step/3


def rk4_period(u, period, r, d, h, kappa, steps_per_half=600):
    # Phase endpoints are integrated separately, so no RK stage spans a jump.
    v=list(u)
    dt=period/(2*steps_per_half)
    for sign in (1,-1):
        upper=r*math.exp(sign*h)
        lower=r*math.exp(-sign*h)
        def rhs(x):
            n=x[0]+x[1]
            return (-d*x[0]+upper*x[1]-kappa*n*x[0],
                    lower*x[0]-d*x[1]-kappa*n*x[1])
        for _ in range(steps_per_half):
            k1=rhs(v)
            k2=rhs((v[0]+dt*k1[0]/2,v[1]+dt*k1[1]/2))
            k3=rhs((v[0]+dt*k2[0]/2,v[1]+dt*k2[1]/2))
            k4=rhs((v[0]+dt*k3[0],v[1]+dt*k3[1]))
            v=[v[j]+dt*(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6 for j in (0,1)]
    return tuple(v)


def bisect_root(r, d, h, lo, hi):
    assert lam(lo,r,d,h)>0 and lam(hi,r,d,h)<0
    for _ in range(75):
        middle=(lo+hi)/2
        if lam(middle,r,d,h)>0:lo=middle
        else:hi=middle
    return (lo+hi)/2


def main():
    checked=0
    for r in (0.4,1.,1.8):
        for d in (0.5,1.125,2.5):
            for h in (0.15,math.log(2),1.2):
                for T in (0.15,0.8,2.,4.,8.):
                    P=monodromy(T,r,d,h)
                    mu,v=perron(P)
                    target=math.exp(T*lam(T,r,d,h))
                    assert abs(mu-target)<1e-9*max(1.,mu,target)
                    assert abs(P[0][0]*P[1][1]-P[0][1]*P[1][0]-math.exp(-2*d*T))<2e-12*(1+abs(P[0][0]*P[1][1])+abs(P[0][1]*P[1][0]))
                    assert max(abs(x-y) for x,y in zip(act(P,v),(mu*v[0],mu*v[1])))<2e-9*max(1.,mu)
                    checked+=1
    r,d,h,kappa=1.,9./8.,math.log(2.),0.7
    Tstar=bisect_root(r,d,h,2.,5.)
    assert 3.37661059<Tstar<3.37661061
    assert lam(2.,r,d,h)>0 and lam(5.,r,d,h)<0
    assert abs(lam(Tstar,r,d,h))<1e-14
    for T in (2.,5.,Tstar):
        P=monodromy(T,r,d,h)
        initial=(0.15,0.32)
        col0=simpson_integral(T,r,d,h,(1.,0.))
        col1=simpson_integral(T,r,d,h,(0.,1.))
        integral=col0*initial[0]+col1*initial[1]
        exact=tuple(x/(1+kappa*integral) for x in act(P,initial))
        numeric=rk4_period(initial,T,r,d,h,kappa)
        assert max(abs(exact[i]-numeric[i]) for i in (0,1))<3e-8
        checked+=1
        if T==2.:
            mu,v=perron(P)
            I=col0*v[0]+col1*v[1]
            level=(mu-1)/(kappa*I)
            attractor=(level*v[0],level*v[1])
            u=initial
            for _ in range(200):
                Iu=col0*u[0]+col1*u[1]
                u=tuple(x/(1+kappa*Iu) for x in act(P,u))
            assert max(abs(u[j]-attractor[j]) for j in (0,1))<1e-10
            checked+=1
        if T==Tstar:
            mu,v=perron(P)
            assert abs(mu-1)<1e-12
            I=col0*v[0]+col1*v[1]
            u=initial
            for _ in range(5000):
                Iu=col0*u[0]+col1*u[1]
                u=tuple(x/(1+kappa*Iu) for x in act(P,u))
            assert max(abs(5000*u[j]-v[j]/(kappa*I)) for j in (0,1))<1e-3
            checked+=1
    print('PASS:',checked,'matrix/periodic-flow checks; unique T* =',format(Tstar,'.12f'))
    print('Floquet exponent at T=2:',format(lam(2,r,d,h),'.12f'))
    print('Floquet exponent at T=5:',format(lam(5,r,d,h),'.12f'))

if __name__=='__main__':
    main()
