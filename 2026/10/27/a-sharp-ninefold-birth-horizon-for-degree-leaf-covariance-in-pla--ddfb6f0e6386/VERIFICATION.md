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

Uniform insertion among 2n−1 gaps gives the uniform plane increasing tree because deletion of the newest vertex recovers its unique prior tree and gap. Write W=1+D and B for the marked leaf indicator. The simultaneous attachment-to-marked and attachment-to-leaf event has conditional probability B/(2n−1). The W and L terms in the conditional product cancel, leaving WL+W+(W−B)/(2n−1). The leaf mean equals (2n−1)/3 for n≥2 starting from L_2=1. On subtracting updated means the covariance difference is (a/3−b)/(2n−1), which telescopes from deterministic marked birth to the exact claim, including its birth zero. Since b/a=(j−1)/(n−1), the differences are negative below 3j−2, zero there, and positive above. For q=j−1 and m=n−1 the sign is the sign of (r_m/r_q)(m+3q)/(4m)−1; the two adjacent candidate sizes correspond to m=9q+4,9q+5. Independently recomputing the rational ratio polynomials matches both frozen numerators and yields positive denominator coefficients. Thus the sequences in q approach 1 from below and above respectively, using the Wallis asymptotic, giving both strict signs for every q≥1 and no later zero. Wallis also gives a→√t and b→1/√t at every finite limiting t≥1. `python /workspace/replay_frozen_reviews.py 2` verifies the polynomial coefficients and enumerates actual ordered trees through n=7 as a separate check of the mixed moment; those finite tree counts do not prove the threshold.

## originality

PASS

The supported distinct claim is the sharp all-label finite-size horizon in the uniform plane increasing tree, with its exact plane-model covariance and strict endpoint signs. Exact marginal moments, root-only statistics, and joint leaf indicators do not give this classification. The edge-seeded degree-proportional preferential-attachment record is materially close: it supplies the same conditional covariance method and the identical scaling limit, but its denominator, leaf mean transient and actual finite covariance differ. The macroscopic factor 9 and general covariance-update technique should not be credited as distinct from that comparison. No inspected statement gives or implies the exact plane-model cutoff by substitution; no historical priority certification is made.

## value

PASS

This is a natural fixed-birth-label dependence statistic in a standard attachment model. The exact integer horizon, uniform in every nonroot birth label, identifies precisely how long the negative degree–leaf dependence survives and rules out equality after birth, including the small-label and near-crossover regimes in which a ratio limit is uninformative. Those strict adjacent finite offsets are useful and not a routine restatement of the scaling crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
