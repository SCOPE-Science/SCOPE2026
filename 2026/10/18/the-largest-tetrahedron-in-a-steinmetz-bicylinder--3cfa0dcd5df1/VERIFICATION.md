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

# Reproducibility and verification scope

The analytically decisive steps are the disk-hull affine equivalence, the multi-affine reduction of candidate vertices to generating circles, the determinant identity for two chords in perpendicular disk planes, the sharp one-variable cubic inequality, and the unique-support argument ruling out any other unrestricted equality cases. All appear in `RESULT.md` and are mathematical proof steps, not inferred from samples.

Run the standalone checker using `python verify.py` in the directory containing that file. At preparation, the checker completed successfully and reported `PASS: 6000 rational cases, 5000 contained tetrahedra, sharp equality and ratio`. The 6,000 rational configurations cover both the two-and-two and three-and-one circle splits (3,000 each), checking squared determinant inequalities with Python exact fractions. The 5,000 sampled interior tetrahedra are floating-point corroboration only. The equality realization and ratio are directly evaluated.

The checker does not exhaust continuous tetrahedron configurations; no independent audit or external formal proof assessment has been performed. Any independent assessment should rederive the determinant expansion and the final uniqueness argument rather than rely solely on the checker output.
