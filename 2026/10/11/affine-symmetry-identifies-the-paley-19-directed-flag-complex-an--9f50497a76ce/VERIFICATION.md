---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Independently enumerated ALL 524287 nonempty vertex subsets, without the verifier's a priori cardinality <=5 restriction, and obtained the exhaustive transitive-subtournament face counts 19,171,684,1026,342, none of higher cardinality; Euler characteristic is -152. Every vertex has outdegree 9 and every pair has 4 common out-neighbors, establishing doubly regularity. Govc Proposition 3.4 gives only two homotopy types at 19, with Euler characteristics -152 and -134, so this is the former. For all 171 affine Paley automorphisms an independent fixed-face signed orientation count gives Lefschetz L=-152 (identity), L=0 (18 translations), L=1 (152 nontranslations). Rational H4 one-dimensional and odd-order action forces triviality, hence chi3=2-L. Solving u+18v=154, u-v=2 gives u=10,v=8. Frozen verifier also computes boundary ranks [18,153,531,341] over five fields; finite-field ranks alone would not prove the homotopy wedge, so the Govc theorem is explicitly used.

## originality

PASS

Govc's primary Proposition 3.4 classifies the two order-19 doubly regular tournament homotopy types without labeling the Paley tournament in that theorem and without computing the affine subgroup action or rational character. The canonical Paley identification is a precise new assignment of the known type, but the substantive added character computation is not implied by nonequivariant homotopy classification. The nearby published Paley-31 nonequivariant computation is at a different order and supplies no order-19 action.

## value

PASS

Identifies the canonical tournament at the first doubly regular order where two distinct directed-flag homotopy types occur and computes the full rational character for its natural 171-element affine symmetry. The equivariant information is mathematically nonredundant with a Betti table or with a title-only named identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
