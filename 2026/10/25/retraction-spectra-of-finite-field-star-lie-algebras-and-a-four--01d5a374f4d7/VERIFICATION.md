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

The standalone `verify.py` checks the quotient-projection classification over prime fields \(\mathbb F_2\) and \(\mathbb F_3\). It directly enumerates all central-lift solutions for the two-leaf cases, tests every map's Lie-homomorphism bracket equations and idempotence, and independently enumerates actual retract images for \(\mathbb F_2\) with two leaves. It also checks the three-leaf binary quotient-projection census. Compare its printed `VERIFY_OK` and `IMAGE_VERIFY_OK` messages against the stated finite examples.

These exhaustive finite cases cannot establish formulas for all \(q,m\); the general proof uses the bracket-kernel condition, projection decomposition, finite-field Grassmannian counts, and a dominated discrete-Gaussian limit. The independent audit remains unperformed.
