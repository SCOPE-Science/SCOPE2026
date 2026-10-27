"""Reproducibility checks for the gapped geometric heat-pump area envelope.
Uses only the Python standard library. All numerical checks are finite corroboration.
"""
from math import pi, sin, cosh, tanh, acosh, asin, sqrt, log, log1p, exp, isfinite


def simpson(f, a, b, n=6000):
    assert n % 2 == 0 and b >= a
    if a == b:
        return 0.0
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(a + h*j)
    return h * total / 3


def G(r):
    # Stable at every r used by these tests.
    return r * tanh(r) - (r + log1p(exp(-2*r)) - log(2.0))


def D(r):
    y = exp(-2*r)
    return 2*r*y/(1+y) + log1p(y)


def profiles(q, rho, T=1.0, n=6000):
    assert T > 0 and rho > 0 and 0 < q < 1/cosh(rho)**2
    left = 0.5*asin(q*cosh(rho)**2)
    right = pi/2-left
    def R(th):
        s=sin(2*th)
        return acosh(sqrt(max(1.0, s/q)))
    area = T*T/2*simpson(lambda th: R(th)**2-rho**2,left,right,n)
    heat = T*simpson(lambda th: sin(2*th)*(G(R(th))-G(rho)),left,right,n)
    tail = T*(simpson(lambda th: sin(2*th)*D(R(th)),left,right,n)
             + 2*simpson(lambda th: sin(2*th)*D(rho),0,left,n))
    return area,heat,tail


def small_coefficient(rho):
    return 3**(5/3)/(5*2**(1/3)) / cosh(rho)**2 * (tanh(rho)/rho)**(2/3)


def check():
    assertions = 0
    for rho in (0.25, 0.7, 1.6):
        s0 = 1/cosh(rho)**2
        data = []
        for ratio in (0.995,0.985,0.94,0.7,0.35,0.05):
            q=s0*ratio
            A,H,tail=profiles(q,rho)
            total=D(rho)
            assert A>0 and 0<H<total and abs(total-H-tail)<2e-8
            assert H<s0*A
            assertions+=5
            data.append((q,A,H))
        assert all(data[k][1]<data[k+1][1] for k in range(len(data)-1))
        assert all(data[k][2]<data[k+1][2] for k in range(len(data)-1))
        assertions+=2
        # Non-uniform local cusp approached from positive q below the maximal curvature.
        q=s0*(1-0.001)
        A,H,_=profiles(q,rho)
        empirical=(s0*A-H)/(A**(5/3))
        expected=small_coefficient(rho)
        assert abs(empirical/expected-1)<0.005
        assertions+=1
        # Differential variational identity: dH/dA = q/T, with T=1 here.
        for ratio in (0.5,0.9):
            q=s0*ratio
            dt=1e-4*q
            A0,H0,_=profiles(q-dt,rho,n=3000)
            A1,H1,_=profiles(q+dt,rho,n=3000)
            slope=(H0-H1)/(A0-A1)
            assert abs(slope/q-1)<0.003
            assertions+=1
        # The large-area tail is stretched exponential with the derived coefficient.
        for L in (24.0,40.0):
            q=exp(-L)
            A,H,gap=profiles(q,rho)
            pred=sqrt(pi*A)*exp(-4*sqrt(A/pi))
            assert 0.60<gap/pred<1.20
            assertions+=1
        # For large r the finite-gap pump capacity is small but positive.
        assert 0<D(rho)<log(2)
        assertions+=1
    print('PASS:',assertions,'finite numerical assertions')

if __name__=='__main__':
    check()
