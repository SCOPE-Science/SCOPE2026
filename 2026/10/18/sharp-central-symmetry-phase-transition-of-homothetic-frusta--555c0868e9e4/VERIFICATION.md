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

Run `python3 verify.py` using Python 3 with only its standard library. The script prints `VERIFY_OK` and an integration error on success. It checks the all-dimensional formula on a finite parameter grid, both sides of the optimizer switch, and nonaxial planar translated-slice intersections by independent Simpson integration. It has no external data files, network dependencies, or elevated execution requirements.

**What the checker does not establish:** Finite grids do not certify continuity in the shape parameter or infinitely many dimensions; the proof in `RESULT.md` supplies exact formulas, quantifier coverage, axial optimality, and uniqueness. A small numerical discrepancy is not a uniqueness proof; the exact inequality at the central horizontal slice establishes that strict condition. External independent scientific audit has not been performed.
