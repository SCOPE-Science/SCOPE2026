#!/usr/bin/env python3
"""Independent arithmetic checks for finite-field radical-square-zero quiver algebra regularity."""
from itertools import product
from math import comb, exp, lgamma, log, floor

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        # F4 = F2[alpha]/(alpha^2+alpha+1), elements a0 + 2*a1*alpha
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        return ((a0*b0)^(a1*b1)) | (((a0*b1)^(a1*b0)^(a1*b1))<<1)
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)

def check_case(q,n,full_nonregular_bruteforce=False):
    f=Field(q)
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    ell=len(edges); d=n+ell
    N=[0]*(n+1); checked=0; brute=0
    for u in product(range(q),repeat=d):
        a=u[:n]; b=u[n:]
        zeros=sum(x==0 for x in a)
        isreg=all(x==0 or a[i]!=0 or a[j]!=0 for x,(i,j) in zip(b,edges))
        if isreg:
            xdiag=tuple(f.inv(v) if v else 0 for v in a)
            xedges=tuple(f.mul(f.neg(b[e]),f.inv(f.mul(a[i],a[j]))) if a[i] and a[j] else 0 for e,(i,j) in enumerate(edges))
            x=xdiag+xedges
            assert mul(mul(u,x,f,n,edges),u,f,n,edges)==u,(q,n,u,x)
            N[zeros]+=1
        if full_nonregular_bruteforce:
            has_witness=any(mul(mul(u,x,f,n,edges),u,f,n,edges)==u for x in product(range(q),repeat=d))
            assert has_witness==isreg,(q,n,u)
            brute+=1
        checked+=1
    expected=[comb(n,k)*(q-1)**(n-k)*q**(ell-comb(k,2)) for k in range(n+1)]
    assert N==expected,(q,n,N,expected)
    print('FIELD',q,'N',n,'ELEMENTS',checked,'REGULAR',sum(N),'BY_ZEROS',N,'BRUTE',brute)
    return checked,brute

def mul(u,v,f,n,edges):
    w=[f.mul(u[i],v[i]) for i in range(n)]
    for e,(i,j) in enumerate(edges):
        w.append(f.add(f.mul(u[i],v[n+e]),f.mul(u[n+e],v[j])))
    return tuple(w)

def theta_test(q,n):
    assert n>q
    lo=0.;hi=log(n,q)+1.
    for _ in range(90):
        x=(lo+hi)*.5
        if (q-1)*(x+1)*q**x+x<n:lo=x
        else:hi=x
    kappa=(hi+lo)*.5;m=floor(kappa);theta=kappa-m
    logs=[lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)-k*log(q-1)-(k*(k-1)/2)*log(q) for k in range(n+1)]
    z=max(logs);weights=[exp(x-z) for x in logs];total=sum(weights)
    exact={k-m:w/total for k,w in enumerate(weights)}
    limit={t:q**(theta*t-t*(t-1)/2) for t in range(-50,51)}
    den=sum(limit.values());limit={t:x/den for t,x in limit.items()}
    tv=.5*sum(abs(exact.get(t,0.)-limit.get(t,0.)) for t in set(exact)|set(limit))
    print('THETA',q,n,'KAPPA',round(kappa,7),'THETA_FRAC',round(theta,7),'TV',round(tv,9),'TV_TIMES_KAPPA',round(tv*kappa,6))
    assert tv < 3.0/max(1.0,kappa)

if __name__=='__main__':
    cases=[(2,2,True),(2,3,True),(3,2,True),(2,4,False),(2,5,False),(3,3,False),(3,4,False),(4,2,False),(4,3,False)]
    nelems=nb=0
    for q,n,full in cases:
        a,b=check_case(q,n,full)
        nelems+=a;nb+=b
    for q in [2,3,4]:
        for n in [30,100,500,2000]:
            theta_test(q,n)
    print('ALL_QUIVER_REGULAR_THETA_TESTS_PASSED cases=%s elements=%s brute_existence=%s theta_cases=%s'%(len(cases),nelems,nb,12))
