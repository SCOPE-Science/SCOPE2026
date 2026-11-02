"""Reproduce finite-dimensional checks for Fourier moment-constrained nodal positivity.

This code checks the grid quadrature, interpolation identities and sample
negative-mass integrals. Asymptotic and projection statements are proved
in RESULT.md; numerical integration is not used as their proof.
"""
import math
import cmath

TWOPI = 2 * math.pi


def solve(A, b):
    n = len(b)
    a = [list(map(float, row)) + [float(b[i])] for i, row in enumerate(A)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        assert abs(a[pivot][k]) > 1e-10
        a[pivot], a[k] = a[k], a[pivot]
        z = a[k][k]
        for j in range(k, n+1):
            a[k][j] /= z
        for i in range(n):
            if i == k:
                continue
            z = a[i][k]
            for j in range(k, n+1):
                a[i][j] -= z * a[k][j]
    return [a[i][n] for i in range(n)]


def moments_and_weights(N, K):
    q, m = 2*K+1, 2*N+1
    indices = [int(math.floor(j*m/q+0.5)) % m for j in range(q)]
    assert len(set(indices)) == q
    theta = [TWOPI*j/m for j in indices]
    rows = [[1.0]*q]
    for k in range(1, K+1):
        rows += [[math.cos(k*t) for t in theta],
                 [math.sin(k*t) for t in theta]]
    w = solve(rows, [1.0] + [0.0]*(q-1))
    assert min(w) > 0
    for row, target in zip(rows, [1.0]+[0.0]*(q-1)):
        assert abs(sum(a*b for a,b in zip(row, w))-target) < 5e-11
    for k in range(1, K+1):
        ck = sum(wj*cmath.exp(-1j*k*tj) for tj, wj in zip(theta,w))
        assert abs(ck) < 1e-10
    return theta, w


def dirichlet(N, x):
    x = (x + math.pi) % TWOPI - math.pi
    den = math.sin(x/2)
    return 2*N+1 if abs(den) < 1e-12 else math.sin((N+0.5)*x)/den


def integrated_negative(N, theta, weights, npts=100000):
    count = 0.0
    for a in range(npts):
        x = TWOPI*(a+0.5)/npts
        p = sum(wj*dirichlet(N, x-tj) for tj, wj in zip(theta,weights))
        count += max(-p,0.0)
    return count/npts


def run():
    cases=0
    for K in (0,1,2,3):
        for N in (31,47,79,127):
            theta,w = moments_and_weights(N,K)
            m=2*N+1
            selected={round(t*m/TWOPI)%m:j for j,t in enumerate(theta)}
            for j in range(m):
                x=TWOPI*j/m
                p=sum(wi*dirichlet(N,x-ti) for ti,wi in zip(theta,w))
                target=m*w[selected[j]] if j in selected else 0.0
                assert abs(p-target) < 2e-8, (N,K,j,p,target)
                cases+=1
            if K:
                neg=integrated_negative(N,theta,w)
                upper=integrated_negative(N,[0.0],[1.0])
                assert neg > 0 and neg <= upper+1e-6
            # For Poisson mixtures, coefficient difference approaches zero as r -> 1.
            r=1.0-1e-9
            parseval=sum((1.0-r**abs(k))**2 for k in range(-N,N+1))
            assert parseval < 5e-10
    # Classical leading coefficient is numerically consistent at large degree.
    vals=[]
    for N in (300,600,1200):
        upper=integrated_negative(N,[0.0],[1.0],npts=160000)
        vals.append(upper)
    d1=(vals[1]-vals[0])/math.log(2)
    d2=(vals[2]-vals[1])/math.log(2)
    c=2/math.pi**2
    assert abs(d1-c)<0.005 and abs(d2-c)<0.005, (d1,d2,c)
    print('VERIFY_OK: nodal_and_moment_checks=%d, K=0..3, N=31,47,79,127, negative_mass_cases=12, Dirichlet_slopes=%0.7f,%0.7f, target=%0.7f' % (cases,d1,d2,c))

if __name__=='__main__':
    run()
