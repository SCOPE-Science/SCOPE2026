#!/usr/bin/env python3
"""Independent exact-moment and direct-sampling checks for parallelogram tomography.

All finite tests are diagnostic; the quantified proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random
from itertools import product


def even_moment(k):
    return F(2, (2*k+1)*(2*k+2))


def multinomial_coeffs(k):
    # Expand (A*u*u + B*v*v + 2*C*u*v)^k without symbolic libraries.
    out = {}
    from math import factorial
    for i in range(k+1):
        for j in range(k-i+1):
            z = k-i-j
            coeff = F(factorial(k), factorial(i)*factorial(j)*factorial(z)) * 2**z
            if z % 2:
                continue
            coeff *= even_moment(i + z//2) * even_moment(j + z//2)
            out[(i, j, z)] = coeff
    return out


def directly_expanded_moment(A, B, C, k):
    return sum((coeff * A**i * B**j * C**z for (i, j, z), coeff in multinomial_coeffs(k).items()), F(0))


def stated_moments(A, B, C):
    S, Q = A + B, A * B
    return S/F(6), S*S/F(15) - F(7,90)*Q + C*C/F(9), S**3/F(28)-F(31,420)*S*Q+F(2,15)*S*C*C


def inverse(m2, m4, m6):
    S = 6*m2
    T = F(105,41)/m2*(m6 - F(75,7)*m2*m4 + 18*m2**3)
    Q = 30*m4 - 2*S**2 + F(10,3)*T
    C2 = Q - T
    return S,Q,C2,T


def test_exact():
    assert even_moment(1)==F(1,6)
    assert even_moment(2)==F(1,15)
    assert even_moment(3)==F(1,28)
    cases=[]
    for A,B in product([F(1,4), F(1,2), F(1), F(3,2), F(3)], repeat=2):
        for t in [F(0), F(1,10), F(1,4), F(1,2)]:
            # rational offdiag C=t*min(A,B) ensures positive determinant.
            C=t*min(A,B)
            cases.append((A,B,C))
    for A,B,C in cases:
        moments=stated_moments(A,B,C)
        for k,m in enumerate(moments,1):
            assert directly_expanded_moment(A,B,C,k)==m,(A,B,C,k)
        S,Q,C2,T=inverse(*moments)
        assert (S,Q,C2,T)==(A+B,A*B,C*C,A*B-C*C)
    # These two shapes have exactly equal second and fourth moments but different area.
    # Q1=1/5,C1^2=0; Q2=21/100,C2^2=7/1000. S=1.
    Q1,Q2=F(1,5),F(21,100)
    C21,C22=F(0),F(7,1000)
    def x(Q,C2): return F(1,15)-F(7,90)*Q+C2/F(9)
    assert x(Q1,C21)==x(Q2,C22)
    assert Q1-C21 != Q2-C22
    assert (Q1>0 and Q1<=F(1,4) and C21<Q1)
    assert (Q2>0 and Q2<=F(1,4) and C22<Q2)
    def mom6(Q,C2): return F(1,28)-F(31,420)*Q+F(2,15)*C2
    assert mom6(Q1,C21) != mom6(Q2,C22)
    # normalized triangular moment image vertices.
    assert (x(F(0),F(0)),mom6(F(0),F(0))) == (F(1,15),F(1,28))
    assert (x(F(1,4),F(0)),mom6(F(1,4),F(0))) == (F(17,360),F(29,1680))
    assert (x(F(1,4),F(1,4)),mom6(F(1,4),F(1,4))) == (F(3,40),F(17,336))
    assert -F(7,90)*F(2,15)-F(1,9)*(-F(31,420)) == -F(41,18900)
    print('EXACT_MOMENT_EXPANSION_INVERSION_AND_TRIANGLE_PASSED',len(cases))


def test_stability():
    for t in [F(1,100),F(1,50),F(1,10),F(1,4)]:
        m0=stated_moments(F(1,2),F(1,2),F(0))
        m1=stated_moments(F(1,2),F(1,2),t)
        assert m1[1]-m0[1]==t*t/F(9)
        assert m1[2]-m0[2]==F(2,15)*t*t
        delta=max(abs(m1[1]-m0[1]),abs(m1[2]-m0[2]))
        gram_distance=sqrt(float(2*t*t))
        assert gram_distance <=sqrt(float(F(16446,41)*delta))
    print('OPTIMAL_SQUARE_ROOT_GRAM_BOUND_CHECKED')


def test_independent_sampling():
    rng=Random(172902)
    for (A,B,C) in [(1.0,0.8,0.35),(2.0,1.1,-0.6),(0.6,0.6,0.1)]:
        a=sqrt(A)
        bx=C/a
        by=sqrt(B-bx*bx)
        n=160000
        z1=z2=z3=0.0
        for _ in range(n):
            u=rng.random()-rng.random()
            v=rng.random()-rng.random()
            z=(a*u+bx*v)**2+(by*v)**2
            z1+=z; z2+=z*z; z3+=z*z*z
        theo=stated_moments(A,B,C)
        observed=(z1/n,z2/n,z3/n)
        for obs,expected in zip(observed,theo):
            assert abs(obs-float(expected)) < 0.025*max(float(expected),0.1),(obs,expected)
    print('INDEPENDENT_EUCLIDEAN_POINT_PAIR_SAMPLING_PASSED')

if __name__=='__main__':
    test_exact()
    test_stability()
    test_independent_sampling()
    print('ALL_CHECKS_PASSED')
