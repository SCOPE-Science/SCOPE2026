import numpy as np

rng = np.random.default_rng(350067)

def softmax(z):
    z = z - np.max(z, axis=-1, keepdims=True)
    e = np.exp(z)
    return e / np.sum(e, axis=-1, keepdims=True)

def ce_from_logits(z, y):
    zmax = np.max(z, axis=-1, keepdims=True)
    lse = zmax[:,0] + np.log(np.sum(np.exp(z-zmax), axis=1))
    return np.mean(lse - z[np.arange(len(y)), y])

def model_loss(V, A, X, y):
    H = np.tanh(X @ A.T)
    return ce_from_logits(H @ V.T, y)

def ordinary_grads(V, A, X, y):
    H = np.tanh(X @ A.T)
    Z = H @ V.T
    P = softmax(Z)
    Y = np.zeros_like(P)
    Y[np.arange(len(y)), y] = 1.0
    GZ = (P-Y) / len(y)
    GV = GZ.T @ H
    GH = GZ @ V
    GA = (GH * (1-H*H)).T @ X
    return GV, GA

def powergrad_grads(W, A, X, y, alpha):
    H = np.tanh(X @ A.T)
    Z = H @ W.T
    P = softmax(Z)
    Ppow = P**alpha
    Pp = Ppow / np.sum(Ppow, axis=1, keepdims=True)
    Pscaled = softmax(alpha*Z)
    assert np.max(np.abs(Pp-Pscaled)) < 2e-13
    Y = np.zeros_like(Pp)
    Y[np.arange(len(y)), y] = 1.0
    GZ = (Pp-Y) / len(y)
    GW = GZ.T @ H
    GH = GZ @ W
    GA = (GH * (1-H*H)).T @ X
    return GW, GA

def psi(W, A, X, y, alpha):
    return model_loss(alpha*W, A, X, y) / alpha

def finite_diff_matrix(fun, M, eps=1e-6):
    G = np.empty_like(M)
    for idx in np.ndindex(M.shape):
        Mp = M.copy(); Mm = M.copy()
        Mp[idx] += eps; Mm[idx] -= eps
        G[idx] = (fun(Mp)-fun(Mm))/(2*eps)
    return G

for alpha in (0.2, 0.4, 0.7, 1.0):
    for _ in range(8):
        n, din, dh, c = 6, 4, 3, 5
        X = rng.normal(size=(n,din))
        y = rng.integers(0,c,size=n)
        A = rng.normal(scale=0.4,size=(dh,din))
        W = rng.normal(scale=0.4,size=(c,dh))

        GWp, GAp = powergrad_grads(W,A,X,y,alpha)
        GV, GAordinary = ordinary_grads(alpha*W,A,X,y)
        assert np.max(np.abs(GWp-GV)) < 2e-12
        assert np.max(np.abs(GAp-GAordinary/alpha)) < 2e-12

        fdW = finite_diff_matrix(lambda Z: psi(Z,A,X,y,alpha), W)
        fdA = finite_diff_matrix(lambda B: psi(W,B,X,y,alpha), A)
        assert np.max(np.abs(fdW-GWp)) < 3e-6
        assert np.max(np.abs(fdA-GAp)) < 3e-6

        etaW = 0.03
        etaA = 0.05
        Wn = W - etaW*GWp
        An = A - etaA*GAp
        V = alpha*W
        Vn = V - (alpha*etaW)*GV
        Aordinary_n = A - (etaA/alpha)*GAordinary
        assert np.max(np.abs(Vn-alpha*Wn)) < 2e-14
        assert np.max(np.abs(Aordinary_n-An)) < 2e-14

# Fixed-feature minibatch trajectory conjugacy.
for alpha in (0.25, 0.6, 1.0):
    n, dh, c = 24, 6, 4
    H = rng.normal(size=(n,dh))
    y = rng.integers(0,c,size=n)
    W = rng.normal(scale=0.1,size=(c,dh))
    V = alpha*W.copy()
    eta = 0.08
    for t in range(120):
        idx = rng.choice(n, size=7, replace=False)
        Hb = H[idx]
        yb = y[idx]

        # PowerGrad gradient.
        Z = Hb @ W.T
        P = softmax(Z)
        Pp = P**alpha
        Pp /= np.sum(Pp, axis=1, keepdims=True)
        Y = np.zeros_like(Pp)
        Y[np.arange(len(yb)), yb] = 1.0
        GW = ((Pp-Y)/len(yb)).T @ Hb
        W = W - eta*GW

        # Ordinary CE gradient in V with step alpha*eta.
        Zv = Hb @ V.T
        Pv = softmax(Zv)
        Yv = np.zeros_like(Pv)
        Yv[np.arange(len(yb)), yb] = 1.0
        GV = ((Pv-Yv)/len(yb)).T @ Hb
        V = V - (alpha*eta)*GV

        assert np.max(np.abs(V-alpha*W)) < 2e-12
        assert np.array_equal(np.argmax(H @ W.T, axis=1),
                              np.argmax(H @ V.T, axis=1))

print("verification passed")
