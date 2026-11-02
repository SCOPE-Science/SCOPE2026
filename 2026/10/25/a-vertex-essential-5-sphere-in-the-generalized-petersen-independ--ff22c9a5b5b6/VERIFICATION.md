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

Independently reconstructed GP(9,2) using outer cycle edges, spokes and inner step-2 edges on 18 labeled vertices. Exhaustive 2^18 mask enumeration gives 2461 independent faces including empty, nonempty face vector (18,126,438,801,747,303,27). Independently constructed the sequential toggle acyclic matching: on full complex 1230 pairs plus one unmatched cardinality-six face; direct Hasse orientation topological sort confirms no closed V-path and the matched empty face leaves critical cells in dimensions 0 and 5, giving S5. On deletion u0, 1878 augmented faces and 939 pairs; on deletion v0, 1874 augmented faces and 937 pairs; in each acyclic and empty paired with a vertex, so 938 or 936 actual elementary collapse pairs to one vertex, verified by free-face elimination. Rotational symmetry covers all 18 vertex deletions. Every proper induced inclusion factors through a contractible deletion. Full signed chain Lefschetz trace on all 18 dihedral elements gives H5 character +1 under rotations and −1 under reflections. All these calculations exhaust a fixed finite graph, not a sampled infinite family.

## originality

PASS

Qualified best-of-knowledge PASS, not certified historical priority: Vertex-essential 5-sphere in generalized Petersen independence complex GP(9,2). Prior claims cannot produce complete 18-vertex deletion acyclicity or sign character by a direct inference; explicit Morse matching and Lefschetz calculation supply substantive independent information.

## value

PASS

The finite graph GP(9,2) is canonical, and the conjunction of a pure homotopy sphere, collapsibility of all vertex deletions, and a nontrivial dihedral homology orientation character is a strong vertex-support rigidity result. It identifies a natural combinatorial instance and its complete support obstruction, beyond a routinely computed independence number or Betti vector. A finite complete exact invariant is independently useful even without a full GP(n,k) census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
