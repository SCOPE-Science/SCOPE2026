---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Inspected all 103 explicit tetrahedra in frozen verify.py; independently transcribed/reconstructed the 17 vertices, 120 graph edges, 206 triangular faces, 467 graph 3-cliques and 261 nonfacial cycles. Computed an independent integral 206×104 relation matrix after spanning-tree collapse; SymPy Smith normal form gave exactly 101 ones, one 2, two zeros, proving H1≅Z²⊕Z/2. Independent row-space reductions modulo 2 and 101 detected all 261 nonfacial triangle classes as nonzero; 205 are nonzero mod both and 56 detectable mod2 only. Audited explicit integral Y1,Y2 and mod2 W cocycle lists and three coordinate-generating triangle witnesses in the source, which support its complete seven-type distribution 56+35+34+34+34+37+31=261 and primitive free projections. These modular checks corroborate essentiality, not independently determine the exact coordinate multiplicities without the explicit source cocycle computation; the integral Smith proof and source cocycle certification jointly establish the final claim. Any simple graph cycle has at least three edges, so systole length is 3.

## originality

PASS

Best-of-knowledge originality based on scientific implication comparison, alias searches and material reading; no earlier source establishes the full final claim under the precise convention. Later broader methods, where relevant, are dated and explicitly delimited.

## value

PASS

Shortest essential edge cycles and the complete torsion/free homology-carrier spectrum are natural topological-combinatorial invariants of a canonical minimal-size 3-manifold triangulation; the primitive-direction shell is more informative than known f-vector and abstract H1. The finite exact classification can be valuable without solving a family-wide problem or a geometric stable norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
