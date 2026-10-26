#!/usr/bin/env python3
"""Reproducibility checks for fixed-launch-velocity AOUP first-passage crossover.
Requires only the Python standard library. No stochastic simulation establishes the theorem.
"""
import math

XSTAR = 1 - 1 / math.sqrt(5)

def mu(x):
    return x - x*x/2

def m2(x):
    return 2*x/3 - x**3/3 + x**4/12

def Q(x):
    return 2/3 - x*x + x**3/3

def H0(x):
    return mu(x)**2-m2(x)/2

def A(g,x):
    if g == 0:
        return x/2-x*x/2+x**3/6
    k=math.sqrt(g)
    return ((1-x)-math.cosh(k*(1-x))/math.cosh(k)
            +math.sinh(k*x)/(k*math.cosh(k)))/g

def G(g,x,y):
    if g == 0:
        return min(x,y)
    k=math.sqrt(g)
    return math.sinh(k*min(x,y))*math.cosh(k*(1-max(x,y)))/(k*math.cosh(k))

def simpson(func,a,b,n=1200):
    h=(b-a)/n
    s=func(a)+func(b)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*func(a+h*j)
    return s*h/3

def B(g,x):
    f=lambda y:G(g,x,y)*(Q(y)+2*A(g,y))
    return simpson(f,0,x)+simpson(f,x,1)

def S(g):
    return -3*math.sqrt(5)*(2*mu(XSTAR)*A(g,XSTAR)-B(g,XSTAR)/2)

def fd_resolvent(g,forcing,N=1800):
    """Solve (g-dxx)u=f, u(0)=0,u'(1)=0 via an independent FD method."""
    h=1/N
    lower=[0.0]*(N+1)
    diag=[0.0]*(N+1)
    upper=[0.0]*(N+1)
    rhs=[0.0]*(N+1)
    diag[0]=1
    for i in range(1,N+1):
        x=i*h
        lower[i]=-2.0 if i==N else -1.0
        diag[i]=2+g*h*h
        if i<N:upper[i]=-1
        rhs[i]=h*h*forcing(i,x)
    # Thomas elimination
    for i in range(1,N+1):
        fac=lower[i]/diag[i-1]
        diag[i]-=fac*upper[i-1]
        rhs[i]-=fac*rhs[i-1]
    out=[0]*(N+1)
    out[N]=rhs[N]/diag[N]
    for i in range(N-1,-1,-1):
        out[i]=(rhs[i]-upper[i]*out[i+1])/diag[i]
    return out

def interp(a,x):
    t=x*(len(a)-1)
    j=int(t)
    return a[j]+(t-j)*(a[j+1]-a[j])

def close(u,v,tol,label):
    assert abs(u-v)<=tol,(label,u,v,abs(u-v))

checks=0
# Exact polynomial passive identity from the backward moment ODE.
for i in range(101):
    x=i/100
    close(H0(x),x*(5*x**3-20*x*x+24*x-8)/24,1e-13,"passive factor")
    checks+=1
close(H0(XSTAR),0.0,1e-14,"passive root")
close((H0(XSTAR+1e-5)-H0(XSTAR-1e-5))/2e-5,1/(3*math.sqrt(5)),1e-9,"root slope")
checks+=2

# Long-persistence (gamma=0) exact polynomial resolvents.
for i in range(101):
    x=i/100
    a=x/2-x*x/2+x**3/6
    b=2*x/3-x*x/3-x**3/6+x**4/6-x**5/30
    close(A(0,x),a,1e-14,"gamma-zero A")
    close(B(0,x),b,2e-10,"gamma-zero B")
    checks+=2
close(S(0),4/125,2e-10,"exact persistent drift coefficient")
checks+=1

# Discrete two-point boundary-value solver independent of the Green formula.
for g in [0.05,0.1,0.2,0.3,1.0,2.0,10.0,100.0]:
    n=1800
    aa=fd_resolvent(g,lambda i,x:1-x,n)
    bb=fd_resolvent(g,lambda i,x:Q(x)+2*aa[i],n)
    for frac in [.1,.25,XSTAR,.7,.9]:
        close(interp(aa,frac),A(g,frac),2.5e-7,"A independent FD")
        close(interp(bb,frac),B(g,frac),3.5e-7,"B independent FD")
        checks+=2
    ss=-3*math.sqrt(5)*(2*mu(XSTAR)*interp(aa,XSTAR)-interp(bb,XSTAR)/2)
    close(ss,S(g),2e-6,"slope independent FD")
    checks+=1

# Test entire moment BVP including derivatives of both orders and two boundaries.
for g in [0.05,0.2,1.0,4.0,10.0]:
    h=1e-4
    for j in range(1,100):
        x=j/100
        a2=(A(g,x+h)-2*A(g,x)+A(g,x-h))/h**2
        close(-a2+g*A(g,x),1-x,8e-6,"A differential equation")
        checks+=1
    close(A(g,0),0,1e-12,"A Dirichlet")
    close((A(g,1+h)-A(g,1-h))/(2*h),0,1e-7,"A Neumann")
    checks+=2

# Coefficient signs, crossover, and an asymptotic ratio check.
assert S(0.1)>0 and S(0.3)<0 and S(1)<0
close(S(0.1),0.01558541551044247,1e-9,"0.1 coefficient")
close(S(1),-0.06134317248316974,1e-9,"1 coefficient")
left,right=.1,.3
for _ in range(45):
    mid=(left+right)/2
    if S(mid)>0:left=mid
    else:right=mid
close((left+right)/2,0.21122136941008,3e-8,"numerical zero")
close(1000*S(1000),-1,3e-3,"fast relaxation asymptotic")
checks+=6
print("PASSED",checks,"deterministic checks")
print("passive xc = %.15f; S(0)=%.12f; S(0.1)=%.12f; S(1)=%.12f" % (XSTAR,S(0),S(.1),S(1)))
print("numerical sign-change location %.12f (no uniqueness assertion)" % ((left+right)/2))
