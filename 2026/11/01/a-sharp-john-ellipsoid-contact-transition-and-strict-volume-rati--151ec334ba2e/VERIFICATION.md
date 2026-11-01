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

# Verification of the simplex-frustum John ellipsoid
The exact support-function identities and the scalar maximization are proved in `RESULT.md` for every integer dimension at least three and every truncation in the open interval. The accompanying `verify.py` is self-contained and uses only Python's standard library. Execute with `python verify.py`.

The program checks the coordinate facet supports, sum-direction supports, both active-set regimes, phase-boundary agreement, determinant optimum against sampled feasible radii, and the limiting normalized-volume constant for dimensions 3 through 15. It reports `SUPPORT_AND_CONTACT_PHASE_PASSED`, `AXIAL_GLOBAL_MAXIMUM_PASSED`, `STRICT_RELATIVE_VOLUME_GRID_AND_LIMIT_PASSED` and `ALL_CHECKS_PASSED` in its executed run. Numerical grid nonreversal uses a tolerance because very small theoretical increases are smaller than machine precision. Exact strictness for all reals is shown by the symmetric-exponent pairing argument in the proof.

No separate human review or independent mathematical audit has been performed. Historical-priority searches are incomplete. The finite computations cannot alone certify the infinite-dimensional-parameter theorem.
