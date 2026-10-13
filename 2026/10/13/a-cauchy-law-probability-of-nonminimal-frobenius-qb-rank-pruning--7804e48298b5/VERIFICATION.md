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

# Verification notes
The theorem follows from the explicit Gaussian QR angle, the standard-Cauchy quotient, an exact two-dimensional chi-square tail, and the singular values of the diagonal input. Those are the infinite-probability and rank-optimality arguments; finite tests do not replace them.

Run `python3 verify.py` from the package directory with Python 3.9 or later. The standalone program verifies rational identities for the two row energies and their threshold comparison, compares exact arctangent mass to an independently evaluated angular integral, checks convergence for several shape parameters, and directly samples both the QR over-retention event and initial acceptance event for 180,000 independent Gaussian blocks. Its simulation tolerance is much broader than the expected sampling error; it is only a supplementary diagnostic.

No independent audit or external certification has been performed. No claim is made about finite-precision QR rank detection or other sketch distributions.
