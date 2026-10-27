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

The standalone checker is `verify.py`, requiring only Python 3's standard library. Execute `python3 verify.py` from the directory containing this document and the script. The supplied execution reported:

```
PASS: 23097 exact-rational equalities and shape checks; four-person optimum checked.
The proof of the universal no-more-than-one-turn law is analytic, not by enumeration.
```

The checker independently constructs the finite polynomial from binomial counts, differentiates it, checks the analytical formula at rational points, and tests the derivative's sign against a reparameterized exact-power comparison. It verifies the minimum for four-person three-of-four adoption, its rational value, and the absence of two- or three-person reversals. It checks samples at group sizes two through ten, integer thresholds, seven rational active-type proportions, and twenty rational homophily values per parameter combination; it does not enumerate infinitely many real parameter choices.

The universal theorem depends on the displayed analytic identity for the binomial-tail derivative and the affine numerator of the logarithmic derivative. The finite-steepness persistence claim depends on coefficientwise, hence derivative-uniform, convergence of fixed-degree polynomials. No external audit or independent validation has been performed.
