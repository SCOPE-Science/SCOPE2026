"""Exact checks for affine L2 projection on balanced complete multipartite metric graphs.

Requires sympy. All computations are exact rational/symbolic except none.
"""
from fractions import Fraction
from itertools import combinations
import sympy as S


def abs_linear_integral(a, b):
    """Integral from 0 to 1 of |(1-t)a+t b|, exact rational."""
    a, b = S.Rational(a), S.Rational(b)
    if a*b >= 0:
        return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))


def formula(m,r):
    return S.Rational(24*m*r*r-70*m*r+51*m+4*r-5,
                      3*(2*r-3)*(2*m*r-3*m+1))


def evaluate(m, r):
    n = m*r
    edges = [(i,j) for i,j in combinations(range(n),2) if i//m != j//m]
    deg = [(r-1)*m]*n
    G = S.zeros(n)
    for i in range(n):
        G[i,i] = S.Rational(deg[i],3)
    for i,j in edges:
        G[i,j] = G[j,i] = S.Rational(1,6)
    H = G.inv()
    assert G*H == S.eye(n)
    T = m*m*(r-1)*(2*r-3)
    X = 3*m*(2*r-3)+1
    checks = 0
    for i in range(n):
        for j in range(n):
            expected = S.Rational(X if i == j else (1 if i//m==j//m else -2),T)
            assert H[i,j] == expected, (m,r,i,j,H[i,j],expected)
            checks += 1
        row = sum((abs_linear_integral(H[i,j],H[i,k]) for j,k in edges), S.S(0))
        assert S.factor(row-formula(m,r)) == 0, (m,r,i,row,formula(m,r))
        assert row >= 1
        checks += 2
    return checks


def symbolic():
    m,r = S.symbols('m r',integer=True,positive=True)
    X=3*m*(2*r-3)+1
    T=m*m*(r-1)*(2*r-3)
    d=m*(r-1)
    raw=S.factor((d*(X**2+4)/(2*(X+2)) + d*(m-1)*S.Rational(5,6)
           +m*m*(r-1)*(r-2))/T)
    claim=(24*m*r**2-70*m*r+51*m+4*r-5)/(3*(2*r-3)*(2*m*r-3*m+1))
    assert S.factor(raw-claim)==0
    assert S.factor((claim-2) - (m*(2*r-3)-8*r+13)/(3*(2*r-3)*(m*(2*r-3)+1))) == 0
    assert S.factor((claim.subs(m,m+1)-claim) - 4*(2*r-3)/(3*(2*m*r-3*m+1)*(2*m*r-3*m+2*r-2)))==0
    assert S.limit(claim,r,S.oo)==2
    assert S.factor(S.limit(claim,m,S.oo) -(12*r-17)/(3*(2*r-3)))==0
    return 5


def main():
    count=symbolic()
    tested=[]
    for r in range(2,8):
        for m in range(1,6):
            if m*r>24:
                continue
            count+=evaluate(m,r)
            tested.append((m,r))
    print('PASS; exact assertions:',count,'balanced multipartite configurations:',len(tested))
    print('Configurations:',tested)
    print('Examples:',[(m,r,str(formula(m,r))) for m,r in [(1,2),(1,3),(2,2),(3,2),(4,2),(4,3),(5,5)]])

if __name__=='__main__':
    main()
