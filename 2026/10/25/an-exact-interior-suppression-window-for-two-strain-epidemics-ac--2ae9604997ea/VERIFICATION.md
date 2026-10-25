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

# Reproducibility checks

The source of the formula is the two-type Poisson offspring matrix, followed by a direct characteristic-polynomial and second-derivative calculation. The proof in `RESULT.md` treats all positive parameters and every allocation in the specified domain; no computational enumeration stands in for this proof.

`verify.py` uses standard-library rational arithmetic to check the exact determinant polynomial and quadratic identities, and high-precision decimal calculations to confirm the example's endpoint/midpoint gap. It checks a deterministic collection of positive transmissibility tuples against the analytic optimizer identity and strict convexity implications. It is an error-finding reproducibility aid, not evidence that finite tests prove the parameter-uniform theorem.

The public claim is limited to the Poisson two-type branching reduction and the resulting threshold. It does not establish a finite-population epidemic-size law, uniqueness for arbitrary mutation matrices, or full prioritization against all mathematical literature. The source's supplementary material was not used as an unverified premise. Independent scientific validation has not been performed.
