"""Exact-rational checks for the star-Laplacian two-step SLQ theorem.

This is a finite regression test, not a proof of the asymptotic statements.
Requires only the Python 3 standard library.
"""
from fractions import Fraction as F
from math import comb, sqrt


def dot(u, v):
    return sum(x*y for x,y in zip(u,v))


def star_mv(v):
    n=len(v)
    return [(n-1)*v[0]-sum(v[1:])] + [x-v[0] for x in v[1:]]


def trace(n,t):
    return 1/t + F(n-2,1)/(t+1) + 1/(t+n)


def direct_resolvent(s,t):
    n=len(s)
    x0=(s[0]*(t+1)+sum(s[1:]))/(t*(t+n))
    xi=[(si+x0)/(t+1) for si in s[1:]]
    x=[x0]+xi
    # verify every component of (tI+L)x=s independently
    assert [t*xj+y for xj,y in zip(x,star_mv(x))]==list(s)
    return dot(s,x)


def data(n,k,t):
    assert n>=3 and 0<=k<=n-1 and t>0
    s=[F(1)]+[-F(1)]*k+[F(1)]*(n-1-k)
    norm=F(n)
    cur=s
    moments=[F(1)]
    for j in range(1,4):
        cur=star_mv(cur)
        moments.append(dot(s,cur)/norm)
    m1,m2,m3=moments[1:]
    assert m1==F(4*k,n)
    assert m2==F(4*k*(k+1),n)
    assert m3==F(4*k*((n+1)*k+1),n)
    w0=F((n-2*k)**2,n*n)
    wn=F(4*k*k,n*n*(n-1))
    w1=1-w0-wn
    assert w1==F(4*k*(n-1-k),n*(n-1))
    assert w0>=0 and w1>=0 and wn>=0 and w0+w1+wn==1
    Q=norm*(w0/t+w1/(t+1)+wn/(t+n))
    assert Q==direct_resolvent(s,t)
    T1=norm/(t+m1)
    if k==0:
        T2=norm/t
        assert Q==T1==T2
        return T1,T2,Q
    beta2=m2-m1*m1
    assert beta2>0
    alpha1=(m3-2*m1*m2+m1**3)/beta2
    r=[li-m1*si for li,si in zip(star_mv(s),s)]
    assert dot(r,r)/norm==beta2
    assert dot(r,star_mv(r))/dot(r,r)==alpha1
    d0=m1*alpha1-beta2
    assert d0==F(4*k*k*(n-1-k), n+(n-4)*k)
    Dt=(t+m1)*(t+alpha1)-beta2
    assert Dt>0 and Dt>=d0>=0
    T2=norm*(t+alpha1)/Dt
    error=F((n-2*k)**2,1)*d0/(t*(t+1)*(t+n)*Dt)
    assert Q-T2==error and error>=0
    assert (error==0)==(k==n-1 or 2*k==n)
    assert error<=F((n-2*k)**2,1)/(t*(t+1)*(t+n))
    return T1,T2,Q


def main():
    checks=0
    tvalues=[F(1,7), F(1,2), F(1), F(3,2), F(3),F(7)]
    for n in range(3,21):
        for k in range(n):
            for t in tvalues:
                t1,t2,q=data(n,k,t)
                assert t1>0 and t2>0 and q>0
                checks+=1
        for t in tvalues:
            tau=trace(n,t)
            unbiased=sum(F(comb(n-1,k),2**(n-1))*data(n,k,t)[2] for k in range(n))
            assert tau==unbiased
            bias=sum(F(comb(n-1,k),2**(n-1))*(data(n,k,t)[2]-data(n,k,t)[1]) for k in range(n))
            assert bias>0
            checks+=1
    # Asymptotic diagnostics for representative centered-binomial deviations.
    for t in [F(1,2),F(1),F(2),F(5)]:
        for n in [400,2500,10000]:
            for y in [-2,-1,0,1,2]:
                k=max(0,min(n-1,round((n-y*sqrt(n))/2)))
                x=(n-2*k)/sqrt(n)
                t1,t2,q=data(n,k,t)
                approximated=x*x/float(t*(t+1)**2)
                err=float(q-t2)
                assert abs(err-approximated)<0.15 + 10/n
                checks+=1
    print(f'VERIFY_OK exact_and_asymptotic_diagnostic_groups={checks}')

if __name__=='__main__': main()
