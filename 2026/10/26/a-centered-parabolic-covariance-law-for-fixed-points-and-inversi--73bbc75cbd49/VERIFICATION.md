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

# Reproduction checks and limitations
Run `python verify.py` with a standard Python 3 interpreter. The checker uses only Python standard-library exact rational arithmetic. Exact weighted enumeration covers every permutation for sizes 3 through 8 at five values of the Ewens parameter, all fixed indices, and their full inversion counts. It verifies the scalar mean, the specified-index conditional law, and the exact parabolic covariance. Additional exact-rational rational-identity and sign checks cover sizes through 150, while the asymptotic radius is spot-checked numerically at larger sizes. The proof in `RESULT.md`, not enumeration, establishes the unrestricted integer-size and positive-real-parameter statements. No independently performed audit or validation is claimed.
