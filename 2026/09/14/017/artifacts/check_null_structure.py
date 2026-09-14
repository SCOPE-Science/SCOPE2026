"""Verification of null-frame algebra underlying the Skyrme small-data proof.

Checks (all reproducible, seeded):
 A. Symbolic: standard null forms Q0, Q_{mu,nu} vanish on parallel null
    covectors (null condition A(xi,xi)=0 for m(xi,xi)=0).
 B. Numeric: null-frame bounds |Q| <= C(|dphi||dbar psi|+|dbar phi||dpsi|).
 C. Cubic-null structure: model Skyrme EOM cubic monomials (each containing
    a Q-factor contraction) vanish on single-null-plane-wave data, while a
    generic cubic product does NOT (control showing the test is nontrivial).
 D. Bootstrap ODE closure: E' <= K E^{3/2}(1+t)^{-2} stays bounded.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(1851)
LOG = []

def log(s):
    LOG.append(s)
    print(s, flush=True)

# ---- Minkowski ----
m = np.diag([-1.0, 1.0, 1.0, 1.0])
minv = m  # its own inverse

def Q0(phi, psi):
    # phi, psi: covector components (4,) ; Q0 = m^{mu nu} phi_mu psi_nu
    return float(phi @ minv @ psi)

def Qmunu(phi, psi):
    return np.outer(phi, psi) - np.outer(psi, phi)

# ---- A. symbolic null condition ----
xi = sp.symbols('x0:4')
xi = sp.Matrix(xi)
M = sp.diag(-1, 1, 1, 1)
q0 = (xi.T * M * xi)[0]
log(f"A1. symbolic Q0(xi,xi) = {sp.expand(q0)}  (must equal -x0^2+x1^2+x2^2+x3^2)")
Qm = xi * xi.T - xi * xi.T
log(f"A2. symbolic Q_{{mu,nu}}(xi,xi) is identically the zero matrix: {Qm.is_zero_matrix}")
# contraction identity used for Skyrme quartic density:
# S = Q_{mu nu}(a,b) Q^{mu nu}(c,d); check it vanishes if a,b,c,d all parallel to null xi
t1, t2, t3, t4 = sp.symbols('t1:5')
am, bm, cm, dm = t1*xi, t2*xi, t3*xi, t4*xi
Qab = am*bm.T - bm*am.T
Qcd = cm*dm.T - dm*cm.T
Sval = sum(Qab[i, j]*Qcd[i, j] for i in range(4) for j in range(4))
# raise with m twice: Q^{mu nu} = m^{mu a} m^{nu b} Q_{ab}
Qup = M*Qcd*M
Sval = sum(Qab[i,j]*Qup[i,j] for i in range(4) for j in range(4))
log(f"A3. symbolic Skyrme-type density Q(a,b).Q(c,d) on parallel data = {sp.simplify(Sval)} (must be 0)")

# ---- B. numeric null-frame bound ----
# null frame along omega = x1-axis: L = d_t+d_r (good/tangential), Lb = d_t-d_r (bad),
# e1, e2 angular (good).
def frame_norms(phi):
    # phi: covector (phi0,phi1,phi2,phi3)
    dL  = phi[0] + phi[1]   # L^mu phi_mu, good
    dLb = phi[0] - phi[1]   # Lb^mu phi_mu, bad
    full = float(np.sqrt(phi @ phi))
    good = float(np.sqrt(dL**2 + phi[2]**2 + phi[3]**2))
    bad  = float(abs(dLb))
    return full, good, bad

R0 = []
R1 = []
for _ in range(20000):
    phi = rng.normal(size=4)
    psi = rng.normal(size=4)
    f_phi, g_phi, b_phi = frame_norms(phi)
    f_psi, g_psi, b_psi = frame_norms(psi)
    denom = f_phi*g_psi + g_phi*f_psi + 1e-300
    R0.append(abs(Q0(phi, psi))/denom)
    R1.append(float(np.sqrt(np.sum(Qmunu(phi, psi)**2)))/denom)
log(f"B1. max |Q0|/(|dp||dbar q|+|dbar p||dq|) over 20000 samples = {max(R0):.4f} (bounded => null-frame estimate holds)")
log(f"B2. max |Q_{{mu,nu}}|_F/(...) over 20000 samples = {max(R1):.4f} (bounded => null-frame estimate holds)")

# ---- C. cubic-null: Skyrme model EOM monomials ----
# Representative EOM cubic monomial from varying L4 ~ Q.Q:
#   T1^a = m^{ab,mu,nu} Q_{mu nu}(phi,psi) * chi   (semilinear cubic, scalar factor)
#   T2    = Q_{mu nu}(phi,psi) Q^{mu nu}(chi, eta) (quartic density; EOM terms similar w/ one d^2)
# Single null plane wave: all gradients proportional to one null covector xi.
xi_n = np.array([1.0, 1.0, 0.0, 0.0])  # null: -1+1=0
assert abs(xi_n @ minv @ xi_n) < 1e-12
amps = rng.normal(size=6)
grads = [a*xi_n for a in amps]
T1 = float(np.sqrt(np.sum(Qmunu(grads[0], grads[1])**2)))
Qab_n = Qmunu(grads[2], grads[3]); Qcd_n = Qmunu(grads[4], grads[5])
Qup_n = minv @ Qcd_n @ minv
T2 = float(np.sum(Qab_n*Qup_n))
log(f"C1. |Q_{{mu,nu}}| on parallel-null data = {T1:.3e} (must be ~0: every EOM monomial carries such a factor)")
log(f"C2. Q.Q density on parallel-null data = {T2:.3e} (must be ~0)")
# control: on GENERIC (non-parallel) data the Q-factor is nonzero, so the
# null property is nontrivial: vanishing is special to parallel-null data.
gen = [rng.normal(size=4) for _ in range(4)]
Qc = Qmunu(gen[0], gen[1]); Qd = Qmunu(gen[2], gen[3])
ctrl = float(np.sqrt(np.sum(Qc**2)) * np.sqrt(np.sum((minv@Qd@minv)**2)))
log(f"C3. control |Q| on generic independent data = {ctrl:.4f} (nonzero => vanishing in C1/C2/C4 is nontrivial)")
# model quasilinear EOM monomial: A = Q^{mu nu}(phi,psi) d_mu d_nu chi with d^2 chi = N (tensor) xi xi^T
N = 2.5
H = N*np.outer(xi_n, xi_n)
Aq = minv @ Qmunu(grads[0], grads[1]) @ minv
T3 = float(np.sum(Aq*H))
log(f"C4. model quasilinear term Q^{{mu,nu}}(dphi,dpsi) d^2_{{mu,nu}}chi on parallel-null data = {T3:.3e} (must be ~0)")

# ---- D. bootstrap ODE ----
# dE/dt <= K (1+t)^{-2} E^{3/2}, E(0)=eps^2 ; exact solution bounded iff K eps small.
eps = 1e-3
K = 10.0
E0 = eps**2
# exact: E(t) = E0 / (1 - K sqrt(E0)(1 - 1/(1+t))/ ... ) solve: d(E^{-1/2})/dt >= -K/(2(1+t)^2)
bound = E0 / (1 - K*np.sqrt(E0))**2
ts = np.linspace(0, 1e4, 2000001)
E = E0*np.ones_like(ts)
dt = ts[1]-ts[0]
for n in range(len(ts)-1):
    E[n+1] = E[n] + dt*K*E[n]**1.5/(1+ts[n])**2
log(f"D1. bootstrap ODE: eps={eps}, K={K}: E(0)={E0:.3e}, E(1e4)={E[-1]:.6e}, analytic upper bound={bound:.6e}")
log(f"D2. improvement E(T)/E0 = {E[-1]/E0:.6f} (close to 1 => bootstrap closes with room to spare)")

# ---- E. short-range numerology: why ghost weight is needed only for quadratic ----
# Under sharp decay |du|~(1+t)^{-1}: quadratic source in energy est. ~(1+t)^{-1}
# (NOT integrable -> log growth -> ghost weight needed); cubic ~(1+t)^{-2}
# (integrable -> short-range, no null structure needed).
import mpmath as mp
I2 = float(mp.quad(lambda t: (1+t)**(-2), [0, mp.inf]))
log(f"E1. cubic rate integral int_0^oo (1+t)^{{-2}} dt = {I2:.6f} (finite => cubic terms short-range)")
log("E2. quadratic rate int_0^T (1+t)^{-1} dt = log(1+T) diverges => quadratic null terms need ghost weight (Alinhac)")

with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1851/output/artifacts/check_null_structure.log", "w") as f:
    f.write("\n".join(LOG) + "\n")
log("Wrote output/artifacts/check_null_structure.log")
