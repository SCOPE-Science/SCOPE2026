"""Supplementary finite checks for Gaussian localization commutator formula.

Run: python check_gaussian_commutator.py
Uses only the Python standard library. Finite checks do not prove the theorem.
"""
from math import sqrt, factorial
from itertools import permutations


def closed_form(a, b, c):
    u = 1.0 / (1.0 + a)
    B = 1.0 + b
    A = B*B-c*c-u*u
    d1 = A*A-c*c*(1.0+u*u)**2
    d2 = A*A-4.0*c*c*u*u
    assert d1 > 0 and d2 > 0
    return 2.0*u*u*(1.0/sqrt(d1)-1.0/sqrt(d2))


def matrix_truncation(a, b, c, cutoff=70):
    # A generating-function recurrence for complex Gaussian moments.
    u = 1.0/(1.0+a)
    B = 1.0+b
    D = B*B-c*c
    coeff = [[0.0]*cutoff for _ in range(cutoff)]
    coeff[0][0] = 1.0/sqrt(D)
    for n in range(2,cutoff,2):
        coeff[0][n] = coeff[0][n-2]*c/(D*n)
    for m in range(1,cutoff):
        for n in range(cutoff):
            v = (B/D)*coeff[m-1][n-1] if n else 0.0
            if m >= 2:
                v += (c/D)*coeff[m-2][n]
            coeff[m][n] = v/m
    scale = [sqrt(factorial(i)) for i in range(cutoff)]
    return sum((u**(m+1)-u**(n+1))**2 *
               (coeff[m][n]*scale[m]*scale[n])**2
               for m in range(cutoff) for n in range(cutoff))


def determinant4(mat):
    total = 0j
    for p in permutations(range(4)):
        inversions = sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        v = (-1 if inversions%2 else 1)
        for i in range(4):
            v *= mat[i][p[i]]
        total += v
    return total


def run():
    # Direct 4x4 determinants at rationally spaced parameters.
    determinant_tests = 0
    for B in [1.1,1.6,2.3]:
        for c in [0.0,0.2,0.6]:
            if c>=B-1: continue
            for x,y in [(0.03,0.2),(0.4,0.7),(0.9,0.45)]:
                p=(x+y)/2
                d=(x-y)/2
                mat=[[B-c,-p,0,-1j*d],[-p,B-c,1j*d,0],
                     [0,1j*d,B+c,-p],[-1j*d,0,-p,B+c]]
                expected=(B*B-c*c-x*y)**2-c*c*(x+y)**2
                assert abs(determinant4(mat)-expected) < 2e-11
                determinant_tests+=1
    examples=[(0.5,1.2,0.3),(1.5,0.9,0.8),(2.,1.5,1.5),
              (0.8,2.,0.7),(1.,1.,0.),(0.25,1.3,1.)]
    for a,b,c in examples:
        exact=closed_form(a,b,c)
        finite=matrix_truncation(a,b,c,70)
        assert abs(finite-exact)<max(1e-10,1e-7*exact),(a,b,c,exact,finite)
        print('comparison',a,b,c,'closed',format(exact,'.12g'),
              'finite',format(finite,'.12g'))
    monotone_tests=0
    for a,b in [(0.5,0.8),(1.,1.),(2.,0.4)]:
        vals=[closed_form(a,b,b*j/25) for j in range(26)]
        assert all(vals[j+1]>vals[j] for j in range(25))
        monotone_tests+=25
    local_tests=0
    for a,b in [(0.5,1.0),(1.,1.5),(2.,0.7)]:
        u=1/(1+a)
        coefficient=(u*(1-u*u)/( (1+b)**2-u*u)**1.5)**2
        for c in [0.01,0.005,0.002]:
            assert abs(closed_form(a,b,c)/c**2-coefficient)<0.005*coefficient
            local_tests+=1
    print('PASS',determinant_tests,'determinants;',len(examples),
          '70x70 matrix truncations;',monotone_tests,'strict monotonicity comparisons;',
          local_tests,'quadratic-scale checks')

if __name__ == '__main__':
    run()
