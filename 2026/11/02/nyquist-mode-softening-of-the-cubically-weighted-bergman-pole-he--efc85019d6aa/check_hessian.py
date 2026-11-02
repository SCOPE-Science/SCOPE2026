"""Independent finite checks for the cubically weighted Bergman pole Hessian.

The all-size theorem is proved analytically in RESULT.md; these calculations
are spot checks, not exhaustive proofs.
"""
import math
from fractions import Fraction


def a(m):
    return Fraction(24*m, (m+1)*(m+2)*(m+3))


def w(m):
    return 24/(m*(m+1)*(m+2)*(m+3))


def mode_eigenvalue(n, k, cutoff=40000):
    # Truncation error for each residue sum is O(n/cutoff).
    sums = [0.0] * n
    for m in range(1, cutoff+1):
        sums[m % n] += float(a(m))
    return n*(sums[k]+sums[n-k]-2*sums[0])


def energy(theta, cutoff=4000):
    value=0.0
    for m in range(1,cutoff+1):
        re=sum(math.cos(m*x) for x in theta)
        im=sum(math.sin(m*x) for x in theta)
        value+=w(m)*(re*re+im*im)
    return value


def check():
    for m in range(1,35):
        d=a(m)-a(m+1)
        q=a(m)-2*a(m+1)+a(m+2)
        assert d==Fraction(24*(2*m-1),(m+1)*(m+2)*(m+3)*(m+4))
        assert q==Fraction(144*(m-1),(m+1)*(m+2)*(m+3)*(m+4)*(m+5))
    for n in range(2,19):
        spec=[mode_eigenvalue(n,k) for k in range(1,n)]
        target={n//2, (n+1)//2}
        best=min(spec)
        assert best>0
        assert {k for k,e in enumerate(spec,1) if abs(e-best)<1e-8}==target
    for n in (2,3,5,7):
        theta=[2*math.pi*j/n for j in range(n)]
        k=n//2
        v=[math.cos(2*math.pi*k*j/n) for j in range(n)]
        norm=math.sqrt(sum(t*t for t in v))
        v=[x/norm for x in v]
        h=0.01
        e0=energy(theta)
        ep=energy([x+h*y for x,y in zip(theta,v)])
        em=energy([x-h*y for x,y in zip(theta,v)])
        fd=(ep+em-2*e0)/(h*h)
        spectral=mode_eigenvalue(n,k)
        assert abs(fd/spectral-1)<0.001,(n,fd,spectral)
    print('PASS: 68 exact difference identities; central modes N=2..18; 4 direct-energy curvature tests')


if __name__=='__main__':
    check()
