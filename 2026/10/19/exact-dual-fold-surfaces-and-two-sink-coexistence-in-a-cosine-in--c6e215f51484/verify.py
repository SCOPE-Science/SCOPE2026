"""Independent numerical consistency checks for the exact two-branch cosine fixed-point theorem.
The analytical proof, not these finite checks, establishes the infinite parameter result.
Requires Python 3 standard library only.
"""
import math
from fractions import Fraction

PI = math.pi


def numerator(u,b):
    t=PI*u/2
    return -b*math.cos(t)+(PI/2)*(1-b*u)*math.sin(t)


def critical_u(b):
    lo,hi=0.0,1.0
    for _ in range(78):
        mid=(lo+hi)/2
        if numerator(mid,b)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def threshold_a(b):
    u=critical_u(b)
    return 1.0-(1-b*u)/math.cos(PI*u/2)


def F(x,a,b,c):
    if x<=b:
        return 1-(1-a)*math.cos(PI*x/(2*b))
    return c*math.cos(PI*(x-1)/(2-2*b))


def derivative(x,a,b,c):
    if x<b:
        return (1-a)*(PI/(2*b))*math.sin(PI*x/(2*b))
    return c*(PI/(2*(1-b)))*math.sin(PI*(1-x)/(2*(1-b)))


def independent_count(a,b,c,n=4800):
    count=0
    for low, high, fl, fr in [
        (0,b,lambda x:F(x,a,b,c)-x,lambda x:F(x,a,b,c)-x),
        (b,1,lambda x:c*math.cos(PI*(x-1)/(2-2*b))-x,
             lambda x:c*math.cos(PI*(x-1)/(2-2*b))-x)]:
        previous=fl(low) if low==0 else -b
        for i in range(1,n+1):
            x=low+(high-low)*i/n
            val=fr(x)
            if previous*val<0:count+=1
            previous=val
    return count


def run():
    checks=0
    # Exact algebraic sign witness for four simple fixed points.
    # 99*sqrt(3)/200 > 5/6 iff 3*297^2 > 500^2.
    assert 3*297**2 > 500**2
    checks += 1
    # A(b) increases, and C(b)=1-A(1-b) is the reflected fold.
    bs=[(i+1)/101 for i in range(100)]
    aa=[threshold_a(b) for b in bs]
    cc=[1-threshold_a(1-b) for b in bs]
    assert all(0 < a < 1-2/PI for a in aa)
    assert all(2/PI < c < 1 for c in cc)
    assert all(aa[i+1]>aa[i] for i in range(99))
    assert all(cc[i+1]>cc[i] for i in range(99))
    checks+=4
    for b,A,C in zip(bs,aa,cc):
        u=critical_u(b)
        assert abs(numerator(u,b))<1e-12
        x=b*u
        assert abs(F(x,A,b,0.5)-x)<1e-11
        assert abs(derivative(x,A,b,0.5)-1)<1e-10
        s=critical_u(1-b)
        xr=1-(1-b)*s
        assert abs(C*math.cos(PI*(xr-1)/(2-2*b))-xr)<1e-11
        assert abs(derivative(xr,0.5,b,C)-1)<1e-10
        checks+=5
    # Independent grid counting away from the neutral surfaces.
    for b,A,C in zip(bs[::5],aa[::5],cc[::5]):
        for left in [-1,1]:
            for right in [-1,1]:
                a=A*0.5 if left<0 else (1+A)*0.5
                c=(1+C)*0.5 if right>0 else C*0.5
                count=independent_count(a,b,c)
                assert count==(2 if left<0 else 0)+(2 if right>0 else 0), (a,b,c,count,A,C)
                checks+=1
    b=0.5
    A=threshold_a(b)
    C=1-threshold_a(1-b)
    assert abs((A+C)-1)<1e-12
    assert A>0.01 and C<0.99
    assert independent_count(0.01,b,0.99)==4
    checks+=3
    # Sharp small-b asymptotics, checked only as a numerical diagnostic.
    for b in [1e-2,1e-3,1e-4]:
        A=threshold_a(b)
        ratio=A/(2*b*b/PI**2)
        assert abs(ratio-1)<3e-4
        checks+=1
    print('PASS',checks,'checks; A(1/2)=',threshold_a(0.5), 'C(1/2)=',1-threshold_a(0.5))

if __name__=='__main__':run()
