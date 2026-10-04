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

The exact verifier is `verify_conic_multiview_nonnormal.py` and uses symbolic arithmetic only.

It reconstructs the three \(2\times2\) minors of the published \(2\times3\) quadratic matrix. It then checks the two plane restrictions, the Jacobian-column collapse on each plane, one explicit singular point of Jacobian rank \(1\), one explicit double-line point of Jacobian rank \(2\), and rank \(3\) for the differential of the quadratic row map at that double-line point.

Expected terminal output begins with `VERIFY_OK`.

The verifier does not compute the full singular locus or a normalization ring; those are outside the claim.
