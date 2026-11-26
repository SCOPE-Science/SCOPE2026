---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof in `RESULT.md` is analytic. The key checks are that no residual Walsh support on four vertices can occur for lengths at least five, that the contributing five-vertex supports are exactly the undirected four-edge paths, and that orienting and extending one such path gives its exact coefficient. Parseval bounds all larger supports. The quantitative claims are not inferred from simulation or extrapolation; the frozen package's finite `verify.py` addresses the triangle projection and is not a verifier of the five-vertex theorem.
