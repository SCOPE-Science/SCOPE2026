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

# Verification

Run `python3 verify.py` after extracting the package files into one directory. The successful program prints `VERIFY_OK`; it uses only standard Python and exact mod-three arithmetic.

The calculation verifies the quadratic residue-field relations, node residue agreements, Frobenius conjugation, and the three-pole divisor of each function. The absence of other degree-three pencils follows mathematically from the intersection number two of the two theta translates. No finite enumeration is treated as proof of this infinite-field classification.

The source-defined nodal curve and the degree convention are precisely specified in `RESULT.md`. The published source establishes the two-node construction and the ground-field gonality. Independent external validation has not been performed.
