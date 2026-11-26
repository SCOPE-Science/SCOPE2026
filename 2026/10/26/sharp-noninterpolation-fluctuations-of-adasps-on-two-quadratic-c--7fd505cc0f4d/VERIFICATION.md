---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For independent fair signs, zero component lower bounds, x₀=0, η₋₁=∞ and fixed c≥1, the loss-to-gradient-square ratio is 1/2 and S_t increases; η_t=1/(2c√S_t)<1 then preserves the open interval by convexity. In S_{t−1}=t/2+½Σx_s²−Σx_sξ_s, the last sum is a bounded-difference martingale, hence P(S_{t−1}<t/4)≤exp(−t/32). The true gain is not predictable. Lagging S_t by one step makes the gain predictable, with an L¹ change O(t^−3/2) by the good event and the increment bound 2. The lagged gain lies in (0,1) and is at least d/√t by S_{t−1}≤2t. Conditional expansion of squares and fourth powers gives successive contractions 1−d/√t with forcing O(t^−1) and O(t^−3/2); for the fourth moment use O(t^−1) times the already controlled second moment on the good event plus an exponential tail. This gives E x_t²=O(t^−1/2) and E x_t⁴=O(t^−1). Markov on dyadic times and monotonicity imply the Cesàro mean of x_t² vanishes almost surely; the martingale average also vanishes. Thus S_t/(t+1)→1/2 and √(t+1)η_t→γ. In L² the loss remainder is even O(√t) by summing ∥x_s²∥₂ and using martingale orthogonality. The inverse-root Lipschitz bound on the good event gives ∥η_t−γ/√(t+1)∥₂=O(t^−1). Coupling to the deterministic-gain process on the same signs, the propagated error has exponentially small old weights and a recent window with geometrically summable mass O(√n), giving ∥x_n−z_n∥₂=O(n^−1/2), sufficient to transfer both limits. For the deterministic process, V_{n+1}=(1−a_n)²V_n+a_n²; √(n+1)V_{n+1}−γ/2 contracts the preceding scaled error by 1−2γ/√(n+1)+O(n^−1), with residual O(n^−1), so tends to zero. The coefficients of n^{1/4}z_n tend uniformly to zero (old weights exponentially small, new ones O(n^−1/4)); bounded-sign Lindeberg gives the asserted normal law. The objective gap is x_n²/2, yielding γ/4. The proof confirms the limits rather than extrapolating from samples.

## originality

PASS

The supported distinct claim is the exact fluctuation law and positive expected-risk coefficient for the original sample-dependent cumulative-loss AdaSPS on this fixed instance, together with its self-normalization. The strongest inspected sources give rate upper bounds, stationary laws for other SPS rules, or fluctuation results for prescribed gains. They do not identify the AdaSPS gain and control its sample dependence to the precision needed here. This is a bounded best-of-knowledge comparison, not a priority certificate.

## value

PASS

This is a simple noninterpolating optimization problem with valid lower bounds and the unmodified algorithm. Its positive γ/4 identifies an actual instance that realizes the known error order for the last iterate, and the Gaussian law distinguishes quantitative fluctuations from a rate bound. The gain analysis is necessary: this witness cannot be obtained by merely prescribing a deterministic decay schedule or computing a stationary variance. The exact coefficient is useful for comparisons of last-iterate rates and scales without claiming general minimax optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
