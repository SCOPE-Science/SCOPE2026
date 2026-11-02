"""Independent numerical spot checks for exact asymmetric exponential Gabor bounds.
Uses only Python standard library. Numerical grids are illustrative, not proof."""
import cmath
import math


def bounds(a,b):
    assert a>0 and b>0
    p,r=math.exp(-a),math.exp(-b)
    u,v=1/(1+p),r/(1+r)
    aa=u*u*(1+p)
    bb=u*v*(1+math.sqrt(p/r))
    cc=v*v*(1+1/r)
    z=((b-a)*bb+math.sqrt((a-b)**2*bb*bb+4*a*b*aa*cc))/(2*b*cc)
    x=math.log(z)/(a+b)
    lower=aa*math.exp(-2*a*x)-2*bb*math.exp((b-a)*x)+cc*math.exp(2*b*x)
    upper=((1-p*r)/((1-p)*(1-r)))**2+(math.sqrt(p)/(1-p)+math.sqrt(r)/(1-r))**2
    return x,lower,upper


def zak(a,b,y,theta):
    p,r=math.exp(-a),math.exp(-b)
    return math.exp(-a*y)/(1-p*cmath.exp(-1j*theta))+r*math.exp(b*y)*cmath.exp(1j*theta)/(1-r*cmath.exp(1j*theta))


def check():
    for a,b in [(1,1),(1,2),(2,1),(.5,3),(3,.5),(4,4),(8,12),(.1,7),(7,.1)]:
        x,lo,up=bounds(a,b)
        assert 0<x<.5 and 0<lo<up,(a,b,x,lo,up)
        low_at_x=abs(zak(a,b,x,math.pi))**2+abs(zak(a,b,x+.5,math.pi))**2
        up_at_0=abs(zak(a,b,0,0))**2+abs(zak(a,b,.5,0))**2
        assert math.isclose(low_at_x,lo,rel_tol=4e-10,abs_tol=4e-10)
        assert math.isclose(up_at_0,up,rel_tol=4e-10,abs_tol=4e-10)
        for j in range(61):
            y=.5*j/60
            for k in range(61):
                theta=2*math.pi*k/60
                s=abs(zak(a,b,y,theta))**2+abs(zak(a,b,y+.5,theta))**2
                assert lo-4e-9<=s<=up+4e-9, (a,b,y,theta,lo,s,up)
        xb,lb,ub=bounds(b,a)
        assert math.isclose(x+xb,.5,abs_tol=1e-9)
        assert math.isclose(lb,lo,rel_tol=1e-9)
        assert math.isclose(ub,up,rel_tol=1e-9)
    print('CHECK_OK: exact geometric Zak fibers, global bounds, internal minimizers and reflection symmetry')

if __name__=='__main__':
    check()
