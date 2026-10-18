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

# Reproducible mathematical checks

Execute `python verify_b_parking_inball.py` with Python 3 and its standard library. The script evaluates exact integer support extrema by enumerating vertex permutations (small dimensions), computes candidate inball slacks with 60-digit decimal arithmetic, and constructs strict interior contact phases for every cardinality in dimensions \(2\) through \(12\).

Observed output:
```
PASS containment_parameter_sets= 360
PASS vertex_support_cases= 120 vertices_total= 5892 subset_support_evaluations= 98616
PASS realized_unique_contact_sizes= 77 dimensions=2..12
PASS n=3 interior_contact_example= [2]
```

This does not exhaust all positive parameters or all dimensions. Decimal calculations are not a symbolic certificate at arbitrary contact boundaries. The infinite theorem is established by the universal halfspace argument and the exact transition-number monotonicity proof in `RESULT.md`. Independent external audit has not been performed.
