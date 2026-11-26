---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With no strict intermediary, (ef)ᵤᵥ=eᵤᵤfᵤᵥ+eᵤᵥfᵥᵥ, so an idempotent's strict entries are free precisely at unequal diagonal bits, including in characteristic two. A product has binary diagonal and vanishes on every edge with both product endpoint bits 1. The same condition is closed under multiplication, since an output diagonal bit 1 requires both factors to have it. To cover the full proposed locus, orient edges from U to V; set the two factor diagonals on each u to (1,hᵤᵤ) and on each v to (hᵥᵥ,1). If hᵥᵥ=0 use the first factor's free strict entry for hᵤᵥ; otherwise use the second factor's entry unless both output bits are one, when zero is required. These choices are independent, giving a genuine factorization over any field. Width means the uniform at-most-two bound in the Finding; the least width is one for an antichain and exactly two once an edge exists, witnessed by a nonzero single-edge nilpotent. For fixed support S there are q^(m−i_G(S)) product elements, and q^(cut_G(S)) idempotents. The largest-power terms are respectively independent sets and bipartite colorings (two per component including isolated vertices). This gives both limits, including m=0. In UT₃ the displayed idempotents multiply to E₁₂+E₂₃, of rank 2 and zero diagonal. Each of two hypothetical factors needs at least two diagonal ones because its idempotent rank equals their integer count. The diagonal supports then intersect, a contradiction in every characteristic. Replay: RESULT.md Steps 1–6 constitute the proof; VERIFICATION.md and verify.py were inspected, not run, and enumerate selected examples, not arbitrary posets or fields.

## originality

PASS

The local idempotent equations and generic hard-core specialization are antecedents. The distinct contribution is the global classification of attainable products in the ambient monoid: a single choice of factor diagonals works simultaneously for all edges of an arbitrary bipartite incidence support and realizes every compatible strict entry. The resulting distinct-output fiber counts and sharp failure at height three are not provided by the strongest compared component and ordered-pair results.

## value

PASS

A field-independent bounded-length normal form resolves the full multiplicative product locus and makes every finite-field diagonal-support fiber explicit. The leading coefficients recover a graph invariant of the poset comparability graph, and an obstruction already in the three-chain makes the general height threshold meaningful. The known independence-polynomial limit of the graph sum is a consequence, not the sole scientific gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
