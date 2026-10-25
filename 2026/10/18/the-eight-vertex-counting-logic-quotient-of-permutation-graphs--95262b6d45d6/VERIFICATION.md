---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS: The definition as inversion graphs of every permutation in S_n is exhaustive; exact graph isomorphism groups presentation duplicates, and simultaneous un-hashed 1-WL refinement for 2n rounds computes C^2 equivalence on each fixed n-vertex class. I read RESULT.md and verify_permutation.py at the assigned Git tree, including global per-round key interning and exact NetworkX isomorphism. Separately enumerated every one of the n! presentations for all n<=8 and independently recovered (p_n,q_n)=(1,1),(2,2),(4,4),(11,11),(33,33),(142,140),(776,770),(5699,5654), including exactly two six-vertex doubletons, six seven-vertex doubletons, and 38 doubles, two triples and one quadruple at eight vertices. This is a complete bounded proof, NOT a theorem about n>8. Two-n rounds suffice for stabilization across a pair via a disjoint union of at most 2n vertices.

## originality

PASS

PASS best of knowledge: raw permutation-graph isomorphism counts and C^2=colour-refinement correspondence are known. Arvind et al. supply that equivalence and related obstruction theory; Guo–Gavrilyuk–Ponomarenko prove an 18-dimensional upper bound rather than this one-dimensional eight-vertex quotient. Neither inspected source or the targeted published-record search yields the complete (p_n,q_n) multiplicity distribution. The claimed contribution is the precise finite quotient and sharp first obstruction; avoid claiming the classical raw counts or basic WL theorem.

## value

PASS

PASS: A sharp smallest obstruction to C^2 identification within a natural well-studied hereditary graph class is a mathematically motivated model-theoretic boundary. The complete distribution of equivalence-class multiplicities through eight vertices goes beyond a routine restatement of pre-existing graph counts and supplies exact finite benchmarks for colour refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
