"""Independent exact-arithmetic checks for occupancy/collision covariances."""
from fractions import Fraction as Q
from math import factorial, comb
from itertools import product

def compositions(n,m):
    if m==1:
        yield (n,)
    else:
        for k in range(n+1):
            for tail in compositions(n-k,m-1):
                yield (k,)+tail

def delta(f,k):return f[k+1]-f[k]
def delta2(f,k):return f[k+2]-2*f[k+1]+f[k]

def expectation_bin(n,p,g):
    return sum((Q(comb(n,k))*p**k*(1-p)**(n-k)*g(k) for k in range(n+1)),Q(0))

def verify(n,p,f):
    m=len(p);s2=sum((x*x for x in p),Q(0))
    eT=eW=eTW=Q(0)
    for v in compositions(n,m):
        multinomial=Q(factorial(n),1)
        for k,x in zip(v,p):multinomial*=x**k/Q(factorial(k))
        T=sum(k*(k-1)//2 for k in v)
        W=sum(f[k] for k in v)
        eT+=multinomial*T;eW+=multinomial*W;eTW+=multinomial*T*W
    lhs=eTW-eT*eW
    gs=[expectation_bin(n-2,x,lambda k:delta(f,k)) for x in p]
    hs=[expectation_bin(n-2,x,lambda k:delta2(f,k)) for x in p]
    rhs=Q(comb(n,2))*((1-s2)*sum((x*x*h for x,h in zip(p,hs)),Q(0)) +2*sum((x*(x-s2)*g for x,g in zip(p,gs)),Q(0)))
    assert lhs==rhs,(n,p,f,lhs,rhs)
    return lhs

def test():
    count=0; nonzero=0
    profiles=[(Q(1,2),Q(1,2)), (Q(1,3),Q(2,3)), (Q(1,2),Q(1,3),Q(1,6)), (Q(1,10),Q(2,10),Q(7,10)), (Q(1,4),)*4]
    for n in range(2,10):
        for p in profiles:
            # Hinge functions are the extremal rays of discrete convex functions modulo affine functions.
            for j in range(1,n):
                f=[max(0,k-j) for k in range(n+1)]
                assert verify(n,p,f)>0
                count+=1;nonzero+=1
            for r in range(n+1):
                f=[int(k==r) for k in range(n+1)]
                lhs=verify(n,p,f)
                if all(x==p[0] for x in p):
                    m=len(p);N=n-2
                    def b(k):return Q(comb(N,k),m**k)*(Q(m-1,m))**(N-k) if 0<=k<=N else Q(0)
                    predicted=Q(comb(n,2)*(m-1),m*m)*(b(r)-2*b(r-1)+b(r-2))
                    assert lhs==predicted
                    if r==1:
                        assert lhs==Q(comb(n,2)*(n-2*m),m*m)*Q(m-1,m)**(n-2)
                    if r>=2:
                        P=m*m*r*r-m*(2*n+m-2)*r+n*(n-1)
                        if r==n:assert lhs>0
                        else:assert (lhs>0)-(lhs<0)==(P>0)-(P<0),(n,m,r,lhs,P)
                count+=1
            assert verify(n,p,list(range(n+1)))==0;count+=1
            assert verify(n,p,[3*k+7 for k in range(n+1)])==0;count+=1
    print(f'PASS: {count} exact-rational occupancy distribution and covariance checks; {nonzero} strict convex hinges; exact boundary identities verified.')
if __name__=='__main__':test()
