"""Exact, reproducible Jacobian-rank certificates for a conic-addition pencil.

Dependency: SymPy 1.14 or later. Run with `python verify.py`.
All ranks are over characteristic zero, not finite-field proxies.
"""
import sympy as s
from sympy.polys.matrices import DomainMatrix

x, y, z, t = s.symbols('x y z t')
f = s.expand((x*x + y*y - z*z)*(y-z)*(x*x-z*z)*(y*y-t*x*z))

def monomials(d):
    return [(a, b, d-a-b) for a in range(d+1) for b in range(d+1-a)]

def jacobian_matrix(r):
    src, dst = monomials(r), monomials(r+6)
    row_of = {m: i for i, m in enumerate(dst)}
    M = s.zeros(len(dst), 3*len(src))
    for k, g in enumerate([s.diff(f,x), s.diff(f,y), s.diff(f,z)]):
        for exponent, coeff in s.Poly(g, x, y, z).terms():
            for j, source_exponent in enumerate(src):
                out = tuple(a+b for a,b in zip(exponent,source_exponent))
                M[row_of[out], k*len(src)+j] = coeff
    return M

def rank_over(M, field):
    return DomainMatrix.from_Matrix(M).convert_to(field).rank()

# Row-column minors, indices are zero based in the matrix constructed above.
MINORS = {
(3,'a'):(
[0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33],
list(range(30)),
-7710244864*t**7*(8*t**2+21)),
(3,'b'):(
[49, 4, 11, 2, 44, 30, 36, 12, 25, 7, 50, 19, 51, 8, 40, 15, 17, 32, 52, 21, 47, 16, 38, 10, 42, 3, 46, 23, 20, 5],
[5, 27, 1, 17, 8, 4, 11, 2, 14, 20, 29, 7, 0, 26, 18, 12, 25, 15, 19, 9, 6, 21, 24, 13, 16, 22, 28, 10, 23, 3],
-30840979456*t**14*(80*t**8-76*t**6-591*t**4-1436*t**2-32)),
(4,'a'):(
[0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47],
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 43, 44],
6963646433329152*t**11*(t**2+4)*(3*t**2+2)),
(4,'b'):(
[7, 21, 8, 2, 38, 4, 12, 23, 3, 0, 5, 1, 60, 34, 40, 11, 6, 63, 13, 18, 37, 39, 24, 27, 52, 16, 26, 53, 57, 19, 30, 49, 59, 20, 14, 58, 44, 35, 36, 56, 43, 61, 42],
[26, 2, 12, 6, 37, 0, 30, 16, 1, 24, 20, 27, 3, 11, 4, 13, 28, 9, 44, 8, 19, 5, 10, 7, 21, 40, 14, 35, 38, 23, 18, 34, 42, 43, 22, 36, 32, 39, 17, 31, 15, 33, 29],
-5416169448144896*t**18*(t**2+4)*(2*t**6+2*t**4+9*t**2-33)),
(5,'a'):(
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60],
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 56, 61, 62],
35746718357756313600*t**15*(t-1)*(t+1)*(t**2+4)**2)
}

def run():
    assert s.factor(s.discriminant(x*x+t*x-1,x))==t*t+4
    assert s.factor(s.resultant(x*x+y*y-1,y*y-t*x,y))==(x*x+t*x-1)**2
    matrices = {r: jacobian_matrix(r) for r in (3,4,5)}
    for key,(rows,cols,expected) in MINORS.items():
        r=key[0]
        assert len(rows)==len(cols)==({3:30,4:43,5:56}[r])
        det=s.factor(matrices[r].extract(rows,cols).det(method='domain-ge'))
        assert s.expand(det-expected)==0, (key,s.factor(det))
    assert s.factor(s.gcd(MINORS[(3,'a')][2],MINORS[(3,'b')][2]))/s.Symbol('t')**7 != 0
    assert s.degree(s.gcd(MINORS[(3,'a')][2],MINORS[(3,'b')][2]),t)==7
    assert s.degree(s.gcd(MINORS[(4,'a')][2],MINORS[(4,'b')][2]),t)==13
    genfield=s.QQ.frac_field(t)
    assert [rank_over(matrices[r],genfield) for r in (3,4,5)] == [30,43,56]
    assert rank_over(matrices[4].subs(t,1),s.QQ)==43
    assert rank_over(matrices[5].subs(t,1),s.QQ)==55

    # Substitution x -> -x transforms the fiber at t into the fiber at -t.
    assert s.expand(f.subs(x,-x)-f.subs(t,-t))==0
    print('VERIFY_MAIN_OK generic_ranks=30,43,56 node_collision_r5=55 min_degree=4')
if __name__=='__main__':run()
