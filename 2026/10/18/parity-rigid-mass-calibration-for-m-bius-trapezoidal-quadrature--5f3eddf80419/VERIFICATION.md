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

`python verify.py` uses Python 3 plus SymPy and mpmath. At 90-decimal-digit precision it compares the directly evaluated circle-node quadrature with the rational aliasing formula in 180 parameter settings, and runs 20 symbolic derivatives/factorizations, 43 parity checks, 28 two-scale extremal tests, and six asymptotic-displacement comparisons. Output: `VERIFIED {'direct_circle_matches': 180, 'convexity_identities': 20, 'parity_classifications': 43, 'two_scale_extrema': 28, 'asymptotic_ratios': 6} TOTAL 277`.

The correctness of the infinite classification comes from the full argument in `RESULT.md`. Finite parameter tests do not establish monotonicity, convexity, or asymptotics; the derivative factorization and its positive lower bound do. Floating-point comparisons do not certify publication priority or numerical conditioning in machine arithmetic. The endpoint at the point at infinity is evaluated via the finite analytic limit, not literal substitution into the singular map.
