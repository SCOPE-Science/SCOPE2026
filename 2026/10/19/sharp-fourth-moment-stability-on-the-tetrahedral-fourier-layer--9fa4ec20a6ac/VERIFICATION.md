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

# Verification and reproducibility

The finite checker `verify_k4.py` was run with Python 3 and no third-party packages. It returned:

`PASS 5029 direct algebraic and finite-group comparisons, including 729 signed patterns`

The checker reconstructs ordered Fourier pair sums directly, compares them to the closed fourth-moment formula and the nonnegative deficit identity, checks normalized finite tori with moduli three and four, verifies all 729 signed ternary choices, and checks 100 independent random phase-factorization equalities. This tests the implementation and detects algebraic mistakes but does not replace the analytic proof for arbitrary complex coefficients.

The proof establishes the sharp constant and the equality family using orthogonality of exact character frequencies, arithmetic–geometric mean inequalities and equality analysis. Its scope is exactly four variables, quadratic square-free characters, Haar probability measure, and finite character orders at least three. Earlier equivalent published results might have escaped the bounded literature search.
