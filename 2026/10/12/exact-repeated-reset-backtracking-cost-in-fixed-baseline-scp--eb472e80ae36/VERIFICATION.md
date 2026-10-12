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

The symbolic proof establishes the general claim. The companion `verify.py` checks one representative instance directly from the stated algorithmic formulas. It verifies the exact rejection pattern, accepted step size, contraction factor, stopping index, total proximal-subproblem count, box containment, and strict inactivity of the constraint.

The computation does not certify any claim beyond the stated scalar family, and finite execution is not used to justify the general algebraic identities. The warm-start comparison is evaluated only for the same family and is not a convergence claim for a modified algorithm.
