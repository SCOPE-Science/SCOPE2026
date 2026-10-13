"""Exact finite check of a three-tip UniFrac/Bray ranking threshold."""
from fractions import Fraction
from itertools import combinations, product


def profiles(n):
    return [(a,b,n-a-b) for a in range(1,n-1) for b in range(1,n-a)]


def bc(x, y):
    n = sum(x)
    return Fraction(sum(abs(a-b) for a,b in zip(x,y)),2*n)


def weighted_edges(x,y,t):
    n = sum(x)
    d = [Fraction(a-b,n) for a,b in zip(x,y)]
    return ((1-t)*(abs(d[0])+abs(d[1])) + t*abs(d[0]+d[1]) + abs(d[2]))/2


def weighted_reduction(x,y,t):
    n=sum(x)
    d=[a-b for a,b in zip(x,y)]
    k=sum(abs(a) for a in d)//2
    c=(abs(d[0])+abs(d[1])-abs(d[2]))//2
    assert c>=0 and c<=k<=n-3
    return Fraction(k,n)-t*Fraction(c,n)


def verify():
    checked_pairs=0
    checked_triplets=0
    for n in range(3,10):
        p=profiles(n)
        for t in [Fraction(1,6),Fraction(1,4),Fraction(1,3),Fraction(2,5),Fraction(1,2),Fraction(3,4),Fraction(9,10)]:
            can_reverse = False
            for x in p:
                for y in p:
                    if y==x: continue
                    u=weighted_edges(x,y,t)
                    assert u==weighted_reduction(x,y,t)
                    checked_pairs+=1
                    for z in p:
                        if z==x or z==y: continue
                        if bc(x,y)>bc(x,z) and u < weighted_edges(x,z,t):
                            can_reverse=True
                            if not t*max(0,n-3)>1:
                                raise AssertionError(('spurious reverse',n,t,x,y,z))
                        checked_triplets+=1
            expected=t*max(0,n-3)>1
            if can_reverse!=expected:
                raise AssertionError(('existence',n,t,can_reverse,expected))
            if expected:
                k=n-3
                x=(k+1,1,1)
                y=(1,k+1,1)
                z=(2,1,k)
                assert bc(x,y)>bc(x,z)
                assert weighted_edges(x,y,t)<weighted_edges(x,z,t)
    print('VERIFY_OK', 'pair identities',checked_pairs,'ordered comparison checks',checked_triplets)

if __name__=='__main__':
    verify()
