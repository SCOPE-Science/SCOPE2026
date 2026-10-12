"""Exact-rational diagnostic checks for two homogeneous shock-portfolio maxima.

Run with Python 3.10+ using only the standard library. Finite tests
supplement the proof; they do not certify its universal quantifiers.
"""
from fractions import Fraction as Q
from itertools import product


def formula(n, p, a, q, b):
    if b >= a:
        return b*p*(1-q) <= a*q*(1-p)
    return (n-1)*(b*q-a*p) >= 2*(a-b)


def atom(n, p, a, q, b):
    return b*p*(1-q) <= a*q*(1-p)


def n_derivative(n, p, a, q, b, s):
    da=1-s+a*s
    db=1-s+b*s
    ea=1-s+a*(1-p)*s
    eb=1-s+b*(1-q)*s
    h=b*(1-q)-a*(1-p)
    return (n-1)*h*da*db-(n+1)*(b-a)*ea*eb


def direct_derivative(n, p, a, q, b, s):
    da=1-s+a*s
    db=1-s+b*s
    ea=1-s+a*(1-p)*s
    eb=1-s+b*(1-q)*s
    return (n-1)*((b*(1-q)-1)/eb-(a*(1-p)-1)/ea)+(n+1)*((a-1)/da-(b-1)/db)


def tests():
    alphas=[Q(1,3),Q(1,2),Q(1),Q(2),Q(3)]
    ps=[Q(1,5),Q(2,5),Q(3,5),Q(4,5)]
    checks=0
    for a,b,p,q,n in product(alphas,alphas,ps,ps,range(1,17)):
        # By the monotonicity proof, the maximum of N(s) is attained
        # at s=1 when b>=a, and at s=0 when b<a.
        worst_s=Q(1) if b>=a else Q(0)
        necessary_sufficient = atom(n,p,a,q,b) and n_derivative(n,p,a,q,b,worst_s)<=0
        assert formula(n,p,a,q,b)==necessary_sufficient,(n,p,a,q,b)
        checks+=1
        for j in range(11):
            s=Q(j,10)
            da=1-s+a*s; db=1-s+b*s
            ea=1-s+a*(1-p)*s; eb=1-s+b*(1-q)*s
            assert direct_derivative(n,p,a,q,b,s)*da*db*ea*eb == n_derivative(n,p,a,q,b,s)
            if formula(n,p,a,q,b):
                assert n_derivative(n,p,a,q,b,s)<=0
            checks+=1
    # A larger occurrence probability reverses the lower-severity
    # disadvantage in likelihood-ratio order at exactly n=5.
    a,b,p,q=Q(2),Q(1),Q(1,5),Q(9,10)
    assert all(not formula(n,p,a,q,b) for n in range(1,5))
    assert all(formula(n,p,a,q,b) for n in range(5,201))
    assert n_derivative(5,p,a,q,b,Q(0))==0
    checks+=3
    print('PASS: %d exact-rational identities/order checks' % checks)

if __name__ == '__main__':
    tests()
