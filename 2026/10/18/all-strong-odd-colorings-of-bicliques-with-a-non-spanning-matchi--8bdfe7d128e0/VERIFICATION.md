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

Properness means that a class meeting both sides is precisely one missing matched pair: there is no third vertex nonadjacent to both endpoints. A class confined to one side is seen in full by an unmatched opposite vertex, hence has odd size. If it meets a matched endpoint, the matched opposite vertex sees one fewer, an even count which must vanish, so that class is a singleton. Conversely an unmatched-side odd block is seen in full or not at all; a matched singleton or pair is seen in at most one vertex, so the three types suffice independently. Fusing j of t pairs and partitioning the two unmatched sets gives 2t−j+k+l distinguishable blocks, assigned distinct named colors by the falling factorial. Odd-block partitions have EGF (sinh z)^k/k!, including the empty convention. Minimum block counts on positive odd and even sets are 1 and 2 respectively. A minimum forces all matched pairs fused; the number of optimal partitions from a positive even unmatched side is half the number of odd subsets, 2^(m−2). Multiplying the two counts and permuting the full optimum palette gives the stated multiplicity. The graph with t=0 and the one-edge deletion give the stated 4→3 and 2→5 changes. Saturation is genuinely excluded: in K2,2 minus a perfect matching two vertices on one side can share a color even though both are matched. An independent exact-cover enumeration using adjacency and all compatible subsets checked the whole block-count histogram and optima in 30 asymmetric cases with a+b≤10.

## originality

PASS

The distinct supported contribution is the structural and enumerative result for positive non-saturating matching deletions, including the full optimum structure. The undeleted case is an exact specialization of an earlier complete-multipartite result and receives no novelty credit. The nearest matching-deletion finding repeats the positive-t result on a later catalogue path; this is an explicit overlap but not evidence of earlier coverage. The inspected primary results and earlier crown finding do not extend to the non-saturating classification.

## value

PASS

Removing a matching is a natural structured perturbation of the biclique and exposes how parity constraints depend on near-complete neighborhoods. The exact class description for all non-saturating sizes gives every palette count and every optimizer. The opposite changes under one deletion in the even/even and odd/odd cases identify a concrete boundary in the behavior of the strong odd chromatic invariant. The contribution is not the previously enumerated undeleted case or numerical tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
