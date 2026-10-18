"""Deterministic reproducibility checks for a two-edge quadratic Brownian conditioning theorem.

Uses only the Python standard library. Finite computations check exact kernels,
resolvents, and their predicted limits; they do not establish asymptotic theorems.
"""
import cmath
import math

checks = 0

def close(a, b, tol=1e-9):
    global checks
    assert abs(a-b) <= tol * (1.0 + abs(a) + abs(b)), (a, b, tol)
    checks += 1


def kernel(T, u, s, t):
    w = cmath.sqrt(2*u)
    return (cmath.sinh(w*min(s,t))*cmath.cosh(w*(T-max(s,t))) /
            (w*cmath.cosh(w*T)))


def mean(T, u, x, t):
    w = cmath.sqrt(2*u)
    return x*cmath.cosh(w*(T-t))/cmath.cosh(w*T)


def tilde(T, u, x):
    w = cmath.sqrt(2*u)
    return cmath.exp(-w*x*x*cmath.tanh(w*T)/2) / cmath.sqrt(cmath.cosh(w*T))


def limit_early(w,s,t):
    return (cmath.exp(-w*abs(s-t))-cmath.exp(-w*(s+t)))/(2*w)


def limit_late(w,r,s):
    return (cmath.exp(-w*abs(r-s))+cmath.exp(-w*(r+s)))/(2*w)


def tridiagonal_solve(diagonal,offdiag,rhs):
    n=len(diagonal); d=list(diagonal); b=list(rhs)
    for i in range(1,n):
        t=offdiag/d[i-1]
        d[i]-=t*offdiag
        b[i]-=t*b[i-1]
    out=[0.0]*n
    out[-1]=b[-1]/d[-1]
    for i in range(n-2,-1,-1):
        out[i]=(b[i]-offdiag*out[i+1])/d[i]
    return out

for theta,x in ((.5,-1.1),(1.,.7),(2.,2.0)):
    u=1/(8*theta*theta); w=1/(2*theta)
    for T in (100.0, 180.0):
        for s in (0.0,.2,.9,2.2):
            close(mean(T,u,x,s),x*math.exp(-w*s),1e-8)
            close(mean(T,u,x,T-s),0.0,1e-8)
            for t in (0.0,.5,1.4,2.5):
                close(kernel(T,u,s,t),limit_early(w,s,t),1e-8)
                close(kernel(T,u,T-s,T-t),limit_late(w,s,t),1e-8)
                close(kernel(T,u,s,T-t),0.,1e-8)
                close(kernel(T,u,s,t),kernel(T,u,t,s),1e-10)
        close(kernel(T,u,T,T),2*theta,1e-8)
        close(kernel(T,u,T/2,T/2),theta,2e-5)
        close(tilde(T,u,x)*cmath.sqrt(cmath.cosh(w*T)),math.exp(-w*x*x*math.tanh(w*T)/2),1e-9)

# Saddle curvature of f(u) = theta*u - sqrt(2*u)/2.
for theta in (.4, .8, 1., 2.5):
    u=1/(8*theta*theta)
    close(theta-1/(2*math.sqrt(2*u)),0)
    close(1/(2*(2*u)**1.5), 4*theta**3) # second derivative f'' = 1/(2*(2u)^1.5)

# Green kernel boundary values, flux at the endpoint and jump of first derivative.
for T,u in ((4., .12),(7.,.25),(11.,1.0)):
    for t in (T/4,T/2,3*T/4):
        close(kernel(T,u,0,t),0)
        h=1e-5
        deriv_jump=(kernel(T,u,t+h,t)-kernel(T,u,t,t))/h - (kernel(T,u,t,t)-kernel(T,u,t-h,t))/h
        close(deriv_jump,-1,3e-5)
        deriv_end=(kernel(T,u,T,t)-kernel(T,u,T-h,t))/h
        close(deriv_end,0,3e-5)

# Discrete Gaussian quadratic-penalty resolvent tends to the exact continuum kernel.
for T,u,x in ((4.,.125,.7),(4.,.5,-.8),(6.,.25,1.3)):
    N=480
    dt=T/N
    main=[(2 if i<N-1 else 1)/dt + (2 if i<N-1 else 1)*u*dt for i in range(N)]
    off=-1/dt
    rhs=[0.]*N;rhs[0]=x/dt
    md=tridiagonal_solve(main,off,rhs)
    for i in (0,N//5,N//2,N-1):
        close(md[i],mean(T,u,x,(i+1)*dt),.02)
    for j in (N//5,N//2,N-1):
        unit=[0.]*N;unit[j]=1
        column=tridiagonal_solve(main,off,unit)
        for i in (0,N//4,N//2,N-1):
            close(column[i],kernel(T,u,(i+1)*dt,(j+1)*dt),.02)

# A Gaussian terminal exponential tilt changes only means, by covariance times mu.
for theta,mu in ((.5,-1.2),(1.,.6),(2.,2.)):
    w=1/(2*theta)
    for r in (0,.5,1.2,2.1):
        close(mu*limit_late(w,r,0),2*theta*mu*math.exp(-r/(2*theta)))
        close(limit_late(w,0,0),2*theta)
        close(limit_late(w,4.,4.),theta*(1+math.exp(-4/theta)))

print(f'PASS: {checks} deterministic kernel, finite-resolvent, and boundary-limit checks.')
