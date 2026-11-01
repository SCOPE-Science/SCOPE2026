"""Standalone finite checks for an affine regular-simplex section face-vector limit.

Tests numerical normalization, finite combinatorial formulas, and asymptotic diagnostics;
the statements for all dimensions follow from the analytic proof, not these tests.
"""
import math
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from scipy.stats import norm


def faces(m, k, j):
    r = j + 2
    c = lambda a, b: math.comb(a, b) if a >= b else 0
    return c(m, r)-c(k, r)-c(m-k, r)


def max_faces(m, j):
    return faces(m, m//2, j)


def psi_variance(a):
    p = norm.sf(a)
    phi = norm.pdf(a)
    return p*(1-p)-phi*phi*(1+a*a/2)


def check_section_direct(m, a, rng):
    z = rng.normal(size=m)
    residual = z-z.mean()
    u = residual / np.linalg.norm(residual)
    h = a / math.sqrt(m-1)
    v = math.sqrt(m/(m-1))*(np.eye(m)-np.ones((m,m))/m)
    signed = v@u-h
    k = int(np.count_nonzero(signed > 0))
    expected = faces(m,k,0)
    if not 0 < k < m:
        assert expected == 0
        return 1
    pts = []
    for i in range(m):
        for j in range(i+1,m):
            if signed[i]*signed[j] >= 0:
                continue
            w = signed[i] / (signed[i]-signed[j])
            x = (1-w)*v[i]+w*v[j]
            assert abs(np.dot(x,u)-h)<1e-11
            assert abs(np.sum(x))<1e-11
            pts.append(x)
    assert len(pts) == expected
    basis = null_space(np.stack([np.ones(m),u]))
    xy = np.array(pts)@basis
    hull=ConvexHull(xy)
    assert len(hull.vertices) == expected
    return 1


def check():
    checks = 0
    rng = np.random.default_rng(2026102819)
    for m in range(4,16):
        for k in range(m+1):
            for j in range(m-2):
                f = faces(m,k,j)
                assert 0 <= f <= math.comb(m,j+2)
                assert f == faces(m,m-k,j)
                assert f <= max_faces(m,j)
                checks += 3
    for m in range(4,8):
        for a in (-0.5,0,0.4,0.9):
            for _ in range(16):
                checks += check_section_direct(m,a,rng)
    for a in (-2.0,-1.0,-0.5,0.0,0.5,1.0,2.0):
        p=norm.sf(a);phi=norm.pdf(a)
        sv=psi_variance(a)
        assert 0<sv<=p*(1-p)
        g=rng.normal(size=180000)
        psi=(g>a).astype(float)-p-phi*g-a*phi*(g*g-1)/2
        assert abs(psi.mean())<0.008
        assert abs(np.mean(psi*psi)-sv)<0.009
        checks += 3
    m=2400; trials=2500
    z=rng.normal(size=(trials,m))
    residual=z-z.mean(axis=1,keepdims=True)
    sd=np.sqrt(np.mean(residual*residual,axis=1))
    vals=residual/sd[:,None]
    for a,local_lambda in [(0.,1.2),(1.,0.)]:
        threshold=local_lambda/math.sqrt(m) if a == 0 else a
        k=(vals>threshold).sum(axis=1)
        if a==0:
            t=(k-m/2)/math.sqrt(m)
            assert abs(t.mean()+local_lambda*norm.pdf(0))<0.035
            assert abs(t.var()-psi_variance(0))<0.035
            for j in range(3):
                f=np.array([faces(m,int(x),j) for x in k],dtype=float)
                d=(max_faces(m,j)-f)/m**(j+1)
                target=t*t/(2**j*math.factorial(j))
                assert np.max(np.abs(d-target))<0.025
                checks+=1
        else:
            p=norm.sf(a)
            t=(k-m*p)/math.sqrt(m)
            assert abs(t.mean())<0.065
            assert abs(t.var()-psi_variance(a))<0.05
            for j in range(3):
                r=j+2
                A=(1-p**r-(1-p)**r)/math.factorial(r)
                Ap=((1-p)**(r-1)-p**(r-1))/math.factorial(r-1)
                f=np.array([faces(m,int(x),j) for x in k],dtype=float)
                actual=(f/m**r-A)*math.sqrt(m)
                target=Ap*t
                assert np.sqrt(np.mean((actual-target)**2))<0.09
                checks+=1
        checks+=2
    print('VERIFY_OK',checks,'checks')

if __name__=='__main__':
    check()
