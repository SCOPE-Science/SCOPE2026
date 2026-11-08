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

The included `verify_density.py` requires Python 3.10 or newer and no external dependencies. Run `python verify_density.py` from the directory containing the source. The code recomputes all finite prime and prime-exponent states rather than reading an unverified table.

Expected terminal evidence from the saved script:

```
VERIFY_OK
primes=96, largest=503
lower_score_mass=771520086457799875/1000000000000000000
additional_equal_cylinders=2; disjoint_shift=-1
certified_density_lower_bound_gt=0.7764
rational_lower_bound_decimal_approx=0.776432356352
```

## Meaning of the certificate

For each rational local divisor-sum ratio, a twenty-term series and a rational tail estimate bound its logarithm from below. The dynamic-programming bins store scaled probability lower bounds. Each update uses integer floor division by the exact prime-exponent probability denominator; truncation is non-renormalizing. The final lower bound combines the retained bin weight, two separately checked equality cylinders, and the analytic squarefree-tail inequality.

The decimal display is illustrative; the final comparison with \(1941/2500\) uses exact fractions. The check does not numerically establish the infinite existence of a natural density, prove that the stated lower bound is optimal, or replace the theoretical density argument.
