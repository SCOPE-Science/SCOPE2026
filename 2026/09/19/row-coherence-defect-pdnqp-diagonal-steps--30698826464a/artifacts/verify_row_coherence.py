import numpy as np

C = 0.99

def build(m, p):
    # Equality-only residual form: A=[1_{m x p}, I_m], B=[A,-I_m], H=I, sigma=1.
    A = np.concatenate([np.ones((m, p)), np.eye(m)], axis=1)
    B = np.concatenate([A, -np.eye(m)], axis=1)
    Hdiag = np.ones(p + 2*m)

    # PDNQP (28a)-(28b) masses for this family.
    mw = np.concatenate([
        np.full(p, m + 1.0),  # shared x columns
        np.full(m, 2.0),      # private x columns
        np.full(m, 2.0),      # residual columns
    ])
    my = np.sum(B*B / mw[None, :], axis=1)

    K = (B / np.sqrt(mw)[None, :]) / np.sqrt(my)[:, None]
    s = np.linalg.svd(K, compute_uv=False)

    a = p/(m+1.0)
    lam2_formula = (m*a + 1.0)/(a + 1.0)

    # A row-l1 dual scale, retaining the same primal masses, controls the coupling norm.
    row_l1 = np.sum(np.abs(B), axis=1)
    K_l1 = (B / np.sqrt(mw)[None, :]) / np.sqrt(row_l1)[:, None]
    s_l1 = np.linalg.svd(K_l1, compute_uv=False)

    # Top-singular-direction increments for the source step metrics (omega=1).
    U, sval, Vt = np.linalg.svd(K, full_matrices=False)
    u = U[:, 0]
    v = Vt[0, :]
    if np.sum(u) < 0:
        u = -u
        v = -v
    tau = C / mw
    eta = C / my
    dw = np.sqrt(tau) * v
    dy = np.sqrt(eta) * u
    lhs = 0.5*np.sum(dw*dw/tau) + 0.5*np.sum(dy*dy/eta)
    hterm = 0.5*np.sum(np.abs(dw * (Hdiag*dw)))
    cross = np.sum(np.abs(dw * (B.T @ dy)))
    rhs = hterm + cross

    return {
        'm': m, 'p': p,
        'row_norm_err': np.max(np.abs(np.linalg.norm(K, axis=1)-1.0)),
        'lambda': s[0],
        'lambda_formula': np.sqrt(lam2_formula),
        'c_lambda': C*s[0],
        'safe_l1_lambda': s_l1[0],
        'accept_lhs': lhs,
        'cross_term': cross,
        'h_term': hterm,
        'accept_rhs': rhs,
    }

print('c =', C)
print('Columns: m p row_norm_err lambda formula c*lambda safe_l1_norm lhs cross Hterm rhs')
for m,p in [(2,1),(4,10),(8,100),(16,1000),(32,2000)]:
    r=build(m,p)
    print(f"{r['m']:2d} {r['p']:5d} {r['row_norm_err']:.3e} "
          f"{r['lambda']:.12f} {r['lambda_formula']:.12f} {r['c_lambda']:.12f} "
          f"{r['safe_l1_lambda']:.12f} {r['accept_lhs']:.12f} "
          f"{r['cross_term']:.12f} {r['h_term']:.12f} {r['accept_rhs']:.12f}")

print('\nAsymptotic closed-form check (no large matrix allocation):')
for m,p in [(4,10**6),(16,10**6),(64,10**7)]:
    a=p/(m+1.0)
    lam=np.sqrt((m*a+1)/(a+1))
    print(f"m={m:2d}, p={p:8d}, lambda={lam:.12f}, sqrt(m)={np.sqrt(m):.12f}, required_common_rescale<={1/(C*lam):.12f}")
