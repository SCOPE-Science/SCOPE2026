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

The accompanying `verification/check.py` runs using the Python 3 standard library only. Run `python3 verification/check.py` from the extracted finding root. It uses `fractions.Fraction` for every cost, payment and residual balance, with no floating-point tolerance.

Observed output:

```
VERIFY_OK support_pairs= 2547 fully_funded_cost_profiles= 383958 laminar_pairs= 1269 crossing_pairs= 1278 crossing_constructed_witnesses= 1278
WITNESS_OK (Fraction(2, 5), Fraction(0, 1), Fraction(1, 5)) (Fraction(1, 5), Fraction(0, 1), Fraction(2, 5)) third_project_cost=3/10
```

The checker compares all distinct nonempty supporter pairs with up to six voters, and a bounded rational grid of positive project costs, rejecting profiles when either order is not fully financed. The checker also constructs a witness for every crossing pair on these finite sizes. It verifies a three-voter example where an optional single-support project is affordable after only one preallocation order.

The analytical argument is necessary to cover arbitrarily many voters and arbitrary positive real costs. The proof of the rebalancing step uses equality between the aggregate endowment and the available budget plus paid project costs. The crossing construction requires positive intersection and both nonempty exclusive regions, guaranteeing a nonempty parameter interval. If mandatory-project costs cannot be financed completely in either order, the claim does not apply. Neither the checker nor these notes certify originality or constitute independent scientific validation.
