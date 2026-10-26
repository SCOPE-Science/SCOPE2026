# Review: Exact two-use majorization for depolarizing channels in every dimension

## Correctness — PASS

The proof reduces mixed inputs to pure Schmidt-form inputs through Ky Fan convexity and local-unitary covariance. Its exact diagonal-plus-off-diagonal decomposition is verified by expanding the two tensor factors. The Gram identity \(I+vv^*-2\Lambda=\sum_{i<j}(\sqrt{\lambda_j}e_i+\sqrt{\lambda_i}e_j)(\cdots)^*\succeq0\) supplies upper and lower spectral controls. On the positive coefficient branch, one eigenvalue is bounded by \(\alpha^2\), all other eigenvalues by \(\alpha b\), and every eigenvalue is at least \(b^2\). On the negative branch, complete positivity gives \(c/b\le1/d\); the operator domination \(|\psi\rangle\langle\psi|\preceq(d/2)(\Lambda\otimes I+I\otimes\Lambda)\) bounds all eigenvalues above by \(b^2\), and the Gram inequality bounds every eigenvalue but possibly one below by \(\alpha b\) and the least one by \(\alpha^2\). The complete Ky Fan inequalities follow by controlling prefixes or complementary suffixes. This covers endpoints and all mixed states. Exact Gram checks and numerical spectral checks were additionally run; finite tests are not the proof.

## Originality — PASS (best-knowledge)

The closest paper, Song et al. [1], explicitly poses the arbitrary-tensor-power exact majorization as a conjecture, obtains log-determinant and approximate majorization, and does not prove the stated two-use case. King [2] proves output Schatten norm multiplicativity, which does not itself imply Ky Fan majorization. Lami–Huber [3] supplies related Schmidt blocks for bipartite depolarizing maps, without the Ky Fan ordering. Targeted queries for two-copy exact majorization, Schmidt spectra, Ky Fan inequalities and the physical negative coefficient regime, as well as a semantic research-record search, revealed no equivalent or dominating result. Comparison is at the statement/implication level. A formally equivalent proof may nevertheless exist outside the inspected corpus; no exhaustive priority guarantee is made.

## Value — PASS

The primary recent paper leaves exact (rather than asymptotic or approximate) majorization open for arbitrary copy count. A complete result for the first entangled two-use case, uniformly in dimension and across the full completely positive parameter interval including \(p>1\), closes a natural nontrivial boundary of that conjecture. Unlike Schatten norm bounds, this directly controls every Ky Fan sum and every Schur-concave output spectral functional simultaneously. It does not claim an arbitrary-copy theorem or a stability gap.

## Primary references and limits

[1] Z. Song, X. Wang, M. Tomamichel, K. Fang, *Approximate majorization and high-order capacity of quantum depolarizing channels*, arXiv:2609.37240v1, 2026, https://arxiv.org/html/2609.37240v1 .

[2] C. King, *The capacity of the quantum depolarizing channel*, arXiv:quant-ph/0204172v2, https://arxiv.org/html/quant-ph/0204172v2 .

[3] L. Lami, M. Huber, *Bipartite depolarizing maps*, arXiv:1603.02158v1, https://arxiv.org/html/1603.02158v1 .

Self-review: passed. Independent audit: not yet performed.
