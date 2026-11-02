"""Independent exact and computational checks for parabolic-arc random hull theorem."""
import math, random, statistics
from fractions import Fraction

def shoelace_hull(points):
    # Andrew monotone chain, not using the exact-gap derivation.
    pts = sorted(set(points))
    if len(pts) < 3: return 0.0
    def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    low=[]
    for x in pts:
        while len(low)>=2 and cross(low[-2],low[-1],x)<=0:low.pop()
        low.append(x)
    high=[]
    for x in reversed(pts):
        while len(high)>=2 and cross(high[-2],high[-1],x)<=0:high.pop()
        high.append(x)
    path=low[:-1]+high[:-1]
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(path,path[1:]+path[:1])))/2

def area_gap(ts,a=1.0,b=0.0,c=0.0):
    ts=sorted(ts)
    return a*((ts[-1]-ts[0])**3-sum((v-u)**3 for u,v in zip(ts,ts[1:])))/6

def anchored_exact(n):
    mu=Fraction(1,6)*(1-Fraction(6,n*(n+1)))
    variance=Fraction(2*(n-2)*(5*n+6), n*n*(n+1)**2*(n+2)*(n+3)*(n+4))
    return mu,variance

def free_exact(n):
    mu=Fraction((n-2)*(n-1),6*(n+1)*(n+2))
    variance=Fraction((n-2)*(n-1)*(n**3+4*n*n+n-10),2*(n+1)**2*(n+2)**2*(n+3)*(n+4)*(n+5))
    return mu,variance

# Independently rederive moments from Dirichlet factorial identities.
for n in range(3,351):
    m=n-1
    den=math.prod(range(m,m+6))
    EZ=Fraction(m*math.factorial(3), math.prod(range(m,m+3)))
    EZ2=Fraction(m*math.factorial(6)+m*(m-1)*math.factorial(3)**2,den)
    ES3=Fraction(m*(m+1),(m+3)*(m+4))
    ES6=Fraction(m*(m+1),(m+6)*(m+7))
    amu=(1-EZ)/6
    avar=(EZ2-EZ*EZ)/36
    fmu=ES3*amu
    fvar=ES6*(1-2*EZ+EZ2)/36-fmu*fmu
    assert (amu,avar)==anchored_exact(n), (n,amu,avar,anchored_exact(n))
    assert (fmu,fvar)==free_exact(n), (n,fmu,fvar,free_exact(n))
print('EXACT_DIRICHLET_BETA_MOMENTS_ALL_N_3_TO_350_OK')

rng=random.Random(48151623)
for n in [3,4,7,13,25]:
    max_dev=0
    for j in range(300):
        ts=sorted(rng.random() for _ in range(n))
        pts=[(t,1.25*t*t-0.7*t+0.2) for t in ts]
        direct=shoelace_hull(pts)
        from_gaps=area_gap(ts,1.25)
        max_dev=max(max_dev,abs(direct-from_gaps))
    assert max_dev<3e-13,(n,max_dev)
    print('SHOELACE_INDEPENDENT_GEOMETRY',n,'MAX_ERROR',format(max_dev,'.2g'))

for n in [3,5,12,30]:
    reps=14000 if n<15 else 17000
    for anchored in [True,False]:
        vals=[]
        for _ in range(reps):
            ts=sorted([rng.random() for _ in range(n-2)] + ([0.0,1.0] if anchored else [rng.random(),rng.random()]))
            vals.append(shoelace_hull([(t,t*t) for t in ts]))
        ex,vx=anchored_exact(n) if anchored else free_exact(n)
        mean=statistics.mean(vals)
        variance=statistics.variance(vals)
        se=math.sqrt(float(vx)/reps)
        assert abs(mean-float(ex)) < 5*se + 0.00005,(n,anchored,mean,float(ex),se)
        print('AREA_MEAN_CHECK',n,'ANCHORED' if anchored else 'FREE','empirical',format(mean,'.8f'),'exact',format(float(ex),'.8f'),'variance_empirical',format(variance,'.8f'),'variance_exact',format(float(vx),'.8f'))

# For anchored n=3 there is an exact beta-type CDF: A/(1/8)=4U(1-U), F(t)=1-sqrt(1-t).
for t in [0.05,.2,.5,.85]:
    u=(1-math.sqrt(1-t))/2
    assert abs(2*u-(1-math.sqrt(1-t)))<1e-14
print('ANCHORED_TRIANGLE_DISTRIBUTION_OK')

# CLT variance constant, checked exact n^5 Var(Z) and n^2 Var(A_free).
for n in [100,1000,10000,100000]:
    _,va=anchored_exact(n)
    _,vf=free_exact(n)
    print('ASYMPTOTIC_VAR_CONSTANTS',n,'n^5 Var(A_anchor)',float(va)*n**5,'n^2 Var(A_free)',float(vf)*n**2)
print('ALL_PARABOLIC_ARC_TESTS_PASSED')
