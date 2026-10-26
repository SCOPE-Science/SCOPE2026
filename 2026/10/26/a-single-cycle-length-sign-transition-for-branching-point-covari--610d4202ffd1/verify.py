"""Independent finite checks of an exact random-mapping mixed-moment identity.
Run: python3 verify.py. Python standard library only.
The proof of the statement for unbounded n is in RESULT.md; these tests
check exact finite instances and do not substitute for that proof.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def count_cycles(f, length):
    """Count directed cycles with exactly 'length' distinct vertices."""
    seen = set()
    count = 0
    for start in range(len(f)):
        if start in seen:
            continue
        index = {}
        path = []
        current = start
        while current not in seen and current not in index:
            index[current] = len(path)
            path.append(current)
            current = f[current]
        if current in index and len(path) - index[current] == length:
            count += 1
        seen.update(path)
    return count


def expected_cycles(n, r):
    return Fraction(factorial(n), factorial(n-r)*r*n**r)


def predicted_covariance(n, r):
    a = Fraction(n-1, n)
    p = (n-r)*(n*n-n+r*r-r)
    return expected_cycles(n, r)*a**(n-r-2)*(p-n*n*(n-1)*a**r)/ (2*n*n)


def conditional_indegree2(n, r):
    # Interpret the vanishing falling factorial terms as zero at m=0,1.
    m=n-r
    a=Fraction(n-1,n)
    first=Fraction(r*m,n)*a**(m-1) if m >= 1 else Fraction(0)
    second=Fraction(m*m*(m-1),2*n*n)*a**(m-2) if m >= 2 else Fraction(0)
    return first+second


def verify():
    enumerated=0
    assertions=0
    for n in range(2,7):
        denom=n**n
        sum_v=0
        sum_c=[0]*(n+1)
        sum_cv=[0]*(n+1)
        for f in product(range(n), repeat=n):
            enumerated += 1
            degree=[0]*n
            for target in f:
                degree[target]+=1
            count_two=sum(d==2 for d in degree)
            sum_v+=count_two
            for r in range(1,n+1):
                c=count_cycles(f,r)
                sum_c[r]+=c
                sum_cv[r]+=c*count_two
        marginal_v=Fraction((n-1),2)*Fraction(n-1,n)**(n-2)
        assert Fraction(sum_v,denom)==marginal_v
        assertions += 1
        for r in range(1,n+1):
            empirical_cov=Fraction(sum_cv[r],denom)-Fraction(sum_c[r]*sum_v,denom**2)
            assert Fraction(sum_c[r],denom)==expected_cycles(n,r)
            assert empirical_cov==predicted_covariance(n,r)
            assert Fraction(sum_cv[r],denom)==expected_cycles(n,r)*conditional_indegree2(n,r)
            assertions+=3
    for n in range(4,151):
        signs=[(predicted_covariance(n,r)>0)-(predicted_covariance(n,r)<0)
               for r in range(1,n+1)]
        assert signs[0]==0 and signs[1]==1 and signs[-1]==-1
        assert all(x==1 for x in signs[1:signs.index(-1)])
        assert all(x==-1 for x in signs[signs.index(-1):])
        assertions+=4
    for n in range(2,151):
        a=Fraction(n-1,n)
        P=lambda r:(n-r)*(n*n-n+r*r-r)
        for r in range(1,n):
            assert P(r+1)-a*P(r)==Fraction(r,n)*(n*n-n-(2*n-1)*r-r*r)
            assertions+=1
    print('PASS',enumerated,'mappings enumerated;',assertions,'exact checks')


if __name__=='__main__':
    verify()
