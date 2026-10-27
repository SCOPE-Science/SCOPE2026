"""Reproducible finite checks of the rational EOS detuning asymptotics.
Finite numerical checks supplement, but do not replace, the analytic proof.
"""
import math

def sigmoid(t):
    return 1/(1+math.exp(-t)) if t>=0 else math.exp(t)/(1+math.exp(t))

def iterate(a,b,q,x):
    mult=1.0
    for _ in range(q):
        s=sigmoid(a*x)
        mult*=1-a*s*(1-s)
        x=x+b-s
    return x,mult

def root(a,b,q,center,radius):
    lo,hi=center-radius,center+radius
    assert iterate(a,b,q,lo)[0]-lo>0
    assert iterate(a,b,q,hi)[0]-hi<0
    for _ in range(70):
        mid=(lo+hi)/2
        if iterate(a,b,q,mid)[0]-mid>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def rk4(xi,y,T=0.4,N=5000):
    dt=T/N
    ff=lambda z:xi-math.sinh(z)
    for _ in range(N):
        k1=ff(y);k2=ff(y+dt*k1/2);k3=ff(y+dt*k2/2);k4=ff(y+dt*k3)
        y+=dt*(k1+2*k2+2*k3+k4)/6
    return y

central=[]
for q,p in ((2,1),(3,1),(5,2),(7,3)):
    a=22*q;eps=math.exp(-a/(2*q));step=2*a*eps
    for xi in (-1.,0.,1.):
        b=p/q+2*eps*xi/q
        y0=.35
        x=.5/q+y0/a
        xx,_=iterate(a,b,q,x)
        err=abs((xx-x)/(2*eps)-(xi-math.sinh(y0)))
        yy=y0
        n=round(.4/step)
        for _ in range(n):
            x,_=iterate(a,b,q,x)
        yy=a*(x-.5/q)
        ode=rk4(xi,y0,T=n*step)
        flow_err=abs(yy-ode)
        eq=math.asinh(xi)
        xr=root(a,b,q,.5/q+eq/a,1/a)
        root_err=abs(a*(xr-.5/q)-eq)
        mult=iterate(a,b,q,xr)[1]
        mult_err=abs((1-mult)/(2*a*eps)-math.sqrt(1+xi*xi))
        assert err<0.02,(q,xi,err)
        assert flow_err<0.015,(q,xi,flow_err)
        assert root_err<0.02,(q,xi,root_err)
        assert mult_err<0.02,(q,xi,mult_err)
        central.append((q,p,xi,round(err,6),round(flow_err,6),round(root_err,6),round(mult_err,6)))

outer=[]
for q,p in ((2,1),(3,1),(5,2),(7,3)):
    a=44*q;tau=1/(4*q);v=math.exp(-a*tau)
    for d in (0.75,1.5):
        for sign in (-1,1):
            b=p/q+sign*d*v/q
            target=((1/q-tau+math.log(d)/a) if sign==1 else (tau-math.log(d)/a))
            xr=root(a,b,q,target,2/a)
            pos_err=a*abs(xr-target)
            mult=iterate(a,b,q,xr)[1]
            mult_err=abs((1-mult)/(a*d*v)-1)
            assert pos_err<0.03,(q,d,sign,pos_err)
            assert mult_err<0.04,(q,d,sign,mult_err)
            outer.append((q,p,d,sign,round(pos_err,6),round(mult_err,6)))

print('CENTRAL',len(central),'max errors',*[max(z[i] for z in central) for i in range(3,7)])
print('OUTER',len(outer),'max errors',max(z[4] for z in outer),max(z[5] for z in outer))
print('CENTRAL_DATA')
for x in central:print(*x)
print('OUTER_DATA')
for x in outer:print(*x)
print('CHECKS_PASS')
