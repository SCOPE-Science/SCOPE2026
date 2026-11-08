"""Finite labeled-chain and limiting-moment checks for the star noisy-voter law.
No third-party publication content is included.
Run with: python verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import comb

def stationary(gen):
    n = len(gen)
    a = [[F(gen[j][i]) for j in range(n)] + [F(0)] for i in range(n)]
    a[-1] = [F(1)]*n + [F(1)]
    for j in range(n):
        pivot = next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot] = a[pivot],a[j]
        v=a[j][j]
        a[j]=[z/v for z in a[j]]
        for i in range(n):
            if i==j:continue
            v=a[i][j]
            if v:a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    result = [a[i][-1] for i in range(n)]
    assert all(t>=0 for t in result) and sum(result)==1
    return result

def lumped(b,q):
    ss=[(h,k) for h in (0,1) for k in range(b+1)]
    ind={s:i for i,s in enumerate(ss)}
    Q=[[F(0)]*len(ss) for i in ss]
    def jump(i,target,r):
        j=ind[target]
        Q[i][j]+=r;Q[i][i]-=r
    for i,(h,k) in enumerate(ss):
        if k<b:jump(i,(h,k+1),F(b-k)*(F(h)+q/2))
        if k:jump(i,(h,k-1),F(k)*(F(1-h)+q/2))
        jump(i,(1-h,k),F(k,b)+q/2 if h==0 else F(b-k,b)+q/2)
    return ss,stationary(Q)

def labeled(b,q):
    states=list(product((0,1),repeat=b+1))
    index={v:i for i,v in enumerate(states)}
    Q=[[F(0)]*len(states) for i in states]
    for i,state in enumerate(states):
        for loc in range(b+1):
            if loc==0:
                neigh=F(sum(state[1:]),b)
            else:neigh=F(state[0])
            rate=(neigh if state[loc]==0 else 1-neigh)+q/2
            v=list(state);v[loc]=1-v[loc]
            j=index[tuple(v)]
            Q[i][j]+=rate;Q[i][i]-=rate
    stat=stationary(Q)
    d={(h,k):F(0) for h in (0,1) for k in range(b+1)}
    for st,p in zip(states,stat):d[(st[0],sum(st[1:]))]+=p
    return d

def variance_formula(b,q):
    s=F(1)+F(1,b)
    u=s/(s+4*q+2*q*q)
    return (1+(b-1)*u)/(4*b)

def rising_ratio(t,m):
    out=F(1)
    for j in range(m):out*= (t+j)/(2*t+j)
    return out

def moment_beta(q,m,extra_z=0):
    c=1+q;a=q/(2*c)
    t=q*(q+2)/(2*c*c)
    # E[(a+Z/c)^m Z^extra_z] for Z~Beta(t,t)
    return sum((F(comb(m,j))*a**(m-j)/c**j*rising_ratio(t,j+extra_z) for j in range(m+1)),F(0))

def main():
    checks=0; listed=0
    for b in (2,3,4):
        for q in (F(1,2),F(1),F(2)):
            states,p=lumped(b,q)
            d=labeled(b,q)
            assert all(d[s]==v for s,v in zip(states,p))
            checks+=len(states)
            mean=sum(F(k,b)*v for (h,k),v in zip(states,p))
            v=sum((F(k,b)-F(1,2))**2*vv for (h,k),vv in zip(states,p))
            assert mean==F(1,2) and v==variance_formula(b,q)
            assert sum(F(h)*vv for (h,k),vv in zip(states,p))==F(1,2)
            checks+=3
            listed+=1
    for q in (F(1,4),F(1,2),F(1),F(2),F(5)):
        c=1+q;a=q/2
        for m in range(1,11):
            vm=moment_beta(q,m)
            vprev=moment_beta(q,m-1)
            wprev=moment_beta(q,m-1,1)
            assert c*vm==a*vprev+wprev
            wolder=moment_beta(q,m-2,1) if m>=2 else F(0)
            assert m*c*wprev==(m-1)*(1+a)*wolder+a*vprev+vm
            checks+=2
        t=q*(q+2)/(2*c*c)
        assert F(0)<t<F(1)
        assert moment_beta(q,1)==F(1,2)
        checks+=2
    for q in (F(1,2),F(1),F(2)):
        c=1+q;t=q*(q+2)/(2*c*c)
        vlim=1/(4*(1+4*q+2*q*q))
        assert vlim == 1/(c*c*4*(2*t+1))
        checks+=1
    print('PASS: exact finite labeled/lumped stationary comparisons =',listed)
    print('PASS: total exact generator, covariance and beta-moment identities =',checks)
    print('LIMIT: finite b enumeration is not used to prove the asymptotic convergence.')

if __name__=='__main__':main()
