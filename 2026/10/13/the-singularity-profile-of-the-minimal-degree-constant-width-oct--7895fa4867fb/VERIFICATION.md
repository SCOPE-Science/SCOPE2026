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

The exact checker in `artifacts/verify.py` verifies the source parametrization against the homogeneous octic equation, checks that the coordinate forms have no common factor, checks the tangent-slope identity used for birationality, verifies the reciprocal-node polynomial certificate, reconstructs the local valuation pairs \((3,4)\) and \((2,7)\), and checks that the delta contributions sum to the octic arithmetic genus \(21\).

The verifier uses only the Python standard library. Its successful replay from the extracted package prints `VERIFY_OK`.

The checker does not attempt a global literature search or an independent audit. The originality conclusion is based on the source inspections and searches recorded in `AUDIT.json`.
