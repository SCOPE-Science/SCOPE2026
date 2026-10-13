from fractions import Fraction
from math import exp, sqrt, e

def exact_u(a,b,u0,t):
    R=b*u0/a
    return u0*exp(-a*t)/(1+R*(1-exp(-a*t)))

def closed_trunc(a,b,u0,N,t):
    R=b*u0/a
    z=R*(1-exp(-a*t))
    return u0*exp(-a*t)*sum((-z)**k for k in range(N))

def triangular_rhs(a,b,N,y):
    out=[]
    for j in range(1,N+1):
        val=-j*a*y[j-1]
        if j < N:
            val -= j*b*y[j]
        out.append(val)
    return out

# Finite-difference replay of the actual triangular finite section
# for several orders and parameter choices.
for a,b,u0 in [(2.0,3.0,0.4),(1.0,2.0,1.0),(3.0,1.0,4.0)]:
    R=b*u0/a
    for N in range(1,8):
        for t in (0.07,0.3,0.8):
            z=R*(1-exp(-a*t))
            # general closed form for every lifted component
            ys=[]
            for j in range(1,N+1):
                s=0.0
                for k in range(N-j+1):
                    # binomial(j+k-1,k)
                    import math
                    s += math.comb(j+k-1,k)*((-z)**k)
                ys.append((u0**j)*exp(-j*a*t)*s)
            h=1e-6
            ysp=[]
            ysm=[]
            for tt, dest in ((t+h,ysp),(t-h,ysm)):
                zz=R*(1-exp(-a*tt))
                for j in range(1,N+1):
                    import math
                    s=sum(math.comb(j+k-1,k)*((-zz)**k) for k in range(N-j+1))
                    dest.append((u0**j)*exp(-j*a*tt)*s)
            fd=[(p-m)/(2*h) for p,m in zip(ysp,ysm)]
            rhs=triangular_rhs(a,b,N,ys)
            assert max(abs(x-y) for x,y in zip(fd,rhs)) < 2e-5
            assert abs(ys[0]-closed_trunc(a,b,u0,N,t)) < 1e-12
            u=exact_u(a,b,u0,t)
            assert abs(abs(ys[0]-u)/u - z**N) < 2e-12

# Critical R=1 exact maximizing point and asymptotic trend.
for N in (1,2,5,10,50,200):
    x=(N+1-sqrt(N*N+1))/N
    assert 0 < x < 1
    # derivative numerator vanishes
    assert abs(N*x*x-2*(N+1)*x+2) < 1e-10
    val=x*((1-x)**N)/(2-x)
    if N >= 50:
        assert abs((2*e*N)*val - 1) < 0.08

# Lifted Rayleigh quotient under the source-prescribed scaling.
for R in (1.1,1.5,2.0,4.0):
    a=2.0
    c=(1+R)*a/2
    N=int((R+3)/(R-1))+2
    ray=-a*N*(N+1)/2 + c*N*(N-1)/2
    closed=N/2*((c-a)*N-(a+c))
    assert abs(ray-closed) < 1e-10
    assert ray > 0

print("VERIFY_OK")
