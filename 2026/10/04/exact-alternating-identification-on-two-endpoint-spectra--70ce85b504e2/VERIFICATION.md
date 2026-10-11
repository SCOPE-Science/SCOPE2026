---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

With alpha_1=1 and spectrum exactly {mu,1}, the first residual is (I-A)r_0=(1-mu)P_mu r_0, so the top eigenspace is annihilated. In the nontrivial branch all later residuals remain in the mu-eigenspace. If q_k is in [0,1-mu], then 1-mu(1+q_k) is at least (1-mu)^2>0, so the norm ratio is exactly q_{k+1}=1-mu-mu q_k and remains in the invariant interval. Solving this affine recurrence gives the stated fixed point, alternating error law, and convergence of alpha to 2/(1+mu), the minimax fixed GD step.

## originality

PASS

The complete current arXiv HTML defines the residual-ratio practical rule and proves bounds for it, while its exact geometric-contraction theorem concerns the spectral-radius oracle. The inspected l=1 theorem gives error bounds rather than the submitted two-endpoint equality and closed form. Fresh Resultary searches returned adjacent adaptive-step analyses, especially AdOGD endpoint-persistence counterexamples, but no result for this residual-ratio map.

## value

PASS

The two-endpoint spectrum is the canonical model behind optimal strongly-convex GD tuning, and endpoint annihilation is a structurally meaningful boundary case for adaptive identification. The exact alternating law explains how this residual-ratio rule still reconstructs the minimax step after the top mode disappears, contrasting with nearby adaptive estimators where endpoint loss can destroy identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
