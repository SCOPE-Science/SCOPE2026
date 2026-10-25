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

The main proof is analytic. Direct independent quadrature of the mixed-disk determinant coefficient produced 13.3727800199277, while the hypergeometric expression produced 13.3727795244994. Polyhedral inner approximations using 12, 20, and 28 vertices per disk increased toward the analytic target 51.0718913675769 for equal disks; three radius triples were tested, and nine relative deficits were below five percent. The checker asserts the inner-hull volume does not exceed the claimed continuous-disk volume and confirms strict anisotropy excess for two unequal boxes. Exact algebra, not these finitely many checks, establishes all quantifiers. Run `python verify_volume.py` after installing `requirements.txt`. Independent audit: not performed.
