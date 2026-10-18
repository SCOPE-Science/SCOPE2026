"""Exact integer checks of wild-prime diagonal-fibre identities."""
from collections import Counter
from fractions import Fraction
from math import isqrt


def primality(p):
    return p >= 2 and all(p % k for k in range(2, isqrt(p) + 1))


def predicted_fibres(p, n):
    assert primality(p) and p >= 5 and n >= 0
    if n == 0:
        return [1]
    N = p**n
    if n == 1:
        return [1] * p
    pp = p*p
    H = {pow(i,p,pp) for i in range(1,p)}
    m = Counter((x+y)%pp for x in H for y in H)
    g = [m[c] + (2 if c in H else 0) for c in range(pp)]
    if n <= p:
        ans = [g[a%pp] for a in range(N)]
        ans[0] += p**(n-2)
        return ans
    small = predicted_fibres(p,n-p)
    ans = [g[a%pp] for a in range(N)]
    scale = p**(p-2)
    mult = p**p
    for t, val in enumerate(small):
        # Every residue with a = p^p*t mod p^n has the same
        # normalized density by the lifting formula.
        ans[mult*t] += scale*val
    return ans


def brute_fibres(p,n):
    N = p**n
    vals = Counter(pow(x,p,N) for x in range(N))
    raw = [0]*N
    for a,na in vals.items():
        for b,nb in vals.items():
            raw[(a+b)%N] += na*nb
    assert all(z%N==0 for z in raw)
    return [z//N for z in raw]


def constants(p):
    H={pow(i,p,p*p) for i in range(1,p)}
    m=Counter((a+b)%(p*p) for a in H for b in H)
    g=[m[c]+(2 if c in H else 0) for c in range(p*p)]
    assert sum(g)==p*p-1
    assert g[0]==p-1
    return sum(z*z for z in g),g


def expected_moment(p,n):
    if n<=1:return Fraction(1)
    sumg2,_=constants(p)
    base=Fraction(sumg2 + 2*(p-1),p*p)
    if n<=p:
        return base+Fraction(p**n,p**4)
    return base + p**(p-4)*expected_moment(p,n-p)


def main():
    checks=0
    for p,nmax in [(5,6),(7,4),(11,3)]:
        assert primality(p)
        _,g=constants(p)
        for n in range(1,nmax+1):
            actual=brute_fibres(p,n)
            pred=predicted_fibres(p,n)
            assert actual==pred,(p,n,next((i for i,(a,b) in enumerate(zip(actual,pred)) if a!=b),None))
            moment=Fraction(sum(z*z for z in actual),p**n)
            assert moment==expected_moment(p,n),(p,n,moment,expected_moment(p,n))
            checks+=len(actual)
        print('verified prime',p,'depth <=',nmax,'unit-value classes',sum(z>0 for z in g))
    _,g5=constants(5)
    assert sum(z*z for z in g5)==52
    assert sum(z>0 for z in g5)==13
    assert expected_moment(5,5)==Fraction(37,5)
    assert expected_moment(5,6)==Fraction(37,5)
    assert expected_moment(5,7)==Fraction(73,5)
    print('VERIFY_OK',checks,'exact residue comparisons and moments')

if __name__=='__main__':main()
