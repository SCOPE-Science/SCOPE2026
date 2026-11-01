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

# Reproducibility and mathematical limits

Run `python3 verify_q.py` (Python standard library only). The deterministic checker executed successfully with 83,568 supplementary finite assertions. It verifies the sharp affine bound on exact maximizing pairs, randomized admissible pairs in dimensions 2, 3, 5 and 9, and zero-valued constrained witnesses. These checks test selected finite-dimensional identities and edge cases, not all possible matrices or infinite-dimensional vectors.

The infinite-dimensional compact case follows from the Takagi spectral representation and the Ky Fan maximum principle in `RESULT.md`. The continuity argument establishes the interior of the disk, and the equality argument proves the strict-gap rigidity. No independent audit is claimed.
