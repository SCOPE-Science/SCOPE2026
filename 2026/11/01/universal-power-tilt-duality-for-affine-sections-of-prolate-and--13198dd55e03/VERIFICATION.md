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

# Verification of spheroid section shape duality

The mathematical proof rests on an exact restriction of the two axial quadratic forms to a random section plane, on the invariant-hyperplane offset measure and on Jacobian transformations. The critical normalization is directional width; treating normals as unweighted after conditioning would give a different distribution.

Execute `python3 verify.py` using Python 3 standard library. The checker uses exact formulas to cross-check the two densities and their \((d+2)\)-moment normalization across dimensions 3, 4, 7 and 15, and multiple aspect ratios. It then independently samples random three-dimensional normals, accepts with support-width probability, draws permitted offsets and computes the section axis ratio from the restricted matrices. Finally it compares finite-dimensional total variation to its sharp high-dimensional limit. The observed terminal report was `ALL_CHECKS_PASSED`.

All infinite-dimensional convergence and uniqueness statements are justified by the analytic arguments in RESULT.md, not by Monte Carlo or a finite set of parameter evaluations. The random-draw checks are reproducible using a deterministic seed. The use of numerical tolerances is confined to independent consistency checks. Older ellipsoid stereology literature remains a historical-priority risk; no independent mathematical audit was performed.
