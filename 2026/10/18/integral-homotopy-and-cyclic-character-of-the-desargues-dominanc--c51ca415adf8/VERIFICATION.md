---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed graph GP(10,3) with 20 vertices, 30 distinct edges, degree three and closed neighborhoods of cardinality four, including the exact 20-bit face predicate N[x] not contained in sigma. Separate local checker independently tested all 2^20 masks without relying on the source recurrence, obtaining 434220 nonempty faces and the exact 14-entry f-vector. Reconstructed the deterministic pivot matching on all faces (217103 pairs) and the entire oriented Hasse graph (3663080 incidences); exact indegree topological sort visited all 434220 nodes, proving true acyclicity, and critical cells were exactly one dimension-zero and 13 dimension-nine faces. Acyclic-matching theorem therefore gives a CW with a single point and 13 9-cells, so an integral wedge of 13 S9 (no possible nontrivial attaching maps to a point). Independently computed all ten signed simplicial Lefschetz traces by fixed orbit unions and per-orbit permutation parity, yielding (13,-1,3,-1,3,-11,3,-1,3,-1). With H0=1 and reduced H9 in odd dimension, tr_H9=1-L. Rational C10 Ramanujan-character decomposition indeed has trivial multiplicity 1, sign 4, faithful cyclotomic10 2, order-five cyclotomic 0. Explicit 20-vertex isomorphism to bipartite Petersen double cover separately checked. All asserted homology over Z follows from homotopy, not a finite-field rank alone.

## originality

PASS

Best-of-knowledge original as a specific integral homotopy and equivariant rational-character classification: direct primary mathematical reading and Resultary exact graph records did not supply the 13-fold 9-sphere wedge or signed C10 character. Stronger general Alexander duality, double-cover and connectivity theorems provide exact reductions but do not compute this graph-specific result. Same Desargues graph independence/matching calculations have categorically different face definitions. Remaining historical-priority risks are explicit; unsuccessful indexed searches are not novelty certification.

## value

PASS

The Desargues graph is a distinguished highly symmetric cubic Levi graph of the ten-point Desargues configuration and canonical bipartite cover of Petersen; its dominance complex is a standard natural invariant with few exact homotopy computations. An exact integral homotopy type of thirteen S9s and the nontrivial full rational rotation character are two substantive, potentially reusable invariants, not a routine reformulation of graph parameters or a known table. The all-face, full oriented-Hasse certificate gives a meaningful complete classification for this canonical object. The cyclic trace additionally reveals sign and faithful cyclotomic constituents invisible to the sphere count. A uniform family theorem or paper-sized application is not needed for this motivated exact case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
