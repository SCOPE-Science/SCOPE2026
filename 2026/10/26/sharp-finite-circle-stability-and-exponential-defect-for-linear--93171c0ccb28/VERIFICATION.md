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

The analytical proof is in RESULT.md. The standalone `check.py` runs with the Python standard library, using exact rational elimination and a 75-digit Decimal cross-check of the inverse-row closed form.

Run `python check.py`. Its expected finite replay reports 1,722 successful assertions on meshes from 3 through 28 knots. These tests validate finite examples, cyclic inverse identities, signs, defect bounds and listed exact fractions; they do not replace the infinite-parameter proof or constitute independent certification.

The public bibliographic comparison covers three cited arXiv texts, including the periodic spline orthoprojection theorems. Independent validation and exhaustive historical priority verification are not performed.
