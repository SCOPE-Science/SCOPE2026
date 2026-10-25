"""Independent coordinate checks for orientation laws of regular-polygon bounding boxes.

Run: python3 verify.py  (standard library only).
Finite checks are diagnostic and not substitutes for the proof in RESULT.md.
"""
import math

PI = math.pi


def params(n, r=1.0):
    assert n >= 3
    a = PI / n
    if n % 4 == 0:
        return 2 * r*r, 1.0, 2*a
    if n % 2 == 0:
        return 2 * r*r, math.cos(a), a
    b = a/2
    return 2*r*r*math.cos(b)**2, math.cos(b), b


def direct_area(n, theta, r=1.0):
    xs, ys = [], []
    for j in range(n):
        q = theta + 2*PI*j/n
        xs.append(r*math.cos(q))
        ys.append(r*math.sin(q))
    return (max(xs)-min(xs))*(max(ys)-min(ys))


def law_area(n, theta, r=1.0):
    a = PI/n
    C,D,b = params(n,r)
    if n % 4 == 0:
        d = theta % (2*a)
        d = min(d, 2*a-d)
        T = 2*d
    elif n % 2 == 0:
        d = theta % (2*a)
        d = min(d, 2*a-d)
        T = 2*d-a
    else:
        d = theta % a
        d = min(d, a-d)
        T = 2*d-a/2
    return C*(D+math.cos(T))


def cdf(n, z, r=1.0):
    C,D,b = params(n,r)
    low,hi = C*(D+math.cos(b)), C*(D+1)
    if z <= low: return 0.
    if z >= hi: return 1.
    arg = max(-1.,min(1.,z/C-D))
    return 1-math.acos(arg)/b


def exact_moments(n, r=1.0):
    C,D,b = params(n,r)
    mean = C*(D+math.sin(b)/b)
    variance = C*C*(0.5+math.sin(2*b)/(4*b)-(math.sin(b)/b)**2)
    return mean,variance


def normalized_cdf(n, x):
    if x <= 0: return 0.
    if x >= 1: return 1.
    b=params(n)[2]
    return 2*math.asin(math.sin(b/2)*math.sqrt(x))/b

# Test completely independent Cartesian support calculations, including n=3 and n=4.
checked = 0
for n in range(3,101):
    for j in range(257):
        angle = (j+0.257)*PI/(2*257)+0.031*n
        lhs=direct_area(n,angle,1.35)
        rhs=law_area(n,angle,1.35)
        assert abs(lhs-rhs)<2e-11*(1+abs(lhs)),(n,angle,lhs,rhs)
        checked += 1
print('CARTESIAN_VERTEX_SUPPORT_ALL_ORDERS_3_TO_100_OK',checked)

# Quadrature checks verify BOTH moments against polygon-coordinate areas.
for n in [3,4,5,6,7,8,9,10,11,12,17,22,35,48]:
    N=2400
    direct=[direct_area(n, PI*(j+.5)/(2*N)) for j in range(N)]
    mean=sum(direct)/N
    var=sum((z-mean)**2 for z in direct)/N
    em,ev=exact_moments(n)
    assert abs(mean-em)<2e-5,(n,mean,em)
    assert abs(var-ev)<2e-5,(n,var,ev)
print('DIRECT_COORDINATE_FIRST_SECOND_MOMENTS_OK')

# Grid CDF checks with deterministic phase equidistribution.
for n in [3,4,5,6,7,8,13,16,19,22]:
    C,D,b=params(n)
    lo,hi=C*(D+math.cos(b)),C*(D+1)
    samples=sorted(direct_area(n,2*PI*(j+.35)/40000) for j in range(40000))
    for q in [0.01,0.05,0.15,0.25,0.5,0.75,0.9,0.99]:
        z=lo+(hi-lo)*q
        obs=sum(v<=z for v in samples)/len(samples)
        assert abs(obs-cdf(n,z))<0.001,(n,q,obs,cdf(n,z))
print('COMPLETE_CDF_ALL_THREE_ARITHMETIC_REGIMES_OK')

# Verify the variance separation and universal Beta(1/2,1) law as n grows.
for remainder,kappa in [(0,2.0),(2,1.0),(1,0.5),(3,0.5)]:
    n=400+remainder
    _,var=exact_moments(n)
    expected=4*kappa**4*PI**4/45
    assert abs(n**4*var/expected-1)<0.02,(n,n**4*var,expected)
    dist=max(abs(normalized_cdf(n,j/10000)-math.sqrt(j/10000)) for j in range(10001))
    sharp=kappa*kappa*PI*PI/(36*math.sqrt(3))
    assert abs(n*n*dist/sharp-1)<0.02,(n,n*n*dist,sharp)
print('SHARP_MOD_FOUR_VARIANCE_AND_BETA_KOLMOGOROV_CONSTANTS_OK')
print('ALL_REGULAR_POLYGON_BOUNDING_BOX_TESTS_OK')
