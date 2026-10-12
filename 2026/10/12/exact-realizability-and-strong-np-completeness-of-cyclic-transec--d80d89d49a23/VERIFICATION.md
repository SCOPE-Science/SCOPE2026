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

# Verification and proof limits

The included `verify_gap_curve.py` checker was executed using Python's standard library only. Its output was:

```
CASE 2 1 matrices 3 curves 2 hist_curves 2
CASE 3 2 matrices 49 curves 6 hist_curves 7
CASE 4 2 matrices 225 curves 14 hist_curves 15
CASE 4 3 matrices 3375 curves 30 hist_curves 34
CASE 5 2 matrices 961 curves 25 hist_curves 30
CASE 5 3 matrices 29791 curves 65 hist_curves 84
CASE 6 2 matrices 3969 curves 53 hist_curves 0
VERIFY_OK matrices 38373 distinct_curves 195 cases 7 infeasible_concave=1 partition_bridge=1
```

For every listed size, all nonempty binary species rows were enumerated without quotienting by cyclic shifts or species permutations. The checker compared direct window enumeration with independent zero-run enumeration, inverted exact rational richness curves, and checked bin feasibility. For the enumerated sizes with \(n\le5\), all gap histograms with compulsory size bounded by total capacity were also traversed. It separately tested an infeasible concave profile with forced item sizes \(3,3,4\) and a feasible six-item equal partition.

The general if-and-only-if theorem follows from exact combinatorial counting and explicit constructive packing, not the finite tests. Strong NP-completeness follows from an explicit polynomial reduction from strongly NP-complete 3-PARTITION. The checker is not a proof of complexity hardness, does not exhaust arbitrary \(n,s\), and does not establish empirical identifiability under noise. Independent audit remains unperformed.
