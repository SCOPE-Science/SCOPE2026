# Scientific review: Dirichlet exceedance and power-concentration dependence

## Correctness — PASS

The marginal beta law and conditional neutrality of Dirichlet vectors give the exact conditional mean \(g(x)=x^q+c(1-x)^q\) and covariance tail integral. For every real \(q>1\), strict convexity of \(g\) and the endpoint signs show that the covariance is either positive at every interior threshold or changes sign exactly once, from negative to positive. The monotonicity of \(\Gamma(z+q)/\Gamma(z+1)\) proves the symmetric case. For \(q=2\), differentiation of the proposed beta-density expression recovers the centered integrand, and the boundary value fixes the integration constant. The exceptional boundary \(\theta_i=0\), the \(m=2\) case, and all real positive concentration parameters are covered. A separate integer-parameter checker passed 888 exact-rational comparisons; those finite checks are supplementary, not the proof of the real-parameter theorem.

## Originality — PASS (subject to historical priority uncertainty)

Huillet–Paroissin (arXiv:0809.4181) discuss finite Dirichlet partitions, sampling richness and Simpson-type functionals, but not the random-mass exceedance/covariance transition. Royen (arXiv:1008.4059) gives the marginal law of the squared Dirichlet norm, not its joint exceedance dependence. Goldstein–Reinert (arXiv:1207.1460) give a general beta Stein characterization, a method usable in deriving the quadratic formula, but not the power-sum dependence classification or the exact asymmetric boundary. Closest indexed comparisons concern either empirical categorical richness with a collision statistic or finite-box frequency counts; their sample spaces and observables differ. Earlier covariance of *ranked gap lengths* with squared gap concentration cannot imply a pointwise exceedance-threshold sign law from its integrated values. The original part asserted here is the complete one-switch/no-switch classification, the symmetric all-real-power theorem, and sharp quadratic parameter thresholds, not standard Dirichlet moment or beta integration formulas.

## Mathematical value — PASS

Mass exceedance counts and power sums measure different features of a random composition: how many components exceed a resolution scale, and how concentrated its total weight is. The exact sign transition explains why these natural diagnostics can be negatively correlated at low thresholds but positively correlated at high thresholds. In the broken-stick model it occurs precisely at \(2/(m+2)\), with a nonzero rescaled limit on the natural \(1/m\) spacing scale. The sharp asymmetric three-component boundary \(a=4u+3\) shows that strong dominance of one component removes the reversal. The result covers the entire Rényi power family, not merely an isolated low-order moment calculation.

## Remaining limitations and priority risks

The result is about covariance, not full association, conditional monotonicity, or the power of statistical tests. The asymmetric single-switch theorem applies to a tagged coordinate, not automatically to the sum of unequal-coordinate exceedance counts. Generic beta Stein identities and classical spacing-statistics literature could yield equivalent results under different notation; historical priority is not independently certified. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
