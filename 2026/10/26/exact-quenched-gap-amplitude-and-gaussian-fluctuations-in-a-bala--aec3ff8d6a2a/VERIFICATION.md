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

The exact finite-string identity was evaluated at three finite system sizes, comparing smallest singular values of the bidiagonal Bogoliubov matrix with the leading eigenvalue of the symmetrized discrete Green matrix. The stand-alone `verify_gap.py` reproduces that numerical consistency test and an independent simulated check of the predicted prefactor and Gaussian variance for uniformly distributed positive couplings. These computations do not establish the infinite-size theorem: the analytic verification is the operator-norm control of the atomic random-mass Green kernel, the simple-eigenvalue first variation, and the bounded weighted triangular-array central limit theorem in `RESULT.md`.

The proof concerns the lowest one-fermion gap, not the parity-preserving dynamical gap. Independent audit has not been performed.
