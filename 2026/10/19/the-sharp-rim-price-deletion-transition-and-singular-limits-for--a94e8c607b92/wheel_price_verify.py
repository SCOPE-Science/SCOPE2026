"""Independent finite-matrix and scalar checks of the priced-wheel resistance theorem.

Requires Python 3 standard library. Checks do not replace the all-order proofs.
"""
from fractions import Fraction as F
from math import pi, sin, sqrt


def invert(a):
    m = len(a)
    z = [[F(a[i][j]) for j in range(m)] + [F(i == j) for j in range(m)] for i in range(m)]
    for k in range(m):
        r = next(i for i in range(k, m) if z[i][k] != 0)
        z[k], z[r] = z[r], z[k]
        pivot = z[k][k]
        z[k] = [x / pivot for x in z[k]]
        for i in range(m):
            if i != k:
                factor = z[i][k]
                z[i] = [z[i][j] - factor*z[k][j] for j in range(2*m)]
    return [row[m:] for row in z]


def trace_inverse_wheel(n, a, b):
    N = n + 1
    L = [[F(0) for _ in range(N)] for _ in range(N)]
    def edge(i, j, weight):
        L[i][i] += weight; L[j][j] += weight
        L[i][j] -= weight; L[j][i] -= weight
    for i in range(n):
        edge(0, i+1, a)
        edge(i+1, ((i+1) % n)+1, b)
    M = [[L[i][j] + F(1,N) for j in range(N)] for i in range(N)]
    inv = invert(M)
    return sum((inv[i][i] for i in range(N)), F(0))-1


def spectral_value(n,a,b):
    return 1/((n+1)*a)+sum(
        1/(a+4*b*sin(pi*k/n)**2) for k in range(1,n))


def scalar(n,t,y):
    x=1-t*y
    return 1/((n+1)*x)+sum(
        1/(x+4*y*sin(pi*k/n)**2) for k in range(1,n))


def derivative(n,t,y):
    x=1-t*y
    return t/((n+1)*x*x)-sum(
        (4*sin(pi*k/n)**2-t)/(x+4*y*sin(pi*k/n)**2)**2
        for k in range(1,n))


def optimum_y(n,t):
    if t >= 2*(n+1)/n:
        return 0.0
    left, right = 0.0, 1.0/t
    for _ in range(90):
        mid = (left+right)/2
        if derivative(n,t,mid)<0:
            left=mid
        else:
            right=mid
    return (left+right)/2


def test():
    checks=0
    # Direct exact inverse of the (n+1)-vertex Laplacian, not a fitted formula.
    for n in (3,4,5,6,7):
        for a,b in ((F(1),F(0)),(F(2),F(1)),(F(1,3),F(5,4))):
            exact=trace_inverse_wheel(n,a,b)
            eval_spectral=spectral_value(n,float(a),float(b))
            assert abs(float(exact)-eval_spectral)<1e-9
            checks+=1
    # Exact-rational Fourier check for small cycles with integral eigenvalues.
    for n, deltas in ((3,(3,3)),(4,(2,4,2)),(6,(1,3,4,3,1))):
        for a,b in ((F(1,2),F(1,3)),(F(5),F(2))):
            val=F(1,(n+1)*a)+sum((1/(a+b*d) for d in deltas),F(0))
            assert trace_inverse_wheel(n,a,b)==val
            checks+=1
    # Boundary and interior first-order conditions across orders/prices.
    for n in (3,4,5,6,8,12,24,60):
        tc=2*(n+1)/n
        assert abs(derivative(n,tc,0))<1e-10
        checks+=1
        for t in (F(1,5), F(1),F(3,2),F(2),F(3),F(5)):
            t=float(t)
            y=optimum_y(n,t)
            assert 0<=y<1/t
            assert (y>1e-12)==(t<tc)
            assert (abs(derivative(n,t,y))<3e-6 if y else derivative(n,t,0)>-3e-8)
            # Convexity-based local perturbation evidence.
            z=max(1e-10,min(0.9/t, y+0.0001/t))
            assert scalar(n,t,y)<=scalar(n,t,z)+1e-8
            checks+=3
    # Exact first-order critical amplitude by numerical convergence.
    for n in (3,5,10,40):
        tc=2*(n+1)/n
        eps=1e-5
        slope=n*n/(4*(n-2)*(n+1))
        y=optimum_y(n,tc-eps)
        assert abs(y/eps-slope)<0.003
        checks+=1
    # Large-cycle law, far from and near the phase boundary.
    for t in (0.5,1.0,1.5,1.9,2.0,2.3,4.0):
        y=optimum_y(1500,t)
        x=1-t*y
        limit_x=(2/(4-t) if t<2 else 1.0)
        assert abs(x-limit_x)<0.015
        checks+=1
    # Finite-order inexpensive-rim singularity.
    for n in (3,5,8):
        t=1e-8
        y=optimum_y(n,t)
        c=sqrt((n+1)*(n*n-1)/12)
        assert abs(y*sqrt(t)/c-1)<0.005
        checks+=1
    return checks

if __name__ == '__main__':
    print('Checks passed:',test())
