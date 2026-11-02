"""Reproducibility diagnostics for asymmetric exponential Gabor frame asymptotics.

Standard library only; finite numerical checks are not a proof of asymptotic claims.
"""
import math


def window(t, r, R):
    c = math.sqrt(2*r*R/(r+R))
    return c*math.exp(r*t if t < 0 else -R*t)


def coeffs(n, eta, r, R, x):
    a=eta/n
    c2=2*r*R/(r+R)
    eR=-math.expm1(-2*R*a)
    er=-math.expm1(-2*r*a)
    ed=-math.expm1(-(R-r)*a)
    d=a*c2*(math.exp(-2*R*x)/eR+math.exp(2*r*(x-a))/er)
    U=math.exp(2*r*(x-a))/er+math.exp((r-R)*x)/ed
    V=math.exp(-2*R*x)/eR-math.exp((r-R)*x)/ed
    return d, a*c2*(U*math.exp(-r*eta)+V*math.exp(-R*eta))


def spectral(n,eta,r,R,x,v):
    a=eta/n;c2=2*r*R/(r+R)
    d=coeffs(n,eta,r,R,x)[0]
    er=-math.expm1(-2*r*a);eR=-math.expm1(-2*R*a);ed=-math.expm1(-(R-r)*a)
    U=math.exp(2*r*(x-a))/er+math.exp((r-R)*x)/ed
    V=math.exp(-2*R*x)/eR-math.exp((r-R)*x)/ed
    def P(q):return (q*math.cos(v)-q*q)/(1-2*q*math.cos(v)+q*q)
    return d+2*a*c2*(U*P(math.exp(-r*eta))+V*P(math.exp(-R*eta)))


def extremal(n,eta,r=1.,R=2.):
    a=eta/n
    values=[spectral(n,eta,r,R,a*i/60,math.pi*j/30) for i in range(61) for j in range(31)]
    return min(values),max(values)


def check():
    tests=0
    for n,eta,r,R in [(3,4.,1.,2.),(20,7.,.8,1.7),(150,10.,1.,2.)]:
        a=eta/n
        for u in (0.,.13,.51,.93):
            x=u*a
            d,c1=coeffs(n,eta,r,R,x)
            kmax=max(2000,int(40/a))
            t=(x+a*k for k in range(-kmax,kmax+1))
            direct_d=0.;direct_c=0.
            for z in t:
                g=window(z,r,R)
                direct_d+=g*g
                direct_c+=g*window(z-eta,r,R)
            assert abs(a*direct_d-d)<2.e-11
            assert abs(a*direct_c-c1)<2.e-11
            tests+=2
        H=(R*math.exp(-r*eta)-r*math.exp(-R*eta))/(R-r)
        # Independent midpoint quadrature for the real-space autocorrelation.
        step=.005
        integral=sum(window(-30+(j+.5)*step,r,R)*window(-30+(j+.5)*step-eta,r,R)
                     for j in range(int(60/step)))*step
        assert abs(H-integral)<1.e-5
        tests+=1
        # Compare the rational spectral formula against a finite Fourier series
        # assembled from direct periodized real-space correlations.
        x=.37*a
        for angle in (.2,1.7,math.pi):
            d=coeffs(n,eta,r,R,x)[0]
            c2=2*r*R/(r+R)
            U=math.exp(2*r*(x-a))/(-math.expm1(-2*r*a))+math.exp((r-R)*x)/(-math.expm1(-(R-r)*a))
            V=math.exp(-2*R*x)/(-math.expm1(-2*R*a))-math.exp((r-R)*x)/(-math.expm1(-(R-r)*a))
            series=d+2*sum(a*c2*(U*math.exp(-r*m*eta)+V*math.exp(-R*m*eta))*math.cos(m*angle)
                           for m in range(1,21))
            assert abs(spectral(n,eta,r,R,x,angle)-series)<2.e-10
            tests+=1
    for n in (100,300,1000):
        L=math.log(n);center=(2*L-math.log(L))
        for t in (-.5,.3,.7,1.1,1.7):
            eta=center+t
            A,B=extremal(n,eta)
            assert A>0 and B>=A
            assert 1-A<.2 and B-1<.2
            tests+=2
        opts={}
        for kind in ('A','B','K'):
            def obj(eta):
                A,B=extremal(n,eta)
                return {'A':1-A,'B':B-1,'K':B/A-1}[kind]
            grid=[center-1+0.08*i for i in range(43)]
            opts[kind]=min(grid,key=obj)
        assert opts['B'] < opts['K'] < opts['A']
        tests+=1
        for key, expected in [('A', math.log(3)), ('K', math.log(2)), ('B', math.log(1.5))]:
            assert abs((opts[key]-center)-expected)<.7
            tests+=1
    print(f'PASS {tests} exact-kernel, spectral and asymptotic diagnostic assertions')


if __name__=='__main__':
    check()
