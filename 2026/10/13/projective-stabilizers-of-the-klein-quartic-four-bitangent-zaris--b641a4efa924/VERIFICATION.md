---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The source checker implements exact cyclotomic arithmetic in Q(zeta_7), enumerates 168 projective quartic automorphisms and their faithful permutation action on all 28 source bitangents, then exhaustively checks each of three set stabilizers (6,1,1) and S3 action. Its exact implementation and normalization were inspected; the 168-element group is complete by the genus-3 Hurwitz bound. A separate full cyclotomic checker replay was not performed this execution; no numerical approximation is used in the inspected algorithm. The component-degree uniqueness reduces plane arrangement stabilizers to those finite subset stabilizers.

## originality

PASS

Known projective automorphism group PSL(2,7) order 168 and original Zariski triple are not new. The narrower computed object is the stabilizer of each specific four-bitangent arrangement inside PGL3, with S3 versus trivial and orbit sizes. Inspected primary triple theorem determines topological connected numbers, not these subgroup orders; related two-graph analysis is not a projective stabilizer theorem. Historical finite-geometry overlap is possible.

## value

PASS

The projective stabilizers of three canonical Zariski-triple representatives distinguish the symmetry of algebraic arrangements from topological-equivalence data, giving exact quotient-orbit weights 28,168,168. This finite exact classification is naturally motivated and not just arbitrary small-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
