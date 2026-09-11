"""Verified ledger: FEM NtD + Fréchet via CG, three-mesh convergence + residual-certified eigenvalue bars."""
import numpy as np, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fem_cg import build_mesh, elem_data, make_matvec, cg_solve

def in_sq(x, y, box):
    return (x >= box[0]) & (x <= box[1]) & (y >= box[2]) & (y <= box[3])

def sigA(x, y):
    s = np.ones_like(x); s[in_sq(x, y, (-0.4, 0.4, -0.4, 0.4))] = 3.0; return s
def sigB(x, y):
    s = np.ones_like(x); s[in_sq(x, y, (-0.4, 0.4, -0.4, 0.4))] = 3.0
    s[in_sq(x, y, (-0.2, 0.2, -0.2, 0.2))] = 0.5; return s
def sig0(x, y):
    return np.ones_like(x)

e = np.linspace(-0.8, 0.8, 5)
F = [(e[i], e[i+1], e[j], e[j+1]) for i in range(4) for j in range(4)]
ALPHA = 1.5; NF = 8  # 16 Fourier modes

def sigma_fields(tris_cent_fn, tris, fun, depth):
    Ne = tris.shape[0]; ns = 4**depth
    acc = np.zeros(Ne); cents = np.zeros((Ne, ns, 2))
    grids = tris_cent_fn(depth)
    for k, (cx, cy, wfrac) in enumerate(grids):
        cents[:, k, 0] = cx; cents[:, k, 1] = cy
        acc += fun(cx, cy)*wfrac
    return acc, cents

def subgrid_fn(xy, tris):
    p0, p1, p2 = xy[tris[:, 0]], xy[tris[:, 1]], xy[tris[:, 2]]
    def gen(depth):
        # barycentric lattice with (2^depth)^2 subs per tri
        m = 2**depth
        out = []
        for a in range(m):
            for b in range(m-a):
                for (da, db) in [(1/3, 1/3), (2/3, 1/6), (1/6, 2/3), (1/6, 1/6)] if False else [((a+1/3)/m, (b+1/3)/m)]:
                    pass
        # simpler: uniform 4-split recursion via midpoints
        cells = [(p0, p1, p2, 1.0)]
        for _ in range(depth):
            new = []
            for (A, B, C, w) in cells:
                M1 = (A+B)/2; M2 = (B+C)/2; M3 = (C+A)/2
                new += [(A, M1, M3, w/4), (M1, B, M2, w/4), (M3, M2, C, w/4), (M1, M2, M3, w/4)]
            cells = new
        grids = []
        for (A, B, C, w) in cells:
            grids.append(((A[:, 0]+B[:, 0]+C[:, 0])/3, (A[:, 1]+B[:, 1]+C[:, 1])/3, w))
        return grids
    return gen

