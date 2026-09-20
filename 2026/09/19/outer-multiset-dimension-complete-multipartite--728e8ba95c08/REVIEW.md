# Review

## Correctness

**PASS.** For a vertex outside the landmark set, its distance multiset in a complete multipartite graph is determined solely by the number of selected landmarks in its own part. This immediately forces at most one omitted vertex per part. Once one vertex is omitted from a part of size \(q\), that part contributes exactly \(q-1\) distance-two landmarks, so omitted vertices from distinct parts collide if and only if the two parts have equal size. This proves the full complement characterization.

The dimension, partition-matroid description, basis count, and generating-function factorization all follow directly from that characterization. The fixed-order spectrum follows from the sharp bound \(1+\cdots+d\le n\) on the number of distinct positive part sizes and an explicit construction attaining every feasible \(d\).

Definition-level exhaustive verification checks all connected complete-multipartite isomorphism types through order eight and agrees with the structural theorem and full enumerator.

## Originality

**PASS, to the best of our knowledge.** The relevant 2023 primary source was inspected directly. It explicitly gives the balanced complete multipartite case and the case of strictly increasing part sizes, but it does not give the arbitrary repeated-size formula. The present result identifies the missing interpolation: only the number of distinct part sizes matters for the minimum, while the entire family of resolving sets is controlled by a partition matroid on the unions of equal-sized parts.

Targeted searches covered the phrases and equivalent formulations “outer multiset dimension” with “complete multipartite,” “outer multiset basis,” arbitrary part sizes, resolving-set counting/polynomials, and matroid formulations. No source located in those searches states the arbitrary-multiplicity classification, the complement partition-matroid structure, or the factored enumerator.

The 2019 foundational paper and the current literature establish the invariant and multiple special families. The 2025 joined-graph work treats selected diameter-two join families rather than arbitrary complete multipartite graphs. The 2026 toroidal-grid work concerns Cartesian products of cycles and does not subsume this theorem.

No specific inaccessible paper was identified whose title or indexed statement materially suggests prior coverage of the arbitrary-multiplicity theorem. Residual originality risk remains from unindexed recent work or older work using substantially different terminology.

## Value

**PASS.** The theorem closes the gap between two complete-multipartite regimes already singled out in the literature: all parts equal and all part sizes distinct. More importantly, it gives a structural mechanism rather than only a dimension formula: complements of all outer multiset resolving sets are precisely the independent sets of a rank-one-per-block partition matroid. This yields exact enumeration of every resolving-set size, a real-rooted factorization, the number of bases, and the complete fixed-order spectrum for the family.

## Limitations

- The theorem is restricted to complete multipartite graphs.
- It does not cover multipartite graphs with missing cross-edges or arbitrary joins.
- Real-rootedness here comes from the explicit factorization and is not claimed for outer multiset resolving-set enumerators of general graphs.
- Finite computation supports but does not replace the proof.
- Residual originality risk remains from unindexed or differently-termed literature.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
