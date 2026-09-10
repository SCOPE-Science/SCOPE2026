"""Hand-check: six cubics kill every monomial of G; print Q10 minor matrix."""
from sympy import Matrix, Rational
from audit_target import monomials_4

R2 = monomials_4(2); R3 = monomials_4(3)
J = [8, 9, 15, 16, 18, 19]
I = [i for i in range(20) if i not in J]
Mult = Matrix.zeros(20, 10)
for j, em in enumerate(R2):
    for k in range(4):
        g = tuple(em[i] + (1 if i == k else 0) for i in range(4))
        Mult[R3.index(g), j] += 1
Q = Mult.extract(I, list(range(10)))
qrows = [0, 1, 2, 4, 5, 7, 8, 9, 11, 13]
Q10 = Q.extract(qrows, list(range(10)))
print("Q10 =")
for r in range(10):
    print([int(Q10[r, c]) for c in range(10)])
print("det =", Q10.det())
print("R3 rows used:", [R3[I[i]] for i in qrows])
print("R2 cols:", R2)
# hand reason for six cubics:
print("Each G monomial has (X,Y)-bidegree <= 2: (2,0),(1,1),(0,2),(0,0),(0,0).")
print("x^3,y^3,x^2y,xy^2 need X,Y-order 3 > 2 -> kill all terms.")
print("y^2u: Y-order 2 + U-order 1: check term by term:")
print(" X^2U^4: dYY=0; XYU^2V^2: dYY kills (Y-exp 1); Y^2V^4: -> 2*V^4 then dU=0; U-terms: dYY=0. OK.")
print("x^2v: X-order 2 + V-order 1:")
print(" X^2U^4: -> 2U^4 then dV=0; XYU^2V^2: dXX=0; Y^2V^4: dXX=0; aU^5V: dXX=0; bUV^5: dXX=0. OK.")
