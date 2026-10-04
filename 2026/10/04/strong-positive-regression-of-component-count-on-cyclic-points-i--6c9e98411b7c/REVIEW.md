# Review

## Correctness

PASS. Exact forest counting gives the cyclic-point distribution and its birthday-tail form. Conditional on the cyclic set, the permutation on those vertices is uniform, so the component count is the classical independent Bernoulli cycle-count sum. This yields the joint distributional representation and an explicit monotone coupling in the cyclic-point count. The covariance identity follows from tail summation, and the asymptotic constants follow from Rayleigh scaling of cyclic points and exact conditional variance of the permutation cycle count.

## Originality

PASS, with a clearly stated bivariate-generating-function residual risk. The Hansen--Jaworski full text explicitly states the conditional component-count law given the number of cyclic vertices; that premise is treated as prior art. Their 2006 paper treats the separate distributions of cyclic points and components but does not state the increasing-function covariance theorem or the asymptotic covariance constant.

Kupka's classical component-count paper was checked at the abstract/reference level and concerns the marginal distribution and factorial moments of component count. Targeted searches for cyclic-point/component covariance, stochastic regression, and the explicit asymptotic constants did not locate the accepted statement.

## Value

PASS. Cyclic-point count and component count are two canonical global statistics of a random functional digraph. The conditional law turns an intuitive dependence into a strong regression theorem valid for every pair of increasing transforms, and the asymptotics show an unusual scale separation: covariance grows like \(\sqrt n\) while correlation vanishes only at logarithmic rate.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK mappings_checked=873611 joint_cells_checked=83 tail_checks=27 conditional_cycle_checks=83 covariance_checks=24 stochastic_checks=77 variance_checks=12 asymptotic_sanity_checks=8`.
