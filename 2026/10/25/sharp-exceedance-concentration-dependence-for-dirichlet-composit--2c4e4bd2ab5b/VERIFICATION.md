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

The all-parameter sign classification follows from the conditional Dirichlet moment formula, strict convexity, and the beta-tail integral. The quadratic exact formula was independently differentiated against the centered integrand; the derivative identity reduced identically to zero symbolically. No extrapolation from a finite computation is used to establish a universal conclusion.

Run `python verify_exceedance_concentration.py` in a standard Python 3 environment; it uses only the standard library. It expands integer-parameter beta-tail integrals as exact rational polynomials, independently calculates their covariances, and compares them with the closed quadratic expression. The test run produced:

```
PASS: 888 exact rational beta-tail/covariance comparisons
PASS: symmetric q=2 transition and asymmetric n=3 boundary cases
PASS: sample higher-power q=3,4,5 positive-regime checks
```

The checks cover different dimensions, positive integer Dirichlet parameters, rational thresholds, and the three-component boundaries \((7,1,1)\) and \((8,1,1)\). A separate high-precision beta-tail quadrature at noninteger positive parameters and real powers \(q\in\{1.4,2.6,3.2\}\) matched the sign alternatives; those numerical examples do not establish uniqueness for all parameters.

Limitations: the checker tests finite parameter grids and integral identities for integer beta shapes. Its evidence is not an exhaustive numerical proof for continuous parameter ranges or real noninteger powers; those cases are established analytically in `RESULT.md`. Publication priority and independent validation are not certified by these computations.
