"""Check all-sample-size centroid avoidance in the equilateral triangle."""
import math, random
import mpmath as mp
mp.mp.dps=65
R=random.Random(45177)

def q(t):
    t=mp.mpf(t)
    return (1-t)**2/(2-3*t) if t<=mp.mpf('0.5') else 1-t*t/(3*t-1)

def integral_probability(m):
    return m*mp.quad(lambda t:q(t)**(m-1),[0,mp.mpf('0.5'),mp.mpf('0.66666666666666666666666666666666666666666666667'),1])

def closed_probability(m):
    # Integral of q(t)^k over t in [0,1/2], expanded exactly as a Laurent polynomial.
    def term(r):
        return mp.log(4) if r == -1 else (mp.power(2,r+1)-mp.power(2,-r-1))/(r+1)
    def I(k):
        return mp.fsum(mp.binomial(2*k,j)*term(j-k) for j in range(2*k+1))/(3*mp.power(9,k))
    return m*(I(m-1)+mp.fsum((-1)**k*mp.binomial(m-1,k)*I(k) for k in range(m)))

def sample_point():
    k=R.randrange(3);t=R.random()
    V=[(0.,0.),(1.,0.),(.5,math.sqrt(3)/2)]
    a,b=V[k],V[(k+1)%3]
    return (a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]))

def has_centroid(points):
    c=(.5,math.sqrt(3)/6)
    angles=sorted(math.atan2(p[1]-c[1],p[0]-c[0])%(2*math.pi) for p in points)
    gaps=[(angles[(j+1)%len(angles)]-angles[j])%(2*math.pi) for j in range(len(angles))]
    return max(gaps)<math.pi

for m in range(1,16):
    a=integral_probability(m);b=closed_probability(m)
    assert abs(a-b)<mp.mpf('1e-35'),('integral-closed',m,a,b)
print('INTEGRAL_CLOSED_EQUIVALENCE',15)
assert abs(closed_probability(3)-(mp.mpf(25)/27-20*mp.log(2)/81))<mp.mpf('1e-50')
assert closed_probability(2)==1
print('BASE_CASE_M3',mp.nstr(closed_probability(3),16))
for m in (3,4,6,10):
    N=16000
    observed=sum(not has_centroid([sample_point() for _ in range(m)]) for _ in range(N))/N
    expected=float(closed_probability(m))
    assert abs(observed-expected)<0.030,('Monte Carlo',m,observed,expected)
    print('SIMULATION',m,N,round(observed,6),round(expected,6))
for m in (50,100,200,500):
    p=integral_probability(m)
    asym=3*mp.sqrt(mp.pi*m/5)*mp.power(mp.mpf(5)/9,m)
    ratio=p/asym
    print('LAPLACE_RATIO',m,mp.nstr(ratio,14))
    if m==500:assert abs(ratio-1)<mp.mpf('0.005')
print('STATUS PASS')
