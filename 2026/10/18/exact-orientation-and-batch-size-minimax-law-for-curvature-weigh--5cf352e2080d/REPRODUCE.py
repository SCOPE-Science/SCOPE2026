"""Independent finite-difference and exact-binomial checks of a planar
Rademacher curvature-weighted three-point estimator theorem.

Requirements: Python 3.10+, NumPy 1.22+. Run: python REPRODUCE.py
Numerics corroborate, but do not replace, the analytic proof.
"""
import math
import numpy as np

Z = (np.array([1., 1.]), np.array([1., -1.]))
I = np.eye(2)
count = 0


def test_close(a, b, atol=2e-10):
    global count
    np.testing.assert_allclose(a, b, rtol=2e-10, atol=atol)
    count += 1


def hessian(kappa, angle):
    c, s = math.cos(angle), math.sin(angle)
    R = np.array([[c, -s], [s, c]])
    return R @ np.diag([kappa, 1.]) @ R.T


def operator_from_three_losses(H, x, z, eps):
    def f(v):
        return 0.5 * (v @ H @ v)
    plus, mid, minus = f(x + eps*z), f(x), f(x-eps*z)
    curvature = (plus-2*mid+minus)/(eps*eps)
    direct = (plus-minus)/(2*eps)
    # The original regularization and power-one weight: no clipping occurs.
    assert curvature > 1
    w = 1. / max(1., abs(curvature))
    return w * direct * z, curvature


def exact_one_step(H, n, eta):
    G = [np.outer(z, z) @ H / (z@H@z) for z in Z]
    M = (G[0]+G[1]) / 2
    direct = np.zeros((2,2))
    for k in range(n+1):
        avg = (k*G[0]+(n-k)*G[1])/n
        T = I - eta * avg
        direct += math.comb(n,k) / 2**n * (T.T @ H @ T)
    polynomial = I - 2*eta*M + eta*eta*((1-1/n)*M@M + M/n)
    prediction = H @ polynomial
    return direct, prediction, M, G


for kappa in [1.01, 1.5, 2.0, 7.0, 100., 10000.]:
    for theta in [0, .071, .22, .44, math.pi/4]:
        H = hessian(kappa, theta)
        c = kappa + 1
        delta = (kappa-1)*math.sin(2*theta)
        r = (kappa-1)*abs(math.cos(2*theta)) / math.sqrt(c*c-delta*delta)
        for n in [1, 2, 3, 4, 8]:
            for eta in [0.12, 0.8, 1., 2*n/(n+1), 2.4]:
                S, prediction, M, G = exact_one_step(H,n,eta)
                test_close(S, prediction, atol=4e-9)
                eig = np.linalg.eigvals(M)
                test_close(sorted(eig), [(1-r)/2, (1+r)/2], atol=1e-10)
                for g in G:
                    test_close(g@g, g, atol=1e-11)
                    test_close(H@g, g.T@H, atol=1e-8)
                expected_rates = sorted(
                    [1-2*eta*l+eta*eta*((1-1/n)*l*l+l/n)
                     for l in [(1-r)/2, (1+r)/2]])
                rates = sorted(np.linalg.eigvals(np.linalg.solve(H,S)))
                test_close(rates, expected_rates, atol=1e-9)
        # Three-point numerical differences independently recover the maps.
        if kappa < 1000:
            x = np.array([.17, -.23])
            for z in Z:
                approx, curve = operator_from_three_losses(H,x,z,.13)
                test_close(approx, np.outer(z,z)@H@x / (z@H@z))
                test_close(curve, z@H@z)

# The unique optimal risk and exact binomial propagated law.
for n in [1, 2, 3, 5, 8, 16]:
    eta = 2*n/(n+1)
    best = 1/(n+1)
    for kappa in [1.01, 3., 150.]:
        H = hessian(kappa, math.pi/4)
        S, prediction, M, G = exact_one_step(H,n,eta)
        test_close(S, best*H)
        test_close(M, I/2)
        # Mean-square identity for each independent batch, by conditional expectation.
        for horizon in [1, 3, 12]:
            x = np.array([.31,-.42])
            test_close((best**horizon)*(x@H@x),
                       ((1-eta/2)**2 + eta*eta/(4*n))**horizon*(x@H@x))
        # Other angles/steps cannot improve on best; strict at nonopt angles.
        for th in [0., .2, .4]:
            for et in [.5, 1., 2., eta]:
                A,B,Mat,_ = exact_one_step(hessian(kappa,th),n,et)
                h = hessian(kappa,th)
                worst = max(np.linalg.eigvals(np.linalg.solve(h,A)).real)
                assert worst > best - 2e-10
                count += 1
                if et==eta:
                    assert worst > best + 1e-11
                    count += 1

print(f'PASS: {count} independent numerical identity/inequality checks')
print('Analytical theorem, not finite numerical search, establishes optimality for all parameters.')
