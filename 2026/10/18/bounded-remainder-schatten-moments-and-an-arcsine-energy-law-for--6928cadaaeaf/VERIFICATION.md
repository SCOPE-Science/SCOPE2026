---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytic proof includes a fixed-coordinate integral comparison for the strict sign and a finite cube comparison for the explicit upper bound on the defect. Run `python3 CHECK.py` to check the strict sign and the bound by \(kc_k\) over exactly 49 small parameter pairs \(1\le n\le7\), \(2\le k\le8\), along with the Gram and first two trace identities. The rational replay does not check the logarithmic refinement or replace the all-parameter proof.
