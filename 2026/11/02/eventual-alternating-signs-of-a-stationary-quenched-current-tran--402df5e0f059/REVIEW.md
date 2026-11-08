# Independent mathematical audit

## correctness

PASS

Both reset Brownian and reset run-and-tumble stationary opposite-side probabilities are U(x)=e^{-kappa x}/2, with kappa=sqrt(r/D) or sqrt(r(r+2gamma))/v. Spatial integration of the log product gives exactly G_lambda(z)=exp[-lambda Li_2((1-z)/2)]. The unique dominant unit-circle singularity z=-1 has expansion G=e^{-lambda pi^2/6}[1-(lambda/2)(1+z)log(1+z)+analytic linear term+O_lambda((1+z)^2 log^2(1+z))]. Coefficient transfer gives (-1)^(n+1)lambda e^{-lambda pi^2/6}/[2n(n-1)]+O_lambda(log n/n^3); positive prefactor gives eventually negative even n for each fixed finite lambda>0. Pringsheim forbids a positive integer-valued PGF, while periodicity under p->p+2pi i forces any nonnegative-measure Laplace representation to lie on N, also impossible. Differentiation gives c2 and threshold (1-log2)/log^2 2. Independent high-precision recurrence confirms c2 and negative c120/positive c119 for lambda 0.4 and 2. The statement is about a formal geometric-ensemble transform, not physical conditional particle probabilities.

## originality

PASS

Qualified PASS for proving all-fixed-positive-lambda eventual coefficient sign alternation and literal PGF/Laplace nonrealizability of the original dilogarithmic formal expression. Di Bello et al. (2023) already derived the exact dilogarithm and called it the stationary quenched current generating functional; no discovery credit for model, transform or cumulants. The original paper does not state the sign obstruction in the read original Sec IV (Eq. 56–58).

## value

PASS

A mathematically meaningful positivity obstruction to interpreting a widely used geometric-ensemble cumulant functional as a literal finite-lambda distribution, with an all-parameter sign-tail asymptotic and an explicit small-lambda negative-coefficient witness. This distinguishes formal large-deviation transforms from actual Poisson-binomial probabilities without rejecting any physical fixed-configuration law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
