# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The central identity reduces the estimator error to an independent sum
\[
\frac1n\sum_i c_i(Z_i-p_i),
\]
where midpoint centering places each unknown coefficient in the exactly attainable symmetric interval \([-d_i,d_i]\). Convexity reduces the least-favorable one-coordinate MGF to an endpoint, and monotonicity of \(\sinh(x)/x\) identifies the endpoint whose sign points toward the rarer Bernoulli outcome. Independence then gives the product envelope. The lower-tail envelope follows by reversing endpoint choices. The variance statement is an exact coordinatewise maximization, while the Bernstein inequality is a standard corollary rather than a separate novelty claim.

The algebra was additionally checked by deterministic evaluation of the MGF orientation and of the displayed confidence widths. The verification script reproduces the numerical table in `RESULT.md`.

## Originality

The closest recent source is Freidling (2026), arXiv:2609.18586. Proposition 3.4 treats heterogeneous Bernoulli propensities with a support-only Hoeffding interval and proves midpoint centering minimizes that Hoeffding width. Proposition 3.5 invokes the sharper sub-Bernoulli construction only under equal treatment probabilities. Sandoval et al. (2026), arXiv:2601.11744, likewise provides the common-propensity sub-Bernoulli treatment-effect interval and establishes the improved rare-arm rate.

Midpoint-differenced Horvitz-Thompson estimation is not claimed as new: Aronow and Lopatto (2026), arXiv:2605.20572, prove its minimax squared-error role for bounded finite populations under independent inclusion sampling. Nor is generic concentration for heterogeneous independent inclusion sampling claimed as new: Bertail and Clémençon, arXiv:1610.03776, explicitly note that standard independent-sum exponential inequalities apply directly to unequal-probability Poisson sampling.

The originality claim is therefore restricted to the exact least-favorable two-sided Laplace envelope for the midpoint-differenced two-arm treatment-effect estimator, the rare-arm endpoint orientation and attainment, and the resulting heterogeneous-propensity Chernoff specialization. Searches for equivalent formulations using midpoint-differenced Horvitz-Thompson estimation, unequal-inclusion Poisson sampling, least-favorable Laplace transforms, heterogeneous propensities, and sub-Bernoulli treatment-effect concentration did not locate these statements. The assessment is **to the best of our knowledge**, not a claim of exhaustive literature coverage.

Two older/general sources remain the most plausible residual coverage risk. Särndal, Swensson, and Wretman, *Model Assisted Survey Sampling* (1992), is a broad reference on unequal-probability sampling; its full text was not inspected section by section, so a specialized exponential-transform result could have been missed. Howard et al. (2021), DOI 10.1214/20-AOS1991, develops general sub-Bernoulli and treatment-effect concentration machinery; its general framework is compatible with the Chernoff step, but no inspected statement supplies the exact heterogeneous least-favorable potential-outcome envelope derived here. These risks do not supply concrete evidence of prior coverage.

## Value

The result closes a specific gap between a location-invariant midpoint estimator with a heterogeneous Hoeffding guarantee and sharper rare-arm concentration previously presented for common propensities. The exact envelope is finite-sample, attained, computationally one-dimensional after summing coordinate log-MGFs, and separates structural information from generic concentration machinery. It also makes the rare-arm scaling transparent and gives the exact worst-case variance for the same estimator.

## Limitations

The argument requires independent Bernoulli assignment, known outcome bounds, and fixed potential outcomes. It does not address dependent randomization, adaptive designs, interference, estimated propensities, or variance-adaptive inference. Exactness applies to the worst-case Laplace transform, not to the inverted tail probability itself. The rare-arm asymptotic comparison does not imply uniform dominance over all existing confidence intervals.
