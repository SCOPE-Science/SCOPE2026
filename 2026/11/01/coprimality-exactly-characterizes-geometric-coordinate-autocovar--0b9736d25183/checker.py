from fractions import Fraction as Q
from math import gcd

def integ(lo,hi,a,b):
    # (x-1/2)(a*x+b-1/2)
    u=b-Q(1,2)
    return a*(hi**3-lo**3)/3+(u-a/Q(2))*(hi**2-lo**2)/2-u/Q(2)*(hi-lo)

def exact(M,N,p,n):
    q=1-p
    pieces=[(Q(0),Q(1),Q(1),Q(0),Q(1))]
    for step in range(n):
        new=[]
        for lo,hi,a,b,w in pieces:
            # expanding map in pieces
            for k in range(M):
                ml=max(lo,(Q(k)-M*b)/(M*a))
                mh=min(hi,(Q(k+1)-M*b)/(M*a))
                if ml < mh:
                    new.append((ml,mh,M*a,M*b-k,w*p))
            for j in range(N):
                new.append((lo,hi,a/N,(b+j)/N,w*q/N))
        pieces=new
    return sum((w*integ(lo,hi,a,b) for lo,hi,a,b,w in pieces),Q(0)),len(pieces)

if __name__=='__main__':
    tests=0; branches=0
    for M,N in [(2,3),(3,2),(2,5),(5,2),(3,4),(4,3),(3,5),(2,2),(2,4),(4,2),(3,3),(4,6),(6,4)]:
        for p in (Q(1,3),Q(2,5)):
            for n in range(5):
                val,b=exact(M,N,p,n); branches+=b
                rho=p/M+(1-p)/N
                if gcd(M,N)==1:
                    expected=rho**n/12
                elif n==2:
                    expected=rho**2/12+p*(1-p)*(gcd(M,N)**2-1)/(12*M*N)
                else:
                    continue
                assert val==expected,(M,N,p,n,val,expected)
                tests+=1
    print('PASS',tests,'exact integration identities; total evaluated branch pieces:',branches)
