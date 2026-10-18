"""Independent finite checks for consecutive centered-square numerical semigroups."""
import heapq
from math import gcd

def apery_three(a,b,c):
    d=[None]*a; d[0]=0; h=[(0,0)]
    while h:
        v,r=heapq.heappop(h)
        if d[r]!=v: continue
        for z in (b,c):
            rr=(r+z)%a; w=v+z
            if d[rr] is None or w<d[rr]:
                d[rr]=w
                heapq.heappush(h,(w,rr))
    return d

def run():
    for n in range(2,81):
        a,b,c=2*n*n-2*n+1,2*n*n+2*n+1,2*n*n+6*n+5
        assert gcd(a,b)==gcd(b,c)==1
        assert gcd(a,c)==(5 if n%5==2 else 1)
        assert gcd(gcd(a,b),c)==1
        if n>2:
            assert all(c!=x*a+y*b for y in range(c//b+1) for x in range((c-y*b)//a+1))
        ds=apery_three(a,b,c)
        F=max(ds)-a
        g=sum(ds)//a - (a-1)//2
        assert (sum(ds)%a)==0, 'Apéry sum divisibility'
        assert (2*g==F+1)==(n==2),(n,a,b,c,F,g)
        if n==2: assert (F,g)==(47,24)
        if n>=7 and n%5==2:
            k=(n-2)//5
            A,C=a//5,c//5
            assert all(x*A+y*C!=b for x in range(b//A+1) for y in range(b//C+1))
    print('VERIFY_OK: 79 Apéry calculations; pairwise gcd, minimality, exceptional gluing and symmetry bounds')

if __name__=='__main__':
    run()
