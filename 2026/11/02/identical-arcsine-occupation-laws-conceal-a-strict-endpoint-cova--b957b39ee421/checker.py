"""Exact elementary checks for occupation-endpoint dependence in uniform permutations."""
from itertools import permutations, product
from fractions import Fraction
from math import factorial, comb, sqrt, pi

def eulerian(n):
    a=[1]
    for m in range(2,n+1):
        a=[(d+1)*(a[d] if d<len(a) else 0)+(m-d)*(a[d-1] if d else 0) for d in range(m)]
    return a

def predicted_cov(n):
    ans=Fraction(0)
    for k in range(1,n+1):
        r=2*k
        a=eulerian(r)
        inner=sum((r-1-2*d)*a[d] for d in range(k))
        ans+=Fraction(2*r*inner,(r+1)*factorial(r))
    return ans

def perm_statistics(p):
    m=len(p)-1
    s=0;n=0
    for j in range(1,m+1):
        old=s
        s+=1 if p[j-1]<p[j] else -1
        if old>=0 and s>=0:n+=1
    return n,s

def exhaustive(n):
    m=2*n
    total=factorial(m+1)
    EN=ES=ENS=EN2=ES2=0
    count=[0]*(n+1)
    for p in permutations(range(m+1)):
        N,S=perm_statistics(p)
        assert N%2==0
        count[N//2]+=1
        EN+=N; ES+=S; ENS+=N*S; EN2+=N*N; ES2+=S*S
    cov=Fraction(ENS,total)-Fraction(EN*ES,total**2)
    assert cov==predicted_cov(n),(n,cov,predicted_cov(n))
    assert Fraction(EN,total)==n
    assert Fraction(ES,total)==0
    assert Fraction(EN2,total)-n*n == Fraction(n*(n+1),2)
    assert Fraction(ES2,total)==Fraction(2*n+2,3)
    for k,c in enumerate(count):
        assert Fraction(c,total)==Fraction(comb(2*k,k)*comb(2*n-2*k,n-k),4**n)
    print('permutation n=',n,'cases=',total,'cov=',cov,'occupation counts=',count)

def simple_walk(n):
    m=2*n
    tN=tS=tNS=0
    for x in product((-1,1),repeat=m):
        s=0;N=0
        for inc in x:
            old=s;s+=inc
            if old>=0 and s>=0:N+=1
        tN+=N;tS+=s;tNS+=N*s
    ans=Fraction(tNS,2**m)-Fraction(tN*tS,4**m)
    rhs=Fraction(0)
    for k in range(1,n+1):
        rhs+=Fraction((2*k-1)*comb(2*k-2,k-1),2**(2*k-2))
    assert ans==rhs
    return ans

if __name__=='__main__':
    for n in range(1,5):
        exhaustive(n)
        assert simple_walk(n)>predicted_cov(n)
        print('simple-walk:',simple_walk(n))
    for r in range(2,9):
        a=eulerian(r)
        # Compare the last-rank moment identity using exhaustive permutations
        weights=[0]*r
        for p in permutations(range(1,r+1)):
            d=sum(p[i]>p[i+1] for i in range(r-1))
            weights[d]+=p[-1]
        for d in range(r):
            assert weights[d]==(r-d)*a[d],(r,d)
    for n in (10,50,100):
        c=float(predicted_cov(n))
        scaled=c/n**1.5
        target=4/(3*sqrt(3*pi))
        print('n',n,'scaled covariance',scaled,'limit',target)
    print('PASS')
