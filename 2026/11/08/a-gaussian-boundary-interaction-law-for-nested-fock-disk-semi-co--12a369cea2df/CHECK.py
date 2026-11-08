import math
from statistics import NormalDist
SQRT2PI=math.sqrt(2*math.pi)
PHI=NormalDist().cdf

def poisson_upper_array(lam,m):
    k=int(lam)
    mass=[0.0]*(m+1)
    mass[k]=math.exp(-lam+k*math.log(lam)-math.lgamma(k+1))
    for i in range(k-1,-1,-1):mass[i]=mass[i+1]*(i+1)/lam
    for i in range(k+1,m+1):mass[i]=mass[i-1]*lam/i
    # from upper tail to avoid 1-cdf cancellation
    tail=[0.0]*(m+1)
    s=0
    for i in range(m,-1,-1):
        tail[i]=s
        s+=mass[i]
    return tail

def exp_phi(a):
    return math.sqrt(2)/SQRT2PI*math.exp(-a*a/4)-a*PHI(-a/math.sqrt(2))

def compute(A,delta):
    B=A+delta*math.sqrt(A)
    m=int(max(A,B)+20*math.sqrt(max(A,B))+30)
    lo,hi=poisson_upper_array(min(A,B),m),poisson_upper_array(max(A,B),m)
    vals=[max(0,x*(1-y)) for x,y in zip(lo,hi)]
    t=sum(vals); t2=math.sqrt(sum(x*x for x in vals))
    norm=max(vals)
    a=abs(delta)
    theory1=math.sqrt(A)*exp_phi(a)
    theorymax=PHI(-a/2)**2
    return t,theory1,norm,theorymax,t2
for a in [0,1,2,-1]:
    for A in [100,400,1600]:
        t,t0,m,m0,s2=compute(A,a)
        assert abs(t/t0-1)<(0.25 if A==100 else 0.12 if A==400 else 0.08), (A,a,t,t0)
        assert abs(m-m0)<0.025,(A,a,m,m0)
        print(f'A={A} gap={a:+g} trace={t:.8f} asympt={t0:.8f} ratio={t/t0:.5f} opnorm={m:.6f} limit={m0:.6f}')
for x in range(15):
 for y in range(15):
    assert sum((x>=n+1 and y<=n) for n in range(15))==max(x-y,0)
print('NESTED_DISK_EDGE_CHECK_OK 225 exact count identities; 12 Gaussian asymptotic comparisons')
