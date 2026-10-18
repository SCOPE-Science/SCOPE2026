"""Reproduce two-sided oblique tangent-projection identities and sketch-risk tests.

Requires Python 3 and NumPy.  Run: python oblique_projection_check.py
All sketches are independent, real and drawn with a fixed random seed.
The expected-risk formulas are proved analytically in RESULT.md; simulations are checks.
"""
import numpy as np

rng = np.random.default_rng(20261014)


def sketch(rows, ambient, ensemble):
    if ensemble == "Gaussian":
        return rng.standard_normal((rows, ambient))
    if ensemble == "Haar":
        q, _ = np.linalg.qr(rng.standard_normal((ambient, rows)))
        return q.T
    raise ValueError(ensemble)


def one_sided_coeff(theta, r):
    return np.linalg.lstsq(theta[:, :r], theta[:, r:], rcond=None)[0]


def one_sided_mean_factor(r, ambient, ell, ensemble):
    if ensemble == "Haar" and ell == ambient:
        return 0.0
    if ell <= r + 1:
        return np.inf
    base = r / (ell - r - 1)
    if ensemble == "Gaussian":
        return base
    return base * (ambient - ell) / (ambient - r)


def leakage_from_blocks(a, b, c):
    return (np.linalg.norm(a @ c, "fro") ** 2
            + np.linalg.norm(c @ b.T, "fro") ** 2
            + np.linalg.norm(a @ c @ b.T, "fro") ** 2)


def check_deterministic(r, m, n, left, right):
    u = np.eye(m)[:, :r]
    v = np.eye(n)[:, :r]
    ul = np.eye(m)[:, r:]
    vr = np.eye(n)[:, r:]
    theta = sketch(left, m, "Gaussian")
    omega = sketch(right, n, "Gaussian")
    a = one_sided_coeff(theta, r)
    b = one_sided_coeff(omega, r)
    c = rng.standard_normal((m-r, n-r))
    z = ul @ c @ vr.T
    l = u @ np.linalg.lstsq(theta @ u, theta, rcond=None)[0]
    rr = v @ np.linalg.lstsq(omega @ v, omega, rcond=None)[0]
    po = l @ z + z @ rr.T - l @ z @ rr.T
    exact = leakage_from_blocks(a,b,c)
    assert np.allclose(np.linalg.norm(po, "fro") ** 2,exact,rtol=2e-11,atol=2e-11)
    aa = np.linalg.svd(a,compute_uv=False)[0]
    bb = np.linalg.svd(b,compute_uv=False)[0]
    optimal = (1+aa**2)*(1+bb**2)-1
    _, _, va = np.linalg.svd(a,full_matrices=False)
    _, _, vb = np.linalg.svd(b,full_matrices=False)
    extremal = np.outer(va[0],vb[0])
    got = leakage_from_blocks(a,b,extremal)
    assert np.allclose(got,optimal,rtol=2e-11,atol=2e-11)
    for _ in range(10):
        random_c=rng.standard_normal(c.shape)
        assert leakage_from_blocks(a,b,random_c) <= optimal*np.linalg.norm(random_c,"fro")**2+1e-9
    return exact


def sample_risks(r,m,n,ell_left,ell_right,ensemble,samples):
    c = rng.standard_normal((m-r,n-r))
    c /= np.linalg.norm(c,"fro")
    acc = 0.0
    for _ in range(samples):
        a=one_sided_coeff(sketch(ell_left,m,ensemble),r)
        b=one_sided_coeff(sketch(ell_right,n,ensemble),r)
        acc += leakage_from_blocks(a,b,c)
    la=one_sided_mean_factor(r,m,ell_left,ensemble)
    rb=one_sided_mean_factor(r,n,ell_right,ensemble)
    exact=la+rb+la*rb
    return acc/samples,exact


def main():
    count=0
    for r,m,n in ((1,4,6),(1,7,8),(2,5,6),(2,7,9)):
        for ll in (r,r+1,r+2):
            for rr in (r,r+1,r+2):
                if ll<=m and rr<=n:
                    check_deterministic(r,m,n,ll,rr)
                    count+=1
    print("Deterministic projection/singular-value identities passed:",count)
    for ensemble in ("Gaussian","Haar"):
        simulated,predicted=sample_risks(1,8,9,6,6,ensemble,6000)
        print("%s: simulated mean %.6f, exact mean %.6f" % (ensemble,simulated,predicted))
        assert abs(simulated-predicted)<0.15
    for r,m,ell in ((1,8,6),(2,9,6),(1,5,5),(1,2,2)):
        g=one_sided_mean_factor(r,m,ell,"Gaussian")
        h=one_sided_mean_factor(r,m,ell,"Haar")
        if np.isfinite(g):
            assert np.isclose(h,g*(m-ell)/(m-r))
        else:
            assert (np.isinf(h) if ell<m else h==0.)
        print("r,m,ell:",r,m,ell,"Gaussian one-side:",g,"Haar one-side:",h)
    print("All deterministic formula checks and simulation tolerances passed.")

if __name__=="__main__":
    main()
