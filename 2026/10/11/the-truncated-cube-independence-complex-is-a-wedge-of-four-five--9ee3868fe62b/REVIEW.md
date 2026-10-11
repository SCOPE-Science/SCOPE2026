# Scientific review

## Correctness — PASS

For the truncated cube's independently specified 24-vertex graph, exhaustive enumeration gives exactly 26,440 nonempty independent simplices. A complete acyclic matching has 13,211 pairs and critical cells in dimensions 0, 5 and 6 only, with counts 1, 5 and 12. The topological sort of all 143,760 oriented nonempty Hasse incidences visits all 26,440 faces. Recursive signed gradient-path elimination gives a 5-by-12 integer Morse differential with precisely six nonzero entries: the fourth and fifth rows are identical, equal to -1 in columns five and six and +1 in column nine. Its only nonzero Smith factor is 1. The 5-skeleton is a wedge of five 5-spheres; attaching maps of 6-cells are classified by integer degree vectors, so unit cancellation yields four 5-spheres and eleven 6-spheres. The second program reconstructs the graph geometrically and independently confirms all mod-two Betti numbers. Both standalone programs completed successfully.

## Originality — PASS, with residual risk

The closest inspected primary sources are Barmak (arXiv:1007.0418v1, sections 3 and 5) and Goyal–Shukla–Singh (arXiv:1905.06926v1, sections 3–5). The first proves general criteria and connectivity bounds, not this exact graph homotopy type; the second calculates different graph families and special replacement operations. Searches for truncated cube/hexahedron, complement clique complex, exact sphere multiplicities and graph-metric analogues found a published published-finding corpus computation of the same graph's scale-three Vietoris–Rips complex. The two complexes do not contain one another: the latter includes adjacent vertices, while the present complex excludes them; the former includes a pair at distance six, excluded at Rips scale three. A previously documented truncated-cube spherical-space triangulation instead concerns a different 16-vertex topological object. Priority beyond indexed work cannot be certified; an unindexed equivalent calculation remains a risk.

## Value — PASS

The regular truncated cube is a canonical Archimedean solid. Its 24-vertex cubic graph has an eight-dimensional-looking chain complex up through simplicial dimension seven, and a complete classification detects a mixed homotopy wedge in dimensions five and six. The integer rank-one attaching map is not visible from the face vector or Euler characteristic and cannot be inferred from a general connectivity theorem. The natural exact invariant provides a reproducible benchmark for polyhedral independence complexes; no family-wide theorem is claimed.

## Limits

The topological statement concerns only the ordinary vertex-independence complex of the specified finite graph. The sources examined do not prove universal priority. All assertions of acyclicity, counts and Morse degrees are regenerated from the files included with this finding; no external certification is claimed.

Same-model review: passed. Independent audit: not yet performed.
