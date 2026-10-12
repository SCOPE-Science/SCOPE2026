# Review

## Correctness

PASS. The proof starts from the exact Dirichlet mixed-moment formula and obtains every logarithmic factor by differentiation with respect to an exponent. Equal-index and unequal-index contributions are kept separate. After substituting digamma identities, the mixed moment reduces algebraically to the stated rational covariance. Two further second-derivative calculations give the entropy variance, while the Greenwood variance comes from fourth-order Dirichlet moments.

The asymptotic correlation uses the standard tail expansion of \(H_{m+1}^{(2)}\). Its leading entropy-variance coefficient is \(\pi^2/3-3>0\), so the limiting normalization is nondegenerate.

## Originality

PASS, with a residual risk from general Dirichlet-moment literature. Royen's full public manuscript gives exact distributional representations for the Dirichlet square sum and Greenwood's statistic but contains no entropy, Shannon, or covariance statement in targeted full-text searches.

Classical spacing papers treat general sum-functions asymptotically. L'Ecuyer's full article studies log-spacing and square-spacing tests separately, but the log statistic there is the unweighted sum of logarithms, not Shannon entropy of the normalized spacing vector.

The closest own result on the same Dirichlet model pairs Greenwood's statistic with maximum spacing. It has a positive covariance and correlation tending to zero; it does not imply the present global-evenness covariance or its nonzero limiting correlation.

## Value

PASS. Greenwood dispersion and Shannon entropy are canonical opposing summaries of concentration and evenness on the simplex. The exact covariance gives a finite-sample quantitative relation between them, while the limiting correlation shows that the dependence remains very strong after standardization even though the raw covariance vanishes.

The contrast between covariance decay and a nonzero limiting correlation is useful when the two statistics are considered as competing diagnostics of spacing irregularity.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK dimensions=200 identity_checks=800 asymptotic_checks=7 limit=-0.92868785736691`.
