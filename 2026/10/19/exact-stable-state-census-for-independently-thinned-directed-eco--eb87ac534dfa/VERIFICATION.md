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

The accompanying `verify.py` enumerates directed edge patterns, possible nonnegative equilibrium supports and full Jacobian eigenvalues for sizes 3 through 7, at four noncritical inhibition strengths. The 992 graph-parameter comparisons passed; the independent survivor-richness probability sum passed for sizes 3 through 11 and probabilities 0.2, 0.5, and 0.8. It requires NumPy.

The infinite-size proof is in `RESULT.md`: scalar triangular reduction for broken cycles, Fourier diagonalization for intact coexistence, transverse invasion tests for boundary states, and an elementary geometric-series average over independent edge deletions. Numeric checks do not prove the theorem at arbitrary size. The exact critical coupling values and other ecological networks remain outside scope.
