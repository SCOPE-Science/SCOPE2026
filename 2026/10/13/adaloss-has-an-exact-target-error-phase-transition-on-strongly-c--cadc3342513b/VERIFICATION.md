---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The deterministic recurrence matches Algorithm 1, including the updated b in the gradient step. The assumption b_0>ηL keeps the modal factors in (0,1), so the gap is bounded above by its initial value. From b_k²≤b_0²+α(|ℓ⋆−c|+G_0)k one can take b_k≤M√k for k≥1 (rescaling M in the displayed bound), giving modal decay exp(−Ω(√t)) and a summable gap. At c=ℓ⋆ this first bounds b_∞, then yields geometric bounds and summable deviations of the multipliers from their positive limits, giving nonzero prefactors. For nonzero δ, the stated basin ensures a fixed sign in the overestimate case; the sum of signed gap increments converges, giving b_t²=Dt+B+o(1), D=αδ. Expanding the logarithm of the product, the inverse-b term gives 2√t/√D, the inverse-b² term gives (log t)/D, and the centered errors and cubic terms have convergent sums. This gives the stated signed modal prefactors and, after squaring, the objective-gap asymptotic dominated by the lowest active eigenvalue, also for repeated eigenvalues. No result outside the stated overestimate basin or for stochastic/nonquadratic objectives is needed. The finite check was inspected, not used as proof.

## originality

PASS

The algorithm and matched-target linear convergence class are prior work. The distinct content supported here is the persistent-error drift and sharp modal law for the endogenous loss-based accumulator, including its log-power correction and the comparison with exact targeting under the stated hypotheses. The inspected prior sources do not cover that claim.

## value

PASS

The target is an input to AdaLoss rather than a known physical constant. The result shows, with unchanged gradients and Hessian, when misspecifying it changes the convergence class and gives explicit sensitivity in the curvature and error, not just an iteration bound. The basin and SPD quadratic limitations keep the result a precise diagnostic rather than an unsupported general robustness claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
