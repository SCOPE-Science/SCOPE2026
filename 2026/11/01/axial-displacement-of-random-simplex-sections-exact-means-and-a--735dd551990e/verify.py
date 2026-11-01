#!/usr/bin/env python3
"""Independent numerical diagnostics for axial random regular-simplex sections.

Requires Python 3.9+ and NumPy. Not a substitute for the analytic proof.
"""
import math
import itertools
import numpy as np

CHECKS = 0


def check(cond, description):
    global CHECKS
    if not bool(cond):
        raise AssertionError(description)
    CHECKS += 1


def analytical_mean(n, t):
    w = n + 2 * t + n * t * t
    a = math.acos(max(-1.0, min(1.0, -(1+n*t) / math.sqrt(n*w))))
    b = math.acos(max(-1.0, min(1.0, 1 - (n+1)/w)))
    return (n*a + n*(n-1)*b/2)/math.pi


def analytical_derivative(n, t):
    w = n+2*t+n*t*t
    z = n-1+4*t+2*n*t*t
    return n*math.sqrt(n+1)/(math.pi*w) * (
        math.sqrt(n-1)-(n-1)*(1+n*t)/math.sqrt(z))


def direct_angle_mean(n, t):
    m=n+1
    basis=np.eye(m)
    centroid=np.ones(m)/m
    y=centroid+t*(basis[0]-centroid)
    rays=basis-y
    total=0.0
    for i in range(m):
        for j in range(i+1,m):
            c=np.dot(rays[i],rays[j])/(np.linalg.norm(rays[i])*np.linalg.norm(rays[j]))
            total+=math.acos(np.clip(c,-1.0,1.0))/math.pi
    return total


# Independent Euclidean-vector angular evaluation of the two edge orbits.
for n in range(2,26):
    for t in (0.0, 0.00001, 0.1, 0.5, 0.75, 0.99):
        check(abs(analytical_mean(n,t)-direct_angle_mean(n,t))<2e-12,
              f"edge-angle orbit count, n={n}, t={t}")

# Analytic derivative against finite differences and global strict-sign check.
for n in range(2,51):
    for t in (0.02,0.1,0.3,0.5,0.8,0.99):
        h=1e-5
        df=(analytical_mean(n,t+h)-analytical_mean(n,t-h))/(2*h)
        target=analytical_derivative(n,t)
        check(abs(df-target)<1e-5*max(1,abs(target)),
              f"differentiation, n={n}, t={t}")
        if n==2:
            check(abs(target)<2e-13,"triangle constant")
        else:
            check(target<0,"strict decreasing")

# Second derivative at the centroid.
for n in range(2,36):
    h=5e-4
    approx=(analytical_mean(n,h)-2*analytical_mean(n,0)+analytical_mean(n,-h))/h**2
    exact=-(n-2)*(n+1)*math.sqrt((n+1)/(n-1))/math.pi
    check(abs(approx-exact)<4e-4*max(1,abs(exact)), "central Hessian")

# Endpoint law from the uniform rank of a distinguished Gaussian label.
for n in range(2,10):
    m=n+1
    counts=[0]*(n+1)
    for perm in itertools.permutations(range(m)):
        # perm orders labels from smallest Gaussian coordinate to largest.
        rank=perm.index(0)
        k=n-rank
        counts[k]+=1
    check(all(z==math.factorial(n) for z in counts), f"uniform rank n={n}")
    endpoint=sum(1+k*(n-k) for k in range(n+1))/(n+1)
    check(abs(endpoint-(1+n*(n-1)/6))<1e-10, "endpoint expectation")

# Exact comparison with the asymptotic limiting profile and uniform O(1/n) bound.
for n in (2,3,4,6,9,15,32,64,128):
    for t in np.linspace(0,1,101):
        mean=analytical_mean(n,float(t)) if t<1 else 1+n*(n-1)/6
        limit=math.acos(t*t/(1+t*t))/(2*math.pi)
        check(abs(mean/n**2-limit)<=2/n, "uniform dimension estimate")

# Direct Monte Carlo from the affine hyperplane's Gaussian normal.
# For interior points, signed heights equal G_i - sum_j p_j G_j.
rng=np.random.default_rng(1729)
for n,t in ((2,0.37),(3,0.0),(3,0.46),(4,0.77),(6,0.3),(8,0.94)):
    N=150_000
    raw=rng.standard_normal((N,n+1))
    p=np.ones(n+1)*(1-t)/(n+1)
    p[0]=(1+n*t)/(n+1)
    heights=raw-raw@p[:,None]
    k=(heights>0).sum(axis=1)
    vertices=k*(n+1-k)
    mean=vertices.mean()
    se=vertices.std(ddof=1)/math.sqrt(N)
    check(abs(mean-analytical_mean(n,t))<7*se+0.012,
          f"independent Gaussian Monte Carlo n={n}, t={t}: {mean}")
    if n<=4:
        for row in heights[:120]:
            crossed=0
            for i in range(n+1):
                for j in range(i+1,n+1):
                    if row[i]*row[j]<0: crossed+=1
            check(crossed==((row>0).sum()*((row<0).sum())),
                  "direct edge enumeration")

# Two-scale asymptotic diagnostics from the raw Gaussian section signs.
for c in (0.0, 1.0, 2.0):
    m=1001
    N=6000
    sample=rng.standard_normal((N,m))
    t=c/math.sqrt(m)
    threshold=t*sample[:,0]+(1-t)*sample.mean(axis=1)
    k=(sample>threshold[:,None]).sum(axis=1)
    deficit=(m*m/4 - k*(m-k))/m
    predicted=0.25-1/(2*math.pi)+c*c/(2*math.pi)
    se=deficit.std(ddof=1)/math.sqrt(N)
    check(abs(deficit.mean()-predicted)<6*se+0.03,
          f"critical window coefficient, c={c}")

for t in (0.25,0.75,1.0):
    m=1001
    N=5000
    sample=rng.standard_normal((N,m))
    z=sample[:,0]
    threshold=t*z+(1-t)*sample.mean(axis=1)
    k=(sample>threshold[:,None]).sum(axis=1)
    if t==1.0:
        # At the vertex, collapse all apex incident crossings into one vertex.
        k_other=(sample[:,1:]>z[:,None]).sum(axis=1)
        actual=(1+k_other*(m-1-k_other))/m**2
    else:
        actual=k*(m-k)/m**2
    phi=np.array([0.5*(1+math.erf(t*x/math.sqrt(2))) for x in z])
    limit=phi*(1-phi)
    check(np.mean((actual-limit)**2)<0.0008, f"fixed shift limit, t={t}")

print(f"VERIFY_OK: {CHECKS} deterministic assertions, including rank enumeration and numerical samples.")
