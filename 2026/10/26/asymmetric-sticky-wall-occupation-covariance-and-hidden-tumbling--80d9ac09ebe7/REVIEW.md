# Scientific assessment

## Correctness — PASS
The stochastic process, stationary law, generator domain, and all time-normalizations are explicit. A bounded two-component Poisson corrector gives the exact integrated Green--Kubo covariance matrix. SymPy checks the generator identities and symbolic covariance formulas; separate upwind finite-state chains converge toward the analytic matrix for three unequal-release parameter sets. The finite chains are not substituted for the general proof. The inverse map follows directly from strictly positive stationary masses and the strictly decreasing affine cross-covariance in the bulk reversal rate.

## Originality — PASS, with priority risk
Bressloff's first-public 2023-02-02 sticky-wall paper develops occupation-time transforms but its explicit joint transform in Section 5 uses identical release rates at the two walls. This earlier symmetric transform can in principle generate the symmetric specialization of the current covariance; no originality is claimed for the symmetric generating-function subcase. Angelani (2023) handles unequal wall rates, but evaluates exit-time quantities rather than stationary residence-fraction cross-covariances. The assessed full unequal-wall covariance, strict global anticorrelation, and reconstruction of an otherwise invisible bulk reversal rate were not identified in the inspected literature or in the accessible prior records. Because general two-wall renewal formulations might contain an equivalent statement, external priority confirmation remains warranted.

## Scientific value — PASS
Unequal surface reactivity is a natural confining-interface parameter, and mean surface occupancy alone cannot reveal the rate of bulk direction reversals. An explicit measurable cross-fluctuation that is strictly monotone in that hidden parameter gives a motivated structural identifiability result, not just a finite table or a nominal algebraic restatement. The proof also classifies the global sign and sensitivity of the two-wall temporal covariance for every positive parameter combination.

## Scope and risks
The findings assume stationarity, Markovian wall release, homogeneous Poisson reversals, no absorption, and known speed and interval length. The result is population-level; sampling errors and noisy estimators are not treated. Exact priority of asymmetrically sticky wall occupation fluctuations has not received independent scholarly assessment.

Self-review: passed. Independent audit: not yet performed.
