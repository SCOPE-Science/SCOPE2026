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

The attached `verify.py` constructs each graph explicitly and implements ordinary color refinement from the uniform coloring.

It checks every \(2\le p,q\le20\) and \(1\le L\le40\). For each parameter triple it verifies both the exact stabilization-depth formula and equality of the stable partition with the explicit automorphism-orbit partition.

The checker returns:

`VERIFY_OK depth_checks=14440 orbit_checks=14440 p,q=2..20 L=1..40`

These finite checks are corroborative only. They do not replace the all-parameter propagation proof in `RESULT.md`.
