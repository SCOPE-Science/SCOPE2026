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

# Verification record

Run `python verify.py` with NumPy and SciPy. The program checks the exact scalar harmonic projection against the orthogonal Gaussian decomposition for reproducible seeded samples; compares sign probabilities to the Student cumulative distribution; integrates the exact density; checks the signed-tail constants by one-dimensional quadrature; and verifies a strictly positive conditional pole density after bounding the sketch norm.

The numerical program previously returned `PATHWISE_AND_DISTRIBUTION_CHECKS_PASS 1200039` for its internal assertions. Numerical samples do not establish tail equivalence or any infinite-moment assertion. Those are consequences of a positive analytic density at zero, proved in RESULT.md. The result does not claim independent validation.
