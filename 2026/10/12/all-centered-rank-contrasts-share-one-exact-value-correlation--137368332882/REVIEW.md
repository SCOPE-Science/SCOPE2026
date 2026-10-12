# Review
## Correctness
PASS. The diagonal rank-value covariance follows from the classical identity \(G=4\operatorname{Cov}(X,F(X))\). Exchangeability and the deterministic rank sum force the off-diagonal covariance. The resulting cross-covariance matrix is scalar on the zero-sum subspace, and the usual permutation covariance of ranks gives the matching variance. The two-sample formula is an exact contrast specialization. Exact rational enumeration independently confirms the uniform cases, and a rational beta-family replay checks the sharp Gini-variance envelope.

## Originality
PASS, with a specific historical-literature risk. The closest accessible full-text source reproduces Stuart's exact correlation between one observation and its own rank, but does not formulate the full centered-contrast operator or its isotropy. A complete article directly comparing t and Wilcoxon procedures contains no exact joint null covariance. Targeted searches under matrix, contrast, rank-score, Mann-Whitney, and Gini formulations did not locate the final theorem.

The strongest residual risk is classical linear-rank literature: the 1954 historical paper itself was not available in complete text, and the short matrix reduction may have appeared under different notation.

## Value
PASS. The result is not a single special-case covariance: it classifies the entire centered contrast space. It yields an allocation-invariant exact null correlation for Mann-Whitney versus the raw mean difference and a sharp uniform-parent extremum, giving a finite-sample quantitative bridge between rank and value procedures.

## Closest literature and limitations
The closest literature separately supplies the one-coordinate rank-value formula and broad empirical comparisons of rank and mean-based tests. The theorem assumes atomless iid observations with finite nonzero variance and deterministic zero-sum linear contrasts. It does not address ties, nonlinear rank statistics, studentization, or power under alternatives.

Self-review: passed. Independent audit: not yet performed.
