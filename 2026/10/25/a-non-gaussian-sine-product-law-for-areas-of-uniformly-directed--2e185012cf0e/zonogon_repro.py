"""Independent finite and asymptotic checks for isotropic random zonogon area."""
import math
import cmath
import random
import statistics

PI=math.pi

def area_from_directions(angles):
    return 4.0*sum(abs(math.sin(angles[i]-angles[j]))
                   for i in range(len(angles)) for j in range(i))

def area_from_minkowski_polygon(angles):
    # Build every sign-vector vertex and use an independent monotone-chain hull.
    pts=[]
    for mask in range(1<<len(angles)):
        x=y=0.0
        for j,a in enumerate(angles):
            s=1.0 if mask>>j&1 else -1.0
            x+=s*math.cos(a); y+=s*math.sin(a)
        pts.append((x,y))
    pts.sort()
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in pts:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    hull=lower[:-1]+upper[:-1]
    return abs(sum(hull[j][0]*hull[(j+1)%len(hull)][1]
                   -hull[j][1]*hull[(j+1)%len(hull)][0]
                   for j in range(len(hull)))/2)

def centered_fourier(angles, mmax):
    n=len(angles)
    return -8/PI*sum((abs(sum(cmath.exp(2j*m*x) for x in angles))**2-n)
                       /(4*m*m-1) for m in range(1,mmax+1))

def exact_laplace(s):
    z=1-8*s/PI
    if abs(z)<1e-13:return 2/PI
    if z>0:return math.sqrt(z)/math.sin(PI/2*math.sqrt(z))
    return math.sqrt(-z)/math.sinh(PI/2*math.sqrt(-z))

def run():
    rng=random.Random(130024)
    for n in range(2,9):
        for _ in range(25):
            a=[rng.uniform(0,PI) for _ in range(n)]
            v=area_from_directions(a)
            w=area_from_minkowski_polygon(a)
            assert abs(v-w)<4e-9*max(1,v),(n,v,w)
    print('INDEPENDENT_SIGN_VERTEX_HULL_AREA_IDENTITY_OK 175')
    for n in (5,11,22):
        for _ in range(8):
            a=[rng.uniform(0,PI) for _ in range(n)]
            val=area_from_directions(a)-4/PI*n*(n-1)
            approx=centered_fourier(a,600)
            assert abs(val-approx)<0.010
    print('SIX_HUNDRED_TERM_FOURIER_AREA_RECONSTRUCTION_OK')
    for n in (10,40,90):
        rep=1800
        sample=[area_from_directions([rng.uniform(0,PI) for _ in range(n)]) for _ in range(rep)]
        m0=4/PI*n*(n-1)
        v0=16*(n*(n-1)/2)*(0.5-4/(PI*PI))
        m=statistics.mean(sample)
        v=statistics.variance(sample)
        assert abs(m-m0)<5*math.sqrt(v0/rep),(n,m,m0)
        assert abs(v-v0)<0.17*v0,(n,v,v0)
    print('FINITE_N_EXACT_MEAN_VARIANCE_MONTE_CARLO_OK 5400')
    for s in (0.02,0.1,0.4,1.0,4.0):
        prod=1.0
        for m in range(1,20000):
            prod*=1/(1+(8*s/PI)/(4*m*m-1))
        assert abs(prod-exact_laplace(s))<0.00004,(s,prod,exact_laplace(s))
    print('EULER_SINE_LAPLACE_PRODUCT_OK')
    reps=3000
    n=160
    shifts=[]
    for _ in range(reps):
        a=[rng.uniform(0,PI) for _ in range(n)]
        L=(area_from_directions(a)-4/PI*n*(n-1))/n
        shifts.append(4/PI-L)
    for s in (0.2,0.6,1.0):
        obs=statistics.mean(math.exp(-s*v) for v in shifts)
        truth=exact_laplace(s)
        assert abs(obs-truth)<0.035,(s,obs,truth)
    print('FINITE_SAMPLE_TO_NON_GAUSSIAN_LAPLACE_LIMIT_OK 3000')
    assert math.isclose(4-32/(PI*PI), (64/(PI*PI))*sum(1/(4*m*m-1)**2 for m in range(1,20000)), rel_tol=1e-10)
    print('FOURIER_VARIANCE_AND_NON_GAUSSIAN_UPPER_SUPPORT_OK')
    print('ALL_ISOTROPIC_ZONOGON_AREA_CHECKS_OK')

if __name__=='__main__':run()