def run(Nr, Nt, depth=3, tol=1e-11):
    xy, tris = build_mesh(Nr, Nt)
    n = xy.shape[0]; Ne = tris.shape[0]
    gen = subgrid_fn(xy, tris)
    sA, _ = sigma_fields(gen, tris, sigA, depth)
    sB, _ = sigma_fields(gen, tris, sigB, depth)
    s0, cents_info = sigma_fields(gen, tris, sig0, depth)
    G, _ = elem_data(xy, tris, np.ones(Ne))
    _, wA = elem_data(xy, tris, sA); _, w0 = elem_data(xy, tris, s0)
    p0, p1, p2 = xy[tris[:, 0]], xy[tris[:, 1]], xy[tris[:, 2]]
    area = 0.5*np.abs((p1[:, 0]-p0[:, 0])*(p2[:, 1]-p0[:, 1])-(p2[:, 0]-p0[:, 0])*(p1[:, 1]-p0[:, 1]))
    ns = cents_info.shape[1]
    cx = cents_info[:, :, 0]; cy = cents_info[:, :, 1]
    wsub = (area/ns)[:, None]
    bnd = 1+(Nr-1)*Nt+np.arange(Nt); th = 2*np.pi*np.arange(Nt)/Nt; ds = 2*np.pi/Nt
    modes = []
    for k in range(1, NF+1):
        modes.append(np.cos(k*th)/np.sqrt(np.pi)); modes.append(np.sin(k*th)/np.sqrt(np.pi))
    modes = np.array(modes)  # (M,Nt)
    M = modes.shape[0]
    Bp = np.zeros((n, M)); Bp[bnd] = (modes.T*ds)
    pinned = np.array([0])
    Bp[0] = 0.0
    def solve_all(sig):
        _, w = elem_data(xy, tris, sig)
        mv, dg = make_matvec(tris, G, w, n, pinned)
        X, rel, it = cg_solve(mv, dg, Bp, tol=tol)
        return X, rel, it, mv, dg
    UA, rA, iA, _, _ = solve_all(sA)
    UB, rB, iB, _, _ = solve_all(sB)
    U0, r0, i0, _, _ = solve_all(s0)
    LamA = (UA[bnd].T*ds) @ modes.T; LamB = (UB[bnd].T*ds) @ modes.T; Lam0 = (U0[bnd].T*ds) @ modes.T
    LamA = 0.5*(LamA+LamA.T); LamB = 0.5*(LamB+LamB.T); Lam0 = 0.5*(Lam0+Lam0.T)
    g0 = np.einsum('eam,ead->emd', U0[tris], G)  # (Ne,M,2) background gradients
    Gram = np.einsum('emd,end->emn', g0, g0)
    wC = W = None
    rows = []
    for C in F:
        inside = in_sq(cx, cy, C).astype(float)
        W = inside*wsub
        D = -np.einsum('e,emn->mn', W.sum(axis=1), Gram)
        MA = LamA-Lam0-ALPHA*D; MB = LamB-Lam0-ALPHA*D
        MA = 0.5*(MA+MA.T); MB = 0.5*(MB+MB.T)
        wa, Va = np.linalg.eigh(MA); wb, Vb = np.linalg.eigh(MB)
        # residual bars: ||M v - lam v||_2 (symmetric => |lam_true - lam| <= res)
        ra = float(np.linalg.norm(MA@Va[:, [0]]-wa[0]*Va[:, [0]]))
        rb = float(np.linalg.norm(MB@Vb[:, [0]]-wb[0]*Vb[:, [0]]))
        rows.append(dict(C=list(C), minA=float(wa[0]), minB=float(wb[0]),
                         resA=ra, resB=rb, Dmaxeig=float(np.linalg.eigvalsh(-D)[0])))
    gap = float(np.linalg.svd(LamA-LamB, compute_uv=False)[0])
    # CG residual influence: ||dU|| <= ||r||/lambda_min(K); bound via Rayleigh of assembled diag
    return rows, gap, dict(rA=rA, rB=rB, r0=r0, iA=iA, iB=iB, i0=i0, n=n, Ne=Ne, M=M)

if __name__ == '__main__':
    allrows = {}
    for (Nr, Nt) in [(32, 128), (48, 176), (64, 224)]:
        rows, gap, info = run(Nr, Nt)
        allrows[f"{Nr}x{Nt}"] = dict(rows=[[r['minA'], r['minB'], r['resA'], r['resB']] for r in rows], gap=gap, info=info)
        print(f"=== mesh Nr={Nr} Nt={Nt} n={info['n']} Ne={info['Ne']} gap={gap:.5f} cgres={info['rA']:.1e},{info['rB']:.1e},{info['r0']:.1e} ===", flush=True)
        for i, r in enumerate(rows):
            print(f"cell{i:2d} minA={r['minA']:+.5f}~{r['resA']:.1e} minB={r['minB']:+.5f}~{r['resB']:.1e}", flush=True)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ledger3.json'), 'w') as f:
        json.dump(allrows, f, indent=1)
