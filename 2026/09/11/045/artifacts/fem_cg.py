"""Matrix-free CG solver for P1 FEM Neumann problems (stdlib+numpy)."""
import numpy as np

def build_mesh(Nr, Nt):
    n = 1 + Nr*Nt
    xy = np.zeros((n, 2))
    for i in range(1, Nr+1):
        r = i/Nr
        for j in range(Nt):
            th = 2*np.pi*j/Nt
            xy[1+(i-1)*Nt+j] = [r*np.cos(th), r*np.sin(th)]
    tris = []
    for j in range(Nt):
        tris.append((0, 1+j, 1+(j+1) % Nt))
    for i in range(1, Nr):
        for j in range(Nt):
            j2 = (j+1) % Nt
            a = 1+(i-1)*Nt+j; b = 1+(i-1)*Nt+j2
            c = 1+i*Nt+j;     d = 1+i*Nt+j2
            tris.append((a, c, d)); tris.append((a, d, b))
    return xy, np.array(tris, dtype=np.int64)

def elem_data(xy, tris, sig):
    p0, p1, p2 = xy[tris[:, 0]], xy[tris[:, 1]], xy[tris[:, 2]]
    area = 0.5*np.abs((p1[:, 0]-p0[:, 0])*(p2[:, 1]-p0[:, 1])-(p2[:, 0]-p0[:, 0])*(p1[:, 1]-p0[:, 1]))
    A2 = 2*area
    def perp(v): return np.stack([-v[:, 1], v[:, 0]], axis=1)
    G = np.stack([perp(p1-p2)/A2[:, None], perp(p2-p0)/A2[:, None],
                  perp(p0-p1)/A2[:, None]], axis=1)  # (Ne,3,2)
    return G, (sig*area)  # w = sig*area

def make_matvec(tris, G, w, n, pinned):
    Ne = tris.shape[0]
    Gw = G * w[:, None, None]
    # local 3x3: Ke = G @ Gw^T summed over dim -> einsum
    Ke = np.einsum('ead,ebd->eab', G, Gw)  # (Ne,3,3)
    T = tris
    def matvec(x):
        xe = x[T]                       # (Ne,3) / (Ne,3,M)
        if xe.ndim == 2:
            ye = np.einsum('eab,eb->ea', Ke, xe)
        else:
            ye = np.einsum('eab,ebm->eam', Ke, xe)
        y = np.zeros_like(x)
        np.add.at(y, T.ravel(), ye.reshape(-1) if ye.ndim == 2 else ye.reshape(-1, ye.shape[-1]))
        y[pinned] = 0.0
        return y
    # Jacobi diag
    d = np.zeros(n)
    for a in range(3):
        np.add.at(d, T[:, a], Ke[:, a, a])
    d[pinned] = 1.0
    return matvec, d

def cg_solve(matvec, diag, b, tol=1e-10, maxit=4000):
    M = b.shape[1] if b.ndim == 2 else 1
    B = b if b.ndim == 2 else b[:, None]
    X = np.zeros_like(B)
    R = B - matvec(X)
    Z = R / diag[:, None]
    P = Z.copy()
    rs = np.einsum('im,im->m', R, Z)
    bnorm = np.sqrt(np.einsum('im,im->m', B, B)) + 1e-300
    it = 0
    for it in range(maxit):
        AP = matvec(P)
        pAp = np.einsum('im,im->m', P, AP) + 1e-300
        al = rs / pAp
        X += P * al[None, :]
        R -= AP * al[None, :]
        rn = np.sqrt(np.einsum('im,im->m', R, R))
        if np.all(rn / bnorm < tol):
            break
        Z = R / diag[:, None]
        rsn = np.einsum('im,im->m', R, Z)
        be = rsn / (rs + 1e-300)
        P = Z + P * be[None, :]
        rs = rsn
    rel = float(np.max(np.sqrt(np.einsum('im,im->m', R, R)) / bnorm))
    return (X[:, 0] if b.ndim == 1 else X), rel, it+1
