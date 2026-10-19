"""Independent numerical cross-check of radial-shell turning-point phase formulas.
Requires scipy and numpy. This checker is illustrative, not an infinite certificate.
"""
import math
import numpy as np
from scipy import special, optimize

def bessel_zeros(order, upto):
    if float(order).is_integer() and order>=0:
        return special.jn_zeros(int(order), upto)
    out=[]
    for n in range(1,upto+1):
        c=(n + order/2-1/4)*math.pi
        left=c-math.pi/3
        right=c+math.pi/3
        a=special.jv(order,left); b=special.jv(order,right)
        assert a*b<0, (order,n,a,b)
        out.append(optimize.brentq(lambda x:special.jv(order,x),left,right,xtol=1e-12))
    return np.array(out)

def calc(d,n,m):
    nu=d/2
    al=bessel_zeros(nu-1,n+1)
    a,b=al[n-1],al[n]
    z=al[m-1]
    f=lambda x: x**nu *special.jv(nu,x)
    X=optimize.brentq(lambda x: f(x)-f(z),a,b,xtol=1e-10)
    q=z/X
    theta=m/n
    parity=(-1)**(m-n)
    gamma=nu/2-3/4
    s=math.acos(parity*theta**(nu-.5))/math.pi
    scaled= n*(q-theta)
    pred=gamma*(1-theta)-theta*s
    assert abs(f(X)-f(z))<1e-5*max(1,abs(f(z)))
    assert a<X<b and 0<q<1
    return q,scaled,pred,(X-a)/math.pi,s

if __name__=='__main__':
    comparisons=0
    for d in (2,3,4,5,6):
        for n,m in ((10,4),(30,11),(50,20),(51,20),(100,40),(101,40),(250,100),(251,100)):
            q,scaled,pred,sx,sp=calc(d,n,m)
            print('d',d,'n',n,'m',m,'q',f'{q:.10f}',
                  'n(q-m/n)',f'{scaled:.6f}','phase_pred',f'{pred:.6f}',
                  'gap_frac',f'{sx:.6f}','phase_limit',f'{sp:.6f}')
            comparisons+=1
    print('COMPARISONS_PASSED',comparisons)
