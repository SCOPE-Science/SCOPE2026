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
# Verification

The proof is an exact finite-dimensional argument. To repeat the finite arithmetic checks, run `python check_certificate.py` with Python 3 and no external packages. It checks all twelve orbit witnesses and the barycenter exactly using `fractions.Fraction`; it also checks every oriented molecular distance and the positive forced-mass bound.

Proof steps not delegated to code: identification of the six-point free norm, the vertex structure of its unit ball, the fact that a slice containing a convex barycenter contains at least one term, the exposure-based Daugavet upper bound, and the transportation-marginal constraint. These follow from the definitions and are explicitly established in `RESULT.md`.

The exact pointwise \(\Delta\)-constant, the smallest metric cardinality admitting this phenomenon, and uniqueness against unindexed literature were not established. No independent audit or independent validation has been performed.
