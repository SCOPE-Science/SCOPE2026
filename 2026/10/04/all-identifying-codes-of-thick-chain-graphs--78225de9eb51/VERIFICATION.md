---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Each canonical chain-graph class is a false-twin class, so any identifying code omits at most one vertex per class. With every class of size at least two, every class still supplies a selected witness. The nested bipartite adjacency then separates distinct same-side levels and all cross-side pairs, except that for \(p=1\) the two selected singleton traces arising from one omission on each side collide exactly in \(K_{2,2}\). Thus the all-but-one condition is sufficient outside that exception. The product polynomial and minimum-code count are immediate classwise. A fresh independent brute replay on one- and two-level profiles with class sizes two and three matched the theorem.

## originality

PASS

The directly relevant full primary paper on identification/location-domination/metric dimension in interval and permutation graphs states in its conclusion that the complexity on bipartite permutation graphs was not known and specifically suggests that the chain-graph approach might also work for Identifying Code. Current Resultary searches under chain/Ferrers/2K2-free terminology return the assigned record but no earlier closed-neighborhood identifying-code classification; nearby chain results concern resolving sets, skew zero forcing, or other invariants. Thus the thick-chain all-code product theorem is original to the best of current knowledge.

## value

PASS

Chain graphs are a canonical bipartite permutation class, and the directly relevant literature identified Identifying Code on them as a natural tractable direction. In the thick regime the theorem gives every code, the full polynomial, the exact minimum and its multiplicity, with a sharp \(K_{2,2}\) exception. This is a natural complete classification, not an arbitrary small-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
