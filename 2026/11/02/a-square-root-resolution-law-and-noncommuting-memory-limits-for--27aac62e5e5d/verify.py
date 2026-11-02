"""Reproduce numerical cross-checks for the noisy rotating OU entropy law.
Uses only the Python 3 standard library. Numerical checks supplement a proof.
"""
import math


def rate(alpha, omega, h, tau):
    assert alpha > 0 and h > 0 and tau >= 0
    q = math.exp(-2 * alpha * h)
    c = -math.expm1(-2 * alpha * h)
    s = math.sin(omega * h)**2
    if tau == 0:
        return 4 * q * s / c
    K = math.sqrt(c * (4 * tau + c * (1-tau)**2))
    u = 2 * tau * q / (c + tau*(1+q) + K)
    return 4*c*u*(1+u)*s/(tau*K*(1-u)*((1-u)**2+4*u*s))


def spectral(alpha, omega, h, tau, count=131072):
    r = math.exp(-alpha*h)
    c = -math.expm1(-2*alpha*h)
    th = omega*h
    z = 0.0
    for j in range(count):
        phi = -math.pi + 2*math.pi*(j+0.5)/count
        f = c/(1-2*r*math.cos(phi-th)+r*r)
        b = c/(1-2*r*math.cos(phi+th)+r*r)
        z += (f-b)**2/((tau+f)*(tau+b))
    return z/(2*count)


def covariance(m, alpha, omega, h, tau):
    d=2*m
    a=[[0.0 for _ in range(d)] for _ in range(d)]
    for i in range(m):
        for j in range(m):
            delta=i-j
            mag=math.exp(-alpha*h*abs(delta))
            co=mag*math.cos(omega*h*delta)
            si=mag*math.sin(omega*h*delta)
            a[2*i][2*j]=co
            a[2*i][2*j+1]=-si
            a[2*i+1][2*j]=si
            a[2*i+1][2*j+1]=co
            if i==j:
                a[2*i][2*j]+=tau
                a[2*i+1][2*j+1]+=tau
    return a


def gauss_solve(a,b):
    n=len(a)
    a=[r[:] + [v] for r,v in zip(a,b)]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(a[i][k]))
        assert abs(a[p][k])>1e-13
        a[p],a[k]=a[k],a[p]
        v=a[k][k]
        for j in range(k,n+1):a[k][j]/=v
        for i in range(n):
            if i==k:continue
            fac=a[i][k]
            for j in range(k,n+1):a[i][j]-=fac*a[k][j]
    return [row[-1] for row in a]


def block_kl(m, alpha, omega, h, tau):
    f=covariance(m,alpha,omega,h,tau)
    d=2*m
    index=[2*(m-1-i)+a for i in range(m) for a in range(2)]
    b=[[f[index[i]][index[j]] for j in range(d)] for i in range(d)]
    trace=0.0
    for col in range(d):
        v=gauss_solve(b,[f[i][col] for i in range(d)])
        trace+=v[col]
    return (trace-d)/2


def check():
    count=0
    params=[(1,2,.1,1),(1,2,.5,.02),(2,.7,1,2),(.05,20,.023,5),
            (1,2,1,0),(.01,1,.05,1000),(1,4,.005,.1),(.7,3,.35,.5),
            (2,1.2,.08,10),(.5,4,.2,.001)]
    for aa,ww,hh,tt in params:
        exact=rate(aa,ww,hh,tt)
        integral=spectral(aa,ww,hh,tt)
        assert abs(exact-integral)<max(1e-9,1e-8*abs(exact)),(aa,ww,hh,tt,exact,integral)
        count+=1
    for aa,ww,hh,tt in params[:8]:
        finite=block_kl(2,aa,ww,hh,tt)
        q=math.exp(-2*aa*hh)
        predicted=4*q*math.sin(ww*hh)**2/((1+tt)**2-q)
        assert abs(finite-predicted)<1e-9,(finite,predicted)
        count+=1
    for m in (2,3,4):
        h=.001
        A=block_kl(m,1.,2.,h,1.)
        B=block_kl(m,1.,2.,h/2,1.)
        assert 3.6 < A/B < 4.4,(m,A,B)
        count+=1
    for tau in (.1,1,5):
        alpha,omega=1.,2.
        for h in (1e-4,2e-4,5e-4):
            ratio=rate(alpha,omega,h,tau)/h/(2*omega**2/alpha)
            approxim=1-1.5*math.sqrt(2*alpha*tau*h)
            assert abs(ratio-approxim)<max(.003,100*h)
            count+=1
    for alpha,omega,h,tau in ((1,2,.7,1),(2,3,.01,100),(1,2,.2,.03)):
        assert 0 < rate(alpha,omega,h,tau) < rate(alpha,omega,h,0)
        count+=1
    for n in (1,2,3):
        h=n*math.pi/2
        assert abs(rate(1,2,h,1))<1e-28
        count+=1
    print('PASS:',count,'deterministic cross-checks (spectral, finite-block, asymptotic, bounds)')

if __name__=='__main__':check()
