# Independent mathematical audit

## correctness

PASS

For balanced folds, summing squared held-out errors within each fold cancels the within-fold cross term and yields the deterministic identity \(n\widehat R_K=W+K^2B/(K-1)^2\), with W and B the within- and between-fold sums of squares. Under Gaussian sampling, the standard orthogonal one-way ANOVA decomposition gives independent \(W/\sigma^2\sim\chi^2_{n-K}\) and \(B/\sigma^2\sim\chi^2_{K-1}\). Taking moments gives the stated expectation and variance. Fresh symbolic differentiation verifies \(d[n-K+K^4/(K-1)^3]/dK=-(6K^2-4K+1)/(K-1)^4<0\) for K>1. The inspected exact-rational verifier independently checks the deterministic decomposition and algebra on many balanced designs.

## originality

PASS

Haberman's complete open article explicitly treats the sample-mean predictor and traditional K-fold replication, but says variance evaluation for the improved/K-fold-type estimator is usually difficult; its sample-mean K-fold example does not state the audited weighted independent-chi-square law or the strict fold-count monotonicity. Targeted Resultary searches likewise returned no equivalent exact distribution or monotonicity theorem. The result uses classical ANOVA ingredients, but the exact combined K-fold score law and fold monotonicity were not found as an implication of a stronger inspected theorem.

## value

PASS

Fold-error dependence and the effect of K on cross-validation variability are recurring methodological questions. In the canonical Gaussian location model, the exact score law and strict decrease of its true sampling variance with K cleanly separate dependence-induced failure of naive standard errors from the different question of whether more folds increase the score's variance. This is a motivated finite-sample benchmark rather than an arbitrary calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
