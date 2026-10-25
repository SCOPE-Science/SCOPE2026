---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Reconstructed the exact cubic edges u_i-u_(i+1), u_i-v_i, v_i-v_(i+2) and the multiplicity-aware reflected quotient neighbor multisets. The six-round base and induction split the three-orbit leading collision while advancing the resolved frontier two indices each round; the four mod-4 seam cases leave a nontrivial collision at R-1 and resolve it at R. Reflection invariance plus singleton orbit-sized final cells proves the full rooted automorphism-orbit statement. Independent full-graph WL, BFS/eccentricity and orbit computation for every n=14..150 (137 parameters) agreed; further independent full-graph wavefront/seam checks on n=26..250 (225 parameters, 6,666 wavefront-round comparisons) agreed. The tests are finite corroboration; the explicitly examined induction is necessary for n unbounded.

## originality

PASS

Exact rooted all-n GP(n,2) one-dimensional counting refinement wavefront, orbit partition and sharp depth not supplied by the inspected automorphism classifications, unmarked Petersen graph examples or unrestricted colour-refinement iteration bounds. Bounded absence of a source cannot prove priority.

## value

PASS

Generalized Petersen graphs are a classical natural cubic family. The exact all-n marked graph orbit recovery, round-by-round wavefront and equality of strict stabilization depth with graph eccentricity are nontrivial structural invariants and a usable example of exact one-dimensional counting-logic propagation; not merely a finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
