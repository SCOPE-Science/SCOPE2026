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

# Verification of the affine-uniform ellipse acuteness law

The exact law is proved by integrating the signed difference of two independent uniform semicircle chord directions. A separate Taylor-series calculation confirms the dilogarithm identity. All right-angle boundary configurations have probability zero for nondegenerate ellipses.

`python checker.py` performs deterministic Simpson quadrature comparisons at six axis ratios and direct random-coordinate Euclidean tests at five axis ratios (85,000 triples each), as well as endpoint and asymptotic diagnostics. The actual run returned `ALL_CHECKS_PASSED`.

These tests support arithmetic and normalization but do not independently certify analytic limits, originality, or mathematical value. The main proof is self-contained modulo classical integral and dilogarithm identities. No external or independent audit was conducted.
