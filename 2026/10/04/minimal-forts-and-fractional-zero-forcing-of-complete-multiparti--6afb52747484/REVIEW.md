# Review of Minimal forts and fractional zero forcing of complete multipartite graphs

## Correctness
PASS. For a vertex outside a candidate fort in part \(X_i\), the number of neighbors inside the fort is exactly \(|F|-|F\cap X_i|\). This yields the complete inclusion-minimal classification: size-two forts are exactly same-part non-singleton pairs and pairs of singleton vertices; any larger minimal fort cannot contain either such pair, so it is forced to be a three-part transversal triple with at most one singleton. The count formulas follow directly. The fort-number proof uses an exchange argument reducing every optimum matching to one where triples consume at most one vertex from each pairing pool, after which only parity leftovers can improve the baseline pairing. The fractional formula follows from pair constraints and an explicit half-weight feasible solution. Exhaustive definition-level verification agrees through order ten.

## Originality
PASS. The 2023 primary fort-hypergraph paper explicitly determines complete graphs, complete bipartite graphs, stars, and several other families, but contains no arbitrary complete-multipartite treatment. Its complete-bipartite calculation is recovered exactly and is treated as prior coverage. The 2024 full paper on counting minimal forts studies paths, cycles, spiders, wheels, sunlets, windmills, and graph products; exact full-text searches show no complete-multipartite or complete-bipartite section. Targeted semantic and exact-phrase searches did not locate the three-family arbitrary-part classification or the resulting closed fort-number and fractional-zero-forcing formulas.

## Value
PASS. Minimal forts are the irredundant constraints of the fort-cover formulation for zero forcing, and the 2023–2024 literature treats their hypergraph structure, disjoint matchings, fractional transversals, and enumeration as substantive objects. The theorem collapses the fort hypergraph of every complete multipartite graph to rank at most three and simultaneously resolves its edge count, matching number, and fractional transversal number. This extends the previously isolated complete and complete-bipartite examples in a structurally new way through the transversal-triple family.

Same-model review: passed. Independent audit: not yet performed.
