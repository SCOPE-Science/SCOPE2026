"""Supplementary finite arithmetic checks for harmonic Bergman spectral outliers.

Run: python3 checker.py
Finite truncations are numerical consistency tests, not infinite-dimensional proofs.
"""
import cmath
import math


def constant(n):
    return n*(n+5)/6


def root(n):
    c=constant(n)
    lo,hi=1.,2.
    def s(r):
        return sum(r**k for k in range(n))
    while s(hi)<c:
        hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if s(mid)<c:lo=mid
        else:hi=mid
    return (lo+hi)/2


def synth(p,alpha):
    """Ascending-coefficient synthetic division by z-alpha."""
    d=len(p)-1
    q=[0j]*d
    q[-1]=p[-1]
    for j in range(d-1,0,-1):
        q[j-1]=p[j]+alpha*q[j]
    return q, p[0]+alpha*q[0]


def gram_h(n,z,w):
    return sum((j+1)*(n-j+1)/(n+1)*z**(n-1-j)*w**j
               for j in range(n))


def projected_weight(j,s):
    # exactly the coefficient against the normalized mode j+s
    return 2*math.sqrt((abs(j)+1)*(abs(j+s)+1)) / (
        abs(j)+abs(j+s)+s+2)


def eigen_residual(n,t,N):
    c=constant(n)
    a=c*t**(n-1)
    alpha=t*cmath.exp(1j*math.pi/(n-1))
    lam=(1-1/c)*a*alpha
    assert abs(alpha**(n-1)+a/c)<1e-12
    hc=[(n-j)*(j+2)/(n+1)*alpha**(n-j-1) for j in range(n)]
    hc[0]+=a
    assert abs(sum(hc[j]*alpha**j for j in range(n)))<1e-9
    p=[-lam,a]+[0j]*(n-2)+[1]
    q,rem=synth(p,alpha)
    num=[0j]+[-v for v in hc]
    numq,rem2=synth(num,alpha)
    assert abs(rem)<1e-8 and abs(rem2)<1e-8
    # f(z)=numq(z)/q(z); coefficients from the nonvanishing denominator q(0).
    f=[0j]*(N+1)
    for k in range(N+1):
        val=numq[k] if k<len(numq) else 0j
        for j in range(1,min(k,len(q)-1)+1):
            val-=q[j]*f[k-j]
        f[k]=val/q[0]
    v=[0j]*(2*N+1)
    for j in range(-N,N+1):
        if j<0:v[j+N]=math.sqrt(1-j)*alpha**(-j)
        elif j==0:v[j+N]=1
        else:v[j+N]=f[j]/math.sqrt(j+1)
    w=[0j]*(2*N+1)
    for j in range(-N,N+1):
        for s,coefficient in ((1,a),(n,1)):
            if j+s<=N:
                w[j+s+N]+=coefficient*projected_weight(j,s)*v[j+N]
        w[j+N]-=lam*v[j+N]
    return math.sqrt(sum(abs(x)**2 for x in w)/sum(abs(x)**2 for x in v))


def run():
    assertions=0
    for n in range(2,151):
        c=constant(n)
        r=root(n)
        t0=1/r
        ts=(n-1)*c/(n*(c-1))
        assert 0<t0<ts<1; assertions+=1
        assert abs(sum(r**k for k in range(n))-c)/c <2e-11;assertions+=1
        amin=c*t0**(n-1)
        assert amin>1;assertions+=1
        def delta(t):return c*t**(n-1)-1-(c-1)*t**n
        assert abs(delta(t0))<2e-8*max(1,c);assertions+=1
        assert abs(delta(1))<2e-8*max(1,c);assertions+=1
        assert delta(ts)>0;assertions+=1
        assert abs(delta(ts)-(c/n*ts**(n-1)-1))<2e-10*max(1,c);assertions+=1
        for frac in (.05,.17,.33,.5,.72,.91,.99):
            t=t0+(1-t0)*frac
            a=c*t**(n-1)
            radius=(1-1/c)*a*t
            assert abs((a-1-radius)-delta(t))<2e-8*max(1,c);assertions+=1
            assert delta(t)>0;assertions+=1
        # The other roots of the cancellation quotient have modulus >=r:
        # if |z|<r, sum |z|^j < c-1, so no root.
        for rho in (0,.25,.7,.99):
            mag=r*rho
            assert sum(mag**j for j in range(1,n))<c-1;assertions+=1
    for n,t,N,cutoff in ((2,.86,380,1e-8),(3,.86,380,1e-8),
                         (4,.9,400,1e-9),(5,.90,500,1e-7),
                         (8,.94,600,1e-6)):
        assert 1/root(n)<t<1
        err=eigen_residual(n,t,N)
        print(f'n={n}: normalized truncated Toeplitz eigen-residual {err:.3g}')
        assert err<cutoff;assertions+=1
    for n in (100,1000,10000):
        c=constant(n); ts=(n-1)*c/(n*(c-1))
        maxgap=(c/n)*ts**(n-1)-1
        print(f'n={n}: maximal gap divided by degree {maxgap/n:.12g} (limit {1/(6*math.e):.12g})')
        assert maxgap/n>0;assertions+=1
    print(f'PASS: {assertions} supplementary checks')

if __name__=='__main__':run()
