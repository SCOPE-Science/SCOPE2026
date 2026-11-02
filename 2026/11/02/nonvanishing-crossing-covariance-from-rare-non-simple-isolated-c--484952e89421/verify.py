"""Independent exact-arithmetic checks of isolated-chord/crossing identities.

Run: python verify.py
Only the finite tests are verified computationally; the all-n theorem
requires the combinatorial proof supplied separately.
"""
from fractions import Fraction
from math import comb


def double_factorial(k):
    result = 1
    while k > 0:
        result *= k
        k -= 2
    return result


def p_isolated(n, s):
    return Fraction(
        double_factorial(2*s - 1)*double_factorial(2*(n-1-s)-1),
        double_factorial(2*n-1),
    )


def candidate_chords(n, s):
    return n if 2*s == n-1 else 2*n


def theory(n, s):
    mean = candidate_chords(n, s)*p_isolated(n,s)
    deficit = Fraction((n-1)+s*(n-1-s),3)
    return mean, -deficit*mean


def all_matchings(points):
    if not points:
        yield ()
        return
    first=points[0]
    for j in range(1,len(points)):
        second=points[j]
        rest=points[1:j]+points[j+1:]
        for sub in all_matchings(rest):
            yield ((first,second),)+sub


def crosses(e, f):
    a,b=e; c,d=f
    return (a<c<b<d) or (c<a<d<b)


def exact_enumeration(n):
    sums=[0]*(n//2+1)
    cross_sums=[0]*len(sums)
    total_cross=total=0
    for matching in all_matchings(tuple(range(2*n))):
        total += 1
        degrees=[0]*n
        for i in range(n):
            for j in range(i+1,n):
                if crosses(matching[i],matching[j]):
                    degrees[i]+=1; degrees[j]+=1
        crossings=sum(degrees)//2
        total_cross += crossings
        for i,(a,b) in enumerate(matching):
            if degrees[i] == 0:
                g=b-a-1
                assert g%2==0
                shorter=min(g,2*n-2-g)//2
                sums[shorter]+=1
                cross_sums[shorter]+=crossings
    return total,sums,cross_sums,total_cross


def check():
    checks=0
    for n in range(2,8):
        total,sums,cross_sums,total_cross=exact_enumeration(n)
        assert total==double_factorial(2*n-1)
        checks+=1
        assert Fraction(total_cross,total)==Fraction(n*(n-1),6)
        checks+=1
        for s in range((n-1)//2+1):
            observed_mean=Fraction(sums[s],total)
            observed_cov=Fraction(cross_sums[s],total)-observed_mean*Fraction(total_cross,total)
            expected_mean,expected_cov=theory(n,s)
            assert observed_mean==expected_mean,(n,s,'mean',observed_mean,expected_mean)
            checks+=1
            assert observed_cov==expected_cov,(n,s,'covariance',observed_cov,expected_cov)
            checks+=1
            assert expected_cov < 0
            checks+=1
        print('n',n,'matchings',total,'strata',((n-1)//2+1),'total covariance',sum(theory(n,s)[1] for s in range((n-1)//2+1)))
    for n in range(4,151):
        mean,cov=theory(n,1)
        assert mean==Fraction(2*n,(2*n-1)*(2*n-3))
        checks+=1
        assert cov==-Fraction(2*n,3*(2*n-1))
        checks+=1
        assert theory(n,0)[1]==-Fraction(2*n*(n-1),3*(2*n-1))
        checks+=1
        for s in range((n-1)//2+1):
            exact_mean,exact_cov=theory(n,s)
            r=Fraction(comb(n-1,s),comb(2*n-2,2*s))
            assert p_isolated(n,s)==r/Fraction(2*n-1)
            checks+=1
    print('PASS exact-rational assertions:',checks)


if __name__=='__main__':
    check()
