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

The proof in `RESULT.md` establishes the exact distribution from a kernel-avoidance count, frame moments and Gaussian-binomial inversion; the field-size limit follows from leading powers of \(q\). Independently, `verify.py` enumerates all matrices of every rank over the six finite fields/dimensions \((q,n)=(2,2),(2,3),(2,4),(4,2),(4,3),(8,2)\), counts their nonzero idempotents directly, and checks every rank-stratum probability as an exact rational number. It also verifies rank-stratum population counts.

Command: `python verify.py` (Python 3 standard library only). Expected final line: `RANK_VERIFICATION_OK`. The computations are exhaustive for the listed finite configurations but do not prove the infinite-dimensional/field-size-parameter statements, whose proof is written in `RESULT.md`. No independent external mathematical audit has been performed.
