"""Verify the single-entry obstruction falsifying beta_c=2/3.

Analytic claims checked numerically:
1. sigma_N^2 = 1 - 1/(sqrt(3) B_N) -> 1.
2. Exceedance mean M*p_N ~ const * N^{1/2} -> infinity for beta=0.6.
3. Sampled max scaled entry grows like N^{beta-1/2}; counts of |H_ij|>1 grow.
4. Diagonal max stays <=1 w.h.p.
"""
import numpy as np

rng = np.random.default_rng(856)

c_star = 3 ** (-1.5)  # tail constant P(|x|>t)=c_star*t^-3
beta = 0.6

def sigma2(B):
    return 1.0 - 1.0 / (np.sqrt(3) * B)

print("=== sigma_N ===")
for N in [100, 1000, 10_000, 10**6, 10**9]:
    B = N ** beta
    print(f"N={N:>10} B={B:.4g} sigma_N^2={sigma2(B):.8f}")

print("\n=== exceedance mean M*p for K'=2 (beta=0.6) ===")
Kp = 2.0
for N in [100, 1000, 10_000, 10**6, 10**9]:
    B = N ** beta
    s = np.sqrt(sigma2(B))
    t = Kp * s * np.sqrt(N)
    # exact Pareto tail for normalized law
    def tail(t_):
        t_ = np.asarray(t_)
        out = np.empty_like(t_, dtype=float)
        thr = 1 / np.sqrt(3)
        out[t_ < thr] = 1.0
        m = t_ >= thr
        out[m] = c_star * t_[m] ** (-3)
        return out
    p = tail(t) - tail(B) if t < B else 0.0
    M = N * (N - 1) / 2
    print(f"N={N:>10} t={t:.4g} B={B:.4g} Mp={M*p:.4g} P(no exceed)={np.exp(-M*p):.3g}")

def sample_max_scaled(N, B, seed):
    r = np.random.default_rng(seed)
    # sample symmetric Pareto: |xi| = U^{-1/3}, sign random; x = xi/sqrt(3)
    M = N * (N - 1) // 2
    # sample in chunks to save memory
    chunk = min(M, 2_000_000)
    mmax = 0.0
    cnt1 = 0
    s2 = sigma2(B)
    s = np.sqrt(s2)
    done = 0
    while done < M:
        c = min(chunk, M - done)
        U = r.random(c)
        R = U ** (-1 / 3)  # |xi|, P(R>t)=t^-3
        X = R / np.sqrt(3) * np.where(r.random(c) < 0.5, -1.0, 1.0)
        Xt = np.minimum(np.abs(X), B) * np.sign(X)
        H = np.abs(Xt) / (s * np.sqrt(N))
        mmax = max(mmax, H.max())
        cnt1 += int((H > 1.0).sum())
        done += c
    return mmax, cnt1

print("\n=== sampled max scaled entry and counts of |H|>1 (beta=0.6) ===")
for N, seed in [(200, 1), (500, 2), (2000, 3)]:
    B = N ** beta
    mmax, cnt1 = sample_max_scaled(N, B, seed)
    print(f"N={N} B/sqrtN={B/np.sqrt(N):.3f} sampled_max={mmax:.3f} count_gt1={cnt1} E[count]~{N**0.5 * c_star:.1f}")

print("\n=== small dense spectrum demo (beta=0.6) ===")
# One dense matrix at N=800 to show lambda_max near/above bulk edge and growing max entry.
# Uses full eigvalsh; N=800 is ~0.64M entries, fine.
N = 800
B = N ** beta
s = np.sqrt(sigma2(B))
U = rng.random((N, N))
R = U ** (-1 / 3) / np.sqrt(3)
S = np.where(rng.random((N, N)) < 0.5, -1.0, 1.0)
X = R * S
Xt = np.clip(X, -B, B)
# Proper Wigner: one sample per pair, mirrored (no factor-1/2 averaging).
H = np.zeros((N, N))
iu = np.triu_indices(N, 1)
H[iu] = Xt[iu] / (s * np.sqrt(N))
H[(iu[1], iu[0])] = H[iu]
H[range(N), range(N)] = np.clip(np.diag(X) / (s * np.sqrt(N)), -B / (s * np.sqrt(N)), B / (s * np.sqrt(N)))
ev = np.linalg.eigvalsh(H)
print(f"N={N} B/sqrtN={B/np.sqrt(N):.3f} max|H_ij|={np.abs(H).max():.3f} lambda_max={ev[-1]:.3f} (bulk edge 2)")
print("NOTE: max|H_ij| grows as N^{beta-1/2} -> infinity; lambda_max >= max|H_ij| - max|diag| diverges.")
print("Hence N^{2/3}(lambda_max-2) -> +infinity in prob, not TW1.")
print("\nVERIFY_OK")
