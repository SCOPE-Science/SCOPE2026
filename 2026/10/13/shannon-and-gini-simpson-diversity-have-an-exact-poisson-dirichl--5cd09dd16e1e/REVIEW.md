# Review

## Correctness

PASS. The central mixed identity is derived from the equal-index and distinct-index decomposition of two Poisson–Dirichlet power sums. The distinct-index term is reconstructed directly from the first two independent beta stick-breaking factors, so it does not depend on an unverified formal differentiation.

The mixed moment is analytic around the required exponents. Differentiating it at the Shannon endpoint gives the exact mixed logarithmic moment. Subtracting the independently known marginal means simplifies to
\[
\operatorname{Cov}(D,H)
=
\frac{\theta+\alpha}{(\theta+1)^2(\theta+2)}.
\]
The variance of Gini–Simpson diversity follows independently from the same mixed power-sum identity at equal quadratic exponents. The Shannon variance used for correlation agrees with the inspected entropy literature.

The packaged checker compares two independently programmed mixed-moment routes over a broad parameter grid and checks the asymptotic correlation formula.

## Originality

PASS, with a specific residual risk. Cerquetti's full paper is the strongest same-family source inspected: it provides separate marginal moments for Tsallis and Shannon diversity under Gnedin–Pitman and Poisson–Dirichlet priors, but its theorem statements and proofs do not state the Shannon/Gini–Simpson cross-covariance.

Archer, Park, and Pillow provide the full size-biased derivation of Shannon entropy moments but do not treat Simpson or Gini–Simpson diversity. Recent Gini–Simpson inference work identifies Shannon and Gini–Simpson as standard companion indices but develops the latter rather than their joint law.

A prior finite-simplex finding on Greenwood concentration and spacing entropy is not covering: it concerns a finite \(\operatorname{Dirichlet}(1,\ldots,1)\) vector whose total concentration grows with dimension, whereas the present theorem concerns the infinite two-parameter Poisson–Dirichlet family and includes a discount parameter and a distinct exact covariance law.

The remaining risk is that an older Poisson–Dirichlet source may have recorded this derivative consequence of classical mixed power-sum machinery under different notation.

## Value

PASS. Shannon and Gini–Simpson diversity are canonical, complementary measures of evenness. Their separate means and variances are routinely used in Bayesian nonparametric diversity analysis, so their exact cross-dependence is a natural missing joint quantity.

The result is stronger than a sign observation. It gives a closed finite-parameter covariance and an explicit nonzero limiting correlation, showing that increasing concentration shrinks both fluctuations without asymptotically decoupling the two indices. That distinction matters when both indices are reported, combined, or used as partially redundant summaries.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK mixed_checks=30 covariance_checks=60 variance_checks=90 correlation_checks=30 asymptotic_checks=5 dirichlet_limit=0.8804959104761448`.
