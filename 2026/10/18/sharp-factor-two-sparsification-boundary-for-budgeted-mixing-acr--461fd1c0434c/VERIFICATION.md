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

Run `python verify.py` with Python 3.9 or newer. The program requires no third-party packages and uses `fractions.Fraction` for exact arithmetic. It was executed successfully and reported `EXACT_CHECKS_OK` for all \(529\) pairs of integers \(2\le p,q\le24\).

The program recomputes the non-symmetric four-orbit quotient's characteristic polynomial by a permutation determinant (no floating-point diagonalization); it independently tests the claimed four factors, the exact budget-saturation identity, centered test-vector variance, nonzero hub/spoke eigenvalue equations, and the factor-two threshold. The proof for all integers \(p,q\ge2\) additionally follows from the exact symbolic factorization and elementary spectral decomposition presented in `RESULT.md`. Finite replay alone is not an infinite proof.

The result permits zero conductance on optional edges; strictly positive weights on every nominal graph edge are not asserted. No independent mathematical audit has been performed.
