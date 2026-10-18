# Review of the conditional leaf regression

## Correctness — PASS

The claimed object is the standard uniform recursive tree with \(n\ge2\) labels. A complete four-case attachment partition gives exact finite transition recurrences for \(G_n(u)=\mathbb E[u^{Z_n}]\) and \(H_n(u)=\mathbb E[L_nu^{Z_n}]\). The differential-operator commutator proves \(2H_n=(n-1)G_n+uG_n'\), so coefficient comparison gives the conditional mean on precisely the positive-probability support. No limit or approximate approximation is used in the regression proof. Exact enumeration for all recursive trees with at most nine vertices and rational polynomial checks through twenty-five vertices independently test the calculations. Correlation is stated only when \(n\ge3\), where both variances are positive.

## Originality — PASS, subject to historical-priority risk

The exact marginal \(Z_n\) distribution is **not new**: the fixed-point/rencontres law follows from the singleton-root-branch generating function in Seelbach Benkner–Wagner (arXiv:2105.04231, Section 5.2). This marginal by itself supplies neither the mixed transform \(\mathbb E[L_nu^{Z_n}]\) nor the conditional expected total leaf count. Their primary result concerns the number of distinct fringe subtree shapes, not this regression. Janson (arXiv:2005.13832, Example 12.4) gives scaled metric limits, not the claim. Devroye–Janson's work on protected nodes and branching-process fringe trees discusses a Poisson-aged root-child limit, not the exact finite-size mixed identity. The closest previously published recursive-tree covariance statement compares *all root children* with leaves, rather than the number of root children that remain leaves; it neither implies the regression nor identifies its conditioning classes. Named alternate formulations (singleton root branches, size-one root fringe subtrees, terminal root children, rencontres fixed points, mixed leaf marking) were checked.

Residual risk: a bivariate increasing-tree generating function, a permutation/tree bijection refined by leaves, or older distributional work may imply the same conditional regression without using these names. The full content of all possible older sources was not exhaustively accessible; novelty is a documented best-knowledge assessment rather than a priority certificate.

## Value — PASS

The result exactly connects a natural *local* motif count—root branches of size one—to the *global* leaf count at every size and every feasible observed value, with a universal slope \(1/2\). It supplies conditional prediction and exact covariance/correlation, substantially stronger information than marginal Poisson convergence or covariance with the root degree. This is a coherent local/global structural identity, not an arbitrarily selected numerical instance.

## Limitations

The proof does not identify the full conditional distribution or its conditional variance and does not extend to attachment weights depending on vertex degree. The marginal rencontres identity is credited to prior enumeration; only the mixed conditional relation is assessed as a new finding.

Self-review: passed. Independent audit: not yet performed.
