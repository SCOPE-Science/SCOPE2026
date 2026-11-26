---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Anchor at a sampled label and rotate to zero; the other n−1 uniform positions yield the uniform (n−1)-simplex gap law. Each geodesic edge has an arc of length ≤r, whose intervening successive gaps are also ≤r. Thus short consecutive gaps generate exactly the graph's connectivity and a proper k-run has two distinct long borders. Each k-component has one such start. Translating those two gaps and applying inclusion–exclusion to the internal caps gives the stated normalized volume, and strictly feasible positive gaps exist for 0<r<1/2. The affine constraints give the required Minkowski inclusion, so Brunn–Minkowski applies in the correct relative dimension n−1. Both endpoint values vanish. On each breakpoint-free interval, a constant polynomial would force its nonzero coefficients into a Vandermonde kernel via derivative orders 1 through J+1≤k≤n−1. This excludes a plateau of maxima. For fixed k the spacing sum converges uniformly on compact c-intervals to f_k(c); the joint density of the k−1 internal gaps is bounded by n^{k−1} and a single bordering-gap probability is at most exp(−c/2). The resulting bounds c^{k−1} and exp(−c/2) confine maximizers to a compact interval, and the log derivative of f_k has one zero at log((k+1)/2). As a small boundary check, n=3,k=2 gives 2r−5r² up to 1/3 and (1−2r)² thereafter, with peak r=1/5. The frozen grid and simulations were inspected but not executed and are not needed for the analytic conclusions.

## originality

PASS

Credit is limited to the full fixed-size-class shape theorem: (n−1)-root concavity and a unique finite-n maximum for every proper non-singleton size, with its fixed-k scaling limit. The spacing expectation, related spacing laws and the k=2 limiting-profile peak alone are not credited as new.

## value

PASS

The radius that maximizes expected counts of a chosen proper size is a natural calibration of the random graph. The result controls the whole curve at finite n, excludes multiple optima despite piecewise changes of formula and gives the leading radius for every fixed k without a numerical search. That combination goes beyond recomputing spacing probabilities or invoking concavity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
