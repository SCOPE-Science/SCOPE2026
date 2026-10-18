---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For sorted (a,b,c) with total S, Gini is 2(a-c)/(3S), and Theil T differs at fixed S by S^(-1)log(P) where P=∏x_i^{x_i}. Independently enumerated all three-part positive integer partitions S=3..13 and compared exact integer P and exact ranges: first opposite strict ordering S=13, unique unordered pair. Exact values G_A=4/13 >G_B=10/39, P_A=1811939328 <P_B=2176782336. Infinite family has Gini ranges x and x−1. Log of P_B/P_A derivative ln[x²/((x+2)(x−3))]>0 for x>3, and the x=6 exact inequality holds. Hence infinite proof not inferred from x<=500 tests.

## originality

PASS

General inequality literature explicitly distinguishes pairwise-distance Gini from entropy-derived Theil and non-Lorenz-dominating distributions. That conceptual difference does not imply the earliest primitive integer equal-total 3-household strict reversal or the specified infinite family. Resultary semantic search found no identical cutoff. Priority vulnerable to unindexed small examples or textbook exercise.

## value

PASS

The smallest primitive lattice realization of a strict reversal between two canonical inequality rankings supplies an exact benchmark and an infinite explicit witness family; equal total removes average-income effects, and the three-household dimension is the first naturally manageable nontrivial setting. Significance is limited to the chosen lattice normalization rather than a universal real-income gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
