#!/usr/bin/env python3
"""Independent numerical checks for conditioned IOUP noise-quadrature formulas.

Pure Python standard library; analytic proof is in RESULT.md.
Run with python verify.py. Assertions sample finite cases; they do not prove the theorem.
"""
import math

CHECKS = 0

def near(x, y, rtol=1e-9, atol=1e-12):
    global CHECKS
    CHECKS += 1
    assert math.isfinite(x) and math.isfinite(y), (x, y)
    assert abs(x-y) <= atol + rtol*max(abs(x),abs(y)), (x, y)

def yes(v):
    global CHECKS
    CHECKS += 1
    assert v

def legendre_pair(n,x):
    p0,p1=1.0,x
    if n==0:return p0,0.0
    if n==1:return p1,p0
    for k in range(2,n+1):
        p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
    return p1,p0

def gauss(m,h):
    ans=[]
    for i in range(1,m+1):
        x=math.cos(math.pi*(i-0.25)/(m+0.5))
        for _ in range(20):
            pn,prev=legendre_pair(m,x)
            dp=m*(x*pn-prev)/(x*x-1)
            delta=pn/dp
            x-=delta
            if abs(delta)<1e-15:break
        pn,prev=legendre_pair(m,x)
        dp=m*(x*pn-prev)/(x*x-1)
        weight=h/((1-x*x)*dp*dp)
        ans.append((h*(1+x)/2,weight))
    return sorted(ans)

def v(t,a):
    return (-math.expm1(-a*t)/a, math.exp(-a*t)) if a>0 else (t,1.0)

def quad_var(a,h,m,kappa=1.0):
    nodes=gauss(m,h)
    # Direct weighted-variance pairwise formula avoids cancellation.
    value=sum(wi*wj*(v(ti,a)[0]-v(tj,a)[0])**2/h
              for i,(ti,wi) in enumerate(nodes)
              for tj,wj in nodes[i+1:])
    return kappa*kappa*value

def exact_var(a,h,kappa=1.0):
    if a==0:return kappa*kappa*h**3/12
    z=a*h
    # exact: kappa^2/a^2 * (int exp(-2at) - int exp(-at)^2/h)
    return kappa*kappa/a**2 * (-math.expm1(-2*z)/(2*a) - math.expm1(-z)**2/(a*a*h))

def condition_matrix(a,h,m):
    nodes=gauss(m,h)
    q00=sum(w*v(t,a)[0]**2 for t,w in nodes)
    q01=sum(w*v(t,a)[0]*v(t,a)[1] for t,w in nodes)
    q11=sum(w*v(t,a)[1]**2 for t,w in nodes)
    # H=(a,1)
    s=a*a*q00+2*a*q01+q11
    k0=(a*q00+q01)/s
    k1=(a*q01+q11)/s
    return q00-(a*q00+q01)**2/s, k0, k1, s

for m in range(1,10):
    for h in (0.2,0.5,1.0,3.0):
        rule=gauss(m,h)
        near(sum(w for _,w in rule),h,rtol=1e-13)
        for r in range(2*m):
            approx=sum(w*t**r for t,w in rule)
            near(approx,h**(r+1)/(r+1),rtol=5e-11)
        for a in (0.,0.01,0.2,1.,3.,10.):
            for t,w in rule:
                near(a*v(t,a)[0]+v(t,a)[1],1,rtol=1e-12)
            direct,k0,k1,s=condition_matrix(a,h,m)
            near(s,h,rtol=5e-13)
            near(direct,quad_var(a,h,m),rtol=1e-7,atol=1e-11)
            near(a*k0+k1,1,rtol=1e-12)
            if m==1:
                near(quad_var(a,h,m),0.)
                near(k0,v(h/2,a)[0])
            else:
                yes(quad_var(a,h,m)>0)
                if a>0:
                    # Exact positive variance is positive for positive rate.
                    yes(exact_var(a,h)>0)

for a in (0.,0.01,0.2,1.,3.):
    for h in (0.3,1.,2.):
        numerical=quad_var(a,h,2)
        explicit=h*math.exp(-a*h)*math.sinh(a*h/(2*math.sqrt(3)))**2/a**2 if a else h**3/12
        near(numerical,explicit,rtol=1e-9)
        if a:
            yes(quad_var(a,h,5)>0)
            near(quad_var(a,h,9),exact_var(a,h),rtol=1e-6)
        else:
            near(exact_var(a,h),h**3/12)

# The prescribed one-node rule yields zero posterior covariance at all mesh points
# for exact initial state and EKL observation, since each next prediction has rank 1.
for a in (0.,0.5,1.,4.):
    h=.35
    cov=[[0.,0.],[0.,0.]]
    for step in range(1,15):
        t,w=gauss(1,h)[0]
        x,y=v(t,a)
        qp=[[w*x*x,w*x*y],[w*x*y,w*y*y]]
        s=a*a*qp[0][0]+2*a*qp[0][1]+qp[1][1]
        u=[qp[0][0]*a+qp[0][1],qp[1][0]*a+qp[1][1]]
        cp=[[qp[i][j]-u[i]*u[j]/s for j in range(2)] for i in range(2)]
        for row in cp:
            for val in row:near(val,0,atol=5e-15)
        cov=cp

for a in (0.1,0.5,1.,3.,8.):
    for h in (0.1,0.3,1.,2.):
        midpoint = h*(-math.expm1(-a*h/2))/a
        exact = h/a + math.expm1(-a*h)/(a*a)
        error=midpoint-exact
        analytic=math.exp(-a*h/2)*(2*math.sinh(a*h/2)-a*h)/a**2
        near(error,analytic,rtol=1e-8,atol=1e-12)
        yes(error>0)
        # For exact process covariance, Kalman gain reproduces the exact solution.
        k0_exact=exact/h
        near(h*k0_exact,exact)
        near(h*v(h/2,a)[0],midpoint)

for h in (0.5,1.0):
    for m in (2,3,4,5):
        # Stiff-mode quadrature output becomes exponentially small while exact is ~1/(2a^3).
        vals=[]
        for a in (5.,15.,40.,1000.):
            vals.append(quad_var(a,h,m)/exact_var(a,h))
        yes(vals[-1]<vals[0])
        yes(vals[-1]<0.015)

print('PASS: %d numerical and quadrature assertions' % CHECKS)
print('h=a=1: midpoint numerical mean',1-math.exp(-0.5),'exact mean',math.exp(-1),
      'exact covariance',exact_var(1,1),'1-node covariance',quad_var(1,1,1),
      '2-node covariance',quad_var(1,1,2))
