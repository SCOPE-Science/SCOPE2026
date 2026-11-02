"""Reproduce exact clipped-quadratic birth-death identities (Python standard library)."""
from fractions import Fraction as F
from math import cos, cosh, exp, pi, sqrt, sinh, tanh

checks = 0

def check(condition, context):
    global checks
    if not condition:
        raise AssertionError(context)
    checks += 1

def clip(a,c):
    return min(max(a,-c),c)

def weights(N,p):
    q=1-p
    w=[(q/p)**j for j in range(N+1)]
    z=sum(w)
    return [x/z for x in w]

def transition(N,p):
    q=1-p
    M=[[F(0) for _ in range(N+1)] for _ in range(N+1)]
    for j in range(N+1):
        M[j][max(j-1,0)] +=p
        M[j][min(j+1,N)] +=q
    return M

def characteristic_value(N,p,z):
    q=1-p
    d0=1.
    d1=z-float(p)
    for _ in range(2,N+1):
        d0,d1=d1,z*d1-float(p*q)*d0
    return (z-float(q))*d1-float(p*q)*d0

for N in range(1,37):
    c=F(1,N)
    for p in (F(1,4),F(2,5),F(1,2),F(3,5),F(3,4)):
        q=1-p
        P=transition(N,p)
        w=weights(N,p)
        check(sum(w)==1,(N,p,'norm'))
        check(all(sum(row)==1 for row in P),(N,p,'rows'))
        check(all(sum(w[j]*P[j][k] for j in range(N+1))==w[k] for k in range(N+1)),(N,p,'invariant'))
        for j in range(N+1):
            x=-q+j*c
            check(x-clip(x+q,c)==-q+max(j-1,0)*c,(N,p,j,'plus'))
            check(x-clip(x-p,c)==-q+min(j+1,N)*c,(N,p,j,'minus'))
        # The two deterministic pure-noise runs reset to either endpoint in N steps.
        for x0 in (-F(7,3),-F(1,2),F(0),F(1,2),F(7,3)):
            x=x0
            for _ in range(5*N+10):
                x=x-clip(x+q,c)
            check(x==-q,(N,p,x0,'plus reset'))
            x=x0
            for _ in range(5*N+10):
                x=x-clip(x-p,c)
            check(x==p,(N,p,x0,'minus reset'))

for N in range(1,15):
    for p in (F(1,4),F(2,5),F(1,2),F(3,5),F(3,4)):
        q=1-p
        check(abs(characteristic_value(N,p,1.))<2.e-9,(N,p,'eigenone'))
        for k in range(1,N+1):
            lam=2*sqrt(float(p*q))*cos(k*pi/(N+1))
            check(abs(characteristic_value(N,p,lam))<2.e-9,(N,p,k,'spectral'))

for N in range(1,61):
    m=F(N,2)
    g=lambda j:(m*m+m+F(1,3))*(F(j)-m)-(F(j)-m)**3/3
    var=F(N*(N+2),12)
    longvar=F(N*(N+2)*(2*N*N+4*N-1),60)
    check(all(g(j)-(g(max(j-1,0))+g(min(j+1,N)))/2==F(j)-m for j in range(N+1)),(N,'poisson'))
    cov=sum((F(j)-m)*g(j) for j in range(N+1))/F(N+1)
    check(2*cov-var==longvar,(N,'longvar'))
    check(longvar/var==F(2*N*N+4*N-1,5),(N,'IAT'))

# Critical finite-size window p_N=1/2 + theta/N.
def continuous_mean_var(theta):
    if theta==0: return 0.,1./12
    mean=1/(4*theta)-0.5/tanh(2*theta)
    var=1/(16*theta**2)-1/(4*sinh(2*theta)**2)
    return mean,var

def discrete_mean_var(N,theta):
    p=.5+theta/N
    q=1-p
    log_r=__import__('math').log(q/p)
    logs=[j*log_r for j in range(N+1)]
    shift=max(logs)
    v=[exp(t-shift) for t in logs]
    zz=sum(v)
    positions=[-q+j/N for j in range(N+1)]
    mu=sum(x*w for x,w in zip(positions,v))/zz
    va=sum((x-mu)**2*w for x,w in zip(positions,v))/zz
    return mu,va

for theta in (-2.,-1.,-.3,0.,.3,1.,2.):
    true_mu,true_var=continuous_mean_var(theta)
    for N in (300,1200):
        mu,va=discrete_mean_var(N,theta)
        check(abs(mu-true_mu)<.015,(theta,N,'critical mean'))
        check(abs(va-true_var)<.015,(theta,N,'critical variance'))
        p=.5+theta/N
        gap=1-2*sqrt(p*(1-p))*cos(pi/(N+1))
        expected=pi*pi/2+2*theta*theta
        check(abs(N*N*gap-expected)<.07,(theta,N,'critical spectral gap'))

print(f'PASS: {checks} exact-rational and numerical check groups')
