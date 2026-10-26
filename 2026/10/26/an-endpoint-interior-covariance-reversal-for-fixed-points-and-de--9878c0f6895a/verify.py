"""Exact-rational finite checks for Ewens fixed-point/descent covariances.

No external packages; analytic all-size proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

def count_cycles(p):
    remaining = set(range(len(p)))
    c = 0
    while remaining:
        c += 1
        j = next(iter(remaining))
        while j in remaining:
            remaining.remove(j)
            j = p[j]-1
    return c

def rise(theta, n):
    val = Fraction(1)
    for j in range(n):
        val *= theta+j
    return val

def local_formula(n, theta, i):
    denom = (theta+n-3)*(theta+n-2)*(theta+n-1)**2
    if i in (1,n):
        u=n-3
        poly=u*(u+1)*(u+2)+theta*u*(3*u+5)+theta**2*(4*u+6)
        return -theta*poly/(2*denom)
    poly=(n-1)*(n-3)+2*theta*(n-2)
    return -theta*(theta-1)*poly/denom

def total_formula(n, theta):
    return -theta**2*(n-1)*(n*n-4*n+2+2*theta*(n-1))/((theta+n-3)*(theta+n-2)*(theta+n-1)**2)

def q_formula(n,theta):
    return Fraction(1,2) + theta*(1-theta)/(2*(theta+n-2)*(theta+n-1))

cases=0
for n in range(4,9):
    for theta in (Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(2),Fraction(5)):
        denom=rise(theta,n)
        weighted_D=Fraction(0)
        weighted_f=[Fraction(0) for _ in range(n)]
        weighted_fD=[Fraction(0) for _ in range(n)]
        total_weight=Fraction(0)
        for p in permutations(range(1,n+1)):
            w=theta**count_cycles(p)
            D=sum(p[j]>p[j+1] for j in range(n-1))
            total_weight+=w
            weighted_D+=w*D
            for j,x in enumerate(p):
                if x==j+1:
                    weighted_f[j]+=w
                    weighted_fD[j]+=w*D
        assert total_weight==denom,(n,theta,'normalization')
        ED=weighted_D/denom
        assert ED==(n-1)*q_formula(n,theta),(n,theta,'mean')
        local=[]
        for i in range(1,n+1):
            v=weighted_fD[i-1]/denom-weighted_f[i-1]/denom*ED
            assert weighted_f[i-1]/denom==theta/(theta+n-1)
            predicted=local_formula(n,theta,i)
            assert v==predicted,(n,theta,i,v,predicted)
            local.append(v)
        assert sum(local)==total_formula(n,theta)
        cases+=1
    print('EWENS_EXACT_PASS',n,'permutations',factorial(n))
print('VERIFY_OK',cases,'exact (n,theta) strata')
