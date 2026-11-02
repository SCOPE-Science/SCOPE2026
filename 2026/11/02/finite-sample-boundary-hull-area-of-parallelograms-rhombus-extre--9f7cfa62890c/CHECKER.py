"""Independent exact-integral and geometric checks of a boundary-hull area theorem.

Run: python3 CHECKER.py
Requires only the Python standard library. Monte Carlo is diagnostic, not a proof.
"""
from fractions import Fraction
from math import comb, cos, sin, log1p, exp
from random import Random


def normalized_missing_exact(n, a, b):
    """Main finite expression, evaluated exactly for integer side lengths."""
    a, b = Fraction(a), Fraction(b)
    L = 2 * (a + b)
    k = n + 2
    numerator = L**k - (2*a+b)**k - (a+2*b)**k + a**k + b**k
    return 2 * numerator / (L**n * (n+1) * (n+2) * a*b)


def normalized_missing_independent_integral(n, a, b):
    """Separately integrate the binomial of u*X+(1-u)*Y, X,Y uniform."""
    a, b = Fraction(a), Fraction(b)
    u, v = a/(a+b), b/(a+b)
    def z_moment(k):
        return sum((Fraction(comb(k,j)) * u**j * v**(k-j)
                    / ((j+1)*(k-j+1)) for j in range(k+1)), Fraction(0))
    return 2 * sum((Fraction(comb(n,k)) * (-1)**k
                   * (Fraction(1,2**k)-Fraction(1,2**n)) * z_moment(k)
                   for k in range(n+1)), Fraction(0))


def extremal_square(n):
    return 1 - (Fraction(32) - 36*Fraction(3,4)**n + 4*Fraction(1,4)**n) / ((n+1)*(n+2))


def extremal_thin(n):
    return Fraction(n-3, n+1) + Fraction(2)**(2-n)/Fraction(n+1)


def sample_rectangle(rng, a, b):
    r = rng.random() * (2*a + 2*b)
    if r < a:
        return (r,0.)
    r -= a
    if r < b:
        return (a,r)
    r -= b
    if r < a:
        return (a-r,b)
    r -= a
    return (0.,b-r)


def area_by_monotone_chain(points):
    points = sorted(points)
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for p in points:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(points):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    vs = lower[:-1]+upper[:-1]
    if len(vs)<3:
        return 0.0
    return abs(sum(vs[i][0]*vs[(i+1)%len(vs)][1] - vs[i][1]*vs[(i+1)%len(vs)][0]
                   for i in range(len(vs))))/2


def normalized_missing_stable(n, u):
    """Numerically stable for n up to several thousand and u of order 1/n."""
    v=1-u
    # Each base is divided by 2 before exponentiation, avoiding overflow.
    F = 4.0 - (2-u)**2 * exp(n*log1p(-u/2.0)) \
        - (1+u)**2*((1+u)/2)**n + u**2*(u/2)**n + v**2*(v/2)**n
    return 2*F/((n+1)*(n+2)*u*v)


def run():
    test_count=0
    for n in (2,3,4,5,6,9,12):
        for a,b in ((1,1),(2,1),(7,3),(17,5)):
            v1=normalized_missing_exact(n,a,b)
            v2=normalized_missing_independent_integral(n,a,b)
            assert v1==v2, (n,a,b,v1,v2)
            if n>=3:
                frac=1-v1
                assert extremal_thin(n)<frac<=extremal_square(n)
                assert frac==extremal_square(n) if a==b else frac<extremal_square(n)
            test_count+=1
    assert 1-normalized_missing_exact(3,1,1)==Fraction(5,32)
    assert 1-normalized_missing_exact(4,1,1)==Fraction(5,16)
    assert 1-normalized_missing_exact(3,3,1)==Fraction(19,128)
    print('EXACT_TWO_INDEPENDENT_INTEGRATIONS_AND_SHARP_BOUNDS_PASSED',test_count)

    rng=Random(20261028)
    for a,b,angle,n,count in ((1.,1.,1.570796326794897,3,16000),
                              (1.,1.,.55,3,16000),
                              (3.,1.,1.570796326794897,5,16000),
                              (3.,1.,.7,5,16000),
                              (9.,1.,.35,9,16000),
                              (1.,1.,.8,8,16000)):
        cx,sx=cos(angle),sin(angle)
        total=0.
        for _ in range(count):
            raw=[sample_rectangle(rng,a,b) for j in range(n)]
            transformed=[(x+y*cx,y*sx) for x,y in raw]
            total+=area_by_monotone_chain(transformed)
        observed=total/count/(a*b*sx)
        exact=1-float(normalized_missing_exact(n,int(a),int(b)))
        assert abs(observed-exact)<0.016,(a,b,angle,n,observed,exact)
        print('INDEPENDENT_SHEARED_HULL_DIAGNOSTIC',a,b,round(angle,5),n,
              'observed',round(observed,6),'exact',round(exact,6))
    print('AFFINE_SHEAR_ANGLE_BLINDNESS_DIAGNOSTICS_PASSED')

    # The thin boundary layer is n*(missing fraction)->8*(1-exp(-tau/2))/tau.
    for tau in (0.2,1.0,3.0,7.0):
        n=5000
        u=tau/n
        limit=8*(-__import__('math').expm1(-tau/2))/tau
        observed=n*normalized_missing_stable(n,u)
        assert abs(observed-limit)<.006,(tau,observed,limit)
    for u in (.1,.25,.5):
        n=3000
        observed=n*n*normalized_missing_stable(n,u)
        limit=8/(u*(1-u))
        assert abs(observed-limit)/limit<.002,(u,observed,limit)
    print('FIXED_SHAPE_AND_THIN_BOUNDARY_LAYER_LIMITS_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    run()
