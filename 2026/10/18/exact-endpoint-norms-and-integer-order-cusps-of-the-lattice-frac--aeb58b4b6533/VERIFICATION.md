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

# Reproducibility and limits

The self-contained `verify.py` uses Python 3 and `mpmath`. Run `python verify.py` in the directory containing this file and the checker. The expected completed output is `VERIFY_OK checks= 739`.

The checker independently integrates the defining Fourier symbol numerically, computes noninteger coefficients by recurrence, compares truncated absolute coefficient sums **plus an analytically evaluated infinite tail** to the finite closed norm, checks all-order signs across test parameter strips, tests exact central-binomial identities for integer powers, and probes one-sided integer-order slopes. The tail identity is applied only beyond the proven sign-change boundary. All numerical statements have high precision and explicit tolerances.

Proof of the infinite signed-kernel norm formula, the exact derivative jumps, the spectral-radius characterization, and the strong-convergence dichotomy is supplied in `RESULT.md`; finite checks alone do not establish these results. No independent mathematical or bibliographic validation is represented by this file.
