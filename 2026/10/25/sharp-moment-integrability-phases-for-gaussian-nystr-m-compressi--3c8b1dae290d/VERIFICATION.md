---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The rank-one PSD flow A(t)=e^{tJ}A₀e^(−tJ) is exact. On the symmetric traceless two-dimensional mode, the pth-degree Taylor/RK endpoint satisfies Z_p=1/2[[1+c,s],[s,1−c]], c+is=P_p(2ih), so det Z_p=d_p=(1−|P_p(2ih)|²)/4. For symmetric invertible 2×2 matrices, the exact Nyström residual identity ||Z−(Zu)(vᵀZ)/(vᵀZu)||_F=|det Z| ||u|| ||v||/|vᵀZu| holds; independently checked exact rational probes and first fourteen Taylor-polynomial determinant degrees from inspected checker math and fresh symbolic expansions through degree ten. For tied u=v, positive definite Z yields a uniformly bounded residual and rank-one Z is reconstructed a.s.; indefinite Z has a quadratic denominator with four simple zero angles, each derivative modulus 2sqrt(−det Z), yielding tail rP(W>r)→2sqrt(−d_p)/π and exactly q<1 finite moments. Independent left/right Gaussian sketches instead exhibit the stated positive inverse-linear tail whenever Z invertible. Exact determinants d₁=−h²,d₂=−h⁴,d₃=h⁴(3−4h²)/9,d₄=h⁶(2−h²)/9 establish RK3/RK4 boundary rank-one cases and the mod-four signs of higher Taylor orders. The true-error tail agrees with the residual tail because the deterministic truncation error is bounded. The all-order statement applies to endpoint Taylor polynomials, not higher-order RK tableaux or stagewise randomized solvers.

## originality

PASS

Lam, Ceruti and Kressner introduce randomized low-rank Runge–Kutta with independently sampled, oversampled generalized Nyström projections applied stagewise, and prove moment bounds under their oversampling hypotheses. Nakatsukasa and Park already prove that indefinite standard Nyström approximation may be unstable; imaginary-axis RK stability polynomials are classical. The current claim is therefore NOT novel as a general warning about instability. Its surviving content is the exact tied-Gaussian 2×2 one-step error-tail constant, integrability frontier as a function of the RK endpoint polynomial, RK3/RK4 thresholds and four-periodic small-step sequence. These precise stochastic endpoint claims are neither the source's oversampled moment estimate nor its stagewise algorithm; indexed results did not provide a dominating special-case theorem. An equivalent heavy-tail ratio statement from older random-projection statistics remains a priority risk.

## value

PASS

The result isolates a sharp failure mode: the exact differential flow remains PSD rank one, yet conventional explicit RK endpoint truncation can become indefinite and a single unoversampled Gaussian compression then has infinite expected true one-step error, even for arbitrarily small h at orders congruent 1 or 2 mod4. The explicit tail constants, finite-order thresholds and tied-versus-independent sketch contrast are meaningful numerical-stability and randomized-linear-algebra diagnostics. It does not claim a general algorithm's global convergence or improve oversampled solver bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
