# Independent mathematical audit

## correctness

PASS

For v=Ag and w=A²g the trace is the scalar regression slope of Ψᵀw on Ψᵀv through the origin. Orthogonal regression conditional on g gives the stated independent normal/chi-square ratio, with location vᵀw/||v||² and scale |det(v,w)|/||v||². Scale is positive almost surely and bounded, so location cannot remove the positive-moment divergence at p≥s. If Q=ε²Y²/(X²+ε²Y²), half-Cauchy integration gives E Q=ε/(1+ε); differentiation gives E Q(1−Q)=(ε/2)d(E Q)/dε. This recovers E Q², Var(μ)=E τ² and, with E W_s⁻¹=1/(s−2), the stated moments and strictly positive variance limit. Integrating the chi CDF at zero against Z_+ gives k_s, with a uniform power bound yielding the two bounded-mixture tail limits. For the anisotropy limit, the exact rescaled half-Cauchy integral is E τ^s/ε=(2/π)(1−ε)^s∫₀^∞ u^s/[(1+u²)^s(1+ε²u²)] du, using u=|X/Y|/ε. This supplies integrable domination and the beta constant for s>1; for s=1 partial fractions give 2ε log(1/ε)/[π(1+ε)] for E τ. The normalization in the Student ratio is 1/√s relative to standard Student-t.

## originality

PASS

The generalized Nyström formula and the conditional Gaussian regression ratio are established ingredients. The supported distinct result is their trace-specific angular mixture analysis, in particular the exact signed-tail scale transition and residual right-sketch variance. No matching or dominating statement was identified in the bounded comparisons.

## value

PASS

A minimal positive-definite model isolates left-sketch noise from right-sketch variation. The thresholds distinguish an undefined absolute mean, finite mean without variance and finite variance; the positive variance floor shows why left oversampling alone cannot stabilize all fluctuations. The sharp anisotropic scale identifies an additional borderline regime that bounded-moment estimates do not show.

The dated certificate retains the supplied scientific assessment, sources and limitations.
