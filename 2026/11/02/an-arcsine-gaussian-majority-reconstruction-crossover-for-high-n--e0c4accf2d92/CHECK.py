"""Independent finite-star and beta-surrogate checks for the high-noise approximation.
Run: python3 CHECK.py (Python standard library only). Finite checks are not infinite proofs.
"""
from fractions import Fraction as Q

def invariant(n, t):
    m=2*(n+1)
    states=[(h,k) for h in range(2) for k in range(n+1)]
    idx={s:i for i,s in enumerate(states)}
    G=[[Q(0) for _ in states] for _ in states]
    for i,(h,k) in enumerate(states):
        x=Q(k,n)
        plus=Q(n-k)*(Q(t,2)+(1 if h else 0))
        minus=Q(k)*(Q(t,2)+(0 if h else 1))
        flip=(1-x if h else x)+Q(t,2)
        for nxt,rate in [((h,k+1),plus),((h,k-1),minus),((1-h,k),flip)]:
            if rate:
                j=idx[nxt]
                G[i][j]+=rate
                G[i][i]-=rate
    A=[[G[j][i] for j in range(m)]+[Q(0)] for i in range(m)]
    A[-1]=[Q(1) for _ in range(m)]+[Q(1)]
    for i in range(m):
        piv=next(j for j in range(i,m) if A[j][i])
        A[piv],A[i]=A[i],A[piv]
        z=A[i][i]
        for h in range(i,m+1): A[i][h]/=z
        for j in range(m):
            if j!=i and A[j][i]:
                z=A[j][i]
                for h in range(i,m+1): A[j][h]-=z*A[i][h]
    return states, [row[-1] for row in A],G

checks=0
for n in range(1,9):
    for t in [Q(1,3),Q(1,2),Q(1),Q(2),Q(4)]:
        states,pi,G=invariant(n,t)
        E=lambda f:sum((p*f(h,k) for (h,k),p in zip(states,pi)),Q(0))
        kap=1+t
        D=2*kap**2-1
        for got,expect in [
            (sum(pi),Q(1)),
            (E(lambda h,k:Q(k,n)),Q(1,2)),
            (E(lambda h,k:Q(h)),Q(1,2)),
            (E(lambda h,k:(Q(k,n)-Q(1,2))**2),Q(n+D,4*(n*D+1))),
            (E(lambda h,k:(Q(h)-Q(1,2))*(Q(k,n)-Q(1,2))),kap*Q(n+1,4*(n*D+1))),
        ]:
            assert got==expect,(n,t,got,expect)
            checks+=1
        # Independently check stationary balance: pi*G=0.
        for j in range(len(states)):
            assert sum((pi[i]*G[i][j] for i in range(len(states))),Q(0))==0
            checks+=1
        assert all(p>0 for p in pi)
        checks+=1

print(f"PASS {checks} exact finite-state assertions")

# Exact rational Beta-binomial comparison for the independent-hub surrogate.
from math import comb, log, sqrt, pi

def polynomial_times(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def polynomial_power(a,n):
    r=[Q(1)]
    for _ in range(n):r=polynomial_times(r,a)
    return r

def surrogate_prob(n,t):
    k=1+t
    alpha=t/(2*k)
    moment=[Q(1)]
    for j in range(1,n+2):moment.append(moment[-1]*(alpha+j-1)/(2*alpha+j-1))
    ans={}
    for kk in range(n+1):
        pol=polynomial_times(polynomial_power([t/2/k,1/k],kk),polynomial_power([(1+t/2)/k,-1/k],n-kk))
        for h in [0,1]:
            polh=polynomial_times(pol, ([Q(1),Q(-1)] if h==0 else [Q(0),Q(1)]))
            ans[(h,kk)]=Q(comb(n,kk))*sum((v*moment[j] for j,v in enumerate(polh)),Q(0))
    assert sum(ans.values(),Q(0))==1
    return ans

surrogate_assertions=0
for n in range(1,9):
    for t in [Q(10),Q(30),Q(100),Q(300),Q(1000)]:
        states,pi,_=invariant(n,t)
        q=surrogate_prob(n,t)
        tv=sum((abs(pi[i]-q[s]) for i,s in enumerate(states)),Q(0))/2
        bound=4*log(n+1)/float(t)+1/(n+1)
        assert float(tv)<=bound+1e-12,(n,t,tv,bound)
        surrogate_assertions+=1
        assert all(v>=0 for v in q.values())
        surrogate_assertions+=1
# Check the variance/covariance predicted by the critical arcsine-Gaussian law.
for lam in [0.3,0.5,1,2,4]:
    for n in [10**5,10**6]:
        t=lam*sqrt(n); k=1+t; d=2*k*k-1
        vn=n*(n+d)/(4*(n*d+1))
        cn=sqrt(n)*k*(n+1)/(4*(n*d+1))
        assert abs(vn-(0.25+1/(8*lam*lam)))<0.035
        assert abs(cn-1/(8*lam))<0.01
        surrogate_assertions+=2
print(f"PASS {surrogate_assertions} additional exact-mixture and critical-moment checks")
