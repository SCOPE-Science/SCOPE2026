"""Independent finite verification of crossing/simple-chord mixed moments."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

@lru_cache(None)
def matchings(points):
    if not points:
        return ((),)
    a=points[0]
    return tuple(((a,b),)+tail for j,b in enumerate(points[1:],1)
                 for tail in matchings(points[1:j]+points[j+1:]))

def statistics(pairs,n):
    simple=sum(b-a==1 or b-a==2*n-1 for a,b in pairs)
    crossed=0
    for i,(a,b) in enumerate(pairs):
        for c,d in pairs[i+1:]:
            crossed += int((a<c<b<d) or (c<a<d<b))
    return simple,crossed

def doublefact(k):
    out=1
    while k>0:
        out*=k
        k-=2
    return out

def cycle_matching_count(N,r):
    return N*comb(N-r,r)//(N-r)

def check():
    tests=0
    histories={0:Counter({0:1})}
    for n in range(1,7):
        pairs=matchings(tuple(range(2*n)))
        freq=Counter(statistics(p,n) for p in pairs)
        assert sum(freq.values())==doublefact(2*n-1)
        tests+=1
        histories[n]=Counter({c:sum(count for (s,cc),count in freq.items() if cc==c) for c in range(n*(n-1)//2+1)})
        if n==1:continue
        population=doublefact(2*n-1)
        expected_c=Fraction(sum(c*k for (s,c),k in freq.items()),population)
        expected_s=Fraction(sum(s*k for (s,c),k in freq.items()),population)
        expected_sc=Fraction(sum(s*c*k for (s,c),k in freq.items()),population)
        expected_s2=Fraction(sum(s*s*k for (s,c),k in freq.items()),population)
        expected_c2=Fraction(sum(c*c*k for (s,c),k in freq.items()),population)
        assert expected_c==Fraction(n*(n-1),6); tests+=1
        assert expected_s==Fraction(2*n,2*n-1); tests+=1
        assert expected_c2-expected_c**2==Fraction(n*(n-1)*(n+3),45); tests+=1
        assert expected_s2-expected_s**2==Fraction(4*n*(n-1),(2*n-1)**2); tests+=1
        assert expected_sc-expected_s*expected_c == -Fraction(2*n*(n-1),3*(2*n-1)); tests+=1
        for r in range(n+1):
            factor=Fraction(factorial(r)*cycle_matching_count(2*n,r)*doublefact(2*(n-r)-1),population)
            rhs={c:factor*Fraction(v, doublefact(2*(n-r)-1)) for c,v in histories[n-r].items()}
            for c in range(n*(n-1)//2+1):
                lhs=Fraction(sum(factorial(s)//factorial(s-r)*cnt if s>=r else 0 for (s,k),cnt in freq.items() if k==c),population)
                assert lhs==rhs.get(c,0),(n,r,c,lhs,rhs.get(c,0))
                tests+=1
        print('n=',n,'matchings=',population,'exact identities=',tests)
    print('PASS:',tests,'exact assertions')
if __name__=='__main__': check()
