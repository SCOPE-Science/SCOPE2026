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

# Verification of the four-visit identifiability theorem

The accompanying `verify.py` requires Python 3 with the standard library only. Run `python3 verify.py` from the directory containing the two files.

The exact-rational program evaluates beta rising-factorial moments, the complete independent Poisson-mark decomposition for every nonempty visit pattern, and the closed-form inverse of four distinct-visit cross-cumulants. It checks five admissible parameter sets including a zero-contamination boundary example. It also constructs six distinct parameter sets with identical three-visit laws and checks the displayed pair's fourth-order discrepancy exactly as \(1/147\). Success reports:

`VERIFY_OK inverted_parameter_sets=5 independent_mark_checks=50 nonidentifiable_three_visit_profiles=6 fourth_order_difference=1/147`

The general claims are proven symbolically in `RESULT.md`, not inferred from these finitely many tests. Neither a finite-sample estimator nor a Monte Carlo confidence interval is asserted. Independent audit: not performed.
