# Scientific review: Morse complex of \(K_{3,4}\)

## Correctness — PASS

The face criterion agrees with Forman's acyclic incidence matching on the graph. Two independent enumerations yield 12,800 faces and agree with the characteristic polynomial of the graph Laplacian. An exhaustive matching with 6,181 pairs is proved acyclic by a topological sort of the entire directed Hasse graph on 12,799 nonempty faces; critical dimensions are 0, 4 and 5, with counts 1, 2 and 434. The full integral Morse-boundary computation exhibits a determinant-\(-1\) two-column minor and therefore cancels both four-cells; the remaining 432 five-cells give the asserted wedge. Signed alternating fixed-simplex traces for all 144 automorphisms and exact irreducible character inner products prove the 15-class representation. Separately the mod-two top simplicial boundary has rank 2592 of 3024 columns. `verify_morse.py` and `verify_character.py` reproduce every critical computation. This is a complete finite proof, not an experimental extrapolation.

## Originality — PASS

The primary source (Scoville–Zaremsky, arXiv:2004.10481, §4.1 Example 4.6) discusses complete bipartite Morse complexes and leaves exact homotopy types untreated, giving connectivity estimates only. The directly relevant earlier graph-family homotopy paper arXiv:1909.11440 and directed-tree shellability work arXiv:1109.4475 do not imply the stated graph and character calculation. Published closest exact calculations cover \(K_{3,3}\) or \(K_{2,n}\); the named two-matching complex of \(K_{3,4}\) is a fundamentally different simplicial construction. Other possible directed-forest equivalents were searched. Residual risk: an unindexed equivalent computation may exist, and certain similar published records were accessible as scientific summaries only, not in complete text.

## Value — PASS

This is a complete homotopy classification for a natural small complete bipartite graph lying outside earlier known parameter families, motivated by a specific published gap. Beyond the 432 top Betti rank, the full rational \(S_3\times S_4\) representation provides 15 character values and their precise irreducible decomposition. The two-degree integral Morse reduction is itself a useful reproducible example of nontrivial attaching-map cancellation. No statement is made for other bipartite parameters or equivariant wedge structures.

Self-review: passed. Independent audit: not yet performed.

