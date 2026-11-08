---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For each n>=4, pairwise same-row open-neighborhood traces force at most one RR and one BB column (a,b<=1). Each part then has size >=n-1>=3, excluding cross-row collisions because equality would force all selected vertices in at most two matched positions. Domination fails only for a single RR or BB when one split orientation is absent; hence the four a,b cases are necessary and sufficient. Counting yields n(2^(n-1)-2)(z^(n-1)+z^(n+1))+(2^n+n(n-1)2^(n-2))z^n and total 2^(n-2)(n^2+3n+4)-4n. For flips, all-split opposite pure words are isolated; all other states reduce via permitted transfers to mixed split words, and mixed words connect through a hypercube with opposite corners removed. Level-0/1 edges are 4n(2^(n-1)-2); level-1/2 edges are 4n(n-1)(2^(n-2)-1); sum n(n+1)(2^n-4). This validates for EVERY integer n>=4 from the symbolic proof, not just finite tests. Fresh independent graph-adjacency enumeration exhaustively checked all 87,296 assignment masks over n=4..8, with exact size coefficients, edges, component orders and zero characterization mismatches; n=3 has 20 isolated states and is explicitly excluded. The source verifier was read as evidence only, not executed as a black box.

## originality

PASS

The genuinely new best-knowledge contribution is the full ordered two-class locating-dominating partition size polynomial and exact one-vertex transfer reconfiguration component/edge census for every n>=4. Prior existence is covered by the 2025/2026 co-bipartite partition theorem; prior lambda(K_n square K_2)=n-1 from a 2017 complete-graph functigraph theorem already IMPLIES the near-balance part. These subresults are not independently original. Earlier work inspected does not furnish the all-partition census or move-graph characterization, and the analogous asymmetric partition result has a different property. Full relevant primary text, Resultary published corpus and graph aliases were checked; historical priority is qualified by explicit remaining risks.

## value

PASS

Two-color locating-dominating partitions are established motivated objects, with a prior broad existence theorem. The new useful exact invariants are a complete infinite-family ordered partition size profile and the state-space geometry under the natural one-vertex move: precisely two frozen states and one connected bulk with a closed edge formula. These data are neither mechanically implied by previously known existence/minimum-size theorems nor an arbitrary parameter slice; the n=3 boundary is genuinely different. Near-balance itself is known from 2017 lambda=n-1 and is credited, not counted as intrinsic novelty or value on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
