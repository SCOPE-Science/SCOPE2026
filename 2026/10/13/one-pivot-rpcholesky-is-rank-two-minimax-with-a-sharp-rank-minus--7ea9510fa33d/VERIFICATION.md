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

`verify.py` uses Python standard-library exact rational arithmetic on actual finite positive-semidefinite Gram matrices and diagonal examples. It reconstructs the pivoted Schur residual, the diagonal-proportional expected residual, and the two-eigenvalue scalarization in rank two. It checks the exact water-filling optimum for diagonal kernels and the sharp rank-dependent ratio on an expanding family of rational examples.

These finite checks are transcription and computation verification only. All-rank correctness rests on the symbolic eigenbasis simplex argument, pairwise harmonic lower bounds, and exact diagonal sharpness proof in `RESULT.md`. No external or independent audit has been performed.
