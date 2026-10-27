"""Independent finite checks for mixed short-chord/crossing identities.

Run: python verify_chords_33.py; standard-library only. Does not prove asymptotics.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a, *rest = vertices
    for j,b in enumerate(rest):
        for tail in matchings(rest[:j]+rest[j+1:]):
            yield ((a,b),)+tail


def statistics(matching):
    shorts = sum(b==a+1 for a,b in matching)
    crosses = sum(a<c<b<d or c<a<d<b for i,(a,b) in enumerate(matching) for c,d in matching[i+1:])
    return shorts,crosses


def dd(k):
    value=1
    for j in range(2*k-1,0,-2): value*=j
    return value


def exact(n):
    return Counter(statistics(M) for M in matchings(list(range(2*n))))


def a(n,r):
    return Fraction(factorial(r)*comb(2*n-r,r)*dd(n-r),dd(n))

checks=0
joint=[Counter({(0,0):1})]
for n in range(1,7):
    empirical=exact(n)
    joint.append(empirical)
    total=sum(empirical.values())
    assert total==dd(n); checks+=1
    # Extract coefficients in both variables via (z-1)^r; verify integer coefficient for every monomial.
    predicted=Counter()
    for r in range(n+1):
        c=comb(2*n-r,r)
        marginal=Counter()
        for (s,k),count in joint[n-r].items(): marginal[k]+=count
        for k,count in marginal.items():
            for s in range(r+1):
                predicted[(s,k)]+=c*comb(r,s)*((-1)**(r-s))*count
    for key in set(predicted)|set(empirical):
        assert predicted[key]==empirical[key],(n,key,predicted[key],empirical[key]);checks+=1
    # Mixed factorial moments against every exact crossing value.
    for r in range(n+1):
        falling=lambda k:factorial(k)//factorial(k-r) if k>=r else 0
        for k in range(comb(n,2)+1):
            lhs=Fraction(sum(count*falling(s) for (s,c),count in empirical.items() if c==k),dd(n))
            rhs=a(n,r)*Fraction(sum(count for (s,c),count in joint[n-r].items() if c==k),dd(n-r))
            assert lhs==rhs,(n,r,k,lhs,rhs);checks+=1
    # Exact joint moments and covariance.
    E=lambda f:Fraction(sum(count*f(s,c) for (s,c),count in empirical.items()),dd(n))
    muS=E(lambda s,c:s);muC=E(lambda s,c:c)
    assert muS==1;checks+=1
    assert muC==Fraction(n*(n-1),6);checks+=1
    assert E(lambda s,c:s*c)-muS*muC==Fraction(-(n-1),3);checks+=1
    assert E(lambda s,c:s*s)-muS*muS==Fraction(2*(n-1),2*n-1);checks+=1
    assert E(lambda s,c:c*c)-muC*muC==Fraction(n*(n-1)*(n+3),45);checks+=1
    for cutoff in range(comb(n,2)+1):
        covariance=E(lambda s,c:s*(c>=cutoff))-muS*E(lambda s,c:(c>=cutoff))
        assert covariance<=0,(n,cutoff,covariance);checks+=1
for n in range(1,201):
    for r in range(0,min(n,12)+1):
        assert 0<=a(n,r)<=1,(n,r);checks+=1
print('PASS',checks,'exact assertions; all matchings through six chords, finite factorial checks through n=200')
