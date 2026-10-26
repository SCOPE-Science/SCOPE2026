# Scientific review: exact multiscale covariance spectrum of fair knockout scores

## Correctness — PASS
The object is the complete binary single-elimination tree on \(n=2^\ell\) equal-strength players with independent fair winners. Survival indicators at distinct bracket levels have exact joint probabilities: they are independent before the common ancestor and mutually exclusive when both require its win. Their double sum gives the proposed negative covariance kernel. For one player, nested survival gives the exact variance. Dyadic subtree Haar contrasts diagonalize this kernel and form a complete orthogonal basis with one constant null mode. Explicit eigenvalues are strictly ordered and positive; the extremal contrast inequalities and condition number follow. Uniform reseeding makes the deterministic score multiset exchangeable. Dominated convergence of spectral log-products gives the generalized-variance limit. The standalone checker enumerates all outcome assignments for brackets of 2, 4, 8 and 16 players and passes 1,085 exact rational assertions; asymptotic numerical diagnostics are supplementary. No finite test is used as an infinite proof.

## Originality — PASS, with residual risk
Adler–Cao–Karp–Peköz–Ross (2016; arXiv:1612.04448) discuss knockout structures and win probabilities; Malinovsky–Rinott (2022; arXiv:2206.08461) analyze tournament-score negative dependence; Su–Zou–Hu (2025; arXiv:2505.01971) establish negative association of fixed fair brackets and correct an earlier counterexample claim. Negative correlations and score-vector dependence are therefore not claimed as new. The compared accessible texts do not state this dyadic covariance eigenspectrum, its sharp all-contrast bounds, or the ratio \(3/4\) of asymptotic geometric-mean generalized variances. Formula-equivalent or stronger results under hierarchical covariance terminology remain a publication-priority risk. A tangential bracket-design paper (Glickman and Hennessy, 2016) was available only in abstract and was not used for a whole-text negative conclusion.

## Value — PASS
The exact eigenspectrum identifies which scoring contrasts are most and least variable, with a sharp condition number of \(3n-2\ell-3\). It resolves a natural quantitative gap left by earlier qualitative negative-dependence results and compares fixed versus randomly seeded bracket uncertainty through a nontrivial universal determinant ratio. The tree-specific hierarchy and all-size sharpness make the claim more than a restatement of pairwise negative covariance.

## Limits and status
The result does not address byes, unequal strengths, weighted outcomes, adaptive formats or independence beyond second moments. Historical originality is not certified; independent scientific audit remains necessary before external reliance.

Self-review: passed. Independent audit: not yet performed.
