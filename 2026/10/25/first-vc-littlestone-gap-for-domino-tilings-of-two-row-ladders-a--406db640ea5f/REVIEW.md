# Scientific review: edge-query shattering of ladder perfect matchings

## Correctness — PASS

The theorem is stated for the full edge-incidence class, not only horizontal face-code bits. The two-row tiling bijection forces horizontal dominoes to occur in top/bottom pairs and enumerates exactly eight perfect matchings of the five-column ladder. A complete three-round decision tree has eight different witnesses, while the eight-concept upper bound excludes four rounds. To exclude three static coordinates, any three-coordinate shattering would need all eight concepts to map bijectively onto eight labels, requiring every queried edge to occur in four matchings. Only the middle rung does. The two horizontally separated queries \(T_1,T_4\) are shattered, giving VC dimension two. The smaller ladder orders follow from cardinality bounds and explicit shattered queries. In the connected amplifiers, even-side bridge cuts forbid every bridge in any perfect matching; this yields exactly the Cartesian product of base matching choices. Blockwise VC bounds and concatenated adaptive trees give the asserted \(2s\) and \(3s\) formulas for all positive integers \(s\). The supplied program independently enumerates full graph matchings and one-dimensional tilings through five columns, checks the complete decision-tree certificate, and enumerates three amplifier orders.

## Originality — PASS, with uncertainty

A statement-level literature comparison was conducted against the full accessible text of Oh's monomer–dimer recurrence and Brezovnik–Tratnik–Žigert Pleteršek's binary encoding of outerplane-bipartite resonance graphs, and relevant portions of Manurangsi–Rubinstein's general dimension-complexity paper. Oh counts tilings, not their edge-query shattering. The resonance-graph encoding classifies matchings by face-code coordinates; in this ladder, the horizontal-only code is an independent-set class of VC and Littlestone dimension two, whereas the *physical rung queries* are derived NOR coordinates and raise the online dimension to three. Thus the specific comparison shows why the existing coding theorem does not imply the adaptive claim. Che's closely related paper on cube-free resonance graphs was checked at the abstract level only and remains a priority uncertainty. No source examined asserts the connected \(2s/3s\) separation for perfect matching incidence queries.

## Mathematical value — PASS

Domino tilings of narrow ladders are a canonical solvable perfect-matching family. The result isolates a sharp first failure of equality between static and adaptive shattering, and pinpoints its mechanism: derived local vertical-edge tests improve adaptive discrimination without increasing the number of matchings or static shattering rank. The same base phenomenon is promoted to an exact, unbounded gap within the restrictive class of connected planar subcubic bipartite graphs. This is more informative than computing an arbitrary small table or taking an unspecified disjoint union.

## Closest literature, limits and risks

- P. Manurangsi and A. Rubinstein, arXiv:1705.09517v1: general VC/Littlestone complexity, not ladder perfect matching incidence.
- S. Oh, arXiv:1901.07847v1: monomer–dimer enumeration, not adaptive or VC dimension.
- S. Brezovnik, N. Tratnik and P. Žigert Pleteršek, DOI 10.46793/match.90-2.453B: full-text binary resonance coding, under different query coordinates.
- Z. Che, DOI 10.1016/j.dam.2020.03.036: closely related Clar/cube-free resonance structure; only the abstract was accessible, so unexplored implications remain a residual risk.

Only ladders of up to five columns are classified for the complete edge-query concept class. Bridges in the constructed connected graphs never belong to a perfect matching. The result does not extend to two-edge-connected, matching-covered or regular cubic amplifiers. No external independent audit or exhaustive priority search has been completed.

Self-review: passed. Independent audit: not yet performed.
