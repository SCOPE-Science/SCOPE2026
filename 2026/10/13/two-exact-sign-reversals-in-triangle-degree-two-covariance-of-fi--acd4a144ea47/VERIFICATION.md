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

The proof is self-contained in RESULT.md. From this directory run `python check.py` using Python 3.9 or later, with no third-party dependencies. The exact-rational checker uses `fractions.Fraction` for every covariance comparison and enumerates every labeled simple graph for \(4\le n\le6\). It separately checks selected polynomial signs and identities for \(6\le n\le200\), without regarding finite checks as universal proof. An actual run reported 34 exact enumeration cells, 2,136 exact polynomial evaluations and strictly positive quadratic leading coefficients across the checked grid. The identity for arbitrary \(n\) is established by conditional uniform-edge sampling; the sign classification is established by displayed exact polynomial factorizations. The asymptotic result uses the usual hypergeometric-to-Poisson limit and coefficient convergence, not a finite computation.

No independent audit has been performed. A broad mixed-moment or generating-function formula could implicitly encode the result; the mathematical claim of originality concerns the explicit full sign classification and its two limiting critical constants.
