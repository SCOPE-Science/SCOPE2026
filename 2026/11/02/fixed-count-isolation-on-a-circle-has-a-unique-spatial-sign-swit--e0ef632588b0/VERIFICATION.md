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

Run `python3 verify.py` from the extracted directory, using Python 3's standard library. The packaged checker completed 8,732 assertions: independent lifted-arc intersection computations; rational distance and radius threshold identities; multiple fixed-population covariance calculations; exact finite-grid iid-background enumeration with replacement; soft-kernel discrete convolutions; exact piecewise Simpson integration for the triangular kernel; and the sharp prevalence optimum. Numerical Poisson comparisons use only a positivity check with tolerance for floating-point subtraction. All algebraic comparisons needed for the proof are explicitly reproduced in the proof; finite enumerations do not certify continuum or infinite-parameter claims.

The verifier computes its results from this package's own code. No external certificate, independently audited proof, or computational claim about all real radii is asserted.
