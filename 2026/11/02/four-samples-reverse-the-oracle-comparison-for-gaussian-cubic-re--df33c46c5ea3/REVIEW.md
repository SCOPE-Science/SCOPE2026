# Review: Four samples reverse the oracle comparison for Gaussian cubic regression control variates

## Correctness
PASS. The fitted-intercept formula follows by centering the Gaussian sample. Independently distributed sample mean and residual direction/radius reduce the variance to Wick and chi-square moments. The closed risk is validated by algebraic reconstruction and 1,790 independent exact-rational checks. The sign criterion is a polynomial strictly positive for all integer sample sizes from four onward. Finite simulation is supporting evidence only.

## Originality
PASS, with publication-priority uncertainty. Portier and Segers (2018) already identify the OLS intercept estimator and its first-order oracle asymptotics. Leluc et al. (2022) analyze the general control-variate quadrature estimator with other nonasymptotic hypotheses. Blanchet et al. (2023) focus on split-sample nonparametric regression. No examined result implied or tabulated the cubic-Gaussian finite-sample risk or its four-sample sign reversal; general OLS formulas by themselves do not resolve this exact quantitative comparison. A previously unpublished or unindexed matching computation cannot be excluded.

## Value
PASS. The first nontrivial odd Hermite component creates a canonical finite-sample testbed for regression-adjusted integration. It exposes a precisely classified reversal of the widely used population-optimal fixed-coefficient comparison and quantifies the crossover for every sample size, without claiming that OLS outperforms every estimator.

## Scientific scope and limits
Independent standard Gaussian samples, one linear control, cubic-plus-linear integrands and exact least-squares arithmetic only. Full-information deterministic integration, separate pilot training, cross-fitting, other sampling laws and larger control spaces are outside the claim. No independent scientific validation is asserted.

Self-review: passed. Independent audit: not yet performed.
