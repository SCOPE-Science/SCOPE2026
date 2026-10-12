"""Reproduce the scalar-complement Type-II preconditioner calculations.

Run with Python 3 and NumPy. All reported mathematical identities follow
from the accompanying analytic proof; floating-point tests are diagnostic.
"""
from fractions import Fraction as F
import math
import numpy as np


def evaluate(H, b, d):
    m = H.shape[0]
    c = float(np.linalg.norm(np.linalg.solve(H, b)))
    p = float(np.linalg.norm(b))
    if p == 0.0 or d * c >= p:
        alpha = 1.0 / d
        target_sq = c*c
    else:
        alpha = d*(1+c*c)/(d*d+p*p)
        target_sq = p*p*(1+c*c)/(d*d+p*p)
    A = np.block([[H, b[:, None]], [b[None, :], np.array([[d]])]])
    B = np.zeros_like(A)
    B[:m, :m] = np.linalg.inv(H)
    B[m, m] = alpha
    E = np.eye(m+1) - B @ A
    observed = float(np.linalg.norm(E, 2))
    assert abs(observed*observed - target_sq) <= 1.0e-8*(1+target_sq)
    assert abs(np.linalg.norm(E, 2) - math.sqrt(target_sq)) <= 1.0e-8*(1+observed)
    return alpha, observed, c, p


def rational_witness():
    # Exact quantities, independent of floating-point SVD.
    b = [F(1, 2), F(2)]
    Hinv_b = [b[0], b[1]/4]
    c2 = Hinv_b[0]**2 + Hinv_b[1]**2
    p2 = b[0]**2 + b[1]**2
    d = F(27, 20)
    tau = b[0]*Hinv_b[0] + b[1]*Hinv_b[1]
    assert tau == F(5, 4) and d - tau == F(1, 10)
    assert c2 == F(1, 2) and p2 == F(17, 4)
    assert d*d < c2*p2
    z = p2*(1+c2)/(d*d+p2)
    alpha = d*(1+c2)/(d*d+p2)
    assert z == F(2550, 2429) and z > 1
    assert alpha == F(810, 2429)
    assert F(2)/(d+tau) == F(10, 13)
    assert F(0)<alpha<F(10, 13)
    H = np.diag([1.0, 4.0])
    aa, obs, *_ = evaluate(H, np.array([0.5, 2.0]), float(d))
    assert abs(obs*obs-float(z)) < 1.e-12
    assert abs(aa-float(alpha)) < 1.e-12
    return 1


def randomized_verification():
    rng = np.random.default_rng(20261009)
    test_count = 0
    for dim in range(1, 8):
        for _ in range(500):
            X = rng.normal(size=(dim, dim))
            H = X.T@X + (0.2+rng.random())*np.eye(dim)
            b = rng.normal(size=dim)
            tau = float(b@np.linalg.solve(H,b))
            d = tau + 0.05 + 3*rng.random()
            alpha, observed, c, p = evaluate(H,b,d)
            # Additional direct optimality comparisons against alpha variations.
            A = np.block([[H, b[:,None]],[b[None,:], np.array([[d]])]])
            HI = np.linalg.inv(H)
            for factor in (0.5, 0.81, 1.12, 2.0):
                pre = np.zeros_like(A)
                pre[:dim,:dim] = HI
                pre[dim,dim] = alpha*factor
                norm = float(np.linalg.norm(np.eye(dim+1)-pre@A,2))
                assert norm + 2.e-9 >= observed
            contracted = observed < 1-1e-9
            predicts = c < 1-1e-8 and d > p*c + 1e-8
            if predicts:
                assert contracted
            test_count += 1
    return test_count


if __name__ == '__main__':
    num_exact = rational_witness()
    num_random = randomized_verification()
    print(f'VERIFY_OK exact_witness={num_exact} random_SPD_blocks={num_random}')
