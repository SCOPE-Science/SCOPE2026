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
# Reproducibility and scope

Run `python3 check.py` with Python 3 and no external dependencies. The recorded successful execution printed `CHECK_OK F3_points=29511 block_residue_cases=11000+ examples=(5,8,11,14)`.

The checker exhaustively enumerates all points of `F_3^n` for `3 <= n <= 9` against the defining polynomial and gradient. It tests the two-block coefficient identity for `3 <= n <= 150`, several exact Hessian ranks, and the degree formulas for `n = 5, 8, 11, 14`. The proof for all algebraically closed characteristic-three fields and all `n >= 3` is in RESULT.md, and finite checks do not constitute proof of infinitely many cases.

The one-dimensional case classifies the reduced projective support and top-dimensional multiplicity, not embedded intersection schemes. No independent audit has been performed.
