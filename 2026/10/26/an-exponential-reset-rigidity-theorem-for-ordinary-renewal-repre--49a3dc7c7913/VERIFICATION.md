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

# Reproduction and mathematical checks

The analytic claim uses the reset-count renewal identity, the standard iid-wait renewal-count transform, and an overlapping-interval affine-rigidity argument. Their assumptions and endpoint normalizations appear in `RESULT.md`.

Run `python verification.py` with Python 3, NumPy, and SciPy. The program reports 207 finite checks. It compares the transformed generating functions for positive and zero exponential reset rates, detects the failed iid-renewal factorization under deterministic resetting, and separately constructs a reset-walk generator and a permanently stopped-walk generator on finite lattice windows. It checks their one-time position distributions and distinct two-time covariance values.

The generator computations use bounded lattice windows and thus have a truncation error. Numerical agreement checks only the selected finite cases. The full if-and-only-if claim follows from transform uniqueness and does not rely on any finite enumeration or simulation. Time-averaged limits follow from a stationary Poisson-regeneration construction, integrability and the ergodic theorem; those infinite-horizon claims are not certified by the finite diagnostic program.

The self-review is passed; no independent validation has been performed.
