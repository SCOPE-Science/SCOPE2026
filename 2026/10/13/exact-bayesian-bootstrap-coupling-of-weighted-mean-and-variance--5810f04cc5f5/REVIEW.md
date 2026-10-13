# Review
## Correctness
PASS. After centering the fixed data, the random mean is a Dirichlet linear form and the random variance is a linear form in squared observations minus the squared random mean. Uniform-Dirichlet factorial moments determine every required mixed moment. The packaged checker independently expands the polynomials and evaluates their Dirichlet expectations exactly.

## Originality
PASS, with a stated literature risk. Rubin's complete original article defines the Dirichlet-weight construction and treats weighted means, but does not state the joint mean-variance posterior moments. Cheng's complete exchangeably weighted-bootstrap paper studies asymptotic moment consistency and explicitly includes the Bayesian bootstrap, but does not give the finite fixed-data formulas. Exact-phrase and alias searches did not locate the stated covariance or its empirical-skewness sign law.

## Value
PASS. Bayesian-bootstrap users routinely propagate both means and variances. The result gives their exact finite joint uncertainty, shows that the dependence sign is exactly empirical skewness, and supplies a closed posterior variance for the dispersion functional.

## Closest literature and limitations
The theorem uses standard Dirichlet moments as ingredients and is restricted to ordinary \(\operatorname{Dirichlet}(1,\ldots,1)\) weights. An equivalent identity may exist in older unindexed Dirichlet-moment literature. The dated public archive anchor is arXiv:1109.4204, first submitted 20 September 2011.

Self-review: passed. Independent audit: not yet performed.
