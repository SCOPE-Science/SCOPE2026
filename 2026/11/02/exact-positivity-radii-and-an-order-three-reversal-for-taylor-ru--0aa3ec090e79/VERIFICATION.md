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

# Reproducibility and scientific limits

Run `python3 verify.py` with Python 3 and its standard library, with no additional packages. The verifier constructs the unit-weight graph Laplacian directly from each integer multipartition, evaluates the degree-two, degree-three and degree-four Taylor update matrices using exact rational arithmetic, and separately evaluates the three projector-entry formulas. It checks every matrix entry on all multipartitions of orders two through eight at three rational step sizes; 23,634 exact comparisons passed. It also compares thresholds against exact rational sign conditions and tests the extremal part profiles through order seventeen; 3,582 phase-transition checks passed. An independent numerical bisection of the positive cubic root gives `rho4: 2.785293563405282`.

The proof of the theorem, unlike these finite tests, holds for arbitrary positive integer part sizes. Its critical infinite-family calculations are the orthogonal projector decomposition, the strict positivity of the fourth-order stability polynomial, the negative discriminant for the fourth-order within-part quadratic, the strict decrease of the third-order polynomial, and the parity-separated inequalities for optimal partitions. The verification program does not test nonlinear systems, arbitrary graph families, nonuniform conductances or internal Runge–Kutta stage positivity.

The mathematical argument and priority comparison have undergone self-review only. Independent audit and independent validation have not been performed.
