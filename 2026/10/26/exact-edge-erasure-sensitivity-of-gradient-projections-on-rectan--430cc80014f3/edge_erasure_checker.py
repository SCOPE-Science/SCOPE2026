"""Exact finite checks for the one-edge-erased complete-bipartite gradient projector.

Requires Python 3 and SymPy. The theorem for all dimensions is proved
algebraically in RESULT.md; these computations test its formulas independently.
"""
from sympy import Matrix, Rational


def run():
    tests = 0
    for a in range(2, 9):
        for b in range(2, 9):
            edges = [(i, j) for i in range(a) for j in range(b)
                     if (i, j) != (0, 0)]
            # Orient all edges left to right; ground the last right vertex.
            B = Matrix.zeros(len(edges), a + b - 1)
            for r, (i, j) in enumerate(edges):
                B[r, i] = 1
                if j < b - 1:
                    B[r, a + j] = -1
            gram = B.T * B
            assert gram.det() != 0
            projector = B * gram.inv() * B.T
            assert projector * projector == projector
            assert projector.T == projector
            predicted = (1 + Rational(2 * (a - 1) * (b - 1), a * b)
                         - Rational(2, a * b * (a - 1) * (b - 1)))
            norms = [sum(abs(projector[r, s]) for s in range(len(edges)))
                     for r in range(len(edges))]
            assert max(norms) == predicted, (a, b)
            for r, (i, j) in enumerate(edges):
                if i == 0:
                    want = 1 + Rational(2 * (a - 1) * (b - 2), a * (b - 1))
                elif j == 0:
                    want = 1 + Rational(2 * (b - 1) * (a - 2), b * (a - 1))
                else:
                    want = predicted
                assert norms[r] == want, (a, b, i, j)
                tests += 1
    print('PASS: %d exact row-norm comparisons in 49 graph instances' % tests)


if __name__ == '__main__':
    run()
