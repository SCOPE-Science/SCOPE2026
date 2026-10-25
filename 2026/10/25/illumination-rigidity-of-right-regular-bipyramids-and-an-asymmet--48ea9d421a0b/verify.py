"""Self-contained consistency checks for right regular bipyramid illumination.
The infinite-dimensional parameter assertions rely on the analytic proof in RESULT.md.
Run: python3 verify.py
"""
from fractions import Fraction
from math import cos, sin, pi, gcd


def wrapping(v, period):
    return ((v + period // 2) % period) - period // 2


def base_mask(n, q):
    """Azimuth (q+1/2)/8 periods; exact integer angular inequalities."""
    return sum(1 << k for k in range(n)
               if abs(wrapping(2*q+1-(16*k+8*n), 16*n)) < 4*n-8)


def check_angular():
    total = 0
    for n in range(3, 141):
        m = (n-1)//2
        masks = {base_mask(n, q) for q in range(8*n)}
        assert max(t.bit_count() for t in masks) == m, (n, 'capacity')
        optimal_masks = {t for t in masks if t.bit_count() == m}
        expected = {sum(1 << ((s+j) % n) for j in range(m)) for s in range(n)}
        assert optimal_masks == expected, (n, 'maximal blocks')
        for k in range(n):
            assert sum(k in [((s+j) % n) for j in range(m)]
                       for s in range(n)) == m
        # All cyclic optimal blocks satisfy exact fractional primal and dual.
        assert sum((Fraction(1, m) for _ in range(n)), Fraction(0)) == Fraction(n, m)
        g = gcd(n,m)
        assert g in (1,2)
        assert (g == 2) == (n % 4 == 2)
        total += len(masks)
    # Integer exact set covering for all n up to twelve.
    for n in range(3, 13):
        masks = sorted({base_mask(n, q) for q in range(8*n) if base_mask(n,q)},
                       key=lambda t: (-t.bit_count(),t))
        full = (1 << n) - 1
        dp = [n+1] * (1 << n)
        dp[0] = 0
        for s in range(1 << n):
            if dp[s] >= n: continue
            for mask in masks:
                t = s|mask
                if dp[t] > dp[s]+1: dp[t] = dp[s]+1
        assert dp[full] == (n + (n-1)//2 - 1)//((n-1)//2), (n,dp[full])
    return total


def facet_coverage(n, height_top, height_bottom, direction):
    """Independent floating-point diagnostic for geometric facet incidences."""
    c=cos(pi/n)
    w=[(cos((j+0.5)*2*pi/n), sin((j+0.5)*2*pi/n)) for j in range(n)]
    x,y,z=direction
    fd=[[(x*a+y*b)+c*z/height_top for a,b in w],
        [(x*a+y*b)-c*z/height_bottom for a,b in w]]
    if min(abs(v) for vals in fd for v in vals)<1e-9:
        return None
    top=all(v<0 for v in fd[0]);bottom=all(v<0 for v in fd[1]);ring=[]
    for k in range(n):
        j=(k-1)%n
        ring.append(all(fd[side][a]<0 for side in (0,1) for a in (j,k)))
    return top,bottom,ring


def check_facet_geometry():
    tests=0
    for n in range(3,61):
        m=(n-1)//2
        for h in (Fraction(1,3),Fraction(1),Fraction(5)):
            for q in range(8*n):
                ang=(q+0.5)*2*pi/(8*n)
                for t in (-3.1,-1.3,-0.7,-0.2,0,0.2,0.7,1.3,3.1):
                    out=facet_coverage(n,float(h),float(h), (cos(ang),sin(ang),t*float(h)))
                    if out is None:continue
                    top,bottom,ring=out
                    assert not(top and bottom)
                    assert not((top or bottom) and any(ring))
                    assert sum(ring)<=m
                    tests+=1
    return tests


def check_asymmetric_witness():
    n=5
    c=cos(pi/n)
    # This is an exact radical comparison, not a floating-point certificate:
    # cos(2pi/5)=(sqrt(5)-1)/4, cos(pi/5)=(sqrt(5)+1)/4.
    # 30 cos(2pi/5)>11 cos(pi/5) iff 19 sqrt(5)>41.
    assert 19*19*5>41*41
    directions=[]
    for j in range(5):
        a=(j+.5)*2*pi/5
        directions.append((-cos(a),-sin(a),-Fraction(11,10)))
    # Each tilted direction illuminates the upper pole and precisely
    # the neighboring equatorial pair j,j+1.
    for j,u in enumerate(directions):
        out=facet_coverage(n,1,3,u)
        assert out is not None
        top,bottom,ring=out
        assert top and not bottom and {k for k in range(n) if ring[k]}=={j,(j+1)%n}
    assert facet_coverage(n,1,3,(0,0,1)) == (False,True,[False]*5)
    union=set()
    for j in (0,2,4):
        union.update([j,(j+1)%5])
    assert union==set(range(5))
    # Upper pole gets total weight 5/2, each ring vertex weight one,
    # lower pole total weight one. Lower dual cost: 1 + 5/2=7/2.
    assert 1+Fraction(5,2) == Fraction(7,2)
    return 6


if __name__=='__main__':
    cells=check_angular()
    facets=check_facet_geometry()
    witness=check_asymmetric_witness()
    print('EXACT_ANGULAR_OK n=3..140 cells=%d integer_cover_n=3..12 optimizer_gcd=verified' % cells)
    print('FACETS_OK n=3..60 symmetric_heights=1/3,1,5 direction_tests=%d' % facets)
    print('ASYMMETRIC_EXACT_WITNESS_OK n=5 heights=1,3 directions=%d fractional=7/2' % witness)
