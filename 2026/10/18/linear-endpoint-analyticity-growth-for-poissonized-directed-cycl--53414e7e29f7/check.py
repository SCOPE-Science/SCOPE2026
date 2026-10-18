"""Finite consistency computations for directed-cycle semigroup asymptotics.

Only finite checks are performed here; the infinite-dimensional limit and
uniqueness of the limiting maximizer are established analytically.
"""
import cmath
import math
from itertools import product

TOL = 2.0e-9
checks = 0


def assert_close(a, b, tol=TOL):
    global checks
    assert math.isfinite(a) and math.isfinite(b)
    assert abs(a-b) <= tol*(1 + abs(a) + abs(b)), (a, b)
    checks += 1


def poisson_wrapped(n, t, upper=0):
    assert n >= 2 and t >= 0
    if not upper:
        upper = max(150, int(t + 14*math.sqrt(t+1) + 20))
    a = math.exp(-t)
    ps = [0.0]*n
    for k in range(upper+1):
        ps[k % n] += a
        a *= t/(k+1)
    return ps


def fourier_derivative(n, t):
    # DFT of the cycle Markov convolution derivative.
    z = [cmath.exp(2j*math.pi*j/n) for j in range(n)]
    f = [(v-1)*cmath.exp(t*(v-1)) for v in z]
    return [sum(f[j]*z[j]**(-k) for j in range(n)).real/n
            for k in range(n)]


def norm_direct(n, t):
    p = poisson_wrapped(n, t)
    return sum(abs(p[(k-1) % n]-p[k]) for k in range(n))


def norm_fourier(n, t):
    return sum(abs(x) for x in fourier_derivative(n,t))


def limiting_profile(s):
    return 8*s*sum(math.exp(-2*math.pi**2*(2*j+1)**2*s)
                   for j in range(18))


def limiting_derivative_u(u):
    return sum((1-(2*j+1)**2*u)*math.exp(-(2*j+1)**2*u)
               for j in range(18))


def unique_root():
    left, right = .6, 1.
    assert limiting_derivative_u(left)>0
    assert limiting_derivative_u(right)<0
    for _ in range(85):
        mid = (left+right)/2
        if limiting_derivative_u(mid)>0:
            left = mid
        else:
            right = mid
    return (left+right)/2


def hilbert_constant(n):
    return 1/(math.e*math.sin(math.pi/n))


def run():
    global checks
    for n in (2,3,4,5,7,10,13,24):
        for t in (.03,.12,.5,1.,3.,8.,17.,35.):
            p = poisson_wrapped(n,t)
            assert_close(sum(p), 1, 2e-13)
            q = fourier_derivative(n,t)
            for k in range(n):
                assert_close(q[k], p[(k-1)%n]-p[k], 3e-9)
            assert_close(sum(q), 0., 3e-9)
            assert_close(sum(abs(v) for v in q),norm_direct(n,t),3e-9)
            checks += 1
    for n in (2,3,4,7,13):
        for t in (0.01,.2,1.,4.,12.):
            p=poisson_wrapped(n,t)
            # Explicit matrix column and row absolute sums have the same norm.
            rows=[]; cols=[]
            for a in range(n):
                rows.append(sum(abs(p[(b-a-1)%n]-p[(b-a)%n]) for b in range(n)))
                cols.append(sum(abs(p[(a-b-1)%n]-p[(a-b)%n]) for b in range(n)))
            assert_close(max(rows), max(cols))
            assert_close(max(rows), norm_direct(n,t))
    u=unique_root()
    s=u/(2*math.pi**2)
    c=limiting_profile(s)
    assert .9972<u<.9974
    assert .0504<s<.0507
    assert .14914<c<.14916
    checks += 3
    for u0 in (.6,.65,.75,.85,.9,.97,1.0):
        z=0.
        for j in range(18):
            k=2*j+1
            z += k*k*(k*k*u0-2)*math.exp(-k*k*u0)
        assert z<0,(u0,z)
        checks += 1
    for n in (24,48,96,192):
        nrm=norm_fourier(n,s*n*n)
        scaled=(s*n*n)*nrm/n
        assert abs(scaled-c)<4/n,(n,scaled,c)
        checks += 1
    for n in (8,16,32,64):
        # Compare a global sampled time envelope to the predicted profile.
        scores=[(ss*n*n)*norm_fourier(n,ss*n*n)/n for ss in (.01,.025,.04,.05,.06,.08,.12)]
        assert max(scores) > .13, (n,scores)
        assert max(scores) < .23, (n,scores)
        checks += 2
    for n in (2,3,5,8,16,32):
        # The spectral formula optimizes each nonzero Fourier mode in time.
        factors=[]
        for j in range(1,n):
            z=cmath.exp(2j*math.pi*j/n)
            lam=1-z
            factors.append(abs(lam)/(math.e*lam.real))
        assert_close(max(factors),hilbert_constant(n),1e-11)
    # The endpoint and Hilbert limits have different positive constants.
    assert c > 1/(math.pi*math.e)
    checks+=1
    print(f"Finite verification: {checks} assertions passed")
    print(f"u_star={u:.15f}; s_star={s:.15f}; C_star={c:.15f}")

if __name__ == '__main__':
    run()
