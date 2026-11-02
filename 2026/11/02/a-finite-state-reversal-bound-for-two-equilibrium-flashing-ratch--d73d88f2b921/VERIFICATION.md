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

Run `python checker.py` with Python 3.9 or newer. The checker uses the standard library only and performs exact rational arithmetic, not floating-point tolerance comparisons.

It reconstructs two detailed-balance generators from vertex equilibrium weights and undirected edge conductances; builds the full generator on both environmental phases; solves the normalized stationary equation; evaluates the reduced resolvent; and checks equality of the resulting oriented edge currents. It also tests the flat-phase triangle example against its explicit rational current at 39 switching rates, including the root, and checks the polynomial-degree identity in four- and five-vertex rings.

Observed output from an actual execution of the embedded checker before packaging:

```
PASS: exact stationary current vs reduced two-dimensional formula: 759 comparisons
PASS: sharp flat-phase reversal at rate 9/8; strict positive denominators
PASS: generic ring sizes 4 and 5, exact reduction, determinant, polynomial-degree: 275 comparisons
```

The tests are finite. The all-\(n\) statement rests on the zero-mass-space proof and the adjugate degree bound in `RESULT.md`, not on extrapolation from enumeration. Historical priority and independent validation are not certified.
