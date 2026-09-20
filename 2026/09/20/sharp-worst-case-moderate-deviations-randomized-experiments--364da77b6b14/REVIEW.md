# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS. The complete-randomization identity reduces the estimation error to a scaled mean of a simple random sample without replacement from the bounded scores \(A_i=(1-\pi)Y_i(1)+\pi Y_i(0)\). Serfling's inequality then gives the stated finite bound. The sharp lower construction uses endpoint-valued sharp-null outcomes, for which the estimator is an affine transform of a hypergeometric count. Stirling expansion of the exact point mass gives the same quadratic exponent as the upper bound. The condition \(nt_n^2/\log n\to\infty\) is sufficient to make prefactors and integer rounding negligible.

For independent fixed strata, the minority-arm Serfling mgfs combine multiplicatively. The resulting denominator has limit \(n\Gamma\). The lower bound uses independent hypergeometric endpoint populations in each stratum; minimizing the sum of stratum quadratic costs subject to a prescribed weighted total error gives \(e_j\propto[p_j(1-p_j)]^{-1}\) and cost \(t^2/\Gamma\), matching the upper exponent. The convexity consequence for heterogeneous treatment fractions was checked separately. Exact hypergeometric calculations support both limiting constants.

Potential failure modes considered included using the wrong arm in the finite-population correction, losing a factor of \(n\) in the stratum weighting, and confusing an MSE minimax claim with a fixed-estimator worst-case tail claim. The record explicitly fixes the difference-in-means estimator and design and does not claim minimaxity over estimators or designs.

## Originality

PASS, to the best of our knowledge, with a material residual risk from older finite-population literature.

Serfling's sampling-without-replacement concentration theorem, Bardenet--Maillard refinements, and Hu--Robinson--Wang finite-population Cramér/moderate-deviation results are prior art. Freidling (2026) already contains a without-replacement representation for the completely randomized treatment-effect error in its appendix and develops complete and stratified finite-sample concentration intervals. Therefore neither that representation nor the generic act of applying a finite-population concentration theorem is treated as new.

Recent treatment-effect work was checked for stronger coverage. Sandoval et al. (2026) establish finite-sample intervals with optimal effective-sample-size order and design-based minimax squared-error lower bounds up to constants. Sudijono, Dobriban and Tchetgen Tchetgen (2026) establish sharp minimax mean-squared-risk theory for binary potential outcomes when the design and estimator are allowed to vary. These are different losses and optimization problems. The sources inspected did not state the exact logarithmic worst-case tail exponent for the standard difference-in-means estimator, its attainment by sharp-null endpoint populations, or the stratified constant \(\Gamma=\sum_jw_j/[p_j(1-p_j)]\).

The strongest residual risk is that survey-sampling, hypergeometric, or permutation-test literature may contain an equivalent worst-case theorem under different terminology. Hu, Robinson and Wang (2007, 2012) are especially relevant general sources. Their accessible statements establish finite-population tail approximations but do not present the bounded-potential-outcome worst-case optimization or the stratified harmonic allocation law. The originality claim is therefore restricted to this randomized-experiment formulation and matching sharpness result, not to generic moderate-deviation machinery.

## Value

PASS. The result upgrades recent rate-level finite-sample theory to an exact bounded-outcome tail exponent for the standard complete-randomization estimator and gives a matching finite confidence bound. The stratified theorem identifies a simple harmonic allocation functional controlling the worst-case tail and yields a direct design implication: unequal stratum treatment fractions degrade this worst-case exponent at fixed overall treatment fraction. It also supplies an exact constant comparison with a recent concentration-based Hoeffding interval.

## Limitations

The asymptotic theorem assumes treatment fractions bounded away from zero and one, a fixed number of strata, and \(nt_n^2/\log n\to\infty\). It does not cover vanishing propensity scores, a growing number of strata, studentized statistics, variance-adaptive procedures, or alternative estimators. The finite Serfling inequalities are consequences of existing finite-population concentration results; the substantive claim is the matching worst-case sharpness and stratified exponent. Older survey-sampling literature remains the main originality uncertainty.
