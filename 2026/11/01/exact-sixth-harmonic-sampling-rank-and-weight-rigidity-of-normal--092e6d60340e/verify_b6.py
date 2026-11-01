"""Exact sixth-harmonic sampling checks for normalized type-B root orbits.

Uses only the Python standard library.  The infinite-dimensional assertions
are proved algebraically in RESULT.md; these finite checks are independent
cross-checks of the explicit Gram entries and exceptional ranks.
"""
from fractions import Fraction as F
from math import comb


def p6(n, u):
    """Gegenbauer numerator as a polynomial in squared inner product."""
    u = F(u)
    return (n+4)*(n+6)*(n+8)*u**3 - 15*(n+4)*(n+6)*u**2 + 45*(n+4)*u-15


def g6(n, u):
    return p6(n,u) / ((n-1)*(n+1)*(n+3))


def projective_points(n):
    # short representative e_i; long representative (e_i + s*e_j)/sqrt(2)
    points = [('S',i) for i in range(n)]
    points += [('L',i,j,s) for i in range(n) for j in range(i+1,n) for s in (-1,1)]
    assert len(points)==n*n
    return points


def dot_squared(a,b):
    if a[0]=='S' and b[0]=='S': return F(int(a[1]==b[1]))
    if a[0]=='S' and b[0]=='L': return F(int(a[1] in b[1:3]),2)
    if a[0]=='L' and b[0]=='S': return F(int(b[1] in a[1:3]),2)
    _,i,j,s=a
    _,u,v,t=b
    dot= int(i==u) + t*int(i==v) +s*int(j==u)+s*t*int(j==v)
    return F(dot*dot,4)


def rational_rank(rows):
    # Exact rational elimination without floating-point rank thresholds.
    a=[[F(x) for x in row] for row in rows]
    m=len(a); n=len(a[0]); k=0
    for c in range(n):
        piv=next((i for i in range(k,m) if a[i][c]),None)
        if piv is None: continue
        a[k],a[piv]=a[piv],a[k]
        v=a[k][c]
        for i in range(k+1,m):
            if not a[i][c]:continue
            q=a[i][c]/v
            for j in range(c+1,n):a[i][j]-=q*a[k][j]
            a[i][c]=0
        k+=1
        if k==m:break
    return k


def check():
    assertions=0
    for n in range(3,23):
        D=(n-1)*(n+1)*(n+3)
        x,y,z=(g6(n,u) for u in (0,F(1,4),F(1,2)))
        one=g6(n,1)
        assert one==1;assertions+=1
        # All five spectral sectors derived from the independent short/long
        # point-product geometry.  These are exact rational identities.
        diff=1-x
        pair=1+3*x-4*y
        A=1-x
        S=A+2*(n-4)*(y-x)
        std_det=A*S-2*(n-2)*(z-x)**2
        triv_A=1+(n-1)*x
        m=comb(n,2)
        triv_D=1-x+4*(n-2)*(y-x)+2*m*x
        triv_B_sq=F(2*n*m)*(x+F(2,n)*(z-x))**2
        assert diff==F((n+4)*(n*n-n+3),D)
        assert pair==F(15*(n-4)*(n+4)*(n+6),16*D)
        assert std_det==F(15*n*(n-3)*(n+4)**2*(n+6)*(n+8),32*D*D)
        assert triv_A==F((n-2)*(n+6),(n+1)*(n+3))
        assert triv_D==F((n-16)**2*(n-2)*(n+6),16*D)
        assert triv_A*triv_D==triv_B_sq
        assert diff>0 and A>0 and S>0 and triv_A>0
        assert (std_det==0)==(n==3)
        assert (pair==0)==(n==4)
        assert n in (3,4) or pair>0
        assertions+=11
        # Distinct root-orbit sizes and B_n-invariant degree-six null weight:
        # short weight 16-n, long weight 4.
        ws=16-n; wl=4
        short_row=(1+(n-1)*x)*ws+(2*(n-1)*z+(n-1)*(n-2)*x)*wl
        assert short_row==0;assertions+=1
        # Every Gram row sums to zero against the proposed signed weights.
        # Test both orbit representatives by explicit combinatorial counts.
        points=projective_points(n)
        for p in (points[0],points[n]):
            total=sum((ws if q[0]=='S' else wl)*g6(n,dot_squared(p,q)) for q in points)
            assert total==0
            assertions+=1
        if n in (3,4,5,6):
            # Assemble all points with exact algebraic inner-product squares,
            # not the representation-theoretic blocks, then eliminate.
            matrix=[[g6(n,dot_squared(p,q)) for q in points] for p in points]
            r=rational_rank(matrix)
            expected={3:6,4:13}.get(n,n*n-1)
            assert r==expected,(n,r,expected)
            assertions+=1
            print('n',n,'exact_rank',r,'expected',expected)
    print('TYPE_B_SIXTH_HARMONIC_EXACT_CHECK_OK',assertions)

if __name__=='__main__':check()
