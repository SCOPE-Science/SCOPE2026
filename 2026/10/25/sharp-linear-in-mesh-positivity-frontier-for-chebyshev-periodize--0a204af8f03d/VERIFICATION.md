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

The proof in `RESULT.md` establishes the infinite claim, including an exact discrete Fourier diagonalization and the strict positivity threshold. Numerical verification is supplemental.

To reproduce the 30 comparative experiments, install NumPy and SciPy for Python 3 and execute `python verification/check.py`. The script directly constructs the source kernel via its Bernoulli polynomial, evaluates the Chebyshev-periodization density integrals, and compares the solved weights with a wholly separate closed formula. Tested even mesh sizes were 4, 6, 8, 10 and 12, at six weight parameters for each size. Tests cover both sides of the critical threshold and the zero-weight boundary.

The tests are finite and approximate, and do not themselves prove the infinite theorem. The asymptotic expansion is analytic and is not inferred from finite mesh calculations. Comparisons with accessible primary sources inform originality but cannot exclude all unpublished or older mathematically equivalent treatments. No independent audit was performed.
