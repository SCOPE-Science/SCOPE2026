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

## Reproducibility

Run `python CHECKER.py` using Python 3.9 or newer. The standard-library checker enumerates all finite-field projective points and contained lines over the field of four elements, computes the complete coordinate-permutation orbits and their incidence counts, and checks the crown graph. Its expected output is four PASS statements.

## Mathematical limits

The checker exhausts the *finite* field geometry. The assertion that these enumerated lines and points exhaust the algebraic closure follows separately from the smooth cubic surface's twenty-seven-line theorem and the tritangent-plane bound. Published Hermitian facts imply all finite-field points are Eckardt, which is also checked here by their three contained lines. No independent audit, external proof certification, or relative scheme computation was performed.
