"""Exact rational checks for degree-four spherical harmonic evaluation on signed-pair roots.

Run: python degree4_root_checker.py
All quantities are rational; the infinite-dimensional theorem uses an algebraic proof.
"""
from fractions import Fraction as F
from itertools import combinations


def kernel(d, t):
    t = F(t)
    return ((d + 2) * (d + 4) * t**4 - 6 * (d + 2) * t**2 + 3) / F((d - 1) * (d + 1))


def theoretical(d):
    return {
        "antisymmetric": (F(d*d - 4, d*d - 1), d*(d-1)//2),
        "constant": (F((d-4)**2*(d+4), 4*(d*d-1)), 1),
        "standard": (F((d-8)**2*(d+2), 8*(d*d-1)), d-1),
        "edge": (F(3*(d+2)*(d+4), 4*(d*d-1)), d*(d-3)//2),
    }


def sample_points(d):
    return [(i, j, s) for i,j in combinations(range(d),2) for s in (1,-1)]


def scalar_product(a,b):
    i,j,s=a; k,l,t=b
    return F((1 if i==k else 0) + (t if i==l else 0)
             + (s if j==k else 0) + (s*t if j==l else 0),2)


def matrix(d):
    pts=sample_points(d)
    return pts, [[kernel(d,scalar_product(a,b)) for b in pts] for a in pts]


def apply(g,vec):
    return [sum((v*x for v,x in zip(row,vec)),F(0)) for row in g]


def eq_eigen(g,vec,value):
    return apply(g,vec)==[value*x for x in vec]


def check(d):
    pts,g=matrix(d)
    n=len(pts)
    lam={a:b for a,(b,m) in theoretical(d).items()}
    assert len(pts)==d*(d-1)
    assert sum(m for val,m in theoretical(d).values())==n
    assert all(g[i][j]==g[j][i] for i in range(n) for j in range(n))
    assert all(g[i][i]==1 for i in range(n))
    def vec(fn): return [F(fn(i,j,s)) for i,j,s in pts]
    # Each signed-pair orientation difference is an eigenvector.
    for i,j in combinations(range(d),2):
        v=vec(lambda a,b,s:int((a,b)==(i,j))*s)
        assert eq_eigen(g,v,lam['antisymmetric'])
    # The block-constant vector and the standard vertex incidence block.
    assert eq_eigen(g,vec(lambda i,j,s:1),lam['constant'])
    for k in range(d-1):
        v=vec(lambda i,j,s:(int(k in (i,j))-int(d-1 in (i,j))))
        assert eq_eigen(g,v,lam['standard'])
    # Remaining Johnson edge sector: coefficient vectors whose vertex incidence sums vanish.
    # Four-cycle vectors span this sector for d>=4.
    for a,b,c,e in combinations(range(d),4):
        edges={(a,b):1,(c,e):1,(a,c):-1,(b,e):-1}
        v=vec(lambda i,j,s:edges.get((i,j),0))
        assert eq_eigen(g,v,lam['edge'])
    rank_expected=n-(int(d==4)+ (d-1)*int(d==8))
    assert sum(m for val,m in theoretical(d).values() if val)!=0
    assert sum(m for val,m in theoretical(d).values() if val>0)==rank_expected
    return rank_expected, min(val for val,m in theoretical(d).values() if val>0 and m>0)


def main():
    print('Exact rational Gram eigenspace checks:')
    for d in range(3,13):
        rank,mineig=check(d)
        print(f'd={d:2d}  samples={d*(d-1):3d}  rank={rank:3d}  minimum-positive={mineig}')
    for d in range(3,501):
        spec=theoretical(d)
        assert all(val>=0 for val,_ in spec.values())
        assert sum(m for val,m in spec.values() if val>0)==d*(d-1)-(int(d==4)+(d-1)*int(d==8))
        assert min(val for val,m in spec.values() if val>0 and m)>=(F(11,640))
    print('Degree dimensions 3..500: all nonzero spectral values >= 11/640; equality at d=9.')
    assert min(v for v,m in theoretical(9).values() if v>0)==F(11,640)
    print('All exact checks passed.')


if __name__ == '__main__':
    main()
