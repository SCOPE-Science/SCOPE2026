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

# Reproduction and limits

Run the self-contained script using `python3 check.py`; only the Python standard library is required. Its enumerator computes the generalized rank statistic by testing all independent transformation tuples and averaging over the four equally likely group states, using exact integers and `fractions.Fraction` throughout.

The observed successful execution reported 5163 exact rational assertions. These include 3960 full-law checks spanning 165 compositions of total transformation weight eight and all 24 four-state score orders; two distinct three-draw distributions checked against separately stated rational fractions; and strict/weak CDF monotonicity checks under elementary probability smoothing.

This checker is not an exhaustive proof over infinitely many group sizes, all real probability vectors, or all possible exchangeable nulls. Those claims are supported instead by the collision-partition proof, involutive pair symmetry and exact balancing derivatives in RESULT.md. In the four-state witness, uniform random data permutations are represented by a uniformly random within-orbit group element; repeating the score pattern over every orbit yields a fully exchangeable null. The no-ties condition applies to distinct transformations, not repeated sampled transformations.

Independent mathematical review, independent audit and historical-priority certification have not been performed.
