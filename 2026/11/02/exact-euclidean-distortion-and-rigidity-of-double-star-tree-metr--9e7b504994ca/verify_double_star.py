"""Supplementary finite high-precision checks for the bistar metric formulas.

Run: python verify_double_star.py
Only the analytic argument in RESULT.md proves the all-parameter theorem.
"""
from decimal import Decimal, getcontext
from itertools import combinations

getcontext().prec = 75
D = lambda x: Decimal(x)
TOL = D('2e-55')


def radius(k):
    return D(2) - D(2)/D(k)


def expression(c, r, s):
    return r+s+((c-r).sqrt()+c.sqrt()+(c-s).sqrt())**2


def square_optimal(m, n):
    r, s = radius(m), radius(n)
    lo, hi = max(r, s), D(3)
    assert expression(lo, r, s) < 9 < expression(hi, r, s)
    for _ in range(280):
        mid = (lo + hi)/2
        if expression(mid, r, s) >= 9:
            hi = mid
        else:
            lo = mid
    c = (lo+hi)/2
    assert abs(expression(c, r, s)-9) < TOL
    return c


def vec(a, m, n, C, x, y):
    """Explicit coordinates: line, A simplex, B simplex.

    a: 'u', 'v', ('A',i), or ('B',j); x and y are positive offsets.
    """
    out = [D(0)] * (m+n+1)
    if a == 'u':
        pass
    elif a == 'v':
        out[0] = C
    elif a[0] == 'A':
        out[0] = -x
        k = a[1]
        for i in range(m):
            out[1+i] = D(2).sqrt()*(D(int(i == k)) - D(1)/D(m))
    elif a[0] == 'B':
        out[0] = C+y
        k = a[1]
        for j in range(n):
            out[1+m+j] = D(2).sqrt()*(D(int(j == k)) - D(1)/D(n))
    else:
        raise ValueError(a)
    return out


def graph_distance(a,b):
    if a == b: return D(0)
    if a in ('u','v') and b in ('u','v'): return D(1)
    if a in ('u','v'):
        if (a=='u' and b[0]=='A') or (a=='v' and b[0]=='B'): return D(1)
        return D(2)
    if b in ('u','v'): return graph_distance(b,a)
    if a[0] == b[0]: return D(2)
    return D(3)


def test_pair(m, n):
    r, s = radius(m), radius(n)
    c = square_optimal(m, n)
    x, y, C = (c-r).sqrt(), (c-s).sqrt(), c.sqrt()
    # Analytical branch inequalities, tested without using distances.
    assert c > max(r, s)
    assert 2*c+2*(c*(c-r)).sqrt() > 4
    assert 2*c+2*(c*(c-s)).sqrt() > 4
    assert 2*c+2*(c*(c-r)).sqrt() <= 4*c
    assert 2*c+2*(c*(c-s)).sqrt() <= 4*c
    nodes = ['u','v']+[('A',i) for i in range(m)]+[('B',j) for j in range(n)]
    V = {a:vec(a,m,n,C,x,y) for a in nodes}
    actual = set()
    total = 0
    for a,b in combinations(nodes,2):
        d = graph_distance(a,b)
        sq = sum((p-q)**2 for p,q in zip(V[a],V[b]))
        assert d*d*(1-TOL) <= sq <= c*d*d*(1+TOL), (m,n,a,b,d,sq,c)
        if a in ('u','v') and b in ('u','v'):
            assert abs(sq-c) < TOL
        if d==D(3):
            assert abs(sq-D(9)) < TOL
        actual.add(round(float(sq/(d*d)),7))
        total+=1
    assert abs(max(actual)-float(c)) < 1e-6
    assert abs(min(actual)-1) < 1e-6
    return c,total


def main():
    cases=0; pairs=0
    for m in range(2,15):
        for n in range(2,15):
            c, p=test_pair(m,n)
            cases+=1; pairs+=p
            if m==n:
                t=radius(m)
                closed=((2*(D(9)+t).sqrt()-(D(9)-2*t).sqrt())/3)**2
                assert abs(c-closed)<TOL
    for m,n in [(2,1000),(1000,2),(1000,1000),(2,100000)]:
        c=square_optimal(m,n)
        assert radius(m)<c and radius(n)<c<D(3)
        cases+=1
    asym=((2*D(11).sqrt()-D(5).sqrt())/3)**2
    assert abs(asym-(D(49)-4*D(55).sqrt())/9)<TOL
    print('CHECK_OK parameter_cases=',cases,'explicit_vertex_pairs=',pairs)
    for m,n in [(2,2),(2,3),(3,3),(2,5),(10,10),(1000,1000)]:
        print('n=',m,n,'distortion=',square_optimal(m,n).sqrt())
    print('balanced_limit=',asym.sqrt())

if __name__=='__main__':
    main()
