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

Run the embedded `verify.py` with Python, NumPy, SciPy and mpmath. The executed checks separately evaluate reset flips by time-domain Bessel sums and Legendre-function spectral values, verify the positivity and strict distance ordering, compare short-time coefficients and check large-separation prefactors. All programmed checks passed on the submitted code. This is numerical corroboration, not an exhaustive numerical proof of the infinite-volume theorem.

The analytic proof uses the exact renewal kernel, dominated convergence on a geometric spectral tail and Laplace's method on a half-integer Legendre integral. The short-time result holds for fixed positive integer \(a\); the large-distance result fixes both positive rates first. No experiment establishes claims beyond those limits.
