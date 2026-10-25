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

# Reproducibility

Run `python3 verify.py` using only the Python standard library. The verified output is `VERIFY_OK 1025 exact identities; enumerated 3548 wheel spanning trees`.

The code calculates grounded Laplacian inverses over exact rational numbers; constructs the transfer-current kernel and covariance; checks symmetry and the analytical adjacent polynomial identity; and exhaustively enumerates spanning trees for wheel rim sizes three through eight. It also checks exact covariance signs for rim sizes three through fifteen. Tests for sizes below five exercise the algebraic engine, but the published non-real-stability contrast and central theorem cover rim size at least five.

The finite computations are consistency checks. Non-real-stability uses the published distance-hereditary classification, and the all-size covariance statement uses the proof in `RESULT.md`. Independent audit has not been performed.
