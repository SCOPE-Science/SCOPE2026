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

# Verification and reproducibility

Run `python3 verify_signed_cycle.py` after extracting it from this package. It requires Python 3 standard libraries only. The deterministic program generates 56 separate small positive-definite inverse-Gram matrices, normalizes their inverse Gram diagonals to create unit-row systems, constructs a Cholesky row matrix, evaluates the proposed probabilities and semidefinite slack, and independently checks the slack eigenvalues, nullity, primal–dual objective, complementary slackness, and expected one-step worst-direction decrement. It compares randomly chosen competing probability distributions and dual-feasible planar correlation matrices. The actual run reported **3,060 assertion groups passed** across dimensions five through twelve.

These are finite floating-point comparisons with explicit tolerances, not an infinite or exact-arithmetic proof. The independent analytic path-energy and Dirichlet Schur-complement arguments in `RESULT.md` establish all dimensions and all admissible parameters. The theorem is limited to fixed iid row choices in square invertible normalized real systems with the stated inverse Gram. Independent mathematical audit has not been performed.
