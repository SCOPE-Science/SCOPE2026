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

# Verification and limitations

The standalone Python verifier checks exact divisibility-function values and reconstructs prime factors from \(\sigma^*(m)/(c\sigma^{(e)}(m)-\sigma^*(m))\) for four prime thresholds through \(100000\). It reproduces the early equality values, including \(1,20,45,320,6615\). The exact run reports `VERIFY_OK`. It does **not** verify asymptotic Euler-product convergence for all integers; that follows from the paper proof using Rankin's bound and the classical Mertens prime-reciprocal estimate.

No external independent audit has been performed. The rate is an upper bound and the constant is not asserted optimal; infinitude of any fiber remains open.
