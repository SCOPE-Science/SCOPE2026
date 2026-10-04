# Same-model review

## Correctness
PASS. The graph, primitive vectors, compatibility condition, and acyclicity condition are explicit. For one-dimensional complexes, a closed \(V\)-path is exactly a directed cycle in the selected partial orientation, so the finite face model is equivalent to the ordinary Morse complex. The complete face census is independently reproduced by principal minors of the Petersen Laplacian via the matrix-forest theorem. The reduced mod-2 boundary ranks are computed from the full face set twice with opposite pivot and traversal conventions, and the Betti numbers satisfy the reduced Euler-characteristic check. The claim is deliberately limited to \(\mathbb F_2\)-homology.

## Originality
PASS. The closest ordinary-Morse-complex literature checked gives family-specific homotopy calculations and general connectivity theorems, not the Petersen Betti vector. A recent overview of strong discrete Morse matchings explicitly distinguishes its strong subcomplex from the ordinary Morse complex and lists the comparatively small collection of ordinary cases with known homotopy types; it does not include the Petersen graph. Searches using Petersen, discrete-Morse, gradient-vector-field, rooted-forest, and exact numerical aliases found no statement implying these ranks. Residual risk remains for non-indexed computations or unpublished tables.

## Value
PASS. The Petersen graph is a canonical symmetric cubic test graph, while exact topology of ordinary Morse complexes is known only in limited families. The calculation gives a natural exact invariant beyond connectivity: nonzero reduced mod-2 homology occurs in two adjacent top dimensions, with ranks \(38\) and \(294\). This supplies a reproducible benchmark for future structural results and computations on Morse complexes without claiming a broader theorem than the evidence supports.

## Closest literature and limitations
Donovan–Lin–Scoville (arXiv:1909.11440v1) compute ordinary Morse complexes for selected families and give structural reductions. Scoville–Zaremsky (arXiv:2004.10481v1) provide connectivity results. Knudson–Owens-White (arXiv:2609.06844v1) treat a different strong-Morse subcomplex and summarize the narrow range of ordinary cases whose homotopy types are known. None of these checked statements implies the Petersen mod-2 Betti vector. The present result is finite, graph-specific, and does not determine integral homology or homotopy type.

Same-model review: passed. Independent audit: not yet performed.
