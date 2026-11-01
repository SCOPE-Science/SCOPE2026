#!/usr/bin/env python3
"""Independent angular tests for a critical radial-mean covariogram limit."""
import math

def facets(vertices):
    output = []
    for a,b in zip(vertices, vertices[1:]+vertices[:1]):
        e=(b[0]-a[0],b[1]-a[1]); length=math.hypot(*e)
        n=(e[1]/length,-e[0]/length); h=n[0]*a[0]+n[1]*a[1]
        if h<0: n=(-n[0],-n[1]); h=-h
        assert h>0
        output.append((n,h,length))
    return output

def logcosh(z):
    t=abs(z)
    return t + math.log1p(math.exp(-2*t)) - math.log(2)

def predicted(faces,y):
    return sum(h*length*logcosh((n[0]*y[0]+n[1]*y[1])/(2*h))
               for n,h,length in faces)

def actual(faces,y,p,N=90000):
    total=0.
    for j in range(N):
        theta=2*math.pi*(j+0.5)/N
        u=(math.cos(theta), math.sin(theta))
        radial=float('inf'); shifted=float('inf')
        for n,h,_ in faces:
            dot=n[0]*u[0]+n[1]*u[1]
            if dot>0:
                radial=min(radial,h/dot)
                shifted=min(shifted,(h+(n[0]*y[0]+n[1]*y[1])/p)/dot)
        log_ratio=math.log(shifted/radial)
        z=-p*log_ratio
        soft=max(0.,z)+math.log1p(math.exp(-abs(z)))-math.log(2)
        log_mean=-soft/p
        total+=radial*radial*(-math.expm1(2*log_mean))
    return p*math.pi*total/N

def test_case(name,vertices,y):
    f=facets(vertices); goal=predicted(f,y)
    errors=[]
    for p in (48,96,192,384):
        got=actual(f,y,p); err=abs(got-goal); errors.append(err)
        print(name, 'p=',p, 'direct=',round(got,9), 'limit=',round(goal,9), 'error=',round(err,9))
    assert all(errors[i+1]<errors[i]*0.67 for i in range(3))
    assert errors[-1]<0.01
    assert abs(predicted(f,(-y[0],-y[1]))-goal)<1e-12

def test_cubical_contacts():
    for d in (2,3,5):
        a=.5; V=(2*a)**d; tau=1.0
        john=2*a*math.sqrt(d)*math.acosh(math.exp(tau/(d*V)))
        loewner=2*a*math.acosh(math.exp(tau/V))
        assert john<loewner
        assert abs(V*d*logcosh(john/(2*a*math.sqrt(d)))-tau)<1e-12
        assert abs(V*logcosh(loewner/(2*a))-tau)<1e-12
        print('cube dimension',d,'John radius',round(john,9),'Loewner radius',round(loewner,9))

if __name__=='__main__':
    test_case('square',[(-.5,-.5),(.5,-.5),(.5,.5),(-.5,.5)],(.45,-.28))
    test_case('triangle',[(1.5,.2),(-1.,-1.),(-.7,1.3)],(.51,-.44))
    test_cubical_contacts()
    print('All independent numerical checks passed; numerical tests do not establish a universal limit.')
