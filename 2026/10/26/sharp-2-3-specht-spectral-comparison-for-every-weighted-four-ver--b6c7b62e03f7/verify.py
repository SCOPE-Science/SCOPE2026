#!/usr/bin/env python3
"""Standalone symbolic identities and seeded numerical checks for a four-vertex spectral inequality."""
from itertools import combinations
import random
import sympy as s
import numpy as np

def main():
    x12, x13, x14, x23, x24, x34 = x = s.symbols('x12 x13 x14 x23 x24 x34', nonnegative=True)
    a, b, c = x12+x34, x13+x24, x14+x23
    W, T = a+b+c, a*a+b*b+c*c
    delta = s.expand((3*T-W*W)/2)
    assert s.expand(delta-(a*a+b*b+c*c-a*b-b*c-c*a)) == 0
    assert s.expand(W*W-delta-3*(a*b+b*c+c*a)) == 0
    L=s.zeros(4)
    for (i,j),v in zip(combinations(range(4),2), x):
        e=s.eye(4)[:,i]-s.eye(4)[:,j]
        L += v*(e*e.T)
    U=s.Matrix([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/2
    assert U.T*U == s.eye(3)
    M=s.simplify(U.T*L*U)
    target=s.Matrix([[b+c,x14-x23,x13-x24],
                     [x14-x23,a+c,x12-x34],
                     [x13-x24,x12-x34,a+b]])
    assert M == target
    assert s.expand(s.trace(M)-2*W) == 0
    assert s.expand((W*W+3*T)-s.trace(M*M)-8*(x12*x34+x13*x24+x14*x23)) == 0
    Q=s.Matrix([[b+c,-c,-b],[-c,a+c,-a],[-b,-a,a+b]])
    t=s.symbols('t')
    assert s.expand(Q.charpoly(t).as_expr()-t*(t*t-2*W*t+3*(a*b+b*c+c*a)))==0
    assert s.expand((W*W)-3*(a*b+b*c+c*a)-delta)==0
    n_checks=0
    rng=random.Random(20261018)
    samples = [tuple(float(v) for v in z) for z in
               [(0,0,0,0,0,0),(1,0,0,0,0,0),(1,1,1,0,0,0),
                (1,1,1,1,1,1),(0,1,0,1,0,1)]]
    samples += [tuple(rng.randrange(0,21)/7 for _ in range(6)) for _ in range(2048)]
    for w in samples:
        a0,b0,c0 = w[0]+w[5],w[1]+w[4],w[2]+w[3]
        W0 = a0+b0+c0
        D0=max(0.0,a0*a0+b0*b0+c0*c0-a0*b0-b0*c0-c0*a0)
        mat=np.array([[b0+c0,w[2]-w[3],w[1]-w[4]],
                      [w[2]-w[3],a0+c0,w[0]-w[5]],
                      [w[1]-w[4],w[0]-w[5],a0+b0]])
        lam211 = 2*W0 - np.linalg.eigvalsh(mat)[-1]
        lam22 = W0 - D0**0.5
        assert lam211 >= (2/3)*lam22 - 5e-12*(1+W0)
        assert lam211 >= -5e-12*(1+W0)
        n_checks += 1
    star=np.array([[2.,1.,1.],[1.,2.,1.],[1.,1.,2.]])
    assert np.allclose(np.linalg.eigvalsh(star),[1,1,4])
    assert abs((6-4)/(3-0)-2/3)<1e-14
    print('PASS: 8 symbolic identities; 2053 seeded numerical edge-rate tests; star equality')

if __name__=='__main__':
    main()
