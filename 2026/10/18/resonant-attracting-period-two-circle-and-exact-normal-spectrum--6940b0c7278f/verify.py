"""Numerical diagnostics for the resonant synchronized period-two circle.

Run: python3 verify.py (requires numpy).
Finite differences are diagnostics; universal assertions require the proof.
"""
import math
import numpy as np
from numpy.linalg import norm, eigvals


def run():
    rng = np.random.default_rng(318073)
    count = 0
    worst = 0.0
    example = None
    for d in (2, 3, 4):
        vals = {2: [2., -5.], 3: [2., -.5, -5.],
                4: [2., -.5, -1.7, -5.]}[d]
        rot, _ = np.linalg.qr(rng.standard_normal((d, d)))
        V = rot @ np.diag(vals) @ rot.T
        eta = 2. / (5. - 2.)
        r = 1. + eta * vals[0]
        for n in (2, 3, 5):
            for H in (1, 2, 3):
                heads = [rng.standard_normal((d, d)) for _ in range(H-1)]
                heads += [V - sum(heads, np.zeros((d, d)))]
                Q = [rng.standard_normal((d, d)) for _ in range(H)]
                K = [rng.standard_normal((d, d)) for _ in range(H)]

                def step(X):
                    W = np.copy(X)
                    for B, q, k in zip(heads, Q, K):
                        score = (X @ q.T) @ (X @ k.T).T
                        score -= score.max(axis=1, keepdims=True)
                        weight = np.exp(score)
                        weight /= weight.sum(axis=1, keepdims=True)
                        W += eta * ((weight @ X) @ B.T)
                    return W / norm(W, axis=1, keepdims=True)

                for theta in (0., math.pi/8, math.pi/4, .67, math.pi/2):
                    v = math.cos(theta) * rot[:, 0] + math.sin(theta) * rot[:, -1]
                    reflect = math.cos(theta) * rot[:, 0] - math.sin(theta) * rot[:, -1]
                    X = np.tile(v, (n, 1))
                    Y = step(X)
                    assert norm(Y - np.tile(reflect, (n, 1))) < 3e-13
                    assert norm(step(Y) - X) < 5e-13

                    w = -math.sin(theta) * rot[:, 0] + math.cos(theta) * rot[:, -1]
                    directions = [w] + [rot[:, j] for j in range(1, d-1)]
                    C = np.array(directions)
                    dim = n * (d-1)
                    h = 2e-5

                    def chart(inp):
                        pert = inp.reshape(n, d-1) @ C
                        Z = X + pert
                        return Z / norm(Z, axis=1, keepdims=True)

                    def output(inp):
                        return ((step(step(chart(inp))) - X) @ C.T).reshape(-1)

                    E = np.eye(dim)
                    J = np.stack([(output(h * q) - output(-h * q)) / (2 * h)
                                  for q in E], axis=1)
                    actual = np.sort(np.real(eigvals(J)))
                    want = [1.]
                    want.extend(((1. + eta * eig) / r)**2
                                for eig in vals[1:-1])
                    want.extend([math.cos(2 * theta)**2 / r**2] * (n-1))
                    want.extend([1. / r**2] * ((n-1)*(d-2)))
                    target = np.sort(np.array(want))
                    err = np.max(np.abs(actual - target))
                    worst = max(worst, float(err))
                    assert err < 2.0e-8, (d,n,H,theta,actual,target,err)
                    count += 1
                    if d==3 and n==4: example = (actual,target)
    # Exact rational arithmetic of the representative critical spectrum
    from fractions import Fraction as F
    eta=F(2,3);r=F(7,3)
    assert ((1+eta*F(-1,2))/r)**2 == F(4,49)
    assert 1/r**2==F(9,49)
    assert (F(0)/r)**2==0  # phase pi/4: cos(2theta)=0
    print('PASS:',count,'multihop spectral/period-two tests; maximum eigenvalue residual:',f'{worst:.2e}')
    print('PASS: three exact rational multiplier checks')

if __name__ == '__main__':
    run()
