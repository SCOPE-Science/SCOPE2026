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

# Reproducibility and evidence boundaries

Run `python verify.py` with NumPy to reproduce the finite numerical checks. The program constructs the inverse branches directly from the square-root equation and iterates the transfer operator on a fine regular grid. It checks normalization, vanishing endpoint values to grid tolerance, the dyadic profile relation, and measured-vs-predicted endpoint profiles for two finite parameters. Finite iteration and interpolation cannot verify uniform convergence as the parameter approaches the tent-map endpoint or any infinite-dimensional norm claim.

The analytical justification is in the proof of `RESULT.md`: a uniform two-iterate bounded-variation inequality and compactness, uniqueness of tent-map invariant density, interior uniform convergence from iterative contraction, and a dominated inverse-branch series for the second endpoint. The endpoint trace relations can be verified exactly by differentiating the explicit inverse Jacobian. The \(W^{2,1}\) existence/uniqueness for each fixed cusp parameter is supplied by the cited primary literature. No independent external audit was performed.
