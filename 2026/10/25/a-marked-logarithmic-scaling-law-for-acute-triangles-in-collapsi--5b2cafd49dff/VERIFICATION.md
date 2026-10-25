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

## Reproducing exact and numerical checks

Run `python3 verify.py` with Python 3 and its standard library only. The script checks rational antiderivative coefficients and normalization with Python's exact rational arithmetic, independently re-evaluates all three acute-angle dot products, and numerically integrates the resulting rare-event indicators by logarithmic importance sampling. A fixed random seed makes the numerical results reproducible. The sampling variable ranges over a larger interval than the limiting support; its Jacobian and its finite rectangle constraint are retained. At the two smallest tested heights it compares the conditional logarithmic-side mass with \(1/2\), and checks four values of the limiting vertical-height CDF.

The analytic proof does not use numerical threshold guessing. Critical ingredients are the exactly derived Jacobian, the compact-logarithmic-scale dominated-convergence theorem, the quantified tail bound, and the exact polynomial evaluation of both interval widths. Verification does not establish statistical error bars or a uniform asymptotic remainder.

## Limits of checks

Finite-height sampling cannot prove the limiting joint distribution or the absence of an earlier equivalent theorem. The remaining scientific priority risk is bibliographic, principally the unavailable full text of the earlier complete scalar rectangle probability calculation. The self-contained limit proof is in RESULT.md.
