---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For n≥2k≥4, transitivity reduces a three-move Ehrenfeucht–Fraïssé strategy to possible adjacency profiles of a fresh third vertex over a chosen distinct pair. For two k-sets intersecting in t∈[0,k−1], a fresh common neighbor exists exactly when n−2k+t≥k, i.e. t≥3k−n. Other three fresh adjacency patterns occur for all n≥2k+1; at n=2k the graph is a disjoint matching. Exhausting t gives exactly four pair-profile spectra: matching n=2k, low 2k+1≤n≤3k−2, boundary n=3k−1 and stable n≥3k, with least representatives 6,35,10,15 vertices. An independent implementation built actual full Kneser adjacency and fresh-pair profiles for (4,2),(7,3),(5,2),(6,2),(8,3),(9,3),(10,4), including n=2k matching case; all agreed. Kneser–Lovász chromatic number n−2k+2 yields unbounded k+1 on triangle-free n=3k−1 members despite rank-three equivalence. Finite checks corroborate, while pair-extension constructions and EF argument establish all parameters.

## originality

PASS

The exact complete two-parameter rank-three EF equivalence classification is distinct from classical Kneser chromatic lower bounds and general logical EF game algorithms. The triangle-free high-chromatic examples are classical, but their collapse to one three-round theory is an additional precise logical statement. No Resultary direct matching theorem was located; historical priority qualified.

## value

PASS

A complete natural finite-model-theoretic classification of an infinite two-parameter graph family. The logical collapse of triangle-free unbounded-chromatic graphs to Petersen at depth three illustrates a sharp expressive limitation, and the sharp 35-vertex representative is a useful exact invariant beyond isolated computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
