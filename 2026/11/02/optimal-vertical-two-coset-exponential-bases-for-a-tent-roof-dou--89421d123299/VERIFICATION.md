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

# Verification and limits

Run `python3 verify.py` with Python 3 and no extra dependencies. The script exercises representatives of each of the three genuine fiber displacements, 2-by-2 Gram eigenvalue identities over sample offsets, a dense but finite grid around the proposed minimax solution, the four exact resonance locations and three quadratic coefficients. A successful run prints `CHECK_OK`.

The proof's continuum conclusions do **not** follow from finite grids; they follow from the unitary unfolding, the exact singular-value calculation, the three-interval trigonometric inequality, and the Taylor expansion in `RESULT.md`. No independent audit or human verification has been carried out.
