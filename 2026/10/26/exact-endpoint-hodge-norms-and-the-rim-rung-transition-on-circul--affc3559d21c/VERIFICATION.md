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

# Verification and limits

Run `python3 verify_prism.py` using Python 3 and the standard library. The program constructs the \(2n\)-vertex prism graphs, forms a grounded graph Laplacian, computes its exact-rational inverse, and tests all \(3n\) columns of the cut projection and its complement against the independently constructed inverse cyclic Green kernel. The observed output is:

```
PASS: sizes 3..18; all 504 edge columns; exact rational identities, orbit comparisons, cut dominance
```

These are finite checks at sixteen graph sizes, not proof of the all-size theorem. The accompanying analytical proof establishes the full integer parameter range, the orbit threshold, and the logarithmic asymptotics. No claim is made about optimality over arbitrary nonorthogonal projections. Independent scientific audit has not been performed.
