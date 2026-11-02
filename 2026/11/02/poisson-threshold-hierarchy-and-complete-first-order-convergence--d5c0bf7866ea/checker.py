"""Independent finite checks for colored disjoint equal-sized equivalence classes."""
from collections import Counter,defaultdict
from fractions import Fraction
from math import comb, factorial
from functools import lru_cache

def profile(colors,m,r,q):
    d=Counter()
    for b in range(m):
        red=sum(colors[b*r:(b+1)*r]); blue=r-red
        d[(min(red,q),min(blue,q))]+=1
    return tuple(sorted((k,min(v,q)) for k,v in d.items()))

def same_partial(a,b,hist):
    # Cross-map of selected vertices, with equality, E and unary colour.
    left=[x for x,_ in hist]; right=[y for _,y in hist]
    if len(set(left))!=len(set(right)): return False
    for x,y in hist:
        if a[0][x]!=b[0][y]:return False
    for (x,y) in hist:
        for (x2,y2) in hist:
            if (x//a[1]==x2//a[1])!=(y//b[1]==y2//b[1]):return False
    return True

def duplicator_wins(a,b,q):
    na=len(a[0]);nb=len(b[0]);
    @lru_cache(None)
    def win(rounds,hist):
        if not same_partial(a,b,hist):return False
        if rounds==0:return True
        for x in range(na):
            if not any(win(rounds-1,hist+((x,y),)) for y in range(nb)):
                return False
        for y in range(nb):
            if not any(win(rounds-1,hist+((x,y),)) for x in range(na)):
                return False
        return True
    return win(q,())

def brute_counts(m,r,j):
    counter=Counter(); N=m*r
    for mask in range(1<<N):
        xy=[0,0]
        for b in range(m):
            s=sum((mask>>(b*r+t))&1 for t in range(r))
            xy[0]+=s==j
            xy[1]+=s==r-j
        counter[tuple(xy)]+=1
    return counter

def expected_counts(m,r,j):
    p=Fraction(comb(r,j),2**r)
    answer={}
    for x in range(m+1):
        for y in range(m-x+1):
            value=Fraction(factorial(m),factorial(x)*factorial(y)*factorial(m-x-y))*p**(x+y)*(1-2*p)**(m-x-y)
            if value:answer[(x,y)]=value*(2**(r*m))
    return answer

def run():
    tests=0
    for m,r in ((1,2),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4)):
        for j in range((r-1)//2+1):
            got=brute_counts(m,r,j)
            expected=expected_counts(m,r,j)
            assert all(v.denominator==1 for v in expected.values())
            assert got==expected,(m,r,j,got,expected)
            tests+=1
    print('EXACT_MULTINOMIAL_CASES',tests)
    ef_tests=0
    for m,r,q in ((2,2,1),(2,3,1),(2,3,2),(2,4,2),(3,2,2)):
        sigrep={}
        for mask in range(1<<(m*r)):
            colors=tuple((mask>>i)&1 for i in range(m*r))
            sig=profile(colors,m,r,q)
            a=(colors,r)
            if sig in sigrep:
                if ef_tests<2000 or m*r<=6:
                    assert duplicator_wins(sigrep[sig],a,q),(m,r,q,mask,sig)
                    ef_tests+=1
            else:sigrep[sig]=a
        print('SIGNATURE_TEST',m,r,q,'classes',len(sigrep))
    print('EF_GAMES_PASSED',ef_tests)
    # exactly calculated model non-convergence at m=n, r=ceil(log2(n))
    for k in (10,14):
        a=1-(1-2**(-k))**(2**k)
        b=1-(1-2**(-k))**(2**(k-1)+1)
        print('OSCILLATING_FINITE_EXAMPLE',k,round(a,9),round(b,9))
    print('ALL_CHECKS_OK')
if __name__=='__main__':run()
