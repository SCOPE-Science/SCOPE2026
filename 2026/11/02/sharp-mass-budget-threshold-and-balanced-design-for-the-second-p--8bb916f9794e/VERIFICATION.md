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

The proof in RESULT.md uses the infinite-chain resolvent, rather than finite sections, to establish the exact existence, optimization and band-edge asymptotic claims. Reproduce numerical diagnostics with `python verification/check.py` (Python 3, NumPy and SciPy). The checker compares the analytic Birman--Schwinger roots against largest eigenvalues of long, truncated mass-weighted chains; it tests the exact count inequality, balanced allocation of mass deficit and weak-mode onset. Finite domains and floating-point arithmetic cannot certify the infinite-chain theorem or historical originality; they are consistency tests. An independent scientific audit has not been performed.
