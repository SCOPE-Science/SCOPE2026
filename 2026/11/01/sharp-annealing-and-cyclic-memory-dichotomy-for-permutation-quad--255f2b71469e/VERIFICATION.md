---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Writing u_n=2x_m(n)-1 gives u_{n+1}=u_n² and normalized z_{n+1}=[α_n I+(1-α_n)P]z_n exactly, including boundary-zero first coordinates when 0<x_m(0)<1. Orthogonal Fourier diagonalization of each permutation cycle yields |λ|²=1-4α(1-α)sin²(πj/ℓ), so D_n→∞ kills precisely all nonconstant modes at e^{-2σD_n}. If D∞<∞, δ_n=min(α,1-α) is summable; factoring P^{b_n} leaves Q_n=product(I+δ_n(P^{±1}-I)), which converges in operator norm with stated tail bound. The residue B_n modulo P order then gives a singleton or the exact finite P-orbit omega set. A nontrivial ℓ>=3 Fourier multiplier never vanishes, while a 2-cycle mode is annihilated exactly by α=1/2; this proves the universal exception. For a 3-cycle and α_n=(n+4)^-p, p=1 gives log product -3/2 log n+O(1), p>1 retains all nonconstant modes. An independent exact-rational finite nonlinear/linear factorization check agrees; no finite test proves arbitrary schedules.

## originality

PASS

The same autonomous parameter-α nonlinear model and its finite omega limits were established by Jamilov (2022/2023). The candidate extension is to arbitrary time-varying deterministic α_n with a necessary-and-sufficient sum criterion, exact involution exception, omega-set formula and critical polynomial decay. Other 2024/2026 static-permutation papers remain a historical-priority risk, not automatic failure.

## value

PASS

The system is a natural nonlinear stochastic map with an exact inhomogeneous extension. It completely separates schedules that erase permutation memory from ones retaining a finite orbit and identifies the single exceptional averaging update on involutions, together with a sharp annealing rate. This is an independently useful classification of arbitrary schedules, not just a renamed constant-coefficient orbit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
