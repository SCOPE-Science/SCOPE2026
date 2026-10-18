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

# Verification notes
The standalone `verify_quota_order.py` was run successfully in Python 3 with SymPy. It checks transfer determinants, the exact trace difference, the factorization of the difference of fixed-point quadratics, and the uniqueness-defining quadratic for a potential threshold tie. For the exact example it checks rational root isolations at the two endpoint quotas, positivity of the intermediate-season populations, the closed radical form of the unique candidate crossing, and its status as the smaller fixed point of both compositions.

The general proof is algebraic; checks at finitely many quota values do not establish it by enumeration. The one-switch statement is asserted only on connected intervals on which both lower thresholds are physically positive, simple roots of the respective two-step compositions. The inaccessible full text of a later related work remains an originality risk, not a correctness limitation. Independent validation has not been performed.
