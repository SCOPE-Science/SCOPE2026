---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The support classification follows from nested neighborhoods: a maximal independent set must contain a prefix of the A-side and then exactly the B-tail beyond its last selected degree, with corners only where the degree jumps. For a fixed corner, the left and right blocking conditions depend on disjoint priority sets, hence factor. Conditioning on the earliest active vertex yields the terminating \(\Phi\) recurrence. An independent exhaustive reconstruction over every connected canonical chain graph with total order at most 7 matched the exact rational support and probabilities for every permutation.

## originality

PASS

The chain/quasi-chain literature explicitly notes only linearly many maximal independent sets and exploits their support structure algorithmically. The general random-greedy MIS paper contains no chain-graph specialization. The audited factorized exact law and recursive corner probabilities therefore add a genuine stochastic classification not supplied by either source family.

## value

PASS

Chain graphs are a canonical nested-neighborhood bipartite class. A complete exact law for a standard random greedy heuristic, expressed directly from the Ferrers degree sequence, is a natural stochastic invariant and gives more than support enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
