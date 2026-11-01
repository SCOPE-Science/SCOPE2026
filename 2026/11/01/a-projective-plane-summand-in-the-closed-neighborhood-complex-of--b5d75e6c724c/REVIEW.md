# Self-review

## Correctness — PASS
The definitions are exact for all 56 three-subsets and the 56 closed-neighborhood facets. The executable regenerates 111,482 faces, verifies 54,910 elementary collapses, and checks a 1,662-cell Hasse graph with 4,190 incidences for matching acyclicity. The critical 1/2-cell substitution graph is acyclic; the attached finite 2-complex is reduced by three explicit integral 1/2-cell cancellations to 406 relators on one generator, with exact exponents -2 (60), 0 (299), +2 (47). A degree-two cell gives \(\mathbb{RP}^{2}\), and every other even-power attaching loop becomes nullhomotopic. Thus the asserted wedge homotopy type follows, including its integral two-torsion. Direct mod-two, mod-three, and mod-five simplicial boundary ranks provide independent consistency checks. The correctness claim is conditional on the reproducible finite calculations; no unsupported infinite generalization is made.

## Originality — PASS, qualified
The closest motivating primary text, Matsushita (2025), treats general correspondences and graph fundamental groups but does not contain the explicit \(\mathrm{KG}(8,3)\) homotopy computation. Matsushita–Wakatsuki (2023) studies open-neighborhood/dominance dualities, not this closed-neighborhood complex. A known specialized collapse for triangle-free graphs with edge-disjoint four-cycles does not apply because this Kneser graph has distinct four-cycles sharing an edge. The nearest indexed Kneser examples are on different parameters and/or use open neighborhoods, independence complexes or other radii. Multiple exact-formulation searches were executed. The main remaining risk is undiscovered or unindexed equivalent prior work, not an identified stronger covering result.

## Mathematical value — PASS
This is the next naturally four-cycle-rich triple Kneser graph after the square-free odd graph \(\mathrm{KG}(7,3)\). Its ordinary closed-neighborhood nerve has a high-dimensional pure face structure but a nontrivial projective-plane homotopy factor, establishing genuine integral torsion and a sharp non-shellability obstruction. The integral homotopy classification is more informative than field Betti numbers and provides a reproducible comparison between open- and closed-neighborhood Kneser topology.

## Closest literature and remaining limits
The most directly related primary text is arXiv:2511.12608 (relevant v2 sections 1, 3 and 5 inspected). The older arXiv:2312.02639 (v2 sections 1, 4 and 5 considered) addresses different graph complexes. Indexed searches found no exact \(\mathrm{KG}(8,3)\) table or stronger universal theorem that implies this claim. Search cannot establish global uniqueness. Reproduction requires Python 3.10+ and the included complete verifier, not selected log excerpts. The classification does not extend to general \(\mathrm{KG}(n,3)\).

Self-review: passed. Independent audit: not yet performed.
