import numpy as np


def realign(x, da, db):
    # X_{ij,kl} -> R(X)_{ik,jl}
    return x.reshape(da, db, da, db).transpose(0, 2, 1, 3).reshape(da * da, db * db)


def partial_b(x, da, db):
    t = x.reshape(da, db, da, db)
    return np.einsum("ijkj->ik", t)


def partial_a(x, da, db):
    t = x.reshape(da, db, da, db)
    return np.einsum("ijil->jl", t)


def traceless_diag(d):
    a = np.arange(1, d + 1, dtype=float)
    a -= a.mean()
    a /= np.linalg.norm(a)
    return np.diag(a)


def check(da, db):
    A = traceless_diag(da)
    B = traceless_diag(db)
    base = np.eye(da * db) / (da * db)
    perturb = np.kron(A, B)
    # Choose a deterministic safely positive perturbation.
    op = np.linalg.norm(perturb, 2)
    eps = 0.05 / ((da * db) * max(op, 1e-15))
    rho = base + eps * perturb
    vals = np.linalg.eigvalsh(rho)
    assert vals.min() > -1e-12
    ra = partial_b(rho, da, db)
    rb = partial_a(rho, da, db)
    assert np.allclose(ra, np.eye(da) / da, atol=1e-12)
    assert np.allclose(rb, np.eye(db) / db, atol=1e-12)

    prod = np.kron(ra, rb)
    tilde = rho - prod
    Rt = realign(tilde, da, db)
    R = realign(rho, da, db)
    u0 = np.eye(da).reshape(-1) / np.sqrt(da)
    v0 = np.eye(db).reshape(-1) / np.sqrt(db)
    assert np.linalg.norm(Rt @ v0) < 1e-12
    assert np.linalg.norm(u0.conj() @ Rt) < 1e-12

    c = 1 / np.sqrt(da * db)
    for k in range(1, 5):
        lhs = np.trace(np.linalg.matrix_power(R @ R.conj().T, k)).real
        rhs = np.trace(np.linalg.matrix_power(Rt @ Rt.conj().T, k)).real + c ** (2 * k)
        assert abs(lhs - rhs) < 1e-10

    G = (1 - 1 / da) * (1 - 1 / db)
    assert np.sqrt(G) + c <= 1 + 1e-14


for dims in [(2, 2), (2, 3), (3, 4)]:
    check(*dims)
print("VERIFY_OK")
