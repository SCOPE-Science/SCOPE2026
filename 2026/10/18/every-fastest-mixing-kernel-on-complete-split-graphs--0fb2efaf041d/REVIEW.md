# Scientific review

## Correctness — PASS
For each integer \(r,s\ge2\), a group-averaged optimizer first yields an exact scalar optimum and a unique aggregate cross weight. At or below the threshold \(s=2r\), the between-parts Rayleigh quotient saturates the lower spectral bound and forces every row and column sum of the cross block; outer difference vectors then saturate the upper bound and force every cross entry to be equal. Above the threshold, total clique row capacity is saturated, while a compressed trace identity forces the same uniformity. The complete core-face constraints are necessary and sufficient by orthogonal block decomposition. Trace bounds plus explicit feasible constant-offdiagonal cores prove both sharp internal-edge extrema. Exact-arithmetic and symbolic tests in the verification program support the algebra, not the infinite quantifiers.

## Originality — PASS, with residual risk
Boyd et al. (arXiv:0709.0955, Sections 3.1.2 and 5) give the symmetry and complete-bipartite optimum. Jafarizadeh (arXiv:2501.02421, Theorem 1 and Section 6.5) already implies the complete-split **optimal value** through a clique-lift of a star and constructs a particular optimum. Those facts are explicitly treated as prior results, not claimed as new. The present result determines **all** globally optimal kernels, proves cross-block rigidity without an assumed symmetry, and classifies the entire remaining spectral face and edge-mass interval. These all-optima statements are not asserted in the inspected prior theorems. Possible unindexed coverage of equality cases remains a risk.

## Value — PASS
Designing a fastest-mixing chain requires knowing whether an internal communication edge can be retained or must be removed, not just the optimal spectral rate or one example chain. The exact two-parameter complete-split classification settles that choice for every optimizer: core links are unavoidable for \(s<r\), optional for \(r\le s<2r\), and absent from every optimizer for \(s\ge2r\). It also gives a sharp allowable total core traffic interval, including non-invariant optima; the forced equal cross-edge probabilities are an unexpectedly strong structural constraint. These distinctions are not consequences of a mere graph relabeling or a generic numerical SDP output.

## Limits and related literature
The result concerns symmetric, uniform-stationary kernels only. Prior work already settles the scalar optimal value; only the equality-case classification is assessed as new. Published equivalent optimizer-face treatments might have escaped indexing. Numerical tests do not certify infinite families. The mathematical proof is independent of the tests.

Self-review: passed. Independent audit: not yet performed.
