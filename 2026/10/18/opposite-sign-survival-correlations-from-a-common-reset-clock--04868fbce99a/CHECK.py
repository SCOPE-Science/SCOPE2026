"""Numerical illustration for two independent Brownian target searches under a common reset clock.
No third-party packages required. Analytic parameter-uniform conclusions are in RESULT.md.
"""
from math import erf,erfc,sqrt,pi,exp

def Q(d,s,D=1.0):
    return 1.0 if s <= 0.0 else erf(d/sqrt(4*D*s))

def delta(d,u,t=1.0,D=1.0):
    return Q(d,u,D)*Q(d,t-u,D)-Q(d,t,D)

def simpson(f,a,b,n=16384):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))+2*sum(f(a+2*k*h) for k in range(1,n//2)))

def main():
    d_near=0.2; d_far=3.0; t=1.0; D=1.0
    assert d_far*d_far >= 6*D*t
    for u in [0.01,0.05,0.2,0.5,0.8,0.99]:
        assert delta(d_far,u,t,D)>0
    coeff=simpson(lambda u:delta(d_near,u,t,D)*delta(d_far,u,t,D),0.,t)
    same=simpson(lambda u:delta(d_near,u,t,D)**2,0.,t)
    assert coeff < -0.001
    assert same>0
    z=0.000000000001
    c=erfc(sqrt(3)*d_far/(2*sqrt(D*t)))
    assert z < sqrt(D*t)*c*c/(3*exp(1)*sqrt(pi))
    print('heterogeneous first-order coefficient:',coeff)
    print('equal-distance first-order coefficient:',same)
    print('analytic sufficient-distance threshold:',sqrt(D*t)*c*c/(3*exp(1)*sqrt(pi)))
    print('checks passed')
if __name__=='__main__':main()
