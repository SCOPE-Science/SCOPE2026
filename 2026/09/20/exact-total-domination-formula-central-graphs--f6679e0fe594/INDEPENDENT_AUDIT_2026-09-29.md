# Independent Audit — 2026/09/20/exact-total-domination-formula-central-graphs--f6679e0fe594

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `01f0fda9acccde6f50749d4c25101716449f26a1`
- Disposition: **PASSED**

## Correctness

**PASS** — The exact formula is valid. Any total dominating set S of C(G) has A=S∩V(G) a vertex cover, because every subdivision vertex c_uv has neighborhood {u,v}. An original vertex v has no neighbor in A inside C(G) exactly when A⊆N_G[v], so precisely the vertices R_G(A) must be dominated by selected subdivision vertices, which are in bijection with edges of G covering R_G(A). Conversely a vertex cover A together with any edge set covering R_G(A) totally dominates C(G). Hence gamma_t(C(G))=min_A(|A|+rho_G(R_G(A))). For any R, a maximum matching in G[R] covers 2nu(G[R]) vertices and the unmatched vertices form an independent set; adding one incident edge for each unmatched vertex gives rho_G(R)<=|R|-nu(G[R]). Conversely the edges of any cover that lie entirely in R contain a matching covering all but at most one endpoint per nonmatching edge, yielding the reverse bound. Thus rho_G(R)=|R|-nu(G[R]). Finally rho=0 exactly when R_G(A)=empty, which is equivalent to A being a total dominating set of the complement, giving the equality criterion. Independent checks found no mismatch on all 30 connected no-isolate graph-atlas graphs of order at most five and on 140 additional random connected graphs of orders two through eight using a binary total-domination MILP.

## Originality

**PASS** — Kazemnejad-Moradi (2019) prove only the general bounds tau(G)<=gamma_t(C(G))<=tau(G)+rho(G) and exact values for selected families; their accessible full text does not state the vertex-cover-dependent partial edge-cover minimum. Chen-Sohn-Wang (2020) study central trees, improve tree bounds and solve an earlier open problem, but do not supply an all-graph exact formula. Targeted searches for the partial-edge-cover expression and the complement total-dominating equality criterion found no prior covering theorem. The contribution is therefore an exact structural refinement of the 2019 bounds, not a claim that central graph total domination itself is new.

## Scientific value

**PASS** — The theorem replaces two global bounds by an exact minimization whose correction term is a standard matching quantity, and it gives a clean equality criterion in the complement. This unifies the earlier family-specific behavior and isolates exactly why the lower bound tau(G) is or is not attained. The minimization can still encode hard vertex-cover structure, so no polynomial-time algorithm is claimed.

## Sources

- **Total domination number of central graphs** — Farshad Kazemnejad; Somayeh Moradi. https://doi.org/10.4134/BKMS.b180891 — 2019 source for the bounds tau(G)<=gamma_t(C(G))<=tau(G)+rho(G) and family-specific exact values.
- **Total domination number of central trees** — X. Chen; M. Sohn; Y. Wang. https://doi.org/10.4134/BKMS.b190184 — 2020 tree-specific follow-up improving bounds and resolving an earlier central-tree problem.

## Limitations

- The result assumes a finite simple graph with no isolated vertices, as required for total domination of the central graph.
- The exact formula is structural rather than an efficient algorithm; minimizing over vertex covers can remain computationally difficult.
- The 2020 tree paper was available only through bibliographic/abstract-level text in this run, but its tree-restricted scope is not decisive for the all-graph originality conclusion.

## Independent checks

```json
{
  "formula_proof_reconstructed": true,
  "partial_edge_cover_matching_identity_checked": true,
  "graph_atlas_connected_no_isolates_order_le_5_checked": 30,
  "random_connected_graph_milp_checks": 140,
  "mismatches": 0,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval, and inaccessible material is explicitly identified rather than inferred.
