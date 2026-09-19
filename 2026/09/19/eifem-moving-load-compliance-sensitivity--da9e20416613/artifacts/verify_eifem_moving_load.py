import numpy as np


def fd(fun, x, h=1e-7):
    return (fun(x + h) - fun(x - h)) / (2.0 * h)


def rank_one(mu):
    c, s = np.cos(mu), np.sin(mu)
    T = np.array([[c], [s]])
    Tp = np.array([[-s], [c]])
    K = np.diag([1.0, 4.0])
    F = np.array([0.0, 1.0])
    A = float((T.T @ K @ T)[0, 0])
    Ap = float((Tp.T @ K @ T + T.T @ K @ Tp)[0, 0])
    f = float((T.T @ F)[0])
    fp = float((Tp.T @ F)[0])
    q = f / A
    J = f * q
    exact = 2.0 * fp * q - q * q * Ap
    stiff_only = -q * q * Ap
    return J, exact, stiff_only, 2.0 * fp * q


def rank_one_J(mu):
    return rank_one(mu)[0]


def full_rotation(mu):
    c, s = np.cos(mu), np.sin(mu)
    T = np.array([[c, -s], [s, c]])
    Tp = np.array([[-s, -c], [c, -s]])
    K = np.diag([1.0, 4.0])
    F = np.array([1.0, 1.0])
    A = T.T @ K @ T
    Ap = Tp.T @ K @ T + T.T @ K @ Tp
    f = T.T @ F
    fp = Tp.T @ F
    q = np.linalg.solve(A, f)
    y = T @ q
    J = float(f @ q)
    exact = float(2.0 * fp @ q - q @ Ap @ q)
    stiff_only = float(-q @ Ap @ q)
    residual = float(np.linalg.norm(F - K @ y))
    return J, exact, stiff_only, float(2.0 * fp @ q), residual


mu = np.pi / 4.0
J, exact, stiff, load_term = rank_one(mu)
print('rank-one moving subspace at mu=pi/4')
print(f'J                       = {J:.15f}')
print(f'finite-difference Jprime = {fd(rank_one_J, mu): .15f}')
print(f'exact pulled-load grad   = {exact: .15f}')
print(f'stiffness-only grad      = {stiff: .15f}')
print(f'missing load term        = {load_term: .15f}')
print()

print('orthogonal coordinate gauge (full space, exact ROM)')
for mu in (0.0, 0.3, 0.7):
    J, exact, stiff, load_term, residual = full_rotation(mu)
    print(
        f'mu={mu:.1f} J={J:.15f} exact_grad={exact: .3e} '
        f'stiff_only={stiff: .15f} load_term={load_term: .15f} '
        f'residual={residual:.3e}'
    )

print()
print('scalar gauge shift test')
A0 = np.array([[2.0, 0.3], [0.3, 1.5]])
f0 = np.array([1.0, -0.4])
q0 = np.linalg.solve(A0, f0)
J0 = float(f0 @ q0)
for c in (1.0, 10.0, -7.0):
    predicted_shift = -2.0 * c * J0
    print(f'c={c: .1f} J={J0:.15f} stiffness-only gauge shift={predicted_shift: .15f}')
