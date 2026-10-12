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

# Reproducibility

Run `python3 verify.py`. Its direct enumerations check ordered triples over \(\mathbb F_2\) and \(\mathbb F_3\) in dimension two and ordered compatible outer-factor pairs over \(\mathbb F_2\) in dimension three, without assuming the closed formula. Separate exact-integer identities compare total fiber mass to the number of zero-product pairs in dimensions two through five. A successful run ends with `VERIFY_OK`.

The field-wide and size-wide theorem is proved by image/kernel subspace counting and the rank-\(ab\) intermediate-map lemma. The verification script does not constitute a proof for untested prime powers or dimensions. Independently audited validation has not been performed.
