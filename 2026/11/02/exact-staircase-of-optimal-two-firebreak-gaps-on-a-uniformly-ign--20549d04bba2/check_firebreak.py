"""Exact finite checks for the two-barrier independent-ignition cycle theorem.

The all-size classification is proved analytically in RESULT.md; these checks
are independent finite tests, not substitutes for its proof.
"""
from fractions import Fraction
from itertools import product


def retained(n, k, q):
    return k * q**k + (n-k) * q**(n-k)


def threshold_expression(n, k, q):
    exponent = n - 2*k - 1
    return sum((q**j for j in range(1, exponent)), Fraction(0)) + (n-k)*q**exponent-k


def expectation_by_ignition_census(n, k, q):
    """Enumerate Bernoulli ignition outcomes without using risk shortcut."""
    p = 1-q
    result = Fraction(0)
    for pattern in product((0, 1), repeat=n):
        probability = p**sum(pattern)*q**(n-sum(pattern))
        burned = k*int(any(pattern[:k]))+(n-k)*int(any(pattern[k:]))
        result += probability*burned
    return result


def root(n,k):
    lo,hi=0.0,1.0
    for _ in range(60):
        mid=(lo+hi)/2
        t=sum(mid**j for j in range(1,n-2*k-1))+(n-k)*mid**(n-2*k-1)-k
        if t>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


def main():
    assertions=0
    # Direct ignition enumeration verifies the modeled expectation.
    for n in range(4,10):
        for k in range(1,n//2+1):
            for q in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                assert expectation_by_ignition_census(n,k,q)==n-retained(n,k,q)
                assertions+=1
    # The pivotal adjacent-interchange identity is tested independently.
    for n in range(4,45):
        for k in range(1,n//2):
            for q in (Fraction(1,7),Fraction(1,2),Fraction(2,3),Fraction(7,8)):
                delta=retained(n,k+1,q)-retained(n,k,q)
                expression=q**k*(1-q)*threshold_expression(n,k,q)
                assert delta==expression
                assertions+=1
    # Ordered thresholds and the uniquely optimal split between them.
    for n in range(4,65):
        roots=[root(n,k) for k in range(1,n//2)]
        assert 0 < min(roots) and max(roots) < 1
        assert all(a+1e-12 < b for a,b in zip(roots, roots[1:]))
        assertions+=2
        bounds=[0.0]+roots+[1.0]
        for segment in range(1,len(bounds)):
            q=(bounds[segment-1]+bounds[segment])/2
            values=[retained(n,k,q) for k in range(1,n//2+1)]
            assert max(range(1,n//2+1),key=lambda k:values[k-1])==segment
            assertions+=1
    # Show the full four-regime succession at eight patches, exactly.
    example={Fraction(2,5):1,Fraction(1,2):2,Fraction(7,12):3,Fraction(3,4):4}
    for q,winner in example.items():
        values=[retained(8,k,q) for k in range(1,5)]
        assert all(values[winner-1]>v for i,v in enumerate(values,1) if i!=winner)
        assertions+=1
    assert threshold_expression(8,3,Fraction(3,5))==0
    assert retained(8,3,Fraction(3,5))==retained(8,4,Fraction(3,5))
    assertions+=2
    print('PASS:',assertions,'independent exact/finite checks')
    print('Eight-patch cutoffs:',*(format(root(8,k),'.12f') for k in range(1,4)))

if __name__=='__main__':
    main()
