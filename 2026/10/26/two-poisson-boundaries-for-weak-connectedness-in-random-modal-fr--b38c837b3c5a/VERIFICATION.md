---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At any world, witnesses for the two diamonds either coincide or are related in one of the two directions. Singleton valuations on a distinct incomparable successor pair prove the converse. In the sparse window the independent rows give a binomial count of vertices with outdegree ≥2, with total mean tending to c²/2; the incidence expectation of comparable forks is n C(n−1,2)p²(2p−p²)=o(1). In the dense window independent unordered dyads give a binomial count of mutually missing pairs with the same limiting mean. For each missing dyad the independent common-predecessor trials fail with probability (1−p²)^(n−2); the expected number of such unwitnessed missing dyads tends to zero. Both arguments include c=0. In the intermediate region the variance of all forks divided by the squared mean is O((n³p²)^−1+(n²p)^−1), using that only pairs of forks in one outgoing row sharing an arc contribute covariance. For p<ε, concentration plus Markov on the comparable forks bounds validity by o(1)+4ε. For p≥ε, missing dyads have diverging expected count and the probability any lacks a common predecessor is ≤n²exp(−ε²(n−2)); sending ε to zero covers oscillatory sequences satisfying the two divergence bounds. Independent full finite enumeration of all valuations and the structural condition reproduced counts 1/1, 4/4, 52/64, 1907/4096 for n=1,2,3,4.

## originality

PASS

The exact deterministic modal correspondence is classical and is not credited as new. The supported distinct finding is the combined independent-arc two-ended probability diagram for the one-sided condition, including the different obstruction counts and scalings at opposite ends and the full vanishing intermediate region.

## value

PASS

The standard modal axiom gives a natural test case where validity disappears and returns as the arc density grows. The two different powers and common curve distinguish isolated outdegree obstructions from many forks clustered on one rare missing pair; counting raw forks at both boundaries would miss that distinction. The intermediate proof completes the classification rather than only evaluating two special-density examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
