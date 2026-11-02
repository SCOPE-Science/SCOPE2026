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

Run `python3 verify.py` with Python 3. The standalone script uses exact rational arithmetic and reconstructs the two three-season products directly from the stated dispersal and habitat matrices. It checks their full characteristic polynomials, their squared row-sum vectors, a strict rational interval separation of the spectral radii, and a scaled profile giving multipliers on opposite sides of one, plus the directionally unbalanced migration cycle. It also checks every distinct two-season ordering among three displayed habitat profiles and symmetric migration examples up to six seasons. The mathematical theorem for arbitrary dimension and season count follows from the independent algebraic proof in RESULT.md; the finite checks are not offered as exhaustive verification over all matrices.

The exact row-sum inequality avoids reliance on floating-point eigenvalue estimates. No external formal or independent mathematical audit has been performed.
