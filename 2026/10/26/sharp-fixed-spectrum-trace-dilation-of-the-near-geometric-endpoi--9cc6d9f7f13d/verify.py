"""Exact rational checks for near-geometric endpoint trace dilation.

Requires Python 3 standard library only. Finite checks corroborate, but do not
replace, the dimension-independent proofs.
"""
from fractions import Fraction as F
from random import Random


def trace_excess(diag_a, s):
    n = len(diag_a)
    return sum((diag_a[i] / diag_a[j] - 1) * s[i][j] * s[j][i]
               for i in range(n) for j in range(n))


def off_diagonal_energy(s, k):
    n = len(s)
    return sum(s[i][j] * s[j][i]
               for i in range(k) for j in range(k, n))


def extremal_spectrum_block(n, k, spectrum):
    """Build 45-degree extreme-pair rotations in a fixed k/(n-k) splitting."""
    r = min(k, n-k)
    s = [[F(0) for _ in range(n)] for _ in range(n)]
    p = list(range(k))
    q = list(range(k, n))
    for j in range(r):
        x, y = p[j], q[j]
        hi, lo = spectrum[j], spectrum[n-j-1]
        s[x][x] = s[y][y] = (hi+lo)/2
        s[x][y] = s[y][x] = (hi-lo)/2
    remaining = [i for i in range(n) if s[i][i] == 0]
    middle = spectrum[r:n-r]
    assert len(remaining) == len(middle)
    for i, value in zip(remaining, middle):
        s[i][i] = value
    return s


def test_exact():
    rng=Random(20261023)
    checks=0
    # General trace identity, via an exact symmetric positive definite square root.
    for n in range(2, 9):
        for repeat in range(100):
            a = [F(rng.randint(1, 15)) for _ in range(n)]
            t = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(n)]
            s = [[sum(t[h][i]*t[h][j] for h in range(n)) + (F(n+1) if i==j else 0)
                  for j in range(n)] for i in range(n)]
            lhs=trace_excess(a,s)
            rhs=sum((a[i]-a[j])**2/(a[i]*a[j]) * s[i][j]**2
                    for i in range(n) for j in range(i+1,n))
            assert lhs==rhs, (n,repeat,lhs,rhs)
            assert rhs >= 0
            checks+=1
    # Optimal configurations for every splitting and several strict positive spectra.
    for n in range(2, 11):
        for k in range(1, n):
            for rep in range(30):
                a,b = F(rng.randint(2,18)),F(1)
                spectrum=sorted((F(rng.randint(1,60)) for _ in range(n)),reverse=True)
                s=extremal_spectrum_block(n,k,spectrum)
                diag_a=[a]*k+[b]*(n-k)
                actual=trace_excess(diag_a,s)
                r=min(k,n-k)
                expected=(a-b)**2/(4*a*b)*sum((spectrum[i]-spectrum[n-i-1])**2
                                                    for i in range(r))
                block=(a-b)**2/(a*b)*off_diagonal_energy(s,k)
                assert actual==expected==block,(n,k,actual,expected,block)
                checks+=1
    # Nonoptimal rational two-by-two rotations, commutator formula and envelope.
    for rep in range(900):
        a,b=F(rng.randint(2,20)), F(1)
        u,v=F(rng.randint(3,20)), F(2)
        t=F(rng.randint(0,10),rng.randint(11,20))
        co=(1-t*t)/(1+t*t); si=2*t/(1+t*t)
        z=(u-v)*co*si
        s=[[u*co*co+v*si*si,z],[z,u*si*si+v*co*co]]
        gap=trace_excess([a,b],s)
        assert gap==(a-b)**2/(a*b)*z*z
        b12=(u*u-v*v)*co*si
        comm_frobenius_squared=2*(a-b)**2*b12*b12
        assert gap==comm_frobenius_squared/(2*a*b*(u+v)**2)
        assert gap<=(a-b)**2/(4*a*b)*(u-v)**2
        checks+=1
    print('PASS', checks, 'exact rational checks across ranks, dimensions and orbit orientations')

if __name__=='__main__':
    test_exact()
