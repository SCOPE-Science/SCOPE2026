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

Analytic checks: strict concavity of logarithmic fitness in the germination decision; leave-one-out Jensen comparison of successive binomial sample means; endpoint derivatives and uniqueness; reciprocal-multiplier first-order identity; binomial concentration controlling all positive favorable-count outcomes; exact all-failure term and its asymptotic constant. Finite enumeration is not the proof of any claim quantified over all patch counts.

Run `python verification/check_seedbank.py` with Python 3 standard library. It performs exact rational derivative identity and monotonicity checks and arbitrary-precision root calculations up to 60 independent patches. The computations were executed successfully from the packaged program.

Scope limits: no density regulation, localized bank, patch dependence, fitness under finite-population extinction, or correlated weather. Independent audit: not performed. Bascompte et al. (2002) could be compared through its accessible abstract but not complete text; the closest 1987 joint dormancy-dispersal articles were only partly accessible. Theoretical originality remains subject to additional literature verification.
