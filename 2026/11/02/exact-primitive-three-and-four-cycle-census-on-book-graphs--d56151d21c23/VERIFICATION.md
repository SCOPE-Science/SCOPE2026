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

For every integer m>=1 on labelled book graph K2 joined to m independent leaves, under simultaneous loopless chip firing all vertices share the same number k of firings per period (connected Laplacian). For q=3, single firing per vertex requires distinct hub phases; predecessor-phase neighbor multiplicities and binomial sum yield 6*m*2^(m-1) states, doubled by complement involution and divided by 3 => N3=m*2^(m+1). For q=4, one-fire hub phases antipodal, multiplicity m(m-1)2^(m-2) per one of four rotations; complement doubles k=1 and k=3 classes. Source's complete six-word analysis forbids primitive k=2 four-cycles; alternating hubs yield only period two. Thus N4=m(m-1)2^(m-1) with crossing m=5. Independently enumerated all confined labelled states for m=1..4 by literal updates and confirmed (N3,N4)=(4,0),(16,4),(48,24),(128,96). Analytic all-m phase argument, not finite test, proves theorem; source verifier inspected.

## originality

PASS

Best-of-knowledge PASS: Jiang's On the Period Lengths of the Parallel Chip-Firing Game (arXiv:1003.0943) supplies firing count, confinement, and period possibilities for complete bipartite/multipartite graphs, but those graph classes are not book graphs B_m (m>=2) and the inspected general material does not imply these labelled primitive orbit populations. Jiang–Scully–Zhang's forbidden-word approach gives restrictions but not a sharp book census. Resultary matches were unrelated parity automata. Prior hidden specialized enumeration possible.

## value

PASS

Exact all-m primitive cycle populations for a natural one-edge sum of triangles, including sharp first four-cycle at m=2 and reversal of dominance at m=5; meaningful dynamical-statistical classification that cannot be deduced merely from period-existence bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
