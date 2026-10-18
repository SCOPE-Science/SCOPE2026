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

The proof is analytic: a spectral-calculus maximum, a rank-two real quadratic-form computation, direct angular integration, and a one-variable Taylor expansion. The independent-looking numerical tests are **not** independent review or an infinite-proof certificate. To reproduce, run `python3 verify_pair.py` using Python 3.9 or later; no external packages are needed. The checker compares 12 specific two-point integrals with 32768-node midpoint quadrature, verifies three monotone sequences, and tests six small-angle asymptotic ratios. All 21 groups of diagnostics passed when run against the embedded script.

No outside paper PDFs, service accounts, or unpublished evidence are required to reproduce the exact formula. Normality is essential for the scalar spectral-calculus reduction. The source of the invariant has publication date 2026-10-04. No independent scientific audit has been performed.
