"""Exact finite verification for a degree-proportional attachment tree.

The initial graph is the edge (1,2). Each subsequent vertex chooses an
old endpoint with probability proportional to its undirected degree.

Run using Python 3: python3 PA_verify.py
"""
from fractions import Fraction
from collections import defaultdict
from math import comb, lgamma, exp, sqrt, pi


def p(n):
    return Fraction(comb(2*n-4, n-2), 4**(n-2))


def expected_root(n):
    return (2*n-3)*p(n)


def expected_leaves(n):
    return Fraction(2*(n-1), 3) + Fraction(4, 3)*p(n)


def expected_cross(n):
    return Fraction(2*n-1,3)*expected_root(n)+p(n)


def covariance(n):
    return Fraction(2*n,3)*p(n) - Fraction(4*(2*n-3),3)*p(n)**2


def leaves_variance(n):
    if n==2:
        return Fraction(0)
    return (n-1+4*p(n)-16*p(n)**2)/9


def degree_variance(n):
    return 2*(n-1)-expected_root(n)-expected_root(n)**2


def law_step(states):
    out = defaultdict(Fraction)
    for degrees,prob in states.items():
        n=len(degrees)
        for i,deg in enumerate(degrees):
            child=list(degrees)
            child[i]+=1
            child.append(1)
            out[tuple(child)]+=prob*Fraction(deg,2*(n-1))
    return out


def exact_enumeration():
    law={(1,1): Fraction(1)}
    seen=0
    for n in range(2,11):
        if n>2:
            law=law_step(law)
        total=sum(law.values(),Fraction(0))
        assert total==1,(n,total)
        moment_D=sum(degrees[0]*pr for degrees,pr in law.items())
        moment_L=sum(sum(x==1 for x in degrees)*pr for degrees,pr in law.items())
        moment_DL=sum(degrees[0]*sum(x==1 for x in degrees)*pr for degrees,pr in law.items())
        moment_D2=sum(degrees[0]**2*pr for degrees,pr in law.items())
        moment_L2=sum(sum(x==1 for x in degrees)**2*pr for degrees,pr in law.items())
        assert moment_D==expected_root(n),(n,'D',moment_D,expected_root(n))
        assert moment_L==expected_leaves(n),(n,'L',moment_L,expected_leaves(n))
        assert moment_DL==expected_cross(n),(n,'DL',moment_DL,expected_cross(n))
        assert moment_DL-moment_D*moment_L==covariance(n),(n,'cov')
        assert moment_D2-moment_D**2==degree_variance(n),(n,'varD')
        assert moment_L2-moment_L**2==leaves_variance(n),(n,'varL',moment_L2-moment_L**2,leaves_variance(n))
        assert sum(pr for degrees,pr in law.items() if degrees[0]==1)==p(n),(n,'probD1')
        assert (covariance(n)==0 if n<=3 else covariance(n)>0),(n,'sign')
        seen+=len(law)
        print('n',n,'states',len(law),'cov',covariance(n))
    return seen


def recurrence_verification():
    check_count=0
    for n in range(2,501):
        q=Fraction(2*(n-1))
        assert p(n+1)==p(n)*Fraction(2*n-3,2*n-2)
        assert expected_root(n+1)==expected_root(n)*(1+1/q)
        assert expected_leaves(n+1)==expected_leaves(n)*(1-1/q)+1
        assert expected_cross(n+1)==expected_cross(n)+expected_root(n)+(expected_root(n)-p(n))/q
        assert expected_root(n+1)**2+degree_variance(n+1)==(expected_root(n)**2+degree_variance(n))*(1+Fraction(1,n-1))+expected_root(n)/q
        if n>=3:
            v=leaves_variance(n)
            l=expected_leaves(n)
            target=(1-Fraction(1,n-1))*v+l/q-(l/q)**2
            assert leaves_variance(n+1)==target,(n,'varL recurrence',leaves_variance(n+1),target)
        check_count+=6 if n>=3 else 5
    return check_count


def asymptotics():
    # Stable Gamma function for very large n avoids huge factorials.
    for n in [10000,100000,1000000]:
        pp=exp(lgamma(2*n-3)-2*lgamma(n-1)-(n-2)*__import__('math').log(4))
        d=(2*n-3)*pp
        vvD=2*(n-1)-d-d*d
        vvL=(n-1+4*pp-16*pp*pp)/9
        cov=(2*n*pp-4*(2*n-3)*pp*pp)/3
        scaled_corr= sqrt(n)*cov/sqrt(vvD*vvL)
        assert abs(scaled_corr-sqrt(2/(pi-2)))<0.03,(n,scaled_corr)
        print('asymptotic n',n,'Cov/sqrt(n)',cov/sqrt(n),'sqrt(n)*Corr',scaled_corr)

if __name__=='__main__':
    states=exact_enumeration()
    recurrence=recurrence_verification()
    asymptotics()
    print(f'OK; {states} exact degree-vector states summed, {recurrence} recurrence identities tested.')
