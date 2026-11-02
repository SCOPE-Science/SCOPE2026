# Scientific review

## Correctness — PASS

The finite decrement factorial moments are obtained by exact adjacency contraction; Brown--Peköz--Ross establish the unit-Poisson stochastic domination needed for a monotone quantile coupling. The gap compensator has logarithmic second moment, yielding \(O(\log n)\) error in both total and idle counts. The renewal vector has an elementary iid Gaussian limit with the covariance matrix displayed in RESULT.md. Stopping-time and overshoot estimates, plus \(L^2\) control, justify transfer of weak and second-moment limits. The packaged checker passes 159 assertions. The principal risk is the careful transfer of the two joint coordinates, addressed by the explicit indicator inequality and stopped-martingale estimates.

## Originality — PASS, subject to historical-priority uncertainty

The 2008 original paper already provides one-round Poisson domination and a one-dimensional coupling, and the 2023 preprint already provides the completion-time CLT; neither is claimed here as a new result. We inspected the available full texts and compared their implications with the present theorem. Neither establishes the joint idle/total limit or the explicit idle variance and cross-covariance, which do not follow from their univariate conclusions. Earlier work on succession-count distributions studies a different observable. A related 2016 completion-time paper was identified but its complete text could not be inspected; this leaves a specific residual priority risk, not evidence of noncoverage.

## Value — PASS

Idle rounds quantify wasted randomization, a natural performance statistic for the original chemical coalescence model. Their joint fluctuations and strong positive correlation with total running time are not determined by the marginal completion-time Gaussian law. The explicit limiting covariance and strong bivariate renewal approximation support joint uncertainty calculations and distinguish idle from productive steps in a natural stochastic algorithm.

Self-review: passed. Independent audit: not yet performed.
