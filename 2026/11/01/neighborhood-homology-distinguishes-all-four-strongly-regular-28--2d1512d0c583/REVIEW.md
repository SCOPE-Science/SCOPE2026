# Scientific review: neighborhood homology of the four \((28,12,6,4)\) graphs

## Correctness — PASS
The graphs arise from a fully specified \(28\)-vertex triangular graph and three exact Seidel switches. For each graph the verifier checks all strongly regular pairs, enumerates every simplex twice by independent routines, and performs every boundary rank computation over \(\mathbb F_2\) without sampling or floating point. All Euler–Poincaré identities hold. A separately implemented low-pivot rank calculation after \(49150,50538,51041,50161\) actual elementary collapse pairs agrees with the original full-complex calculation. The classical Chang classification certifies that these four representatives exhaust the entire \((28,12,6,4)\) graph family. No inference beyond the finite parameter class or mod-two coefficients is made.

## Originality — PASS against inspected evidence
The closest same-invariant published calculation, *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, treats triangular graphs through \(T_7\) only and explicitly makes no assertion about \(T_8\) or any Chang graph. Matsushita–Wakatsuki provide foundational Alexander duality but not these numerical homology groups. Fröberg's open-access article addresses algebraic Stanley–Reisner resolutions for other graph families. Chang-graph encyclopedic and software references classify the graphs and switching classes, not their topological homology. Indexed scientific-record searches for Chang, triangular \(T_8\), and Hom aliases did not reveal an implication-equivalent theorem. This is a best-knowledge literature comparison, not proof of global novelty; an unindexed equivalent calculation remains possible.

## Value — PASS
This is a complete, motivated four-class topological classification in a canonical cospectral family. Although graph degree, intersection parameters, spectrum, and number of vertices agree, the four open-neighborhood complexes have four different mod-two homology signatures, proving pairwise distinct homotopy types. The distinction is an exact natural invariant, not a numerical increment for an arbitrary chosen graph. Integral homology and the spaces' individual homotopy decompositions remain open within this work.

Self-review: passed. Independent audit: not yet performed.
