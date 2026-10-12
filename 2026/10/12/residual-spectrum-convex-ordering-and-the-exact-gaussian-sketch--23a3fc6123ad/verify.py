"""Standalone checks for Gaussian oblique-sketch residual geometry.
Checks exact algebra, direct floating-point reconstruction, and distributional diagnostics.
The general theorem is proved analytically in RESULT.md, not by experiments.
"""
from fractions import Fraction as F
import math
import numpy as np
from scipy.stats import betaprime


def check_exact_decomposition():
    # Q spans the first two coordinate axes. This is the rank-one-residual case.
    import sympy as sp
    A = sp.diag(3, 2, 1)
    Q = sp.eye(3)[:, :2]
    Y = sp.Matrix([[1, 3, 2, 1, 0], [0, 1, 1, 2, -1], [2, 0, 3, 1, 2]])
    G = Y.T * Q
    y_res = Y.T * sp.eye(3)[:, 2]
    B = (sp.eye(3) - Q * Q.T) * A
    approx = Q * (G.T * G).inv() * G.T * Y.T * A
    z = (G.T * G).inv() * G.T * y_res
    ratio = sp.trace((A - approx).T * (A - approx)) / sp.trace(B.T * B)
    assert sp.simplify(ratio - (1 + (z.T * z)[0])) == 0
    # A second exact configuration has residual rank two and distinct singular scales.
    A2 = sp.diag(3, 2, 3, 1)
    Q2 = sp.eye(4)[:, :2]
    Y2 = sp.Matrix([[1,2,0,3,1],[0,1,2,1,-1],[2,0,3,1,2],[1,2,1,0,3]])
    G2 = Y2.T * Q2
    H2 = Y2.T * sp.eye(4)[:,2:4]
    W2 = (G2.T*G2).inv()*G2.T*H2
    approx2 = Q2 * (G2.T*G2).inv()*G2.T*Y2.T*A2
    residual2 = A2 - Q2*Q2.T*A2
    ratio2 = sp.trace((A2-approx2).T*(A2-approx2)) / sp.trace(residual2.T*residual2)
    rhs2 = 1 + sp.Rational(9,10)*((W2[:,0].T*W2[:,0])[0]) + sp.Rational(1,10)*((W2[:,1].T*W2[:,1])[0])
    assert sp.simplify(ratio2-rhs2) == 0
    return 'two exact rational matrix identities passed'


def check_convex_order():
    # Finite-dimensional Jensen inequality for permutation symmetrization.
    for i in range(1,81):
        z1, z2 = F(3*i+1, 2*i+3), F(i*i+1, 7*i+1)
        for t in (F(3,5), F(9,10), F(1,1)):
            a=1+t*z1+(1-t)*z2
            b=1+t*z2+(1-t)*z1
            c=1+F(1,2)*(z1+z2)
            assert (a*a+b*b)/2-c*c >= 0
            assert (a*a+b*b)/2-c*c == ((2*t-1)**2)*(z1-z2)**2/F(4,1)
    return '240 exact rational convexity/permutation comparisons passed'


def check_gaussian_geometry():
    rng=np.random.default_rng(271828)
    err_max=0.0
    for d in (1,2,3):
        r=2; m=r+d; n=m; ell=r+5
        A=np.diag([5,4]+[3/(i+1) for i in range(d)])
        Q=np.eye(m)[:,:r]
        B=(np.eye(m)-Q@Q.T)@A
        U=np.eye(m)[:,r:]
        ss=np.diag(A)[r:]**2
        lam=ss/ss.sum()
        for i in range(180):
            Y=rng.normal(size=(m,ell))
            G=Y.T@Q
            H=Y.T@U
            approx=Q@np.linalg.pinv(G)@Y.T@A
            empirical=np.linalg.norm(A-approx,ord='fro')**2/np.linalg.norm(B,ord='fro')**2
            theory=1+sum(lam[j]*np.linalg.norm(np.linalg.pinv(G)@H[:,j])**2 for j in range(d))
            err_max=max(err_max,abs(empirical-theory))
            assert abs(empirical-theory)<1e-9*(1+theory)
    return f'540 direct Gaussian matrix replays passed (max abs gap {err_max:.2g})'


def check_beta_prime():
    # Simulates the conditional 1-d residual case. This is a diagnostic only.
    rng=np.random.default_rng(271828+1)
    r,ell=2,8;nu=ell-r+1
    N=35000
    vals=np.empty(N)
    for j in range(N):
        G=rng.standard_normal((ell,r))
        h=rng.standard_normal(ell)
        vals[j]=float(np.dot(np.linalg.lstsq(G,h,rcond=None)[0],np.linalg.lstsq(G,h,rcond=None)[0]))
    points=np.array([.1,.25,.5,.75,.9,.95,.99])
    q_emp=np.quantile(vals,points)
    q_exact=betaprime.ppf(points,r/2,nu/2)
    assert np.max(np.abs(q_emp-q_exact)/(1+q_exact))<.055
    # Closed-form mean for ell>r+1, divergence of second moment when ell<=r+3.
    mean=r/(ell-r-1)
    assert abs(np.mean(vals)-mean)<.065
    return f'35,000 independent Gaussian beta-prime diagnostic draws passed; observed mean {np.mean(vals):.6f}, exact {mean:.6f}'


def check_moment_formula():
    for r in (1,2,3,4):
        for ell in range(r,r+11):
            nu=ell-r+1
            a=F(r,2); b=F(nu,2)
            if nu>2:
                mean=a/(b-1)
                assert mean == F(r,ell-r-1)
            if nu>4:
                second=a*(a+1)/((b-1)*(b-2))
                assert second == F(r*(r+2),(nu-2)*(nu-4))
    return '44 parameter pairs checked against beta-prime rational moment identities'

if __name__=='__main__':
    for checker in (check_exact_decomposition,check_convex_order,check_gaussian_geometry,check_beta_prime,check_moment_formula):
        print(checker())
    print('PASS: algebraic and diagnostic checks completed; the general theorem requires its analytical proof.')
