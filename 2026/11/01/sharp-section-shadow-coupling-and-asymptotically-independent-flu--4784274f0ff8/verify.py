"""Reproduce geometric and probabilistic checks for simplex sections and shadows.

Requires NumPy and SciPy. Execute: python verify.py
The weak limit is established analytically, not by this finite checker.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from scipy.special import gammaln
from scipy.integrate import quad

SEED = 20261031
rng = np.random.default_rng(SEED)
MU = math.sqrt(2 / math.pi)
SIGMA_B2 = 1 - 3 / math.pi
SIGMA_T2 = 1/4 - 1/(2*math.pi)

def mean_second(n):
    d = n - 1
    mean = math.exp(math.log(n)+gammaln(d/2)-0.5*math.log(math.pi)-gammaln((d+1)/2))
    second = n/d + 2*n/math.pi * (math.sqrt(1-1/(d*d)) + math.asin(1/d)/d)
    return mean, second

def sample_normal(n):
    a = rng.normal(size=n)
    a -= a.mean()
    return a / np.linalg.norm(a)

def brightness_and_vertices(u):
    n = len(u)
    p = int(np.count_nonzero(u > 0))
    c = p*(n-p)
    y = math.sqrt(n/(n-1)) * np.abs(u).sum()
    return y,c,p

def independent_projected_volume(u):
    n=len(u)
    basis=null_space(np.array([np.ones(n),u]))
    points=basis.copy()  # row i is projected coordinate of vertex e_i
    if n == 3:
        return float(np.max(points[:,0])-np.min(points[:,0]))
    return float(ConvexHull(points).volume)

def independent_section_count(u):
    n=len(u)
    basis=null_space(np.array([np.ones(n),u]))
    positive=np.flatnonzero(u>0)
    negative=np.flatnonzero(u<0)
    vertices=[]
    for i in positive:
        for j in negative:
            x=np.zeros(n)
            # u_i*x_i+u_j*x_j=0 and x_i+x_j=1.
            x[i]=-u[j]/(u[i]-u[j]); x[j]=u[i]/(u[i]-u[j])
            assert abs(x.sum()-1)<1e-12 and abs(x @ u)<1e-12
            vertices.append(x @ basis)
    if n == 3:
        return len(vertices)
    h=ConvexHull(np.asarray(vertices))
    return len(h.vertices)

def gaussian_reference(n, trials, batch=2000):
    y_all=[]; t_all=[]
    for start in range(0,trials,batch):
        count=min(batch,trials-start)
        x=rng.normal(size=(count,n))
        x-=np.mean(x,axis=1,keepdims=True)
        x/=np.linalg.norm(x,axis=1,keepdims=True)
        y=np.sqrt(n/(n-1))*np.abs(x).sum(axis=1)
        p=(x>0).sum(axis=1)
        t=(p-n/2)/math.sqrt(n)
        y_all.append(y); t_all.append(t)
    return np.concatenate(y_all),np.concatenate(t_all)

# Independent low-dimensional convex hull reconstruction.
for n in (3,4,5,6):
    facet_volume=math.sqrt(n-1)/math.factorial(n-2)
    for _ in range(120):
        u=sample_normal(n)
        y,c,p=brightness_and_vertices(u)
        independent=independent_projected_volume(u)
        predicted=facet_volume*y/2
        assert abs(predicted-independent) < 4e-10*(1+abs(predicted)), (n,independent,predicted)
        assert independent_section_count(u)==c

# Deterministic exact extrema of the conditional brightness envelope, including strict lower bound.
for n in range(3,20):
    for p in range(1,n):
        q=n-p
        u=np.array([float(q)]*p + [-float(p)]*q)
        u/=np.linalg.norm(u)
        y,c,k=brightness_and_vertices(u)
        upper=2*math.sqrt(c/(n-1))
        lower=math.sqrt(2*n/(n-1))
        assert k==p and c==p*q
        assert abs(y-upper)<1e-12
        assert y>lower+1e-12
        # Concentrate one positive and one negative mass while keeping every sign fixed.
        eps=1e-7
        pos=[1.0] + [eps]*(p-1)
        neg=[-(1+(p-1)*eps-(q-1)*eps)] + [-eps]*(q-1)
        z=np.array(pos+neg)
        assert abs(z.sum())<1e-12 and np.all(z[:p]>0) and np.all(z[p:]<0)
        z/=np.linalg.norm(z)
        yz,cz,kz=brightness_and_vertices(z)
        assert cz==c and kz==p and yz>lower and yz-lower<3e-4

for n in [3,4,7,12,30,80]:
    for _ in range(200):
        u=sample_normal(n); y,c,p=brightness_and_vertices(u)
        assert math.sqrt(2*n/(n-1))-1e-12<y<=2*math.sqrt(c/(n-1))+1e-12

# Independent Gaussian integral for a pair of distinct projected normal coordinates.
from scipy.special import erf
for d in [2,3,4,10,100]:
    rho=-1/d; scale=math.sqrt(1-rho**2)
    def integrand(x):
        ex=scale*MU*math.exp(-rho*rho*x*x/(2*scale*scale))+abs(rho*x)*erf(abs(rho*x)/(math.sqrt(2)*scale))
        return 2/math.sqrt(2*math.pi)*math.exp(-x*x/2)*x*ex
    value=quad(integrand,0,12,epsabs=3e-12)[0]
    formula=2/math.pi*(math.sqrt(1-rho*rho)+rho*math.asin(rho))
    assert abs(value-formula)<1e-9, (d,value,formula)

# Exact finite-size mean and second moment; probability simulations only corroborate.
for n in [3,4,8,20,100]:
    y,t=gaussian_reference(n,40000)
    mean, second=mean_second(n)
    var=second-mean**2
    empirical_var=float(np.var(y))
    assert abs(float(np.mean(y))-mean) < 6*math.sqrt(var/40000)+1e-4
    assert abs(empirical_var-var)<0.085*var
    print(f'finite n={n}: EY exact={mean:.8f}, Var exact={var:.8f}; empirical={y.mean():.8f}, {empirical_var:.8f}')

for n in [300,1000]:
    y,t=gaussian_reference(n,50000)
    z_b=y-MU*math.sqrt(n)
    deficit=t**2
    assert abs(float(np.mean(z_b))-(mean_second(n)[0]-MU*math.sqrt(n)))<0.015
    assert abs(np.var(z_b)-SIGMA_B2)<0.012
    assert abs(np.mean(deficit)-SIGMA_T2)<0.015
    corr=float(np.corrcoef(z_b,deficit)[0,1])
    if n==1000:
        assert abs(corr)<0.11
    print(f'limit n={n}: mean_B={z_b.mean():.5f}, var_B={z_b.var():.5f}, Edef={deficit.mean():.5f}, corr={corr:.5f}')
print('ALL_SIMPLEX_SECTION_SHADOW_CHECKS_PASSED')
