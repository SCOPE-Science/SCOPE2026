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

Run `python verify.py` using Python 3.11 or newer. The dependency-free verifier enumerates all partitions through \(n=18\), checks 513 simultaneous multiplicity-survival identities, verifies 19 marked-part expectation identities, computes four exact-partition-count expectation diagnostics through \(n=1200\), and tests four Gamma-versus-finite-product values. The last group approximates the infinite transform but does not certify an infinite product by computation.

The proof separately derives all infinite claims using Hardy–Ramanujan, Erdős–Lehner, a global partition-ratio inequality, uniform weighted-tail bounds, and Slutsky. No independent validation has been performed; no finite computation proves an infinite weak limit or the external classical theorems.
