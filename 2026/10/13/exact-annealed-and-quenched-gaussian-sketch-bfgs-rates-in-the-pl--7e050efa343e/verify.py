"""Reproduce algebraic and numerical checks for planar Gaussian-sketch BFGS rates.
Only Python's standard library is required. Numerical checks are diagnostics,
not substitutes for the analytic argument in RESULT.md.
"""
from fractions import Fraction as F
from math import atan2, cos, log, pi, sin, sqrt
import random


def exact_matrix(r):
    return [
        [F(3, 8), 3*r/F(8), 3*r*r/F(8)],
        [r/F(2), (1+r*r)/F(4), (r+r**3)/F(4)],
        [r*r/F(8), (r+r**3)/F(16), (1+r**4)/F(16)],
    ]


def det3(A):
    a, b, c = A
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def charpoly(A):
    trace = sum(A[i][i] for i in range(3))
    pair = sum(A[i][i]*A[j][j]-A[i][j]*A[j][i]
               for i in range(3) for j in range(i+1, 3))
    return [F(1), -trace, pair, -det3(A)]


def perron(A):
    x = [1., 1., 1.]
    for _ in range(10000):
        y = [sum(float(A[i][j])*x[j] for j in range(3)) for i in range(3)]
        lam = max(y)
        y = [v/lam for v in y]
        if max(abs(y[i]-x[i]) for i in range(3)) < 1.e-14:
            return lam
        x = y
    raise AssertionError('power iteration failed')


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def trans(A):
    return [list(x) for x in zip(*A)]


def f_norm(A):
    return sum(v*v for row in A for v in row)


def direct_check():
    rng = random.Random(78219)
    for _ in range(500):
        h1 = 1.0 + 12.0*rng.random()
        h2 = 0.2 + 2.0*rng.random()
        s1, s2 = rng.gauss(0,1), rng.gauss(0,1)
        denom = h1*s1*s1 + h2*s2*s2
        G = [[s1*s1/denom, s1*s2/denom], [s1*s2/denom,s2*s2/denom]]
        H = [[h1,0.],[0.,h2]]
        I = [[1.,0.],[0.,1.]]
        B = [[1.1+rng.random(), rng.random()/5],
             [0., 1.1+rng.random()]]
        B[1][0] = B[0][1]
        left = [[I[i][j]-mm(G,H)[i][j] for j in range(2)] for i in range(2)]
        right = trans(left)
        newB = mm(mm(left,B),right)
        newB = [[newB[i][j]+G[i][j] for j in range(2)] for i in range(2)]
        e = [[sqrt(H[i][i])*B[i][j]*sqrt(H[j][j]) - I[i][j]
              for j in range(2)] for i in range(2)]
        enew = [[sqrt(H[i][i])*newB[i][j]*sqrt(H[j][j])-I[i][j]
                for j in range(2)] for i in range(2)]
        u1,u2=sqrt(h1)*s1/sqrt(denom),sqrt(h2)*s2/sqrt(denom)
        v1,v2=-u2,u1
        a=v1*(e[0][0]*v1+e[0][1]*v2)+v2*(e[1][0]*v1+e[1][1]*v2)
        expect=[[a*v1*v1,a*v1*v2],[a*v1*v2,a*v2*v2]]
        assert f_norm([[enew[i][j]-expect[i][j] for j in range(2)] for i in range(2)]) < 2e-24
    print('500 direct quasi-Newton matrix update/projection identities: PASS')


def angular_check():
    N=16384
    for rr in [0.,1/3,0.5,0.8]:
        h1=((1+rr)/(1-rr))**2
        aa=[2*pi*(j+0.5)/N for j in range(N)]
        dens=[(1-rr*rr)/(1-2*rr*cos(2*t)+rr*rr) for t in aa]
        assert abs(sum(dens)/N-1.)<2.e-11
        for k in range(1,5):
            m=sum(dens[j]*cos(2*k*aa[j]) for j in range(N))/N
            assert abs(m-rr**k)<2.e-11
        # independent Gaussian direction integration moment E cos(2 angle)
        assert abs(rr-(sqrt(h1)-1)/(sqrt(h1)+1))<1.e-13
    print('16,384-point angular Fourier quadrature, four anisotropies: PASS')


def spectral_check():
    prev=-1.
    for j in range(100):
        rr=F(j, 100)
        A=exact_matrix(rr)
        c=charpoly(A)
        exact=[F(1),-(32*rr**4+128*rr**2+352)/512,
               (68-48*rr**2-20*rr**4)/512,
               -3*(1-rr*rr)**2/512]
        assert c==exact
        lam=perron(A)
        assert 0 < lam < 1.00000000001
        if j: assert lam>prev
        prev=lam
    assert perron(exact_matrix(F(0)))==F(3,8)
    assert abs(perron(exact_matrix(F(1,3)))-0.483866235324)<1e-10
    print('100 exact rational cubic coefficient identities and Perron ordering: PASS')


def path_check():
    rng=random.Random(871424)
    for r in (0.,1/3., 0.5):
        h1=((1+r)/(1-r))**2
        prev=None
        sums=0.
        n=250000
        for j in range(n):
            x,y=rng.gauss(0,1),rng.gauss(0,1)
            theta=atan2(y,sqrt(h1)*x)
            if prev is not None:
                sums+=4*log(abs(cos(theta-prev)))
            prev=theta
        fitted=sums/(n-1)
        target=4*log((1+r*r)/2)
        assert abs(fitted-target)<0.035,(r,fitted,target)
        print('Quenched log rate',r, 'empirical',round(fitted,6),'exact',round(target,6))

if __name__=='__main__':
    direct_check()
    angular_check()
    spectral_check()
    path_check()
    print('All checks passed.')
