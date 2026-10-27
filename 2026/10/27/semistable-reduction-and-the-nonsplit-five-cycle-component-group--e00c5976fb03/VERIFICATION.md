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
# Computational verification

Execute `python3 verify.py` using a stock Python 3 interpreter; no downloads are needed. The program builds \(\mathbb F_4\) and the five-coordinate Segre parametrization, checks the exact cubic factorization, verifies that the five component intersections are distinct, and computes the elementary-symmetric local polynomial identities. It also checks the dual graph, component-group order five and Frobenius-fixed subgroup order one.

The finite computations are checks of explicit finite algebra, not a substitute for the regularity argument in `RESULT.md`, the semistable Néron component-group theorem, or historical priority evaluation. Independent audit remains unperformed.
