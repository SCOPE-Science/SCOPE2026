"""Independent reproducibility calculations for a two-periodic DGDA theorem.

Analytical identities are checked over exact symbolic expressions; numerical
checks illustrate, but do not prove, statements quantified over all dimensions.
"""
import numpy as np
import sympy as sp


def transfer(a, rho, eta, sign=1):
    """One step in the real stacked order (z, filtered z)."""
    a = np.asarray(a, dtype=float)
    n = a.shape[0]
    assert a.shape == (n, n)
    zero = np.zeros((n, n))
    k = np.block([[zero, a], [-a.T, zero]])
    ident = np.eye(2 * n)
    c = 1 - rho
    return np.block([[c * ident - sign * eta * k, rho * ident],
                     [rho * ident, c * ident]])


def multipliers(rho, t):
    tr = 2 * ((1-rho)**2 + rho**2) + t**2
    det = (1-2*rho)**2 + (1-rho)**2 * t**2
    delta = (tr * tr - 4 * det)**0.5
    return (tr - delta) / 2, (tr + delta) / 2


def exact_identities():
    r, t = sp.symbols('r t', real=True)
    c = 1-r
    one = sp.eye(2)
    hp = sp.Matrix([[c + sp.I*t, r], [r, c]])
    qm = sp.simplify(hp.conjugate().T * hp)
    tr = 2*(c*c+r*r)+t*t
    det = (1-2*r)**2+c*c*t*t
    assert sp.simplify(sp.trace(qm)-tr) == 0
    assert sp.simplify(qm.det()-det) == 0
    assert sp.factor((one-qm).det()) == r*(r-2)*t**2
    v = sp.Matrix([1, 1])
    assert sp.simplify((v.conjugate().T * qm * v)[0]/2 - (1+t*t/2)) == 0
    assert sp.factor((1-tr+det)) == r*(r-2)*t**2
    # Perturbation of the unstable root at t=0 for each fixed 0<r<1.
    deriv = sp.factor((1-(1-r)**2) / (1-(1-2*r)**2))
    assert sp.simplify(deriv-(2-r)/(4*(1-r))) == 0
    half = sp.Rational(1,2)
    tr_half = sp.factor(tr.subs({r:half,t:half}))
    det_half = sp.factor(det.subs({r:half,t:half}))
    assert tr_half == sp.Rational(5,4)
    assert det_half == sp.Rational(1,16)
    assert sp.factor(tr_half**2-4*det_half) == sp.Rational(21,16)


def numerical_checks():
    rng = np.random.default_rng(73251)
    tested = 0
    for n in range(1, 5):
        for _ in range(60):
            a = rng.normal(size=(n, n)) + 0.35*np.eye(n)
            if np.linalg.svd(a, compute_uv=False)[-1] < 0.04:
                a += 0.8 * np.eye(n)
            rho = rng.uniform(0.025, 0.975)
            eta = rng.uniform(0.025, 1.25)
            plus = transfer(a,rho,eta,1)
            minus = transfer(a,rho,eta,-1)
            q = minus@plus
            assert np.allclose(minus, plus.T, atol=1e-11)
            assert np.allclose(q,plus.T@plus,atol=1e-11)
            assert np.allclose(q, q.T, atol=1e-11)
            expected = []
            for sigma in np.linalg.svd(a,compute_uv=False):
                lo,hi = multipliers(rho,eta*sigma)
                assert 0 < lo < 1 < hi
                expected.extend([lo,lo,hi,hi])
            actual = np.linalg.eigvalsh(q)
            assert np.allclose(actual,sorted(expected),rtol=1e-8,atol=5e-9)
            z0 = rng.normal(size=2*n)
            v = np.r_[z0,z0]
            kv = np.block([[np.zeros_like(a),a],[-a.T,np.zeros_like(a)]])@z0
            exact_ratio = 1 + eta**2*np.dot(kv,kv)/(2*np.dot(z0,z0))
            assert np.allclose(np.dot(v,q@v)/np.dot(v,v),exact_ratio,atol=2e-11)
            # Every synchronized nonzero initial condition excites growing modes.
            vals,vecs = np.linalg.eigh(q)
            coeff = vecs.T@v
            assert np.linalg.norm(coeff[vals>1]) > 1e-8*np.linalg.norm(v)
            tested += 1
    a=np.array([[1.]])
    h=transfer(a,.5,.5,1)
    assert max(abs(np.linalg.eigvals(h)))<1
    hm=transfer(a,.5,.5,-1)
    q=hm@h
    expected=(5+np.sqrt(21))/8
    assert np.allclose(max(np.linalg.eigvalsh(q)),expected)
    # Verify the auxiliary-state elimination at rho=1/2 against OGDA.
    z=np.array([1.,-.25])
    f=z.copy()
    eta=.32
    k=np.array([[0.,1.],[-1.,0.]])
    zz=[z.copy()]
    for j in range(15):
        sign=1 if j%2==0 else -1
        z,f=(.5*np.eye(2)-eta*sign*k)@z+.5*f, .5*z+.5*f
        zz.append(z.copy())
    for j in range(1,15):
        next_ogda=(np.eye(2)-eta*((-1)**j)*k)@zz[j]+(eta/2)*((-1)**(j-1))*k@zz[j-1]
        assert np.allclose(zz[j+1],next_ogda,atol=1e-10)
    return tested


if __name__=='__main__':
    exact_identities()
    tested=numerical_checks()
    print(f'VERIFY_OK exact symbolic trace/determinant/root threshold, {tested} SVD Floquet tests, stable-frozen comparator and OGDA equivalence')
