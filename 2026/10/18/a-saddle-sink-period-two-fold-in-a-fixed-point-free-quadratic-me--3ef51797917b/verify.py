#!/usr/bin/env python3
"""Independent reproducibility checks for a period-two fold theorem.

Requires only Python 3 standard library. Finite tests supplement, but do not
replace, the analytical proof in RESULT.md.
"""
import math

COUNT = 0

def check(condition, message='failed assertion'):
    global COUNT
    assert condition, message
    COUNT += 1


def close(a, b, atol=1e-11, rtol=1e-10):
    check(abs(a-b) <= atol+rtol*max(abs(a),abs(b)), f'{a} vs {b}')


def threshold_data(b):
    r = math.sqrt(1.0-1.0/b)
    k = 2*r
    def amp(t):
        return 4*b*r**3*t*t*math.sqrt(1-t*t)/math.cos(k*t)
    def dlog(t):
        return 2/t-t/(1-t*t)+k*math.tan(k*t)
    def d2log(t):
        return -2/(t*t)-(1+t*t)/(1-t*t)**2+k*k/math.cos(k*t)**2
    low, high = 1e-6, 1-1e-6
    check(dlog(low)>0 and dlog(high)<0)
    for _ in range(80):
        mid=(low+high)/2
        if dlog(mid)>0: low=mid
        else: high=mid
    ts=(low+high)/2
    check(0<ts<1)
    close(dlog(ts),0,atol=1e-9)
    return r,ts,amp(ts),amp,dlog,d2log


def f(a,b,x,y):
    return (a*math.cos(x)+b*(y*y-1)*x,y+x)


def jac(a,b,x,y):
    return ((-a*math.sin(x)+b*(y*y-1),2*b*x*y),(1.,1.))


def matmul(p,q):
    return tuple(tuple(sum(p[i][k]*q[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def tr_det(p):
    return p[0][0]+p[1][1],p[0][0]*p[1][1]-p[0][1]*p[1][0]


def inverse_branch(amp,target,low,high,increasing):
    for _ in range(85):
        mid=(low+high)/2
        if (amp(mid)<target)==increasing:low=mid
        else: high=mid
    return (low+high)/2


def main():
    for b in [1.005,1.01,1.05,1.1,1.125,1.2,1.25,4/3]:
        r,tstar,acrit,amp,dlog,d2log=threshold_data(b)
        check(acrit>0)
        for j in range(1,250):
            t=j/250
            check(d2log(t)<0, f'concavity {b},{t}')
        for fraction in (0.1,0.5,0.9):
            a=acrit*fraction
            for high in (False,True):
                t=inverse_branch(amp,a,tstar,1-1e-13,False) if high else inverse_branch(amp,a,1e-13,tstar,True)
                u=2*r*t
                z=r*math.sqrt(1-t*t)
                v=z-u/2
                p=(u,v)
                q=f(a,b,*p)
                pp=f(a,b,*q)
                close(q[0],-u)
                close(q[1],z+u/2)
                for x,y in zip(pp,p):close(x,y)
                J2=matmul(jac(a,b,*q),jac(a,b,*p))
                tr,d=tr_det(J2)
                S=b*u*z*(1+u*math.tan(u))
                close(tr,2-S*S-2*b*u*u)
                close(d,(b*u*u-1)**2-(S+2*b*u*z)**2)
                close(1-tr+d,b*b*u*u*(u*u-4*z*z*(2+u*math.tan(u))))
                check((1-tr+d>0)==high)
                if b<=1.125:
                    check(0<d<1)
                    check(1+tr+d>0)
                    if high:check(1-tr+d>0)
                    else:check(1-tr+d<0)
        # At the fold, one eigenvalue is 1 to numerical accuracy.
        u=2*r*tstar;z=r*math.sqrt(1-tstar*tstar);v=z-u/2
        p=(u,v);q=f(acrit,b,*p)
        J2=matmul(jac(acrit,b,*q),jac(acrit,b,*p))
        tr,d=tr_det(J2)
        close(1-tr+d,0,atol=3e-9)
        check(d<1)
    coeff=8/(3*math.sqrt(3))
    for eps in (1e-3,1e-4,1e-5):
        b=1+eps
        _,_,crit,*_=threshold_data(b)
        ratio=crit/(coeff*eps**1.5)
        check(abs(ratio-(1+5*eps/6))<5*eps*eps)
    print(f'PASS: {COUNT} finite checks; standard library only.')

if __name__=='__main__':main()
