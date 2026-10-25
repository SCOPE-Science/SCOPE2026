# Scientific review of the induced-forest graph-complex comparison

## Correctness — PASS

The exact definitions fix the Shrikhande Cayley connection set and the rook adjacency relation on the same sixteen labels. The reproducible verifier independently tests induced acyclicity with both union-find and depth-first cycle detection on every subset, constructs all simplicial incidences, and topologically sorts the orientation of the complete Hasse graph induced by a deterministic face matching. Its critical-cell vectors are \((2,143,36)\) and \((4,37,72)\) in dimensions four to six. Signed integral projection of all critical attaching boundaries gives zero in degree six-to-five, and a maximal unimodular minor in the five-to-four differential for each graph (determinants \(+1\) and \(-1\)). The CW attaching-map argument justifies the *homotopy* wedge conclusions. Independently constructed ordinary simplicial mod-two boundary ranks corroborate the resulting Betti numbers; modular ranks alone are not used to establish integrality.

## Originality — PASS, qualified

The closest directly relevant pre-existing framework is Taylan's general graph devoid complex (arXiv:1501.06754v1) and the explicit vertex-induced forest filtration studied by Carnero Bravo (arXiv:2307.13271). Inspected definitions, stated classification domains and relevant graph-family theorems do not give the claimed Shrikhande or rook results. Indexed records for the same two graphs classify *different* complexes (ordinary/higher independence, triangle-avoidance, neighborhood and graph Čech complexes). None implies the homotopy of the complex that forbids **every** induced graph cycle. Searches under cycle-hypergraph independence, feedback-vertex-set complexes and acyclic vertex-subset complexes did not identify an exact or dominating result. The residual risk is equivalent unindexed or uninspected prior work; absence from search is not proof of uniqueness.

## Value — PASS

The two canonical nonisomorphic strongly regular graphs have identical local numerical parameters, exactly thirty-two triangles and induced-forest cardinality cutoff seven, but their entire integral homotopy decompositions differ in **both** nonzero dimensions. This is a complete computation of a natural filtration endpoint associated to feedback vertex sets, not an arbitrary subgraph statistic or a restatement of the already known distinction between their independence complexes. The explicit integral, torsion-free wedge decompositions are useful to distinguish graph-derived topology beyond Betti-number parity and graph parameter counts. The result is finite and does not assert a new classification theorem for an infinite family.

## Closest sources and limits

- D. Taylan (2015), arXiv:1501.06754v1, Sections 3–5: general devoid-complex construction and matchings; graph families differ.
- A. Carnero Bravo (2023), arXiv:2307.13271, Sections 3–4: induced-forest filtration, paths, cycles, stars, cactus graphs and product families; this pair is not a covered classification case.
- Previously available results on the Shrikhande/rook independence and triangle-avoidance complexes: mathematically distinct face predicates and homotopy statements.
- An equivalent calculation outside indexed or inspected material remains possible; no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
