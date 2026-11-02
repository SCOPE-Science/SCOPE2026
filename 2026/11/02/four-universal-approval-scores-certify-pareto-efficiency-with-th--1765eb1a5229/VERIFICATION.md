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

# Verification record

Run `python3 verify_three_voter.py` in the directory containing this file. The script uses Python 3 standard-library components only. Observed output:

```
PASS 6561 exhaustive capacity profiles; 400 seeded higher-capacity profiles; checked 1620453 unique utility profiles
```

The checker enumerates candidate approval types and feasible committee count vectors, computes Pareto dominance by direct comparison of attainable integral utility vectors, and independently tests the four weighted-score maxima. It is not a complete enumeration of all candidate multiplicities and does not replace the universal symbolic proof. Positive-weight support and the hypersimplex convex-hull argument are proved in RESULT.md. No external independent review or certification is asserted.
