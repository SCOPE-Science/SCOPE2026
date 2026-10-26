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

# Verification record

The pure-standard-library program `verify.py` was executed from its packaged source directory and returned `CHECK_OK: 1000 spectral identities + 2000 forward/inverse comparisons`. It independently diagonalizes the positive two-state absorption matrix to evaluate the first and second moments through a mixture of two exponentials. Reconstructed switching rates and contrasts were compared with the exact parameter inputs; conversely sampled moment pairs in the admissibility wedge returned physically allowed parameters and reproduced their target observables. These are finite numerical checks, **not** an infinite-domain proof; the universal assertions follow from the analytic eigenfunction reduction and exact algebra in `RESULT.md`.

The comparison with Chen et al. used accessible publisher full-text HTML; the comparison with Grebenkov (2019) used only accessible abstracts and metadata because the complete preprint and publisher article were not retrieved. Thus historical priority cannot be asserted exhaustively; see `AUDIT.json`. The independent audit channel has not been performed.
