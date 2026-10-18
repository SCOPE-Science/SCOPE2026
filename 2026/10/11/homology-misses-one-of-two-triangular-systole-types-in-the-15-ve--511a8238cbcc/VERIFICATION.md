---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The 87 frozen facets give f=(15,102,174,87). An independently implemented JS reconstruction computed all 417 triangular cliques, subtracting 174 faces to give 243 candidates. Exact permutation products of the fetched EDGE_WORDS verify each of 174 face relators, and the generated image has order 24. The primary Lutz topology identifies pi1 with the order-24 binary tetrahedral group, so the surjective representation is an isomorphism. Each missing triangle maps nontrivially: 215 order six in two inverse conjugacy classes with hits 110 and 105, 28 order four in one inverse-stable class. The commutator subgroup has order eight and contains exactly the 28 order-four instances, giving the H1 split. Simple cycles cannot have fewer than three edges.

## originality

PASS

Lutz supplies this complex, its 87 facets, H1 and fundamental group, but does not give the missing-triangle conjugacy spectrum. Resultary exact-object/alias search found classifications on other manifolds (Q8, lens spaces, projective complexes), which cannot imply this nonabelian T* triangulation-specific count. No checked source dominates the claim.

## value

PASS

The complete finite geometric loop spectrum of the canonical 15-vertex binary-tetrahedral space shows that minimal noncontractible loops include a genuinely nullhomologous type. This is a motivated systolic and homotopical invariant, not an arbitrary clique count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
