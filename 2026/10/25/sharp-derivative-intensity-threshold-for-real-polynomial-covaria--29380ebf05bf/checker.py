"""Exact finite-dimensional checks of the derivative-intensity covariance theorem.
Run: python checker.py (requires Python 3 and sympy).
This checker corroborates, but does not replace, the all-degree proof.
"""
from itertools import product
from math import factorial
from sympy import Matrix, binomial, symbols, Poly, expand, eye

x, y = symbols('x y')
checks = 0
for n in range(1, 13):
    pairs = [(i, j) for i in range(n + 1) for j in range(i, n + 1)]
    d = len(pairs)
    for k in range(0, min(n, 7) + 1):
        # One independent intensity-polynomial row per derivative order and power.
        rows = []
        for j in range(k+1):
            for power in range(2*(n-j)+1):
                row = []
                for i,l in pairs:
                    c = (1 if i == l else 2)* (factorial(i)//factorial(i-j))*(factorial(l)//factorial(l-j)) if min(i,l)>=j and i+l-2*j==power else 0
                    row.append(c)
                rows.append(row)
        M = Matrix(rows)
        nullity = d - M.rank()
        remaining = n-2*k-2
        expected = (remaining+1)*(remaining+2)//2 if remaining>=0 else 0
        assert nullity == expected, (n,k,nullity,expected)
        checks+=1
        if 2*(k+1)<=n:
            B = Poly(expand((x-y)**(2*k+2)), x,y)
            H=Matrix(n+1,n+1,lambda i,l: B.coeff_monomial(x**i*y**l))
            assert H == H.T and H!=Matrix.zeros(n+1)
            coeff=Matrix([H[i,l] for i,l in pairs])
            assert M*coeff == Matrix.zeros(M.rows,1)
            # Exactly positive-definite ambiguous pair: I +- small epsilon*H.
            eps = 1/(2*sum(abs(t) for t in H) + 2)
            P=eye(n+1)+eps*H
            Q=eye(n+1)-eps*H
            # Strict diagonal dominance after scaling proves SPD via Gershgorin.
            for Z in [P,Q]:
                for i in range(n+1):
                    assert Z[i,i] > sum(abs(Z[i,l]) for l in range(n+1) if l != i)
            checks+=1
print(f'PASS: {checks} exact assertions, degrees n=1..12, derivative ranges up to 7')
