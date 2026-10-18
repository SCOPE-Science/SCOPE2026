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

# Reproducibility and boundaries

Run the included `verify.py` with a standard Python 3 interpreter:

```sh
python verify.py
```

The program performs exact Fraction-based Gaussian-rational arithmetic and checks sixteen nondegenerate points of the two-parameter family, the symbolic autocorrelation formula specialized at those points, the exact Gaussian-integer witness with autocorrelations \(15,-8,5,-2\), and the three-point equal-endpoint reflection scenario. No floating-point tolerance, numerical root solve, or outside package is required.

The mathematical proof independently establishes all parameters and all three-point supports. Finite tests are not a proof of the infinite quantifier. Originality was assessed against relevant literature without a claim to exhaustive bibliographic coverage. This package does not constitute independent validation.
