"""Exact arithmetic checks of the rooted linear-routing observability factorization.

Requires Python 3 and sympy; all computations are finite checks of an analytical theorem.
"""
from itertools import product
from random import Random
from sympy import Matrix, Rational, prod, symbols, simplify


def comparable(i, j, parent):
    def ancestor(a, x):
        while x != -1:
            if x == a:
                return True
            x = parent[x]
        return False
    return ancestor(i, j) or ancestor(j, i)


def matrices(parent, k, b, c):
    n = len(parent)
    A = Matrix.zeros(n)
    for i in range(n):
        A[i, i] = -k[i]
        if i:
            A[parent[i], i] = b[i]
    C = Matrix([[c] + [0]*(n-1)])
    O = Matrix.vstack(*(C * A**j for j in range(n)))
    return A, C, O


def predicted(parent, k, b, c):
    n = len(parent)
    g = []
    for i in range(n):
        p = i
        weight = 1
        while p:
            weight *= b[p]
            p = parent[p]
        g.append(weight)
    f = c**n * prod(g)
    for i in range(n):
        for j in range(i+1, n):
            if not comparable(i, j, parent):
                f *= (k[i]-k[j])
    return f


def test():
    symbolic_cases = 0
    for n in range(1, 6):
        for prefix in product(*(range(i) for i in range(1, n))):
            parent = [-1] + list(prefix)
            k = symbols('k0:'+str(n))
            b = (1,) + symbols('b1:'+str(n))
            c = symbols('c')
            _, _, O = matrices(parent, k, b, c)
            assert simplify(O.det(method='berkowitz') - predicted(parent, k, b, c)) == 0, parent
            symbolic_cases += 1
    rng = Random(129773)
    rational_cases = 0
    degeneracy_cases = 0
    for n in range(2, 9):
        for trial in range(95):
            parent = [-1] + [rng.randrange(i) for i in range(1, n)]
            k = [Rational(rng.randrange(1, 13), rng.randrange(1, 7)) for _ in range(n)]
            b = [0] + [k[i]*Rational(rng.randrange(1, 7), 7) for i in range(1, n)]
            c = k[0]
            _, _, O = matrices(parent, k, b, c)
            target = predicted(parent, k, b, c)
            det = O.det(method='domain-ge')
            assert det == target, (parent, k, b, det, target)
            assert (det == 0) == any(k[i] == k[j] and not comparable(i, j, parent) for i in range(n) for j in range(i+1, n))
            rational_cases += 1
            degeneracy_cases += int(det == 0)
    # Degenerate equal-rate cases on a chain, and across siblings.
    for parent, k, expected in [([-1,0,1], [2,2,2], True),
                                ([-1,0,0], [2,3,3], False),
                                ([-1,0,0,1], [2,3,5,3], True),
                                ([-1,0,0,1], [2,3,5,5], False)]:
        n=len(parent)
        b=[0]+[Rational(1,2)*k[i] for i in range(1,n)]
        _,_,O=matrices(parent,k,b,k[0])
        assert (O.det() !=0) is expected
    print('PASS: symbolic rooted trees:',symbolic_cases)
    print('PASS: exact rational routed networks:',rational_cases)
    print('PASS: singular instances among these:',degeneracy_cases)
    print('PASS: repeated-rate chain/sibling boundary cases: 4')


if __name__ == '__main__':
    test()
