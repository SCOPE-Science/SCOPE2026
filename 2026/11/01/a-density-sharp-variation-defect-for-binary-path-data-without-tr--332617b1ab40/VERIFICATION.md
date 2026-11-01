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

The proof is exact and applies to every finite path length; the finite checker is supplemental. Execute `python3 checks/path_binary.py` in the extracted package. It evaluates every nonconstant binary input with no triple consecutive zeros on lengths three through fourteen by rational arithmetic, checks the exact runwise defect and the ball-density equality condition, and verifies both the nine-vertex multi-gap equality example and the seven-vertex three-zero local boundary example. It does not provide exhaustive evidence for any larger length or any unrestricted binary variation conjecture.

The essential infinite-family proof steps are the complement-of-maximum identity, two-vertex endpoint ball correspondence, and the exact two-height variation formula. Independent review has not been performed.
