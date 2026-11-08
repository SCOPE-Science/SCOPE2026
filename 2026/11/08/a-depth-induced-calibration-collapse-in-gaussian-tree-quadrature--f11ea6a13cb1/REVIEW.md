# Mathematical assessment: Gaussian quadrature tree calibration

## Correctness — PASS

The local covariance \(1+v\cos(2\pi(t-s))\) is positive semidefinite, and the local integral cancels the sine/cosine components exactly. The leaf Gaussian posterior is obtained by a one-dimensional Schur complement. For a balanced binary node with two independent children, the correct prior covariance is exactly \(mI_2\), and the reported child variance is \(mv/(1+jv)\). Direct insertion into the stipulated pseudo-observation update gives the next denominator \(1+(j+1)v\). This closes the induction for every \(h\ge0\) and every \(v>0\). The normalized root estimation error is exactly Gaussian, with variance computed from two independent normal sums; the coverage asymptotic follows from the normal density at zero. The extracted exact-rational checker corroborates 2,268 finite-depth assertions but is not used as a substitute for proof.

## Originality — PASS, with priority caveats

The motivating Weiland–Karvonen–Hennig paper defines the recursive Gaussian-conditioning update and studies convergence of its integral estimates, but the inspected recombination and theoretical/experimental sections do not establish this depth-dependent unconditional error-to-reported-variance factor or its vanishing credible-interval coverage. Distributed Gaussian-product expert methods can be overconfident (Deisenroth–Ng), whereas the present operation updates sums of *different* subintegrals using posterior means as pseudo-observations. Nested Kriging (Rullière et al.) propagates the covariances of the expert estimators explicitly, a different construction. Searches for hierarchical Bayes quadrature, posterior pseudo-observations, and depth-driven double conditioning in the accessible mathematical record returned no direct implication. General historical Bayesian double-counting observations are a plausible priority risk, and the absence of indexed matches is not a uniqueness proof.

## Value — PASS

Hierarchical quadrature's reported posterior variance is used to assess numerical integration uncertainty and can inform refinement. The exact depth law proves that small reported uncertainty need not indicate calibrated integral uncertainty even when the leaf priors and parent prior covariance are correct. The loss is unbounded and the nominal fixed-width interval coverage tends to zero, so the consequence is structural rather than a tiny numerical discrepancy. The correctly calibrated direct sum in the same construction gives a concrete benchmark for diagnosing the variance-recombination step.

## Scientific limits

This is a family of growing-domain independent-cell priors, not an assertion about real-world adaptive tree selection or the source implementation's default stationary parent kernel. The exact formulas use Gaussian prior-predictive coverage and an oracle parent covariance. A different estimator fusion scheme can avoid the effect. An independent historical-priority check and mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
