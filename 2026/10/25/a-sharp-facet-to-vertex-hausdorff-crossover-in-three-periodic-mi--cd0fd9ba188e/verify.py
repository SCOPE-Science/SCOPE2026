"""Checks finite instances of the periodic-three Minkowski polygon phase law.
Finite checks are supplementary to the analytic proof in RESULT.md.
"""
import math

def data(n,t):
    assert n%3==0 and n>=9 and 0<=t<=1
    d=2*math.pi/n;c=math.cos(d);ss=math.sin(d)
    A=(d/2)/math.tan(d/2);L=d*ss/(1+2*c)
    q=[-t,t/2,t/2]
    r=[A-L*q[i%3] for i in range(n)]
    v=[]
    for j in range(n):
        theta=j*d
        tangent=(r[(j+1)%n]-c*r[j])/ss
        v.append((r[j]*math.cos(theta)-tangent*math.sin(theta),
                  r[j]*math.sin(theta)+tangent*math.cos(theta)))
    return d,A,L,r,v

checks=0
for n in (9,12,15,18,24,30,60,90,120):
    for t in (0,.02,.25,.75,.9,.98,.999,1):
        d,A,L,r,v=data(n,t)
        lengths=[math.hypot(v[j][0]-v[(j-1)%n][0],v[j][1]-v[(j-1)%n][1]) for j in range(n)]
        for j in range(n):
            want=d*(1+(-t if j%3==0 else t/2))
            assert math.isclose(lengths[j],want,abs_tol=3e-11,rel_tol=3e-11),(n,t,j,lengths[j],want)
            checks+=1
        assert math.isclose(sum(lengths),2*math.pi,rel_tol=1e-10)
        rin=min(r)
        R=max(math.hypot(*z) for z in v)
        a=A+L*t;b=A-L*t/2;c=math.cos(d)
        Rformula=math.sqrt((a*a+b*b-2*c*a*b)/(1-c*c))
        assert math.isclose(R,Rformula,rel_tol=1e-10)
        assert math.isclose(rin,b,rel_tol=1e-10)
        pos=Rformula-1;neg=1-b
        err=max(pos,neg)
        assert err>=0
        checks+=1
    if n>=9:
        d,A,L,_,_=data(n,0)
        c=math.cos(d)
        k0=A*A/(math.cos(d/2)**2)-(2-A)**2
        k1=L*(A/(1+c)-(2-A))
        k2=L*L*(c+2)**2/(4*(1-c*c))
        root=(-k1+math.sqrt(k1*k1-4*k2*k0))/(2*k2)
        assert 0<root<1
        def H(t):
            a=A+L*t;b=A-L*t/2
            return (a*a+b*b-2*c*a*b)/(1-c*c)-(2-b)**2
        assert abs(H(root))<1e-11
        assert H(0)<0 and H(1)>0
        checks+=1
print('VERIFY_OK',checks)
