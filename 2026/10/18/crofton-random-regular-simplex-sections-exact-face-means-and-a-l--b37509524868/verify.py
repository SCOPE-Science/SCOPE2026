"""Independent finite checks for Crofton-random regular-simplex section formulas.
Run: python3 verify.py (Python standard library). Finite tests do not prove limits.
"""
import math
import random

SQRT2 = math.sqrt(2.0)
def phi(x):
    return 0.5 * math.erfc(-x / SQRT2)

def midpoint_integral(f, left=-11., right=11., n=24000):
    h = (right-left)/n
    return h * sum(f(left+(j+0.5)*h) for j in range(n))

def normal_range(n):
    return midpoint_integral(lambda t: 1.0 - phi(t)**n - (1.0-phi(t))**n)

def gap(n,k):
    return math.comb(n,k)*midpoint_integral(lambda t: phi(t)**k * (1-phi(t))**(n-k))

def f(n,k,j):
    m = j+2
    return math.comb(n,m) - (math.comb(k,m) if k>=m else 0) - (math.comb(n-k,m) if n-k>=m else 0)

def run():
    for n in range(3,13):
        for k in range(1,n):
            assert f(n,k,0)==k*(n-k)
            for j in range(n-1):
                direct=sum(math.comb(k,a+1)*math.comb(n-k,j-a+1)
                           for a in range(j+1) if a+1<=k and j-a+1<=n-k)
                assert f(n,k,j)==direct,(n,k,j)
    for n in (3,4,7,12):
        R=normal_range(n)
        gaps=[gap(n,k) for k in range(1,n)]
        assert abs(sum(gaps)-R)<0.000015,(n,R,sum(gaps))
        assert all(abs(gaps[k-1]-gaps[n-k-1])<1e-7 for k in range(1,n))
        for j in range(n-1):
            from_rank=sum(f(n,k,j)*gaps[k-1] for k in range(1,n))/R
            from_faces=math.comb(n,j+2)*normal_range(j+2)/R
            assert abs(from_rank-from_faces)<3e-5 * max(1,from_faces),(n,j,from_rank,from_faces)
    assert abs(normal_range(2)-2/math.sqrt(math.pi))<1e-7
    assert abs(normal_range(3)-3/math.sqrt(math.pi))<1e-7
    rng=random.Random(240503)
    for n in (4,7,10):
        wtot=0.; sums=[0.]*(n-1)
        for _ in range(11000):
            v=sorted(rng.gauss(0,1) for __ in range(n))
            avg=sum(v)/n
            radius=math.sqrt(sum((x-avg)**2 for x in v))
            gs=[(v[k]-v[k-1])/radius for k in range(1,n)]
            wtot+=sum(gs)
            for j in range(n-1):
                sums[j]+=sum(f(n,k,j)*gs[k-1] for k in range(1,n))
        for j in (0,1,n-2):
            observed=sums[j]/wtot
            expected=math.comb(n,j+2)*normal_range(j+2)/normal_range(n)
            assert abs(observed-expected)<0.035*max(1,expected),(n,j,observed,expected)
    print('VERIFY_OK: finite face identities, Gaussian rank integrals, independent Crofton quadrature and 33000 sampled normals')
if __name__=='__main__':
    run()
