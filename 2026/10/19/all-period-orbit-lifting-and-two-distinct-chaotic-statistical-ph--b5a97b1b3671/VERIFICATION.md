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

The standalone script `verify_signed_logistic.py` uses `fractions.Fraction` only. It evaluates each of the \(2^n\) inverse branches of the full tent map at every \(1\le n\le12\); verifies each exact rational solution of the inverse-branch fixed-point equation; iterates it forward exactly; and checks branch-unique fixed-point counts and the signed count formulas. It reports PASS only after every assertion succeeds. The numerical range does not certify a universal theorem; the analytic orbit-lifting and tent-branch arguments establish the all-period claims.

To reproduce: `python3 verify_signed_logistic.py` (standard-library Python only). The script is complete and has no external data dependencies. The transformed density integrates exactly to one by the classical beta integral. No independent review or audit is asserted.
