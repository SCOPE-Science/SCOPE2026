"""Independent finite diagnostics for equal-radius disk unions on a center circle.

Only Python 3 standard library is required. Finite quadrature is a check, not
an analytic proof of optimality, uniqueness, or asymptotic statements.
"""
import math
import random

PI=math.pi

def formula(m,R,r):
    s=math.sin(PI/m); c=math.cos(PI/m)
    if r<=R*s:return m*PI*r*r
    q=math.sqrt(max(0,r*r-R*R*s*s)); z=math.asin(R*s/r)
    if r<R:return 2*m*(R*s*q+r*r*z)
    return m*(r*r*PI/m+R*R*s*c+R*s*q+r*r*z)

def polar_quadrature(angles,R,r,N=25000):
    centers=[(R*math.cos(t),R*math.sin(t)) for t in angles]
    total=0.0
    for j in range(N):
        theta=(j+0.5)*2*PI/N;ux=math.cos(theta);uy=math.sin(theta)
        intervals=[]
        for cx,cy in centers:
            dot=ux*cx+uy*cy
            disc=dot*dot+r*r-R*R
            if disc<0:continue
            root=math.sqrt(max(0,disc));lo=max(0,dot-root);hi=dot+root
            if hi>lo:intervals.append((lo,hi))
        intervals.sort();L=-1.;H=-1.
        for lo,hi in intervals:
            if L<0:L,H=lo,hi
            elif lo<=H:H=max(H,hi)
            else:total+=(H*H-L*L)/2;L,H=lo,hi
        if L>=0:total+=(H*H-L*L)/2
    return total*2*PI/N

def lens_overlap(r,d):
    if d>=2*r:return 0.
    if d<=0:return PI*r*r
    return 2*r*r*math.acos(d/(2*r))-.5*d*math.sqrt(max(0.,4*r*r-d*d))

def curvature(m,R,r):
    s=math.sin(PI/m);c=math.cos(PI/m)
    assert r>R*s
    q=math.sqrt(r*r-R*R*s*s)
    if r<=R:return R*s*(q*q+R*R*c*c)/q
    return R*s*(R*c+q)**2/(2*q)

def main():
    random.seed(716071)
    largest=0.;samples=0
    for m,R in ((3,1.),(4,1.3),(5,2.),(7,0.7)):
        critical=R*math.sin(PI/m)
        for r in (critical*.7,critical,critical*1.12,R,R*1.4):
            angles=[2*PI*j/m for j in range(m)]
            area=polar_quadrature(angles,R,r)
            error=abs(area-formula(m,R,r))
            largest=max(largest,error)
            assert error<1.2e-3,(m,R,r,area,formula(m,R,r))
            samples+=1
            for case in range(2):
                random_angles=sorted(random.random()*2*PI for _ in range(m))
                random_area=polar_quadrature(random_angles,R,r,8000)
                assert random_area<=formula(m,R,r)+3e-3
    for m in (3,4,6):
        R=1.;rs=math.sin(PI/m);K=(4/3)*math.sqrt(rs)*(math.cos(PI/m))**1.5
        for eps in (.02,.008):
            gaps=[2*PI/m-eps,2*PI/m+eps]+[2*PI/m]*(m-2)
            angles=[0.]
            for g in gaps[:-1]:angles.append(angles[-1]+g)
            area_defect=m*PI*rs**2-polar_quadrature(angles,R,rs,70000)
            ratio=area_defect/(K*eps**1.5)
            assert .89<ratio<1.14,(m,eps,ratio)
            d=2*R*math.sin((2*PI/m-eps)/2)
            assert abs(lens_overlap(rs,d)-K*eps**1.5)/(K*eps**1.5)<.02
    for m in (3,5,8):
        for r in (1.05*math.sin(PI/m),1.,1.6):
            R=1.;eps=.025
            gaps=[2*PI/m-eps,2*PI/m+eps]+[2*PI/m]*(m-2)
            angles=[0.]
            for g in gaps[:-1]:angles.append(angles[-1]+g)
            loss=formula(m,R,r)-polar_quadrature(angles,R,r,75000)
            expected=curvature(m,R,r)*eps**2
            assert abs(loss-expected)<max(5e-4,.15*expected),(m,r,loss,expected)
    print('ALL_CHECKS_PASSED independent_polar_cases=',samples,'max_abs_area_error=',largest)

if __name__=='__main__':main()
