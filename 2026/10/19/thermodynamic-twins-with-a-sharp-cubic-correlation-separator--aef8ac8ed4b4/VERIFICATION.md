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

The standalone `verify.py` requires Python 3 and uses only the standard library. It executes 4,080 exact rational point-orbit coupling checks, 49 exact full-branch sharpness-witness checks, 16 exact polynomial-integral matrix entries and the polynomial-degree cancellation identities. It must print `VERIFICATION_OK` when complete.

Analytical proofs cover all real initial points and all natural-number observation horizons. No finite experiment can establish those universal statements; they are proved from explicit orbit formulas and affine full branches. Exact integrals are symbolic rational evaluations of the three specified affine formulas. Potentialwise pressure equality uses standard compact-system variational and entropy-of-iterate theorems, not an empirical surrogate.

The motivating preprint supplies the maps and iterate descriptions. Independent scientific review is not performed.
