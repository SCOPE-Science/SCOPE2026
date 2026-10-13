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

Run `python3 check_efron_constants.py` using Python 3.9 or later. The program uses the Python standard library. It enumerates all phase residues arising from cycle lengths at most six, uses the lower energy of a nonzero frequency to rule out unexamined active-coordinate counts, verifies the first five claimed constants numerically, and directly computes the cosine witness expectations for the displayed small cycles. It additionally tests the principal-angle inequality over finite grids and compares large-support finite witnesses to the theoretical bound.

The analytic certificate in `RESULT.md` is necessary for unrestricted supports and all coordinate counts: the finite scan, numerical root, grid checks and asymptotic illustrations are diagnostic checks and **not** exhaustive proofs of infinite statements. The exact small-support formulas follow from algebraic trigonometric identities in the proof. The asymptotic rests on the unimodality of \(\sin^2s/s\), the principal-angle cost inequality and matching directed-cycle constructions.

External independent audit: not performed.
