# Self-review

## Correctness
PASS. For a Young sector with first-column length \(h=\lambda'_1\), sectors with \(h\le r\) can never grow an antisymmetric block to size \(r+1\), so the truncated decision has zero error there. For \(h\ge r+1\), the inspected first-column growth bound gives the history-uniform probability lower bound
\[
p_k\ge \frac{r+1-k}{n(k+1)}.
\]
The source's history-dependent stochastic domination and geometric-sum concentration results then imply the stated cutoff \(M_r\), using the exact identity
\[
\sum_{k=1}^r\frac{n(k+1)}{r+1-k}=n((r+2)H_r-r).
\]
Replacing at most \(M_r\) ideal antisymmetric calls by the inspected pairwise-SWAP construction at diamond error \(\varepsilon/(2M_r)\) contributes at most another \(\varepsilon/2\) by a hybrid argument. The proof therefore establishes the claimed binary total-variation bound for every permutation-invariant input. The finite verifier only checks algebraic identities and small partition instances; it is not used to infer the general theorem.

## Originality
PASS. The closest primary source supplies the full unitary-Schur-sampling protocol, the first-column growth estimates, stochastic-domination tools, and the pairwise-SWAP realization, but its stated complexity follows the entire Young diagram and depends on \(d\). Its discussion separately notes that rank testing needs only the first-column length and identifies improved local-dimension dependence as a future direction. O'Donnell--Wright give the one-sided rank tester and its copy complexity, but not a pairwise-SWAP implementation. Searches for rank-threshold, first-column, partial-Schur, antisymmetric-growth, and pairwise-SWAP formulations did not locate the threshold-dependent, dimension-free bound proved here. The main residual risk is a contemporaneous or differently indexed partial-Schur implementation that combines the same ingredients.

## Value
PASS. The result answers a specifically motivated implementation gap: it removes ambient local dimension from the elementary-operation cost of the Schur decision stage used by the optimal one-sided rank tester. The structural reason is nontrivial and reusable: a binary threshold never needs exact bottom-of-column certification or traversal of later columns, and the remaining first-column waiting times have an exact harmonic mean bound. This gives \(\widetilde O(nr^2)\) rather than inheriting the full-diagram dependence on \(d\).

## Closest literature and limitations
The closest sources are arXiv:2610.02103v1 for random-SWAP unitary Schur sampling and arXiv:1501.05028 for the weak-Schur rank tester. The theorem does not claim a new statistical sample-complexity bound, a full Schur instrument, or optimal logarithmic factors. Because the anchor preprint is very recent, a separately indexed equivalent threshold construction remains a literature risk.

Self-review: passed. Independent audit: not yet performed.
