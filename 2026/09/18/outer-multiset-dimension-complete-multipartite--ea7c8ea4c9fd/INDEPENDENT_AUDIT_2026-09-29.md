# Independent Audit — 2026/09/18/outer-multiset-dimension-complete-multipartite--ea7c8ea4c9fd

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d82b0f51e7b5b891676d9eb378bf77147053e862`
- Disposition: **PASSED**

## Correctness

**PASS** — The proof follows directly from the distance structure of a complete multipartite graph. For an omitted vertex v in V_i, its outer multiset code relative to S contains s_i=|S∩V_i| copies of distance 2 and |S|-s_i copies of distance 1. Hence two omitted vertices from the same part can never be distinguished, so at most one may be omitted per part. If one vertex is omitted from each of V_i and V_j, then s_i=n_i-1 and s_j=n_j-1, and the codes coincide exactly when n_i=n_j. Thus omissions may occur in at most one part from each distinct size class. This gives the lower bound n-d and the matching construction, and the basis count ∏_m c_m m and elementary-symmetric enumeration follow bijectively. Singleton parts and K_2 satisfy the same argument.

## Originality

**PASS** — The foundational outer-multiset literature treats the balanced complete multipartite case, while the 2023 development records the balanced and pairwise-distinct part-size endpoints. The 2025 joined-graphs paper treats specific diameter-two joins—stars, wheels, generalized wheels, windmills, fans and generalized fans—rather than the arbitrary mixed-multiplicity multipartite family. Targeted searches did not locate the formula n minus the number of distinct part sizes, the full resolving-set characterization, or the basis enumeration for arbitrary complete multipartite graphs. The theorem is elementary once stated, so the novelty claim is deliberately limited to this exact mixed-size classification.

## Scientific value

**PASS** — The result closes the natural regime between two previously recorded endpoint cases and gives more than a scalar dimension: it characterizes every resolving set and counts bases exactly. The formula also isolates the additional obstruction created by repeated size classes, which is not captured by the basic twin-class lower bound.

## Sources

- Distance-based vertex identification in graphs: The outer multiset dimension (R. Gil-Pons; Y. Ramírez-Cruz; R. Trujillo-Rasua; I. G. Yero): https://arxiv.org/abs/1902.03017 — Foundational outer-multiset-dimension source; complete multipartite treatment is the balanced case.
- Further Contributions on the Outer Multiset Dimension of Graphs (S. Klavžar; D. Kuziak; I. G. Yero): https://arxiv.org/abs/2207.06834 — Provides the balanced and pairwise-distinct complete-multipartite endpoint formulas used for comparison.
- Outer multiset dimension of joined graphs (Hassan Pervaiz; Rinovia Simanjuntak; Suhadi Wido Saputro): https://doi.org/10.19184/ijc.2025.9.2.1 — Treats selected joined graph families rather than arbitrary complete multipartite graphs.

## Limitations

- The theorem is restricted to connected complete multipartite graphs and does not extend automatically to arbitrary diameter-two joins.
- The proof is short enough that an equivalent statement may exist implicitly under different terminology; originality is therefore to the best of the targeted literature search.
- No algorithmic complexity claim beyond the explicit family classification is made.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this record.
