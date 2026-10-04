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

The analytic proof uses no numerical approximation. Uniform tie-breaking is converted to continuous jitter, yielding the exact finite integral displayed in `RESULT.md`. The factorization is then an identity in \(p\) and \(\delta\), and positivity is checked on the full stated parameter interval.

`verify.py` independently reconstructs the probability from all \(3^4\) possible success-count configurations with exact rational tie probabilities and also from the jitter integral. It verifies equality, the centered factorization, and the endpoint expression for the positive factor. Exact rational spot checks are included.

The verification does not test or certify any claim for \(n\ge4\), larger balanced systems, or odd sample sizes. It does not remove the recorded originality risk caused by incomplete full-text access to close literature.
