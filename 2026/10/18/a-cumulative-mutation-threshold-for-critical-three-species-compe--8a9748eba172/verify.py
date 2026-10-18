"""Independent finite checks for a cumulative-mutation theorem in cyclic competition.

Run with Python 3, no third-party dependencies. Finite tests support but do not prove
asymptotic claims, which require the analytical argument.
"""
from fractions import Fraction as Q
from math import log, exp, sqrt, isclose


def rhs_m(m, a, b, mu):
    x,y,z = m
    return (x*(1-x-a*y-b*z)+mu*(y+z-2*x),
            y*(1-b*x-y-a*z)+mu*(x+z-2*y),
            z*(1-a*x-b*y-z)+mu*(x+y-2*z))


def rhs_p(p, S, a, mu):
    # b = 2-a, so the competitive component is antisymmetric.
    v=a-1
    x,y,z=p
    return (-S*v*x*(y-z)+mu*(1-3*x),
            -S*v*y*(z-x)+mu*(1-3*y),
            -S*v*z*(x-y)+mu*(1-3*z))


def entropy(p):
    return -sum(log(3*u) for u in p)/3


def dissipation(p):
    return (sum(1/u for u in p)-9)/3


def rk4_step(m,t,h,mu,a):
    b=2-a
    def f(z,tt): return rhs_m(z,a,b,mu(tt))
    def add(v,k,scale): return tuple(v[i]+scale*k[i] for i in range(3))
    k1=f(m,t)
    k2=f(add(m,k1,h/2),t+h/2)
    k3=f(add(m,k2,h/2),t+h/2)
    k4=f(add(m,k3,h),t+h)
    return tuple(m[i]+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3))


def integrate(T,mu,a=.7,step=.04):
    m=(.55,.30,.15)
    t=0.
    n=round(T/step)
    h=T/n
    H=[]
    for i in range(n):
        m=rk4_step(m,t,h,mu,a)
        t=(i+1)*h
        if i % max(1,n//20)==0 or i==n-1:
            S=sum(m)
            p=tuple(v/S for v in m)
            assert min(m)>0
            assert abs(S-1)<2e-9, S
            H.append((t,entropy(p)))
    return H


def main():
    ct=0
    for i in range(1,36):
        # Exact rational identities for multiple distinct species vectors.
        m=tuple(Q(i+j, 8*i+35) for j in [1,4,7]); S=sum(m)
        p=tuple(x/S for x in m)
        a=Q(i%9+2,10); b=2-a; mu=Q(i%11+1,30)
        dm=rhs_m(m,a,b,mu)
        dp=rhs_p(p,S,a,mu)
        assert sum(dm)==S*(1-S)
        assert sum(dp)==0
        assert all(dp[k]==dm[k]/S-m[k]*sum(dm)/S**2 for k in range(3))
        # Hdot = -mu D, expressed as its exact rational derivative.
        hdot=-sum(dp[k]/p[k] for k in range(3))/3
        d=(sum(1/pk for pk in p)-9)/3
        assert hdot == -mu*d
        assert d>0
        ct+=5

    # Discrete valid entropy-dissipation inequality and uniform limit.
    for t in range(1,100):
        eps=0.001*t
        p=(Q(1,3)+Q(t,1000),Q(1,3),Q(1,3)-Q(t,1000))
        H=entropy(p); D=float(dissipation(p))
        assert D >= 3*H-1e-11
        ct+=1
    last=[]
    for eps in [1e-2,1e-3,1e-4,1e-5]:
        p=(1/3+eps,1/3-eps,1/3)
        last.append(dissipation(p)/entropy(p))
    assert abs(last[-1]-6)<.002 and abs(last[-1]-6)<abs(last[0]-6)
    ct+=2

    # Compare two mutation budgets on the same ecological equations.
    H0=entropy((.55,.30,.15))
    for q,T in [(1.0,350.),(2.0,350.),(.5,400.)]:
        a=.25
        mu=lambda t,q=q: a/(1+t)**q
        data=integrate(T,mu)
        H=data[-1][1]
        M=(a*log1p(T) if q==1 else a*((1+T)**(1-q)-1)/(1-q))
        assert 0<H<H0
        assert H<=H0*exp(-3*M)*1.000001
        if q==2:
            assert H>H0*exp(-80*a)  # Coarse nonzero compact-level bound.
            assert H > 1e-5
        if q==.5:
            assert H<1e-3
        ct+=4
        print(f'power q={q}: at t={T:g}, budget={M:.6g}, KL={H:.10g}')
    print(f'PASS: {ct} exact/algebraic, entropy, limiting-ratio and trajectory checks')


def log1p(z): return log(1+z)


if __name__=='__main__':
    main()
