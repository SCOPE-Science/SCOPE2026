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

`verify.py` is a standalone standard-library Python checker. Execute `python3 verify.py` in the same directory. The expected last line is `CCA_PATH_VERIFY_OK` with a count of checked states. The test independently applies the three-color successor-contact rule on each labelled path, compares first all-equal times to height-maximizer covering radii, and checks the claimed diameter-end counts from explicit trinomial coefficients. It includes finite two-color infection-distance checks and exact rational variance checks; no stochastic numerical sample is used to certify an asymptotic theorem.

The proof for all lengths relies on the maximum evolution identity, reflection principle, a stationary one-dependent functional central limit theorem and Brownian uniqueness/arcsine distribution. Finite enumeration alone does not establish these infinite assertions. Independent validation has not been performed.
