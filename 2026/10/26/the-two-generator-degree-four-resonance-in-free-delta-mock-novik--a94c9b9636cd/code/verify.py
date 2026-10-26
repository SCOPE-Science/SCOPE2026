"""Exact certificates for the degree-four free delta-mock-Novikov algebra on two generators.
Run: python3 code/verify.py (requires SymPy)."""
from functools import lru_cache
from itertools import product
import sympy as sp
from sympy.polys.matrices import DomainMatrix

@lru_cache(None)
def shapes(n):
    if n == 1:
        return (None,)
    return tuple((l, r) for i in range(1, n)
                 for l in shapes(i) for r in shapes(n - i))

def label(t, it):
    return next(it) if t is None else (label(t[0], it), label(t[1], it))

words = [label(t, iter(v)) for t in shapes(4)
         for v in product((0, 1), repeat=4)]
assert len(words) == len(set(words)) == 80
index = {w: i for i, w in enumerate(words)}

def relation_f(a, b, c, d):
    return [(((a, b), c), d), (((b, a), c), d),
            ((a, (b, c)), 1), ((b, (a, c)), 1)]

def relation_g(a, b, c, d):
    return [(((a, b), c), 1), (((a, c), b), 1)]

def relation_rows(d):
    out = []
    def include(terms):
        row = {}
        for word, coefficient in terms:
            j = index[word]
            row[j] = row.get(j, 0) + coefficient
        out.append({j: v for j, v in row.items() if v != 0})
    for a, b, c, z in product((0, 1), repeat=4):
        for rel in (relation_f, relation_g):
            terms = rel(a, b, c, d)
            include([((w, z), coef) for w, coef in terms])
            include([((z, w), coef) for w, coef in terms])
            for slot in range(3):
                arguments = [a, b, c]
                arguments[slot] = (arguments[slot], z)
                include(rel(*arguments, d))
    assert len(out) == 160
    return out

def matrix(d):
    return sp.MutableSparseMatrix(160, 80,
        {(i, j): v for i, row in enumerate(relation_rows(d))
         for j, v in row.items()})

def check_null(M, vector):
    assert len(vector) == 80
    assert all(sp.expand(value) == 0 for value in M * sp.Matrix(vector))

def vector(entries):
    result = [sp.Integer(0)] * 80
    for i, val in entries:
        result[i] = val
    return result

def number_of_zeros(t):
    return (int(t == 0) if isinstance(t, int) else
            number_of_zeros(t[0]) + number_of_zeros(t[1]))

def bidegree_dimension(M, n):
    col = [i for i, w in enumerate(words) if number_of_zeros(w) == n]
    row = [i for i in range(M.rows) if any(M[i, j] != 0 for j in col)]
    sub = M.extract(row, col)
    return len(col) - sub.rank()

def main():
    d = sp.symbols('d')
    M = matrix(d)
    generic = DomainMatrix.from_Matrix(M).convert_to(sp.QQ.frac_field(d))
    col = generic.rref()[1]
    row = generic.transpose().rref()[1]
    assert len(col) == len(row) == 79
    assert set(range(80)) - set(col) == {58}
    minor = M.extract(list(row), list(col))
    det = DomainMatrix.from_Matrix(minor).convert_to(sp.QQ.poly_ring(d)).det().as_expr()
    assert sp.expand(det + 2**41 * d**9 * (d + 1)**3) == 0
    upper = vector([(3,-d),(5,d**2),(6,-d*(d-1)),(9,-d*(d-1)),
        (10,d**2),(12,-d),(21,1-d),(22,d-1),(25,d-1),(26,1-d),
        (35,1),(38,-1),(41,-1),(44,1),(53,1),(54,-1),(57,-1),(58,1)])
    check_null(M, upper)
    assert upper[58] == 1
    M_ex = matrix(-1)
    D = DomainMatrix.from_Matrix(M_ex)
    c_ex = D.rref()[1]
    r_ex = D.transpose().rref()[1]
    assert len(c_ex) == len(r_ex) == 76
    assert set(range(80)) - set(c_ex) == {56,57,58,59}
    assert int(DomainMatrix.from_Matrix(M_ex.extract(list(r_ex),list(c_ex))).det()) == -2**38
    kernel = [
        [(2,1),(4,-1),(34,1),(40,-1),(52,-1),(56,1)],
        [(5,-1),(6,1),(9,1),(12,-1),(21,-1),(22,1),(25,1),(26,-1),
         (38,1),(44,-1),(53,-1),(57,1)],
        [(3,1),(6,-1),(9,-1),(10,1),(21,1),(22,-1),(25,-1),(26,1),
         (35,1),(41,-1),(54,-1),(58,1)],
        [(11,1),(13,-1),(39,1),(45,-1),(55,-1),(59,1)]]
    for j, entries in enumerate(kernel):
        v = vector(entries)
        check_null(M_ex, v)
        assert [v[i] for i in (56,57,58,59)] == [int(j==k) for k in range(4)]
    for val, expected in ((2, [0,0,1,0,0]),(-1,[0,1,2,1,0])):
        mval = matrix(val)
        # Each relation is homogeneous in the counts of generators.
        for i in range(mval.rows):
            supp = [j for j in range(mval.cols) if mval[i,j]]
            assert len({number_of_zeros(words[j]) for j in supp}) <= 1
        assert [bidegree_dimension(mval,k) for k in range(5)] == expected
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
