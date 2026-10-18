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

# Verification record

The standalone `checker.py` was executed from the newly packaged file bytes and checked the following against independently intersected box edges: 5 shapes, 250,000 randomly sampled planes each, all four polygon types, normal width-weighting, exact sum-to-one and expected-vertex identities, and the known cube specialization. Its successful output begins with `AFFINE_BOX_SECTION_LAW_OK` and reports 1,250,000 independent edge-count checks. The code is an empirical test suite, not an infinite proof.

A separate arbitrary-precision evaluation checked the stated quadratic flattening coefficient at several shrinking positive widths. The analytical proofs of the complete probability law and the limit are in `RESULT.md`, with all quantifiers and assumptions explicit. No external independent scientific audit or formal proof assistant certificate was obtained.
