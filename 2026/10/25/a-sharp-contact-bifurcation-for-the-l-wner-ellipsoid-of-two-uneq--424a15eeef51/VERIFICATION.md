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

## Verification performed
The analytic proof checks both ball support functions, the exact square containment identity for the point-hull phase, the contact-radius condition, monotonicity and endpoints of the scalar root, the covariance identity for the two-orbit contact measure, and the global trace–determinant optimality certificate. The included `verify.py` independently evaluates representative parameter settings and asserts sampled support inequalities and the covariance relation.

## Scope of computation and uncertainty
Finite sampled directions cannot replace the for-all-directions support proof; numerical root finding does not establish uniqueness. The exact proof gives both. The numerical tests cover selected dimensions and unequal radius ratios only. Published-priority comparison was not independently audited. A plausible earlier 2006 general ellipsoid-hull algorithm paper was available in abstract form only; its complete text was inaccessible and remains a residual bibliographic risk.
