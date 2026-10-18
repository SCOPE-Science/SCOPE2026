# Independent mathematical audit

## correctness

PASS

Poisson thinning makes each coupon stream independent rate p_i. Given continuous cover time T=t and last-arrival type J=j, others have independent zero-truncated Poisson counts of means a_i=x_i/(1-e^-x_i) and singleton probabilities q_i=x_i/(e^xi-1), while stream j has one point. Last-type weights w_j=q_j/sum q. Conditional covariance equals sum (1-w_i)q_i(1-a_i)+Cov_w(a_i,q_i)<0 by opposite monotonicity of a and q. The conditional means n(t) and s(t) are respectively strictly increasing and decreasing, as derivatives prove; total covariance then strictly negative. All m>=2 and all positive p; no independence claim for N and S. Independent exact rational first-step recurrence checked 56 small positive weight vectors and sampled unequal cases.

## originality

PASS

PASS best-of-knowledge: uniform coupon N,S joint law of Myers-Wilf covers the uniform corollary, but unequal-probability cover-time laws of Brown-Pekoz-Ross and Anceaume-Busnel-Sericola and fixed-draw occupancy work do not supply the terminal mixed moment or universal covariance sign. Relevant Resultary reset-coupon work concerns a different stopping mechanism. General nonuniform joint law remains possible but unlocated.

## value

PASS

PASS: the strict negative dependence law is a natural exact multivariate stopping-time invariant for heterogeneous coupon collection; extending uniform joint distribution to all strictly positive probability vectors provides a useful monotonicity/association fact not inferred from cover-time marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
