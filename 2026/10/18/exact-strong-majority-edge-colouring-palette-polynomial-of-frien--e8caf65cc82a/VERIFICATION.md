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
# Reproducible checks and proof limits

`verification/verify_friendship.py` implements the original graph-theoretic strong-majority predicate, starting only from the labelled edges and their endpoint intersections. Separately it implements the proposed universal-spoke-colour characterization and the symbolic closed count. Execute `python3 verification/verify_friendship.py`; its expected output is embedded in `verification/output.txt`.

The test covers exactly 834,518 labelled colour assignments over twelve parameter pairs, including all named palettes of sizes two through five across the documented small friendship graphs. The checker compares every assignment's original predicate to the proposed structural one, and all totals to the formula. There are no random or approximate computations, and no inaccessible package dependencies beyond Python 3's standard library.

The finite checker is not a proof for unrestricted graph size or palette; the structural necessity/sufficiency and inclusion-exclusion in `RESULT.md` establish the infinite claim. The check does not establish bibliographic originality or provide independent external mathematical validation.
