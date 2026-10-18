# Scientific review: reverse-direction two-neighbor rank covariance

## Correctness

**PASS (self-review).** The null reduces exactly to a uniform permutation, and the Lin–Han boundary convention gives the explicit sum of two edge-distance terms plus three terminal rank appearances. The proof decomposes edge arrays into the constant, vertex-score and zero-vertex-score components; it justifies the associated two-dimensional matrix-coefficient orthogonality using the three-dimensional commutant of unordered edge pairs. This determines both the ordinary variance and the covariance with the inverse permutation without assuming independent directions. The vertex-boundary cross terms are explicitly calculated, including the exact cancellation of cross-direction edge/boundary terms. The final rational moments and the unique \(n=5\) maximum follow by algebra and a positive-coefficient shifted polynomial.

The embedded checker passed 5,915 exact assertions. It exhaustively enumerated every permutation for \(n=4,5,6,7,8\), separately rebuilt edge projections for \(4\le n\le40\), and checked rational correlation inequalities through \(n=500\). These finite checks are supplementary to the all-\(n\) argument.

## Originality

**PASS on inspected sources, with historical uncertainty.** Lin–Han, *On boosting the power of Chatterjee's rank correlation* (arXiv:2108.06828, equation 2.4 and Section 3), supplies the underlying \(M\)-neighbor statistic and marginal null analysis but does not give its opposite-direction joint second moment at \(M=2\). Zhang, *On the asymptotic distribution of the symmetrized Chatterjee's correlation coefficient* (arXiv:2205.01769, Lemma 1 and Section 4), computes inverse-direction moments for the *original* Chatterjee coefficient and expressly leaves the multineighbor case \(M\ge2\) for future work. Zhang, *On the extensions of the Chatterjee-Spearman test* (arXiv:2406.16859, Sections 2.1–2.2), combines the original coefficient with other rank statistics, not the Lin–Han two-right-neighbor inverse pair.

The known pair-representation decomposition and Lin–Han's one-direction variance are not claimed as new. The mathematical contribution assessed here is the explicit **joint** finite-sample covariance, correlation shape and sharp \(10/n\) coefficient for \(M=2\). Semantic mathematical-record searches found related inversion/precision results and population Chatterjee-functionals but not this implication. Own accessible findings include a bound on the lower support endpoint of the same statistic; that bound neither specifies nor implies its reverse-direction covariance.

The possibility of an implicit equivalent in general permutation quadratic-assignment moment identities, or of another unindexed later article, remains. This same-model finding has not been independently certified for historical priority.

## Value

**PASS.** An inspected primary paper identifies the multineighbor reverse-direction problem explicitly. Finite-sample joint moments are necessary to understand dependence between directional measurements, especially when forming symmetric max-type statistics. The exact correlation is unexpectedly very high for small \(n\), has a unique peak at \(n=5\), and decays with a computable universal leading coefficient. This is a motivated and fully quantified special case \(M=2\), not a cosmetic renaming of the \(M=1\) calculation. No full joint central limit or finished test calibration is inferred from covariance alone.

## Limitations

The result requires independent atomless marginals and the published self-replacing right-neighbor convention; it has no claim for dependent samples or \(M>2\). The exact formula does not establish any asymptotic joint normality. Further independent scientific review and broader historical comparison remain to be done.

Self-review: passed. Independent audit: not yet performed.
