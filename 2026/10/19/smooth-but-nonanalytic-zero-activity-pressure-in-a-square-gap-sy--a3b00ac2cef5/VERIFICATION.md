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
# Reproduction and scope

Run `python3 verify.py` with Python 3 and `mpmath` installed. The code computes the normalization of the return-word pressure root by direct Gaussian sums, independently computes the Gaussian theta sum by Poisson duality, checks the marker frequency as a pressure derivative, and observes the predicted positive nonperturbative correction at four activities.

Actual output on the supplied code:

```
z=1: analytic_root=0.2476155676112764662; flat_correction=3.5740017e-18; ratio=0.737356097122
z=0.75: analytic_root=0.1789985547951768412; flat_correction=6.3701715e-25; ratio=0.7858276241
z=0.5: analytic_root=0.1058925637772993474; flat_correction=1.2014498e-41; ratio=0.852585633095
z=0.35: analytic_root=0.06261143591450929628; flat_correction=7.8591812e-70; ratio=0.902898035631
VERIFY_OK: 4 renewal normalizations; 4 Jacobi-dual checks; 4 pressure-density checks; 4 beyond-all-orders ratios; mixing gcd
```

The numerical calculations are finite, with explicitly chosen Gaussian tails and high precision. They cannot establish asymptotic equivalence, infinitely many derivatives, or originality. Those assertions require the analytic proof in `RESULT.md`. The independent audit channel remains unperformed.
