# Review

## Correctness

PASS. After normalizing the observable spectral measure to a probability law, the two known autocorrelations are its first two moments. Factoring
\[
1+\lambda
=
\sqrt{\frac{1+\lambda}{1-\lambda}}
\sqrt{1-\lambda^2}
\]
and applying Cauchy--Schwarz gives
\[
(1+\rho_1)^2
\le
\tau_g(1-\rho_2).
\]
The equality condition forces all spectral mass away from \(-1\) to a single point. Solving the two moment equations gives the stated \(q\) and weight.

The four-state symmetric transition matrix realizes the equality spectrum exactly for every feasible two-lag pair. The recalibrated lazy construction preserves both target moments exactly and proves the aperiodic sharp-infimum statement.

## Originality

PASS, with a residual classical moment-problem risk. The full accessible Häggström--Rosenthal source was inspected at the spectral-measure and asymptotic-variance formulas and at its comparison theorem. Longla's full arXiv text was inspected at the spectral representation and variance-integrability discussion. Berg--Song's full arXiv HTML was inspected at the autocovariance moment representation and paired-sequence framework.

Those sources provide the ingredients and broad spectral setting but do not state the two-lag lower envelope, its equality fiber, or exact finite-state realizability for every feasible \((\rho_1,\rho_2)\). Exact-formula and alias searches also did not locate the raw-autocovariance inequality.

## Value

PASS. In reversible MCMC, asymptotic variance and integrated autocorrelation time determine Monte Carlo efficiency, while the first few autocorrelations are often the most stable dependence summaries available. The theorem gives the best possible guarantee obtainable from the first two lags alone, strictly improves the one-lag Jensen bound whenever \(\rho_2>\rho_1^2\), and identifies exactly when the floor is attainable versus only approachable under aperiodicity.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK generic_checks=20000 equality_checks=36000 matrix_checks=48000 lazy_checks=60000 one_lag_checks=20000`.
