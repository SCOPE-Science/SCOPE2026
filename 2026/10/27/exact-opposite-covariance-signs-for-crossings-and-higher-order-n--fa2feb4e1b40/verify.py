"""Exact independent matching enumeration for pair-versus-high-order arc covariance."""
from itertools import combinations
from fractions import Fraction
from math import comb, factorial

def matchings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for idx in range(1, len(xs)):
        b = xs[idx]
        for t in matchings(xs[1:idx] + xs[idx+1:]):
            yield ((a,b),)+t

def crossing(a,b):
    a0,a1=a; b0,b1=b
    return (a0<b0<a1<b1) or (b0<a0<b1<a1)

def nesting(a,b):
    a0,a1=a; b0,b1=b
    return (a0<b0<b1<a1) or (b0<a0<a1<b1)

def double_fact(k):
    z=1
    for v in range(1,k+1,2): z*=v
    return z

def verify():
    assertions=0
    for n in range(3,7):
        allM=list(matchings(tuple(range(2*n))))
        N=len(allM)
        assert N == double_fact(2*n-1);assertions+=1
        totals={r:[0,0,0,0,0] for r in range(3,n+1)}
        for M in allM:
            pairs=list(combinations(range(n),2))
            cp={(i,j):crossing(M[i],M[j]) for i,j in pairs}
            np={(i,j):nesting(M[i],M[j]) for i,j in pairs}
            c2=sum(cp.values())
            for r in range(3,n+1):
                x=y=0
                for S in combinations(range(n),r):
                    q=list(combinations(S,2))
                    x+=int(all(cp[e] for e in q))
                    y+=int(all(np[e] for e in q))
                z=totals[r];z[0]+=c2;z[1]+=x;z[2]+=y;z[3]+=c2*x;z[4]+=c2*y
        for r in range(3,n+1):
            z=totals[r]
            ex=Fraction(comb(n,r),double_fact(2*r-1))
            assert Fraction(z[1],N)==ex; assertions+=1
            assert Fraction(z[2],N)==ex; assertions+=1
            mean2=Fraction(z[0],N)
            assert mean2==Fraction(comb(n,2),3);assertions+=1
            cvx=Fraction(z[3],N)-mean2*ex
            cvy=Fraction(z[4],N)-mean2*ex
            wantx=ex*Fraction(r*(r-1)*(n+r+1),3*(2*r+1))
            wanty=-ex*Fraction(r*(r-1),6)
            assert cvx==wantx, (n,r,cvx,wantx); assertions+=1
            assert cvy==wanty, (n,r,cvy,wanty); assertions+=1
            print(f'n={n} r={r} pair-cross/r-cross={cvx} pair-cross/r-nest={cvy}')
    print('PASS:',assertions,'exact identity assertions; exhaustive matchings through 12 endpoints')

if __name__=='__main__': verify()
