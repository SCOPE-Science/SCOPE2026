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

# Reproducibility and verification

The supplied `verify.py` implements the complete independent-threshold probability space in exact arithmetic. Run `python verify.py` with Python 3 and SymPy available. Its output on the supplied package was:

```
PASS: 348 exact assertions; 240 threshold assignments checked twice
Critical p = 1 - sqrt(2)/2 ~ 0.2928932188134525
```

For every two-seed subset, the program independently computes the least stable active closure by synchronous iteration and by intersection of all stable supersets, enumerates all sixteen remaining-node threshold assignments, and checks coefficients and all four algebraic comparisons. Polynomial factorizations provide analytic signs throughout the open unit interval. An exact integer enumeration over 240 assignments is complete for this specifically stated finite model; it is not a claim about larger networks or different threshold laws. No independent external audit has been undertaken.
