"""Reproducible exact-arithmetic checks for the planar rank-one stabilization benchmark.

The general theorem follows from the analytic arguments in RESULT.md, not from
these finite checks. Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product

N = 0

def check(c):
    global N
    assert c
    N += 1

def td(h,b,d):
    # Trace and determinant of h*I+b*J+d, J=[[0,-1],[1,0]].
    x,y=d[0]
    z,w=d[1]
    return 2*h+x+w, (h+x)*(h+w)-(-b+y)*(b+z)

def nsq(d):
    return sum(v*v for row in d for v in row)

# Count exact rational cases, including b=0, b<h, b=h and b>h.
for h,b in product([F(v,5) for v in range(1,41)],
                    [F(v,5) for v in range(0,51)]):
    A2=h*h+b*b
    if b==0:
        # Every rank-one perturbation of scalar hI has eigenvalue h>0.
        for r in [-5,-2,0,1,7]:
            for s in [-5,-1,2,3,8]:
                # elementary explicit rank-one representatives u=e1
                d=((F(r),F(s)),(F(0),F(0)))
                check(td(h,b,d)[0]>0 or td(h,b,d)[1]<0 or td(h,b,d)[1]==0)
        continue
    if b<h:
        t=A2/b
        q=-(h*h-b*b)/b
        d=((-2*h,q),(F(0),F(0)))
        check(td(h,b,d)==(0,0))
        check(nsq(d)==t*t)
        check(t>2*h)
        # Strictly feasible rank-one perturbations converge to this optimum.
        ep=F(1,1000)
        dd=((-2*h-ep,q-(h/b+1)*ep),(F(0),F(0)))
        tr,det=td(h,b,dd)
        check(tr<0 and det>0)
        check(nsq(dd)>nsq(d))
    else:
        d=((-2*h,F(0)),(F(0),F(0)))
        tr,det=td(h,b,d)
        check(tr==0 and det==b*b-h*h)
        check(nsq(d)==4*h*h)
        ep=F(1,1000)
        dd=((-2*h-ep,-(h/b+1)*ep),(F(0),F(0)))
        tr,det=td(h,b,dd)
        check(tr<0 and det>0)
        check(nsq(dd)>nsq(d))
    # Passive rank-one damping at trace-zero cost 2h.
    sym=((-2*h,F(0)),(F(0),F(0)))
    tr,det=td(h,b,sym)
    check(tr==0)
    check((det>=0)==(b>=h))
    # For b>h overdamping eventually makes determinant negative.
    if b>h:
        for eps in [F(1,100), F(1,10)]:
            d=((-(A2/h+eps),F(0)),(F(0),F(0)))
            check(td(h,b,d)[1]<0)
    # Full-rank correction -hI is exactly on the boundary.
    full=((-h,F(0)),(F(0),-h))
    check(td(h,b,full)==(0,b*b))
    check(nsq(full)==2*h*h)

# The necessary low-rank constraints for arbitrary uv^T are exact identities.
for u1,u2,v1,v2 in product(range(-4,5),repeat=4):
    u=(F(u1),F(u2)); v=(F(v1),F(v2))
    d=((u[0]*v[0],u[0]*v[1]),(u[1]*v[0],u[1]*v[1]))
    p=u[0]*v[0]+u[1]*v[1]
    q=v[0]*(-u[1])+v[1]*u[0] # v^T J u, J u=(-u2,u1)
    check(p*p+q*q==nsq(d))
    tr,det=td(F(5,3),F(7,4),d)
    check(tr==F(10,3)+p)
    check(det==F(25,9)+F(49,16)+F(5,3)*p-F(7,4)*q)

print('CHECKS_PASSED', N)
