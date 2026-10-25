"""Exact finite-dimensional checks for the central-edge observability theorem.

Requires Python 3 and SymPy. Analytic all-size arguments appear in RESULT.md;
this script checks 462 rational instances independently by characteristic polynomials.
"""
import math
import sympy as sp

z = sp.Symbol("z")


def tridiagonal_characteristic(diagonal, edge_weights):
    """Return det(diag(diagonal)+offdiag(-weights)-zI), exact in Q[z]."""
    if not diagonal:
        return sp.Integer(1)
    prev, now = sp.Integer(1), diagonal[0] - z
    for index in range(1, len(diagonal)):
        prev, now = now, sp.expand(
            (diagonal[index] - z) * now - edge_weights[index-1]**2 * prev
        )
    return sp.Poly(now, z)


def unobservable(m, j, central_weight):
    n = 2 * m
    edges = [sp.Integer(1)] * (n - 1)
    edges[m - 1] = sp.Rational(central_weight)
    diagonal = [edges[0]] + [edges[i-1]+edges[i] for i in range(1,n-1)] + [edges[-1]]
    def principal(start, stop):
        return tridiagonal_characteristic(diagonal[start:stop], edges[start:stop-1])
    whole = principal(0,n)
    # The deleted-vertex minor is block diagonal; on a simple-spectrum
    # Jacobi matrix, a common root is equivalent to an eigenvector zero.
    left, right = principal(0, j-1), principal(j,n)
    return sp.degree(sp.gcd(whole, left*right)) > 0


def predicted(m, j, w):
    if math.gcd(m,2*j-1) > 1:
        return True
    for r in range(1,j):
        theta=(2*r-1)*math.pi/(2*j-1)
        denominator=math.cos((m-0.5)*theta)
        if abs(denominator)<1e-8:
            continue
        candidate=math.sin(theta/2)*math.sin(m*theta)/denominator
        if candidate>0 and abs(candidate-w)<1e-7:
            return True
    return False


def main():
    weights = [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),
               sp.Integer(1),sp.Rational(3,2),sp.Integer(2)]
    count=0
    for m in range(2,13):
        for weight in weights:
            for j in range(1,m+1):
                actual=unobservable(m,j,weight)
                expected=predicted(m,j,float(weight))
                assert actual==expected, (m,j,weight,actual,expected)
                count+=1
    assert count==462
    second_count=0
    for m in range(2,13):
        for weight in [sp.Rational(1,2),sp.Integer(1)]:
            actual=unobservable(m,2,weight)
            expected=(m%3==0 or (m%3==1 and weight==sp.Rational(1,2)))
            assert actual==expected, (m,weight)
            second_count+=1
    assert second_count==22
    print('PASS: 462 exact polynomial-GCD versus trigonometric-classification cases')
    print('PASS: 22 exact second-vertex mod-3 and weight-one-half cases')
    print('NOTE: finite checks supplement, not establish, the all-size theorem')


if __name__=='__main__':
    main()
