---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The parameter B-coloring is proper EDGE-coloring such that each 4-cycle is rainbow (distinct from the unrelated vertex b-chromatic number). In crown Cr_n, edge a_i b_j corresponds to arc i→j with i≠j. Distinct edges i→j and k→ℓ may share a color only if their tails and heads are distinct (properness) AND one opposite cross edge of the potential 4-cycle is missing, namely j=k or ℓ=i. Each color class is therefore a pair of composable directed arcs, or, if triple, precisely the three arcs of an oriented directed 3-cycle; no class of size four. Lower bound is ceil(n(n−1)/3). Gardner's classical complete-directed-graph packing theorem, inspected in its original full 1997 primary text, decomposes all arcs into directed 3-cycles for n≡0,1 mod3 except n=6, and for n≡2 mod3 leaves a directed 2-cycle that forms one legal same-color pair. Order 6 has no Mendelsohn triple system, giving ≥11; eight explicitly displayed directed triangles plus three two-arc classes form exactly 11 legal colors covering all 30 arcs. Independent re-enumeration checked 8/20/40 legal 3-arc classes in n=4/5/6 and verified all 11 six-vertex blocks partition the arcs and meet each pairwise 4-cycle constraint. This proves all n≥4 using the full classical existence theorem rather than extrapolating finitely. Upper bound q_B=ceil(n(n−1)/3) except q_B(Cr_6)=11.

## originality

PASS

Gardner's 1997 complete digraph 3-circuit theorem indeed gives all necessary packings and exact order-six exception; that prior design theorem alone is not a statement about B-edge-coloring of crown graphs and requires proving legal-color-class equivalence. Lu–Ying–Song's accessible full 2026 B-coloring paper gives q_B(K_{Δ,Δ})=Δ² and bipartite-exclusion bounds but no crown matching-deleted formula found in inspected relevant pages and full-text search. Search of published SCOPE/Resultary found B-coloring of cacti and vertex colorings of crowns, which are different graph classes/parameters. Best-of-knowledge O PASS, subject to older rainbow-C4 edge-coloring aliases.

## value

PASS

This is the exact B-edge-coloring number of the natural matching-deleted biclique, with the concrete exceptional order six. The structural reduction to Mendelsohn 3-circuit packings explains an initially striking discontinuity: K_{n,n} needs n² colors while Cr_n after deleting n matched edges needs n(n−1)/3+O(1). The graph/design translation and sharp exception are useful for 4-cycle-rainbow edge colorings and cannot be read off from a generic chromatic bound; the classical Mendelsohn packing theorem is acknowledged as a non-new ingredient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
