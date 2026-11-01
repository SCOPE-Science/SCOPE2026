---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS: Simultaneous functional dependency x->y and inclusion pi_x subset pi_y force every finite consistent nonempty subrelation to be a permutation on its used vertices. A strict extension is a cycle on unused vertices; maximality iff unused vertices lie in at most one part. Allowed permutations exist exactly for 2 max(s_i)<=sum(s_i), by cyclic rotation across contiguous part blocks. Rook inclusion-exclusion yields D(s), and omitting t vertices from one part gives the exact labelled generating polynomial. Omissions from largest part realize every integer from max(n-a1,2 a2) through min(n,2(n-a1)), and other omission choices lie within. Independently checked six profiles and full example (3,2,2) polynomial 4z^4+48z^5+384z^6+288z^7.

## originality

PASS

General FD+ID repair/argumentation equivalence and complexity are prior results but do not state labelled multipartite size polynomial or gap-free interval. Rook inclusion-exclusion is classical, but the maximality criterion and support-spectrum combination is a new exact instance to best knowledge.

## value

PASS

PASS: Exact labelled sizes and gap-free maximal-repair spectrum answer a concrete database-consistency counting question with mathematically natural block restrictions. The partial-permutation/omission criterion is structural and the support interval is an informative classification, despite the routine rook summation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
