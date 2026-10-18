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

From the extracted directory run `python verify_mixed_volterra.py` after installing `sympy` as specified in `requirements.txt`. The exact program returned `MIXED_VOLTERRA_EXACT_OK 159 checks`. Checks reconstruct the moment action in the polynomial basis for orders 1 through 12, verify the Hilbert and coefficient matrix identities, full rank, determinant product, trace, exact Hilbert--Schmidt norm and parity, and integrate monomial test inputs up to degree five for orders through eight. No data files or network connections are needed.

# Proof boundary

The code checks finitely many cases. Universal rank and signed inertia are proved by polynomial-moment factorization; infinite-rank singular asymptotics and Schatten thresholds are proved by Fourier finite-rank interlacing. The code does not claim exhaustive high-order enumeration or certify literary priority.
