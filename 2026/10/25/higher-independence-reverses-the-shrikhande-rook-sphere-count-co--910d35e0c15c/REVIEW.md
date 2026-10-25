# Scientific review of the two-independence comparison

## Correctness — PASS
The vertices, edges, face predicate, matching order and oriented Hasse-diagram convention are all explicit. A complete executable check enumerates all 65,536 subsets for each graph, tests equivalent degree and forbidden-triple predicates, verifies the face counts, constructs the entire partial matching and proves its acyclicity by exhaustively topologically sorting the reversed matched-incidence graph. The resulting new critical multisets are one zero-cell plus 57 three-cells (Shrikhande) and one zero-cell plus 105 three-cells (rook). Forman's CW theorem gives the integral homotopy wedge directly; this is stronger than a rational-homology assertion. The independent Euler calculation agrees. Reproducibility and face-count limitations are detailed in `VERIFICATION.md`.

## Originality — PASS, with residual risk
The most direct indexed prior comparison already proves the *ordinary* independence sphere wedges with ranks 23 and 15. That theorem does not imply the new degree-two homotopy types: the allowed induced vertex configurations change, and neither conclusion identifies the higher attaching maps. Primary papers on higher independence complexes treat complete multipartite graphs, whiskering, paths, cycles, perfect rooted trees or chordal graphs; neither exceptional strongly regular graph is in those families. Both graphs contain induced four-cycles, excluding the chordal hypothesis. Relevant exact, alias, reduction and database searches found no covering degree-two theorem. An unindexed or inaccessible equivalent computation remains a genuine priority risk; failed search is not proof of absolute novelty.

## Value — PASS
The pair is the complete exceptional ambiguity for strongly regular parameters \((16,6,2,2)\). Its ordinary independence Betti ranking is \(23>15\), while the new exact integral topological ranking is \(57<105\). This reversal is a motivated comparison of two canonical graph complexes, not an arbitrary induced-subset slice or a known-table recomputation. The acyclic matchings moreover establish the full homotopy type of two nonpure higher-independence complexes, not just their Euler characteristics.

## Limits
The result is confined to the stated pair and to \(r=2\), with the \(r=1\) computation retained as prior-work context. No general strongly regular-graph classification or equivariant representation is claimed. Publication priority cannot be guaranteed, and an independent scientific audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
