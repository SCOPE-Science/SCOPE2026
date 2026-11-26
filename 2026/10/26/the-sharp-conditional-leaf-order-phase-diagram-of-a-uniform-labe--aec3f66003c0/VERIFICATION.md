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

In the uniform Prüfer word, conditioning on d−1 marked labels leaves n−d−1 iid draws on the other n−1 labels, plus one marked leaf iff d=1. Prefix coupling gives the strict increasing order for d≥2, and adding one draw for d=1 can remove at most one empty box, with a repeat occurring with positive probability (strict comparison with d=2). The star law is the point mass n−1 and strictly dominates L1. At every interior d≥3, the lower endpoint is at least d, whereas L1=2 has positive mass; the upper endpoint is at most n−2, whereas L1=n−1 has positive mass. The two endpoint tails cross. With q=n−1 the degree-three difference is f(q)−1, f(q)=(2−1/q)(1−1/q)^(q−3). The displayed log derivative is negative already by log(1−1/q)≤−1/q. I checked f(7)=16848/16807>1 and f(8)=252105/262144<1. The d=4 expression is positive for q≥11 since (1−1/q)^(q−4)>e^(−1) and 3−3/q+1/q²≥331/121>e; direct exact checks for q=4..10 have smallest positive difference 44020511/100000000. Strict stochastic monotonicity then handles all d>4. Replay: /workspace/replays/recheck_frozen.py, leaves(), inclusion–exclusion tail checks at n=5..20 and exact boundary arithmetic. The analysis, not the bounded checks, handles all n.

## originality

PASS

The earlier indexed stochastic-valley result already covers the exact law, conditional means as a formula and the monotone chain with its degree-two valley. The incomparability follows readily from that law’s support and is not credited alone. The supported distinct result is the full conditional mean sign classification, in particular the sharp reversal at nine while first-order incomparability persists. The later 0e8a59994112 record is genuine statement-level overlap on the full stochastic diagram and crossing, not a mere topical hit. Its later path date is not evidence that it predates this frozen result, and its compared Finding and reversal proof do not give the higher-degree all-size mean inequality, which does not follow just from the crossing and the chain for n≥9. Historical priority is not certified.

## value

PASS

A marked vertex's degree is a natural predictor for the global leaf count. The result turns the known degree-two valley into a complete set of comparisons and pinpoints a nontrivial all-size sign pattern for means: degree three switches at nine while the stochastic incomparability never changes, and degree four and above never switch. The useful distinction is between prediction in expectation and full tail order, not a new occupancy model or a census through an arbitrary n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
