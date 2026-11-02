#!/usr/bin/env python3
"""Numerical and rational checks for the interval-cover-time mean/variance claim.
No third-party packages; proofs and their scope are stated in RESULT.md.
"""
from fractions import Fraction as F
from math import cosh, sinh, tanh, sqrt

N = 0

def check(p, msg):
    global N
    assert p, msg
    N += 1

def moments(x, k):
    # L=D=1. Three first-passage problems: right, left, either.
    raw = []
    for u, a in ((x, 1.0), (1-x, 1.0), (x-.5, .5)):
        f = cosh(k*u)/cosh(k*a)
        derivative_r = f*(u*tanh(k*u)-a*tanh(k*a))/(2*k)
        raw.append(((1-f)/(k*k*f),
                    2*((1-f)+k*k*derivative_r)/(k**4*f*f)))
    m = raw[0][0]+raw[1][0]-raw[2][0]
    m2 = raw[0][1]+raw[1][1]-raw[2][1]
    return m, m2-m*m

def taylor_exp_bounds(t):
    # Rigorous rational enclosure at 0<=t<=3/2, 20th partial sum.
    nmax=20
    s=F(1); term=F(1)
    for n in range(1,nmax+1):
        term*=t/n
        s+=term
    first=term*t/(nmax+1)
    upper=s+first/(1-t/F(nmax+2))
    return s,upper

def opadd(a,b):return (a[0]+b[0],a[1]+b[1])
def opneg(a):return (-a[1],-a[0])
def opsub(a,b):return opadd(a,opneg(b))
def opmul(a,b):
    vals=[x*y for x in a for y in b]
    return min(vals),max(vals)
def opdiv(a,b):
    assert b[0]>0
    return opmul(a,(1/b[1],1/b[0]))
def opconst(x): return (F(x),F(x))
def hyperbolic(t):
    e=taylor_exp_bounds(t)
    inv=opdiv(opconst(1),e)
    return opdiv(opadd(e,inv),opconst(2)), opdiv(opsub(e,inv),opconst(2))

c05,s05=hyperbolic(F(1,2)); c1,s1=hyperbolic(F(1)); c15,s15=hyperbolic(F(3,2))
ve = opmul(s1,opsub(s1,opconst(1)))
vc = opdiv(opsub(opmul(opconst(10),opmul(s1,s1)),
                  opadd(opmul(opconst(11),s05),opmul(opconst(3),s15))),
           opmul(opconst(4),opadd(c1,opconst(1))))
Medge = opsub(c1,opconst(1))
Mcenter = opsub(opsub(opmul(opconst(3),c05),opdiv(opconst(2),c05)),opconst(1))
check(opsub(Mcenter,Medge)[0]>0, 'certified mean order')
check(opsub(ve,vc)[0]>0, 'certified variance order')
check(opdiv(opadd(c1,opconst(1)),opconst(2))[1] < F(7,5), 'mean-optimal polynomial region')
check(F(5)*(F(7,5)-1)**2-F(1)<0, 'certified derivative sign')
print('CERTIFIED mean(center)-mean(edge):',tuple(float(v) for v in opsub(Mcenter,Medge)))
print('CERTIFIED variance(edge)-variance(center):',tuple(float(v) for v in opsub(ve,vc)))

# Independent continuous numerical evaluations of the formulas.
for k in (0.4,0.7,1.0,1.2,1.45,1.8,2.4,3.2):
    for j in range(61):
        x=j/120
        m,v=moments(x,k)
        mr,vr=moments(1-x,k)
        check(abs(m-mr)<3e-9 and abs(v-vr)<3e-8, 'reflection symmetry')
        check(m>0 and v>0,'nonnegative moments')
        # Independent mean identity from three Laplace transforms.
        fr=cosh(k*x)/cosh(k)
        fl=cosh(k*(1-x))/cosh(k)
        fe=cosh(k*(x-.5))/cosh(k/2)
        alt=(1/fr+1/fl-1/fe-1)/(k*k)
        check(abs(m-alt)<2e-9,'independent mean decomposition')
# The κ=1 mean is strictly increasing from each endpoint towards the center.
last=moments(0,1)[0]
for j in range(1,501):
    cur=moments(j/1000,1)[0]
    check(cur>last,'sampled mean monotonicity');last=cur

# A discretized reflecting CTMC, independently solving a Laplace BVP.
def discrete_laplace(n,j,r,absorbing):
    h=1/n; D=1
    low=[0.0]*(n+1);diag=[0.0]*(n+1);up=[0.0]*(n+1);rhs=[0.0]*(n+1)
    target=set(absorbing)
    for i in range(n+1):
        if i in target:
            diag[i]=1.0;rhs[i]=1.0;continue
        moves=([(1,2/h**2)] if i==0 else ([(n-1,2/h**2)] if i==n else [(i-1,1/h**2),(i+1,1/h**2)]))
        diag[i]=r+sum(q for _,q in moves)
        for t,q in moves:
            if t==i-1: low[i]=-q
            elif t==i+1:up[i]=-q
    # Standard Thomas elimination.
    for i in range(1,n+1):
        w=low[i]/diag[i-1]
        diag[i]-=w*up[i-1]
        rhs[i]-=w*rhs[i-1]
    f=[0.0]*(n+1);f[n]=rhs[n]/diag[n]
    for i in range(n-1,-1,-1):f[i]=(rhs[i]-up[i]*f[i+1])/diag[i]
    return f[j]

def discrete_moments(n,j,r):
    h=1e-4
    v=[]
    for targets in ([n],[0],[0,n]):
        f=discrete_laplace(n,j,r,targets)
        df=(discrete_laplace(n,j,r+h,targets)-discrete_laplace(n,j,r-h,targets))/(2*h)
        v.append(((1-f)/(r*f),2*((1-f)+r*df)/(r*r*f*f)))
    m=v[0][0]+v[1][0]-v[2][0]
    m2=v[0][1]+v[1][1]-v[2][1]
    return m,m2-m*m
for n in (60,120,240):
    for frac in (0,.25,.5,.75,1):
        x=frac;j=round(n*x)
        M,V=discrete_moments(n,j,1)
        mm,vv=moments(x,1)
        check(abs(M-mm)<.012,'independent finite-grid mean')
        check(abs(V-vv)<.015,'independent finite-grid variance')
print('PASS',N,'checks, including certified rational Taylor interval inequalities and independent finite-grid killed generators')
