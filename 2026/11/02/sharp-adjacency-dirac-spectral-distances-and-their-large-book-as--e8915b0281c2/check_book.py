"""Supplemental finite-dimensional diagnostics for book-graph spectral distances.

Requires Python >=3.9, NumPy and SciPy. The theorem's infinite-family
asymptotic is proved analytically in RESULT.md; finite checks are not a proof.
"""
import math
import numpy as np
from scipy.optimize import minimize


def reduced_matrix(m, x, v):
    t = math.sqrt(m - 1)
    return np.array([[0., -x, -1., -t*v],
                     [x, 0., x-1., t*(x-v)],
                     [1., 1.-x, 0., 0.],
                     [t*v, t*(v-x), 0., 0.]])


def closed_norm(m, x, v):
    t = math.sqrt(m - 1)
    S = x*x + 1 + (1-x)**2 + t*t*(v*v+(x-v)**2)
    pf = t*x*(1-v)
    return 0.5 * (math.sqrt(max(0., S+2*abs(pf))) +
                  math.sqrt(max(0., S-2*abs(pf))))


def full_matrix(m, x, v):
    # f(h_1)=1, f(h_2)=1-x, f(z_1)=0, others=1-v.
    f = np.array([1., 1.-x, 0.]+[1.-v]*(m-1))
    A = np.zeros((m+2,m+2))
    A[0,1]=A[1,0]=1
    A[:2,2:]=1
    A[2:,:2]=1
    return A*(f[None,:]-f[:,None])


def check():
    checked=0
    rng=np.random.default_rng(812357)
    for m in range(2,19):
        for _ in range(50):
            x,v=rng.uniform(-1.5,1.5,size=2)
            a=np.linalg.norm(full_matrix(m,x,v),2)
            b=np.linalg.norm(reduced_matrix(m,x,v),2)
            c=closed_norm(m,x,v)
            assert abs(a-b)<2e-12*(1+a)
            assert abs(a-c)<2e-12*(1+a)
            checked+=1
    distances=[]
    for m in [2,3,4,6,10,20,100,1000,10000]:
        r=minimize(lambda z:closed_norm(m,*z),[.3,.2],method='Nelder-Mead',
                   options={'xatol':1e-12,'fatol':1e-12,'maxiter':2500})
        assert r.success or r.fun < math.sqrt(2)
        assert math.sqrt(1.5)-1e-9<=r.fun<math.sqrt(2)
        t=math.sqrt(m-1)
        assert r.fun >= math.sqrt(1+(1-2/t)**2)-1e-9 if t>=2 else True
        distances.append((m,1/r.fun))
    assert all(distances[i][1]>=distances[i+1][1]-1e-9 for i in range(len(distances)-1))
    print(f'PASS: {checked} full/reduced/spectral-norm identities')
    print('PASS: numerical convex minima and monotonicity checkpoints')
    for m,d in distances:
        print(f'm={m:5d}: hub-leaf distance ~{d:.12f}')
    for m in [100,1000,10000,100000]:
        t=math.sqrt(m-1)
        b=1-t**(-.25)
        q=closed_norm(m,2*b/t,b/t)
        assert q < math.sqrt(2)
        assert q >= math.sqrt(1+(1-2/t)**2)-1e-8
    print('PASS: explicit asymptotic witnesses and analytic lower-bound checks')

if __name__=='__main__':
    check()
