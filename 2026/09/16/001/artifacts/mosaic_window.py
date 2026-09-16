"""Mosaic kappa=2 Liouville ME: conjugacy check, LE curve, beta bounds, window DOS/IPR."""
import json, math
import numpy as np

# ---------- 1. Liouvillean alpha with 0<beta<infty ----------
# CF with one exponentially-large partial quotient: a = [0; 2,1,3,40,1,1,2,1]
a = [0, 2, 1, 3, 40, 1, 1, 2, 1]

def convergents(a):
    p0, p1 = a[0], a[0]*a[1]+1 if len(a)>1 else (a[0], 1)
    # standard recurrence
    ps = [a[0]]; qs = [1]
    if len(a) == 1:
        return ps, qs
    ps = [a[0], a[0]*a[1]+1]; qs = [0, 1]
    # redo cleanly:
    p_prev2, p_prev1 = a[0], a[0]*a[1]+1
    q_prev2, q_prev1 = 1, a[1]
    ps = [p_prev2, p_prev1]; qs = [q_prev2, q_prev1]
    for k in range(2, len(a)):
        p = a[k]*p_prev1 + p_prev2
        q = a[k]*q_prev1 + q_prev2
        ps.append(p); qs.append(q)
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
    return ps, qs

ps, qs = convergents(a)
alpha = ps[-1]/qs[-1]  # rational approximant used for numerics (high accuracy)
beta_cf = max(math.log(qs[n+1])/qs[n] for n in range(len(qs)-1))
print("convergents q:", qs)
print("alpha approx:", alpha)
print("CF beta estimator max log(q_{n+1})/q_n =", beta_cf)

def dist_to_int(x):
    return abs(x - round(x))

def beta_bruteforce(omega, Qmax):
    best = 0.0; bestq = 0
    for q in range(1, Qmax+1):
        d = dist_to_int(q*omega)
        if d < 1e-300 or d <= 0:
            continue
        v = -math.log(d)/q
        if v > best:
            best = v; bestq = q
    return best, bestq

b_a, qa = beta_bruteforce(alpha, 2000)
b_2a, q2 = beta_bruteforce(2*alpha % 1, 2000)
print(f"brute-force beta(alpha)~{b_a:.4f} @q={qa}; beta(2alpha)~{b_2a:.4f} @q={q2}")
print(f"lemma check: beta(a)={b_a:.4f} <= beta(2a)={b_2a:.4f} <= 2*beta(a)={2*b_a:.4f} ?",
      b_a - 1e-12 <= b_2a <= 2*b_a + 1e-12)
beta2 = b_2a  # working estimate of beta(2 alpha)

# ---------- 2. LE curve vs 1/2 max(0, log|lambda E|) ----------
lam = 2.0
theta = 0.1

def mosaic_LE(E, N=4000):
    # product of 1-step matrices, with rescaling
    M = np.eye(2)
    acc = 0.0
    for n in range(N):
        Vn = 2*lam*math.cos(2*math.pi*(theta + n*alpha)) if n % 2 == 0 else 0.0
        S = np.array([[E - Vn, -1.0],[1.0, 0.0]])
        M = S @ M
        nm = np.linalg.norm(M)
        if nm > 1e100:
            M = M/nm; acc += math.log(nm)
    return (acc + math.log(np.linalg.norm(M)))/N

Es = [0.2, 0.4, 0.5, 0.6, 0.8, 1.2, 2.0, 3.0]
le_rows = []
for E in Es:
    L = mosaic_LE(E)
    theory = 0.5*max(0.0, math.log(abs(lam*E)))
    le_rows.append([E, L, theory])
    print(f"E={E:5.2f} LE_num={L:.4f} theory={theory:.4f}")

# ---------- 3. Conjugacy D_E = B A  <->  effective AMO, P=[[1,0],[-1,E]] ----------
def check_conjugacy(E, phi):
    c = math.cos(2*math.pi*phi)
    Aval = np.array([[E-2*lam*c, -1.0],[1.0, 0.0]])
    B = np.array([[E, -1.0],[1.0, 0.0]])
    D = B @ Aval
    tE = E**2 - 2; tl = lam*E
    St = np.array([[tE-2*tl*c, -1.0],[1.0, 0.0]])
    P = np.array([[1.0, 0.0],[-1.0, E]])
    Pinv = np.array([[1.0, 0.0],[1.0/E, 1.0/E]])
    err = np.linalg.norm(St - P @ D @ Pinv)
    return err

for E in [0.6, 1.3, 2.5]:
    print(f"conjugacy err E={E}:", check_conjugacy(E, 0.37))

# ---------- 4. Finite-volume mosaic spectrum: window DOS + IPR + effective residual ----------
L = 400  # even
n = np.arange(L)
V = np.where(n % 2 == 0, 2*lam*np.cos(2*math.pi*(theta + n*alpha)), 0.0)
H = np.diag(V) + np.diag(np.ones(L-1), 1) + np.diag(np.ones(L-1), -1)
evals, evecs = np.linalg.eigh(H)
Ec = 1.0/abs(lam)
upper = math.exp(beta2)/abs(lam)
print(f"lambda={lam} Ec={Ec} beta2~{beta2:.4f} upper={upper:.4f}")
in_window = [e for e in evals if Ec < abs(e) < upper]
in_loc = [e for e in evals if abs(e) > upper]
print(f"#eig in Gordon window (|Ec|<|E|<upper): {len(in_window)}; #eig beyond: {len(in_loc)}")

def ipr(v):
    return float(np.sum(np.abs(v)**4))

# pick representative states: deepest in window, and deep localized
if in_window:
    Ew = min(in_window, key=lambda e: abs(abs(e)-(Ec+upper)/2))
else:
    Ew = None
if in_loc:
    El = max(in_loc, key=abs)
else:
    El = None
print("representative window E:", Ew, " localized E:", El)
res = {}
for tag, E in [("window", Ew), ("localized", El)]:
    if E is None: continue
    j = int(np.argmin(np.abs(evals - E)))
    v = evecs[:, j]
    ip = ipr(v)
    # effective residual on interior even sites
    u = v
    Eיוון = float(evals[j])
    lam_eff = lam*Eיוון; Et = Eיוון**2 - 2
    ve = u[0::2]
    m = np.arange(len(ve))
    Vef = 2*lam_eff*np.cos(2*math.pi*(theta + m*(2*alpha)))
    Hv = np.zeros_like(ve)
    Hv[1:-1] = ve[:-2] + ve[2:] + Vef[1:-1]*ve[1:-1]
    r = Hv[1:-1] - Et*ve[1:-1]
    res[tag] = {"E": Eיוון, "IPR": ip,
                "interior_residual_max": float(np.max(np.abs(r)))}
    print(tag, res[tag])

out = {
  "alpha_CF": a, "convergents_q": qs, "alpha": alpha,
  "beta_CF_est": beta_cf, "beta_alpha_bruteforce": b_a, "beta_2alpha_bruteforce": beta2,
  "lemma_holds": bool(b_a - 1e-12 <= beta2 <= 2*b_a + 1e-12),
  "lambda": lam, "Ec": Ec, "upper": upper,
  "LE_rows_E_num_theory": le_rows,
  "n_window_eigs": len(in_window), "n_localized_eigs": len(in_loc),
  "representatives": res,
}
with open("/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20435/output/artifacts/mosaic_window.json", "w") as f:
    json.dump(out, f, indent=1)
print("wrote mosaic_window.json")
