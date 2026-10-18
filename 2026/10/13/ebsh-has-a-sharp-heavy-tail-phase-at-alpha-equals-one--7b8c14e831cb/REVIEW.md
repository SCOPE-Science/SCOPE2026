# Independent mathematical audit

## correctness

PASS

The exact EBSH CDF is sinh(a(1-exp(-x^alpha))^theta)/sinh(a), a=pi/2, alpha,theta>0. Put u=exp(-x^alpha). The two Taylor expansions (1-u)^theta=1-theta*u+O(u^2) and sinh(a(1-theta*u+O(u^2)))=sinh(a)-a*theta*cosh(a)*u+O(u^2) give S(x)~(a*theta*coth(a))*exp(-x^alpha). Differentiating the published exact density supplies f(x)~C_theta*alpha*x^(alpha-1)*exp(-x^alpha); their ratio gives h(x)~alpha*x^(alpha-1). Direct exponential-integral comparison of exp(tx-x^alpha) gives the exact MGF trichotomy, including divergence at t=1 for alpha=1; log S(x+y)-log S(x) tends to zero for 0<alpha<1. Integrating powers and inverting the quantile give all positive polynomial moments and Q(1-q)~(log 1/q)^(1/alpha). Independent 80-digit evaluation of three distinct regimes corroborated all normalized asymptotic ratios; those evaluations are not the infinite proof.

## originality

PASS

The 27 May 2026 defining EBSH paper provides the formula but explicitly labels the whole family light-tailed because it sees an exp(-x^alpha) factor. That statement is incorrect under the positive-MGF criterion when alpha<1. The inspected survival and density sections, Section 3.1 tail paragraph, and quantile section do not supply the C_theta equivalent, hazard equivalent, or exact alpha-dependent MGF domain. The bounded parent law cannot supply unbounded-tail asymptotics. Stretched-exponential generalities predict the phase after substitution but do not themselves correct this published parameter-uniform assertion.

## value

PASS

The all-light-tailed characterization is published for a model used in reliability, survival analysis and medical datasets, yet is false for the entire nonempty alpha<1 parameter region. The exact survival multiplier, the true domain of positive exponential moments, and hazard/quantile regimes together give a mathematically sharp and potentially necessary correction for selecting tail-risk models; their motivation is not merely an arbitrary asymptotic exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
