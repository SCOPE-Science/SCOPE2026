"""Standalone arithmetic and numerical checks for the priced cyclic-ladder design theorem.
Standard-library Python 3; the analytic proof, not these finite checks, handles all parameters.
"""
from fractions import Fraction
from math import acos, acosh, cos, pi, sqrt, tanh, log, isfinite
import random

NTEST=0

def check(cond, info=''):
    global NTEST
    NTEST+=1
    if not cond: raise AssertionError(info)

def cheb(n,x):
    if n==0:return 1
    a,b=1,x
    for k in range(2,n+1):a,b=b,2*x*b-a
    return b

def exact_tree_formula(n,a,b):
    t=Fraction(b,a)
    return Fraction(n*a**(2*n-1))* (cheb(n,1+t)-1)

def minor(n,a,b):
    N=2*n; L=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(n):
        for u,v,w in ((i,(i+1)%n,a),(i+n,(i+1)%n+n,a),(i,i+n,b)):
            L[u][u]+=w;L[v][v]+=w;L[u][v]-=w;L[v][u]-=w
    return [row[:-1] for row in L[:-1]]

def bareiss(A):
    A=[row[:] for row in A];N=len(A);last=1
    if N==0:return 1
    for k in range(N-1):
        pivot=A[k][k]
        check(pivot!=0,'zero pivot')
        for i in range(k+1,N):
            for j in range(k+1,N):
                q,r=divmod(A[i][j]*pivot-A[i][k]*A[k][j],last)
                check(r==0,'noninteger Bareiss step')
                A[i][j]=q
        for i in range(k+1,N):A[i][k]=0
        last=pivot
    return A[-1][-1]

def Sn(n,t):
    return sum(1/(t+1-cos(2*pi*k/n)) for k in range(n))

def Hn(n,t):
    s=Sn(n,t)
    return 2*s/(2*n-1-t*s)

def optimum_t(n,P,Q):
    ratio=Q/P
    lo=1e-15;hi=1e15
    check(Hn(n,lo)>ratio and Hn(n,hi)<ratio,'root bracket')
    for _ in range(120):
        mid=(lo+hi)/2
        if Hn(n,mid)>ratio:lo=mid
        else:hi=mid
    return (lo+hi)/2

def logdet_spd(A):
    m=len(A); L=[[0.0]*m for _ in range(m)]
    for i in range(m):
        for j in range(i+1):
            v=A[i][j]-sum(L[i][k]*L[j][k] for k in range(j))
            if i==j:
                if v<=0:return float('-inf')
                L[i][j]=sqrt(v)
            else:L[i][j]=v/L[j][j]
    return 2*sum(log(L[i][i]) for i in range(m))

def continuous_minor(n,weights):
    N=2*n;L=[[0.0]*N for _ in range(N)]
    edges=[]
    for i in range(n):
        edges += [(i,(i+1)%n),(i+n,(i+1)%n+n)]
    edges += [(i,i+n) for i in range(n)]
    for (u,v),w in zip(edges,weights):
        L[u][u]+=w;L[v][v]+=w;L[u][v]-=w;L[v][u]-=w
    return [row[:-1] for row in L[:-1]]

for n in range(3,9):
    for a in (1,2,5):
        for b in (1,3,7):
            x=bareiss(minor(n,a,b));y=exact_tree_formula(n,a,b)
            check(x==y,(n,a,b,x,y))

for n in (3,4,5,9,17,40):
    for t in (.0001,.01,.1,.5,1.,2.,10.,100.):
        eta=acosh(1+t)
        rhs=n/sqrt(t*(t+2))/tanh(n*eta/2)
        check(abs(Sn(n,t)-rhs)<1e-6*max(1,rhs),(n,t))
    for j in range(-15,15):
        lo=10**(j/5); hi=lo*1.03
        check(Hn(n,lo)>Hn(n,hi),('H not decreasing',n,lo,hi))

rng=random.Random(20261030)
for n in (3,4,5,7):
    for P,Q in ((1,1),(1,5),(5,1),(3,11)):
        B=15.0
        t=optimum_t(n,P,Q)
        a=B/(n*(2*P+Q*t)); b=t*a
        costs=[P]*(2*n)+[Q]*n
        expected=logdet_spd(continuous_minor(n,[a]*(2*n)+[b]*n))
        analytic=log(float(exact_tree_formula(n,1,1))) if a==b==1 else (log(n)+(2*n-1)*log(a)+log(cheb(n,1+t)-1))
        check(abs(expected-analytic)<1e-8,('logdet mismatch',n,P,Q,expected,analytic))
        check(abs(Hn(n,t)-Q/P)<1e-8,('stationarity',n,P,Q))
        for rep in range(90):
            raw=[rng.expovariate(1) for _ in range(3*n)]
            spend=sum(c*w for c,w in zip(costs,raw))
            weights=[w*B/spend for w in raw]
            cand=logdet_spd(continuous_minor(n,weights))
            check(cand<=expected+1e-8,('candidate better than optimum',n,P,Q,rep,expected,cand))

for n in (3,4,8,17):
    for ratio in (1e-7,1e7):
        t=optimum_t(n,1.,ratio)
        fraction=ratio*t/(2+ratio*t)
        target=n/(2*n-1) if ratio<1 else 1/(2*n-1)
        check(abs(fraction-target)<1e-4,('extreme price',n,ratio,fraction,target))

# Critical scaling: increasing n gives the predicted finite crossover.
def g(u):
    z=sqrt(u/2)
    return 1/(2*z*tanh(z))

def u_root(k):
    lo=1e-9;hi=1e5
    for _ in range(110):
        m=(lo+hi)/2
        if g(m)>k:lo=m
        else:hi=m
    return (lo+hi)/2

for k in (.25,1.,4.):
    u=u_root(k)
    errors=[]
    for n in (60,120,240):
        val=n*n*optimum_t(n,1.,k*n)
        errors.append(abs(val-u))
        check(abs(val-u)< max(1.,u)*7/n,('critical bound',n,k,val,u))
    check(errors[2]<errors[1]<errors[0],('critical convergence',k,errors))

print('PASS:',NTEST,'checks; exact integer matrix-tree identities, spectral resolvent,',
      'monotonicity, independent-weight competitors, boundary prices, critical crossover')
