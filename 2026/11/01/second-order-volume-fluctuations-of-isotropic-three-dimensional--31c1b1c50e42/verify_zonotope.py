"""Independent finite-n and spectral checks for random three-dimensional zonotope volume.

Python 3.10+, numpy, scipy. All formulas refer to unit vectors sampled
uniformly on the two-sphere and unscaled segments [0,u_i].
"""
from fractions import Fraction
import math
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull
from scipy.special import eval_legendre

PI=math.pi
MU=PI/8
PAIR_COV=Fraction(1,6)-PI*PI/64
TRIPLE_VAR=Fraction(2,9)-PI*PI/64


def formula_mean(n):
    return math.comb(n,3)*MU

def formula_variance(n):
    return math.comb(n,3)*TRIPLE_VAR+2*math.comb(n,2)*math.comb(n-2,2)*PAIR_COV if n>=3 else 0.

def zonotope_volume_determinants(vectors):
    return sum(abs(np.linalg.det(vectors[[i,j,k], :])) for i,j,k in combinations(range(len(vectors)),3))

def zonotope_volume_hull(vectors):
    pts=np.array([sum((vectors[i] for i in range(len(vectors)) if (mask>>i)&1),start=np.zeros(3)) for mask in range(1<<len(vectors))]);
    return ConvexHull(pts).volume

def direct_j(m):
    # robust form avoiding overwritten index
    c=[Fraction(1)];b=[Fraction(0),Fraction(1)]
    if m==0:return Fraction(1,2)
    for k in range(1,2*m):
        v=[Fraction(0)]*(len(b)+1)
        for i,t in enumerate(b):v[i+1]+=(2*k+1)*t
        for i,t in enumerate(c):v[i]-=k*t
        v=[x/(k+1) for x in v]
        c,b=b,v
    total=Fraction(0)
    for i,t in enumerate(b):
        if i%2==0:
            r=i//2
            total+=t*Fraction(math.factorial(2*r),2*4**r*math.factorial(r)*math.factorial(r+1))
    return total


def spectral_lambda(m):
    if m==0:return PI/8
    return -PI/4*(math.comb(2*m,m)/4**m)**2/((2*m-1)*(2*m+2))


def main():
    assert direct_j(0)==Fraction(1,2)
    for m in range(1,15):
        assert direct_j(m)==-Fraction(math.comb(2*m,m)**2,16**m*(2*m-1)*(2*m+2)), (m,direct_j(m))
    # first 1000 harmonic terms approximate trace and Hilbert-Schmidt norm
    ell=np.array([spectral_lambda(m) for m in range(1,1001)])
    mult=np.array([4*m+1 for m in range(1,1001)])
    assert abs(sum(mult*ell)+MU)<3e-4
    assert abs(sum(mult*ell**2)-PAIR_COV)<1e-11
    # deterministic geometric cross-check independent of determinant sum
    rng=np.random.default_rng(20261031)
    for n in [3,4,6,8]:
        for _ in range(8):
            x=rng.normal(size=(n,3));x/=np.linalg.norm(x,axis=1)[:,None]
            lhs=zonotope_volume_determinants(x)
            rhs=zonotope_volume_hull(x)
            assert abs(lhs-rhs)<5e-11, (n,lhs,rhs)
    # independent random experiments for moment and concentration
    n=7;count=18000; dat=np.empty(count)
    for t in range(count):
        x=rng.normal(size=(n,3));x/=np.linalg.norm(x,axis=1)[:,None]
        dat[t]=zonotope_volume_determinants(x)
    m,v=float(dat.mean()),float(dat.var())
    expected_mean=float(formula_mean(n));expected_var=float(formula_variance(n))
    assert abs(m-expected_mean)<0.045, (m,expected_mean)
    assert abs(v-expected_var)<0.40,(v,expected_var)
    # exact finite-n overlap expansion and correct normalization
    assert abs(formula_variance(3)-TRIPLE_VAR)<1e-14
    assert abs(formula_variance(4)-4*TRIPLE_VAR-12*PAIR_COV)<1e-14
    assert abs(PAIR_COV/2 - (Fraction(1,12)-PI*PI/128))<1e-14
    print('n=7 sample mean',m,'theory',expected_mean,'sample variance',v,'theory',expected_var)
    print('spectral trace partial',sum(mult*ell),'target',-MU)
    print('spectral norm partial',sum(mult*ell**2),'target',PAIR_COV)
    print('ALL_EXACT_MOMENT_SPECTRAL_AND_HULL_CHECKS_PASSED')

if __name__=='__main__':main()
