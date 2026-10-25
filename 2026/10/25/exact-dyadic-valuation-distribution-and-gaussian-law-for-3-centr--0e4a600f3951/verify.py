#!/usr/bin/env python3
"""Independent finite checks of 3-central binomial valuation statistics."""
from collections import Counter
from fractions import Fraction

def v2(k):
    assert k > 0
    return (k & -k).bit_length()-1

def polynomial_by_matrix(length):
    states = [Counter({0: 1}), Counter()]
    # Rows of the two-bit weighted carry matrix.
    transitions = [((0,0,2), (1,1,2)),
                   ((0,0,1), (1,1,1), (1,2,2))]
    for _ in range(length):
        nxt = [Counter(), Counter()]
        for start, polynomial in enumerate(states):
            for stop, valuation, multiplicity in transitions[start]:
                for degree, count in polynomial.items():
                    nxt[stop][degree + valuation] += count * multiplicity
        states = nxt
    out = states[0] + states[1]
    return +out

def derivative_moments(hist):
    total = sum(hist.values())
    mean = Fraction(sum(k*v for k,v in hist.items()), total)
    factorial2 = Fraction(sum(k*(k-1)*v for k,v in hist.items()), total)
    return mean, factorial2+mean-mean*mean

def main():
    max_length = 7
    total_cases = 0
    for length in range(max_length+1):
        cap=4**length
        actual=Counter()
        value=0
        for n in range(cap):
            # From c(n+1) / c(n) = 3(3n+1)/(n+1).
            assert value >= 0
            actual[value] += 1
            value += v2(3*n+1)-v2(n+1)
        predicted=polynomial_by_matrix(length)
        assert actual == predicted, (length,actual,predicted)
        mean,var=derivative_moments(actual)
        expected_mean=Fraction(length)-Fraction(2,3)+Fraction(2,3*4**length)
        expected_var=Fraction(4*length,3)-Fraction(14,9)+Fraction(2,4**length)-Fraction(4,9*16**length)
        assert mean==expected_mean, (length,mean,expected_mean)
        assert var==expected_var, (length,var,expected_var)
        assert sum(actual.values())==cap
        total_cases+=cap
    # For F(lambda,z)=lambda^2-(2+z+2z^2)lambda+4z^2,
    # compute implicit derivatives at (lambda,z)=(4,1).
    f_lambda=2*4-5
    f_z=-(1+4)*4+8
    lam_prime=Fraction(-f_z,f_lambda)
    f_zz=-(4)*4+8
    f_zlambda=-5
    f_lambdalambda=2
    lam_double=-(f_zz+2*f_zlambda*lam_prime+f_lambdalambda*lam_prime**2)/f_lambda
    assert lam_prime==4 and lam_double==Fraction(16,3)
    log_curvature=(lam_double+lam_prime)/4-(lam_prime/4)**2
    assert log_curvature==Fraction(4,3)
    print('VERIFY_OK complete_blocks',max_length+1,'integer_cases',total_cases,
          'matrix_coefficients_exact','moments_exact','dominant_eigen_derivatives_exact')

if __name__ == '__main__':
    main()
