---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The exact configurations and closed-neighborhood token-adjacency definition were reconstructed from RESULT.md. For any dominating set, one-A configurations select edges P on the B part; every triangle of the complementary graph Q has to occur as a selected all-B configuration. Deleting one Q edge per such triangle leaves a triangle-free graph, so Mantel yields |P|+|T|>=C(n,2)-floor(n²/4). The supplied four disjoint witness families use same-half B pairs with a0, all pairs of A-indices >=1 with any B vertex, {a0,a1,b} outside a fixed three-set R, and R itself; direct layer-by-layer adjacency verifies domination for all m>=2. The construction has the exact stated size, giving fixed-m squeezing. Independently enumerated 23 small (m,n) cases from graph adjacency; that test is not the infinite proof. No exact lower-order domination number is established.

## originality

PASS

Exact 3-token complete-bipartite theorem and fixed-m coefficient 1/4 are not consequences of published weaker generic k-token bounds, two-token exact results, or three-token complete-graph extremal results. An explicitly referenced unpublished project on higher tokens and Turán numbers remains a concrete priority risk; best-of-knowledge PASS with that qualification.

## value

PASS

Determining a sharp leading-order quadratic coefficient for ordinary domination on the first nontrivial three-token complete-bipartite family, with explicit O_m(n) error and a precise Mantel obstruction, resolves a natural asymptotic question beyond the known two-token case; it does not pretend to settle exact finite values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
