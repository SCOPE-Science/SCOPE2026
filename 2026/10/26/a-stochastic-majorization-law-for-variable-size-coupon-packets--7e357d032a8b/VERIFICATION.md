---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Write missing count as size of intersection of independent uniform complements m_i=n-s_i. For an elementary pair balancing (a,b)->(a+1,b-1), hypergeometric mass ratio p_new(j)/p_old(j) is proportional to (b-j)/(a+1-j), nondecreasing in j, including the extra largest endpoint; this establishes pairwise likelihood-ratio and first-order stochastic dominance. Conditional on size, intersection is uniform among subsets: a common random permutation yields nested uniform intersections J<=Jprime. Intersect with the remaining independent complements and iterate balancing transfers to prove whole-array dominance for all n,k and all integer thresholds. E U = n product_i (1-s_i/n) and the positive balancing increment establishes interior strict expected order; boundary cases with zeros or whole-population packets are allowed in the weak stochastic result. Independent exact rational enumeration checked hypergeometric tails up to n14 and 3-packet distributions up to n6, not an infinite proof.

## originality

PASS

Betken–Thale 2022/2023 and Stadje 1990 study uniform group drawings with the same packet cardinality in every round. Schilling 2021 and Berend–Sher 2026 vary probabilities of drawing different subsets of one fixed cardinality, not deterministic unequal packet sizes across rounds. Their fixed-size/selection-probability statements do not imply the full all-round majorization stochastic order. Classical hypergeometric likelihood ratios and majorization transfers are acknowledged mathematical tools; an overlooked broader sampling-without-replacement stochastic-order theorem remains possible.

## value

PASS

At a fixed coupon-exposure budget, exact dominance for every missing-count tail answers a genuine packet-allocation optimization question, stronger than mean comparison or asymptotics. The uniform pairwise coupling and all-round transfer yield sharp simultaneous optimal profiles, rather than recomputing a known fixed-size collector waiting time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
