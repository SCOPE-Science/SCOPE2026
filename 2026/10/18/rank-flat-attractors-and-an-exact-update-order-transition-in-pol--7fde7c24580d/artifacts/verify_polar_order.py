"""Finite reproducibility checks for exact post/pre polar shrinkage recurrences.

Requires Python 3 and NumPy. Outputs only check counts; proofs are in RESULT.md.
"""
from fractions import Fraction
import numpy as np


def polar(a):
    u, s, vt = np.linalg.svd(a, full_matrices=False)
    # Partial polar factor, with the zero singular subspace excluded.
    return (u * (s > 1e-13)) @ vt


def post(w, alpha, tau):
    z = alpha * w
    return z - tau * polar(z)


def pre(w, alpha, tau):
    return alpha * w - tau * polar(w)


def soft(w, alpha, tau):
    z = alpha * w
    u, s, vt = np.linalg.svd(z, full_matrices=False)
    return (u * np.maximum(s - tau, 0)) @ vt


def scalar_checks():
    count = 0
    H = [Fraction(1, 7), Fraction(1, 2), Fraction(6, 7),
         Fraction(8, 7), Fraction(3, 2), Fraction(13, 7)]
    for h in H:
        alpha = 1 - h
        q = abs(alpha)
        tau = Fraction(3, 5) * h
        target_post = tau / (1 + q)
        target_pre = target_post if h < 1 else tau / (1 - q)
        for s0 in [Fraction(1, 19), Fraction(2, 3), Fraction(9, 2)]:
            s_post, s_pre, s_soft = s0, s0, s0
            for k in range(250):
                new_post = abs(q * s_post - tau)
                new_pre = abs(alpha * s_pre - tau) if alpha > 0 else q * s_pre + tau
                assert abs(new_post - target_post) <= q * abs(s_post - target_post)
                assert abs(new_pre - target_pre) <= q * abs(s_pre - target_pre)
                s_post, s_pre = new_post, new_pre
                s_soft = max(q * s_soft - tau, Fraction(0))
                count += 3
            assert abs(s_post - target_post) < Fraction(1, 10**12)
            assert abs(s_pre - target_pre) < Fraction(1, 10**12)
            assert s_soft == 0
            count += 3
    return count


def matrix_checks():
    rng = np.random.default_rng(3412)
    count = 0
    for h in [0.2, 0.65, 0.9, 1.1, 1.35, 1.7]:
        a, lam = 2.0, 1.3
        eta = h/a
        alpha = 1-h
        tau = eta*lam
        q = abs(alpha)
        target_post = tau/(1+q)
        target_pre = tau/(1+q) if h < 1 else tau/(1-q)
        for m, n in [(3, 2), (4, 3), (6, 4)]:
            for _ in range(3):
                w = rng.normal(size=(m, n))
                w_post, w_pre, w_prox = w.copy(), w.copy(), w.copy()
                first_s = np.linalg.svd(w, compute_uv=False)
                for k in range(170):
                    s_post = np.linalg.svd(w_post, compute_uv=False)
                    s_pre = np.linalg.svd(w_pre, compute_uv=False)
                    w_post = post(w_post, alpha, tau)
                    w_pre = pre(w_pre, alpha, tau)
                    w_prox = soft(w_prox, alpha, tau)
                    new_s_post = np.linalg.svd(w_post, compute_uv=False)
                    new_s_pre = np.linalg.svd(w_pre, compute_uv=False)
                    assert np.allclose(new_s_post, np.sort(abs(q*s_post-tau))[::-1], atol=3e-12)
                    if h < 1:
                        assert np.allclose(new_s_pre, np.sort(abs(q*s_pre-tau))[::-1], atol=3e-12)
                    else:
                        assert np.allclose(new_s_pre, q*s_pre+tau, atol=3e-12)
                    count += 2
                assert np.linalg.norm(np.linalg.svd(w_post, compute_uv=False)-target_post) < 1e-9
                assert np.linalg.norm(np.linalg.svd(w_pre, compute_uv=False)-target_pre) < 1e-9
                assert np.linalg.norm(w_prox) < 1e-12
                ww1=post(w_post,alpha,tau)
                if h<1: assert np.linalg.norm(ww1+w_post)<1e-8
                else: assert np.linalg.norm(ww1-w_post)<1e-8
                wp1=pre(w_pre,alpha,tau)
                assert np.linalg.norm(wp1+w_pre)<1e-8
                count += 5
    # The canonical polar factor of the zero matrix is zero.
    for shape in [(2, 2), (4, 3)]:
        w = rng.normal(size=shape)
        assert np.allclose(post(w,0,1.0),0)
        assert np.allclose(pre(w,0,1.0), -polar(w))
        assert np.allclose(pre(pre(w,0,1.0),0,1.0), -pre(w,0,1.0))
        count += 3
    return count


if __name__ == '__main__':
    n=scalar_checks(); m=matrix_checks()
    print('PASS exact-rational conditional recurrence checks:', n)
    print('PASS dense-matrix recurrence and asymptotic checks:', m)
    print('Finite checks support, but do not establish, universal claims.')
