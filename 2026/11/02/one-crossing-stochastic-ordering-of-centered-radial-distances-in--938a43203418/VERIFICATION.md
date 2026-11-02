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

# Reproduction

Run `python3 check.py` with standard Python 3. The script independently integrates polar-sector CDFs numerically, checks the expected radial-density signs, the unique crossing, the squared-distance geometric parameters, and transport-gap reductions on finite numerical grids. It reports 75,384 passing deterministic comparisons, including the square-versus-hexagon case.

This finite computation is only a diagnostic. The universal all-integer claim follows analytically from elementary monotonicity and the strict sign of the crossing derivative, as written in `RESULT.md`; no experiment was treated as an infinite proof. The report does not certify worldwide originality or independent verification.
