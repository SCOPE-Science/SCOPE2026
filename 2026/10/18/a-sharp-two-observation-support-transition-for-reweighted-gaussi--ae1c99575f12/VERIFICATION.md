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

# Verification details

Execute `python3 verify.py` in the directory containing these files. The standalone standard-library checker runs 29,849 deterministic numerical assertions on the critical contact, the nonzero second contact for unequal weights, derivatives, curvature signs, and a grid of subcritical sensitivity values. It also checks that adding a tiny second atom increases the weighted likelihood in supercritical examples.

These finite checks are diagnostics, **not** a proof for all weights, supports or separations. The essential all-real-argument moment-generating-function inequality and its unique nonzero equality point are Theorem 1.1 in E. Schlemm, arXiv:1405.4496v1; the remainder is proved analytically in `RESULT.md`. The full relevant source texts were inspected for the scientific comparison. No independently produced audit is asserted.
