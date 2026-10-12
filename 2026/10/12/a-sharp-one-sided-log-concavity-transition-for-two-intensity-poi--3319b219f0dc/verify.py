#!/usr/bin/env python3
"""Reproduce exact checks for the two-intensity Poisson mixture theorem.

The global theorem is proved analytically; finite checks are only diagnostics.
No external packages are required.
"""
from fractions import Fraction
import math


def q(A, B, a, b, k):
    return A * a**k + B * b**k


def curvature_numerator(A, B, a, b, k):
    assert k >= 1
    return (k+1)*q(A, B, a, b, k)**2 - k*q(A, B, a, b, k-1)*q(A, B, a, b, k+1)


def factored_numerator(A, B, a, b, k):
    return q(A, B, a, b, k)**2 - k*A*B*(a*b)**(k-1)*(b-a)**2


def threshold(a, b):
    assert 0 < a < b
    d = math.log(b/a)
    C = (b-a)**2/(a*b)
    r0 = 4/C
    K = math.floor(r0)+1
    w = math.acosh(K*C/2-1)
    log_theta = -K*d+w
    # posterior-intensity odds theta = B/A
    theta = math.exp(log_theta)
    prob = math.exp(b-a + log_theta)/(1+math.exp(b-a + log_theta))
    return K, theta, prob


def main():
    ncheck = 0
    for a in range(1, 5):
        for b in range(a+1, 7):
            for A, B in [(1,1),(2,3),(5,11),(77,2)]:
                for k in range(1, 41):
                    left = curvature_numerator(A,B,a,b,k)
                    right = factored_numerator(A,B,a,b,k)
                    assert left == right,(a,b,A,B,k,left,right)
                    ncheck += 1
    print('Exact polynomial identities:',ncheck,'PASS')

    # The weights A,B are proportional to mixing weights multiplied by e^{-a},e^{-b}.
    # At an integer r = 4ab/(b-a)^2 the critical odds are (a/b)^r.
    exact_cases = [
        (1,2,256,1,{8,9}),
        (1,3,27,1,{3,4}),
        (2,3,3**24,2**24,{24,25}),
        (1,4,8,1,{2}),
    ]
    for a,b,A,B,zero_set in exact_cases:
        got=set()
        for k in range(1, 90):
            value=curvature_numerator(A,B,a,b,k)
            assert value>=0,(a,b,k,value)
            if value==0:got.add(k)
        assert got == zero_set,(a,b,got,zero_set)
        print('Exact boundary',a,b,'equality indices',sorted(got),'PASS')

    for a,b,A,B in [(1,2,300,1),(1,3,30,1),(1,4,9,1),(2,3,3**24+100,2**24)]:
        negatives = [k for k in range(1, 110) if curvature_numerator(A,B,a,b,k)<0]
        assert negatives, (a,b,A,B)
        assert negatives == list(range(min(negatives),max(negatives)+1)),negatives
        print('Below-threshold example',a,b,'violations',min(negatives),max(negatives),'PASS')

    for a,b in [(1,2),(1,3),(1,4),(2,3),(0.2,0.5),(0.99,1.01),(1,11)]:
        K,theta,p=threshold(a,b)
        d=math.log(b/a)
        C=(b-a)**2/(a*b)
        def W(k): return math.acosh(k*C/2-1)
        assert math.isclose(W(4/C+1),d,rel_tol=2e-10,abs_tol=2e-10)
        rhs=[-k*d+W(k) for k in range(K,K+120)]
        assert all(rhs[i]>rhs[i+1] for i in range(len(rhs)-1)),(a,b,K)
        assert all(W(k+1)>d for k in range(K,K+120))
        assert theta>0 and 0<p<1
        print('Threshold diagnostic',a,b,'K',K,'odds',theta,'weight',p,'PASS')
    print('All standalone finite diagnostics passed; infinite statements rely on the proof.')

if __name__ == '__main__':
    main()
