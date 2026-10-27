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

# Reproduction and boundaries

Running `python3 verify.py` in this directory (standard Python only) prints `VERIFY_OK product_cases= 2658  toric_minors=checked free_last_rows=checked nonclosure_witness=checked` on successful exact-arithmetic checks. The tests enumerate 2,658 finite products of operators in dimensions 3–7, multiple obstruction thresholds and lengths up to five, all pertinent minors, and constructive choices of the arbitrary final row. They also test a concrete nonlocal product. They are finite checks only.

The proof in `RESULT.md` establishes the general matrix-product identity, algebraic density, full determinantal ideal, component number, intersections and dimensions. The published local-operator theorem is a stated and checked hypothesis; no theorem here classifies local operators independently of that literature. The result is restricted to complex reduced-normal-form maximal-nilindex evolution algebras in characteristic zero. No independent review has been performed.
