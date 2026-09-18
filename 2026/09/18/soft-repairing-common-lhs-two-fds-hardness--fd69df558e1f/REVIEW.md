# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The reduction was checked directly from the soft-repair cost definition. With all facts sharing one A-value, the two violation counts are
\[
\binom{s}{2}-\sum_v\binom{x_v}{2}
\quad\text{and}\quad
\binom{s}{2}-\sum_c\binom{y_c}{2},
\]
so their sum is exactly
\[
s^2-\frac12\sum_vx_v^2-\frac12\sum_cy_c^2.
\]
For the constructed incidence graph every right degree is at most two, giving \(\sum_c y_c^2=s+2z\). These identities yield the stated utility
\[
U=(W+1/2)s-s^2+\tfrac12\sum_vx_v^2+z.
\]

The cardinality-locking argument was checked at both possible failure points. For \(s=qD_0+t\ne rD_0\), maximizing the left square-sum subject to the degree cap gives \(qD_0^2+t^2\), and the resulting base-value gap is at least \((D_0+1)/2=m+1\). At \(s=rD_0\), every nonsaturated integer degree vector loses at least \(D_0-1=2m\) in base value. Since the shared-right bonus always satisfies \(z\le m\), neither type of deviation can be optimal.

For a union of \(r\) full stars, the degree-square part is constant and \(z\) is exactly the number of original graph edges induced by the chosen \(r\) vertices. The decision threshold therefore distinguishes an r-clique exactly. The construction size and weight bit lengths are polynomial, and the threshold version is in NP.

A compact finite checker exhaustively evaluates the reduction on a three-vertex path and a triangle and reproduces the predicted optima. This is supporting evidence only; no finite computation is used in the general proof.

## Originality

The 2024 ACM Transactions on Database Systems version of Carmeli, Grohe, Kimelfeld, Livshits and Tibi explicitly lists \(\{A\to B,A\to C\}\) among the simplest FD sets for which the complexity of soft repairing is open. The same article explains why this set cannot simply be replaced by the logically equivalent single FD \(A\to BC\) under soft semantics.

Exact and synonymous searches were made for the FD pair, common-left soft functional dependencies, soft-repair hardness, and later work citing the Carmeli et al. paper. No published resolution of this case was located. The currently indexed journal article still presents the case as open. The most directly relevant 2026 citing work located, by Guo, Chen, Yang and Miao, improves approximation for soft repairs (giving ratio 2 for FD violations) rather than classifying this fixed FD set exactly.

Meunier and Onn (arXiv:2608.05827, 2026) prove that the fixed-cardinality sum-of-degree-squares problem is NP-hard even for bipartite graphs and discuss related quadratic degree-sequence optimization. That result is relevant but does not settle the present database problem because soft repairing has no externally prescribed selected cardinality. The new step here is the uniform-weight cardinality lock that forces every optimum to be a union of exactly r full incidence stars.

The originality assessment is therefore to the best of our knowledge. A later, simultaneous, or poorly indexed resolution of the same open FD set remains the principal residual risk.

## Value

The theorem closes a named open classification case for soft functional dependencies and separates it sharply from the tractable single-FD case \(\{A\to BC\}\), despite logical equivalence under hard semantics. The restrictions in the theorem show that hardness is not caused by varying FD weights, multiple A-blocks, or heterogeneous fact weights.

The result does not determine the optimal approximation factor and does not prove hardness for unit fact weights.

## Review status

The proof, literature comparison, and stated limitations support acceptance under the Phase II standard. No independent validation is asserted.
