---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Every maximal independent set of K_1 join disjoint union_i K_(m_i) is the hub singleton or a one-vertex transversal across all r blocks, giving P+1 outputs. The hub is first in a uniform vertex permutation with probability 1/(M+1); otherwise it is rejected and each block minimum is chosen. Independent permutation symmetries act transitively on tuples of block minima conditional on hub not first, giving each transversal mass M/((M+1)P). Total variation from uniform is |P-M|/((M+1)(P+1)), zero iff P=M. Family blade sizes (2,q,1 repeated q-2 times) has M=P=2q, one singleton and 2q maximal sets of size q, unbounded size discrepancy. Independently literally enumerated all permutations for five small bouquets, matching exact probabilities and total variation identity.

## originality

PASS

The 2026 Fairfax–Ball result proves tree-only greedy equidistribution obstruction; bouquets with at least two nontrivial clique blades are cyclic and cannot be covered by tree theorem. Kryven et al. analyze stronger iterative-uniformity regimes and Krivelevich et al. 2024 compute asymptotic greedy output size, not finite exact distribution across all maximal independent sets in this graph family. Relevant indexed threshold/chain-graph greedy laws apply distinct classes.

## value

PASS

Although the block-first law has an elementary proof, the exact equality P=M criterion makes a meaningful natural clique-join family of uniformly sampled maximal independent sets, with a nontrivial infinite family in which equal probabilities coexist with arbitrarily unequal cardinalities. This addresses a structural obstruction phenomenon beyond trivial first-vertex conditioning, and is a self-contained exact fact with a clear combinatorial purpose.

The dated certificate retains the supplied scientific assessment, sources and limitations.
