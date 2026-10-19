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
# Computational verification and limits

Run `python3 verify_zak.py` using the standard Python library. `verification_output.txt` records an actual execution of the delivered checker. The independent finite checks directly compare truncated defining Zak sums with rational formulas, centered finite-difference Jacobians with the exact expression, two equivalent positive formulas for the area coefficient, small-level polar area with its quadratic prediction, and representative parameters on each side of the local transition and in the large-rate limit.

The real two-dimensional inverse-function calculation and all-parametric optimization statements are analytical proofs given in RESULT.md. Finite numerical sampling does not certify a universal theorem, a global uniqueness statement, the literature novelty, or independent auditing. In particular, the polar-area approximation is a numerical consistency test rather than exhaustive integration at every rate.
