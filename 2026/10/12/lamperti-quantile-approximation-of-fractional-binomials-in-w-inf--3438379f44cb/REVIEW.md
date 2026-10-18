# Independent mathematical audit

## correctness

PASS

From independent positive alpha-stable S,Sprime, the Tonelli/Laplace identity E[(1+uS/Sprime)^-1]=(1+u^alpha)^-1 holds for u>0. Differentiating the Bernoulli cumulant integral gives Hprime(t)=logistic(alpha t), hence H(t)=alpha^-1 log((1+e^(alpha t))/2). Midpoint Riemann sums yield the same scaled log-MGF Lambda as alpha Bin(N,1/2), and bounded tilted variance plus Chernoff give left/right strict log tails with common rate I. The strictly monotone rate on either side of alpha/2 converts any hypothetical macroscopic quantile separation, including endpoint probability levels, into a contradictory ordering of CDFs. The proof covers real fixed alpha, floor m_N and generalized inverses. Independent numerical quadrature checked the fractional cumulant identity for alpha=0.3,0.5,2/3,0.85 and several positive/negative tilts; finite small-N transport computations only corroborate, not prove asymptotics.

## originality

PASS

The Lamperti stable-ratio distribution is classical, and Tang–Tang formulate the 2/3 strong-Rayleigh sublinear transport question. The claim supplies a new deterministic full-rate Bernoulli construction and upgrades coincident strict large-deviation tails to W_infinity=o(N). No covering statement located in Resultary or examined direct papers; equivalence under alternate stable-mixture terminology remains possible.

## value

PASS

Resolves the o(n) portion of Tang–Tang Open Problem 4.6 for 2/3 Bin(3n,1/2) and gives a constructive answer uniformly across all fixed real scaling 0<alpha<1. A transport-rate theorem with controlled extreme quantiles is a substantive exact solution to the posed asymptotic approximation problem, not moment fitting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
