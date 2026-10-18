---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Computational and analytic verification

Run `python3 check.py` using Python 3 with no additional packages. The checker evaluates the stated singular-face formula and, independently, the full Bernoulli-product coefficient kernel for positive exceptional-state probabilities. It verifies convergence toward the atomless row, the exact all-interval identity, and the first-order formula for 440 finite parameter families. The proofs of the exact infinite-dimensional endpoint norms, the joint Gaussian/Hermite limit, and the diffuse-dominated asymptotic rely on the measure decomposition, approximation by positive-measure rare events, Newton identities, and uniform second moments in RESULT.md, rather than on any finite test. The historical-novelty comparison is limited to the cited and inspected sources; no independent review has been performed.
