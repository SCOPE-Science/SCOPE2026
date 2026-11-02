"""Independent numerical checks for polygonal perimeter-loss formulas.

Run with Python 3: python perimeter_verify.py
These calculations test formulas; the analytic arguments are in RESULT.md.
"""
from math import asin, asinh, cos, exp, pi, sin, sqrt
from random import Random

RNG = Random(100729)

def shortcut(x, y, alpha):
    return x+y-sqrt(max(0.0,x*x+y*y-2*x*y*cos(alpha)))

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull_perimeter(points):
    points=sorted(set(points))
    if len(points)<3:
        return 0.0 if len(points)<2 else 2*sqrt(sum((points[1][i]-points[0][i])**2 for i in (0,1)))
    lo=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:
            hi.pop()
        hi.append(p)
    hp=lo[:-1]+hi[:-1]
    return sum(sqrt((p[0]-q[0])**2+(p[1]-q[1])**2) for p,q in zip(hp,hp[1:]+hp[:1]))

def finite_geometry():
    for m in (3,4,5,7):
        vertices=[(cos(2*pi*j/m),sin(2*pi*j/m)) for j in range(m)]
        lengths=[sqrt(sum((vertices[(j+1)%m][k]-vertices[j][k])**2 for k in (0,1))) for j in range(m)]
        alpha=pi-2*pi/m
        P=sum(lengths)
        for _ in range(80):
            sample=[(RNG.randrange(m),RNG.random()) for _ in range(260)]
            pts=[tuple((1-u)*vertices[j][k]+u*vertices[(j+1)%m][k] for k in (0,1)) for j,u in sample]
            observed=P-hull_perimeter(pts)
            predicted=0.0
            for j in range(m):
                a=[u for idx,u in sample if idx==(j-1)%m]
                b=[u for idx,u in sample if idx==j]
                assert a and b
                predicted+=shortcut(lengths[(j-1)%m]*(1-max(a)),lengths[j]*min(b),alpha)
            assert abs(observed-predicted)<1e-10,(m,observed,predicted)
    print('EXACT_CHORD_DECOMPOSITION_PASSED')

def cdf_corner(z,lam,mu,alpha):
    # For E_lambda, E_mu independent, integrate the exact conditional probability.
    S=1+cos(alpha)
    y0=z/S
    hi=max(y0+50/mu,y0+1)
    vmax=sqrt(hi-y0)
    steps=50000
    dt=vmax/steps
    acc=0.0
    for j in range(steps+1):
        t=j*dt
        y=y0+t*t
        if j==0:
            value=0.0
        else:
            x=z*(y-z/2)/(S*y-z)
            value=2*t*mu*exp(-mu*y)*(1-exp(-lam*x))
        acc+=(1 if j==0 or j==steps else 4 if j%2 else 2)*value
    return 1-exp(-mu*y0)+acc*dt/3

def corner_asymptotics():
    for alpha in (pi/3,pi/2,2*pi/3):
        for lam,mu in ((1.0,1.0),(0.75,2.0)):
            z=0.0001
            estimate=cdf_corner(z,lam,mu,alpha)/z
            true=(lam+mu)/(1+cos(alpha))
            assert abs(estimate/true-1)<0.004,(alpha,lam,mu,estimate,true)
    print('SMALL_DEFICIT_COEFFICIENT_PASSED')

def optimal_parity():
    for m in (3,4,5,6,7,8):
        uniform=[1/m]*m
        variation=[(1+(-1)**i*0.55)/m for i in range(m)]
        if m%2:
            s=sum(variation)
            variation=[a/s for a in variation]
        product=lambda w: __import__('math').prod(w[i]+w[i-1] for i in range(m))
        bound=(2/m)**m
        assert abs(product(uniform)-bound)<1e-12
        if m%2==0:
            assert abs(product(variation)-bound)<1e-12
        else:
            assert product(variation)<bound-1e-8
        for _ in range(500):
            w=[RNG.random()+0.0001 for _ in range(m)]
            den=sum(w)
            w=[x/den for x in w]
            assert product(w)<=bound+1e-12
    print('SHARP_PARITY_OPTIMIZERS_PASSED')

def mean_check():
    # Regular polygon and equal edge weights: T=X+Y Gamma(2, rate), U=X/T uniform.
    for m in (3,4,5,6):
        P=2*m*sin(pi/m)
        alpha=pi-2*pi/m
        s=sin(alpha/2)
        c=cos(alpha/2)
        exact=m*P*(1-(s*s/c)*asinh(c/s))
        M=50000
        total=0.0
        sq=0.0
        for _ in range(M):
            z=sum(shortcut(RNG.expovariate(1/P),RNG.expovariate(1/P),alpha) for i in range(m))
            total+=z
            sq+=z*z
        ave=total/M
        se=sqrt(max(0.0,sq/M-ave*ave)/M)
        assert abs(ave-exact)<6*se,(m,ave,exact,se)
    print('EXACT_REGULAR_MEAN_PASSED')

if __name__=='__main__':
    finite_geometry()
    corner_asymptotics()
    optimal_parity()
    mean_check()
    print('ALL_CHECKS_PASSED')
