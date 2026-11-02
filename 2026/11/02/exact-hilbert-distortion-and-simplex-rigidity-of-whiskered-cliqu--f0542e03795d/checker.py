"""Standalone finite exact-algebra and high-precision checks for a metric-embedding theorem.

Run with Python 3.10 or later: python checker.py
The exhaustive statements are solely for the enumerated indices; the accompanying
mathematical proof establishes the theorem for every integer n >= 2.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext


def field(n):
    """Represent a+b*c in Q[c], with (n+1)c*c+6(n-1)c-9(n-1)=0."""
    def add(x, y): return x[0]+y[0], x[1]+y[1]
    def neg(x): return -x[0], -x[1]
    def mul(x, y):
        a, b = x
        d, e = y
        return a*d+b*e*Q(9*(n-1), n+1), a*e+b*d-b*e*Q(6*(n-1), n+1)
    def scl(k, x): return Q(k)*x[0], Q(k)*x[1]
    def sub(x, y): return add(x, neg(y))
    return add, mul, scl, sub


def dec(v): return Decimal(v)


def theorem_check():
    exact = 0
    coord = 0
    with localcontext() as ctx:
        ctx.prec = 65
        prev = None
        for n in range(2, 101):
            add, mul, scl, sub = field(n)
            unit, C = (Q(1), Q(0)), (Q(0), Q(1))
            three = scl(3, unit)
            c2 = mul(C, C)
            a = Q(n-1, 2*n)
            z = scl(a, mul(sub(three, C), sub(three, C)))
            w = scl(Q(n-1, 2*n), add(c2, scl(9, unit)))
            w = add(w, scl(Q(3, n), C))
            assert z == c2, (n, z, c2)
            assert sub(w, z) == scl(3, C), (n, w, z)
            assert w == add(c2, scl(3, C)), (n, w)
            exact += 3

            c = dec(3)/(dec(1)+(dec(2*n)/dec(n-1)).sqrt())
            assert c >= 1 and c < 3
            if prev is not None:
                assert c > prev
            prev = c
            eps = dec('1e-55')
            assert abs(dec(n+1)*c*c + dec(6*(n-1))*c - dec(9*(n-1))) < eps
            assert abs(dec(n-1)/dec(2*n)*(dec(3)-c)**2-c*c) < eps
            d = c*c + dec(3)*c
            assert dec(4)-eps <= d <= dec(4)*c*c+eps
            exact += 4
            if n <= 17:
                # Direct ambient (n-1)-dimensional Gram realization, checked
                # on every unordered pair of the 2n vertices in Q(sqrt(...)).
                u = [[(dec(1) if j == i else dec(0))-dec(1)/dec(n) for j in range(n)] for i in range(n)]
                pts = [[(c/dec(2).sqrt())*v for v in row] for row in u]
                pts += [[(dec(3)/dec(2).sqrt())*v for v in row] for row in u]
                def original(i, j):
                    li, lj = i//n, j//n
                    ri, rj = i % n, j % n
                    if li == lj:
                        return dec(1) if li == 0 else dec(3)
                    return dec(1) if ri == rj else dec(2)
                for i in range(2*n):
                    for j in range(i+1, 2*n):
                        sq = sum((pts[i][k]-pts[j][k])**2 for k in range(n))
                        dd = original(i,j)
                        assert dd*dd-dec('1e-50') <= sq <= c*c*dd*dd+dec('1e-50'), (n,i,j,sq,dd,c)
                        if i < n and j < n: assert abs(sq-c*c) < dec('1e-50')
                        if i >= n and j >= n: assert abs(sq-9) < dec('1e-50')
                        if i < n and j >= n and j-i == n: assert abs(sq-c*c)< dec('1e-50')
                        if i < n and j >= n and j-i != n: assert abs(sq-(c*c+3*c))< dec('1e-50')
                        coord += 1
        assert dec(3)/(dec(1)+dec(2).sqrt()) > prev
    print(f'CHECK_OK exact_field_and_high_precision_assertions={exact} exhaustive_coordinate_pairs={coord} n_exact=2..100 n_coordinate=2..17')


if __name__ == '__main__':
    theorem_check()
