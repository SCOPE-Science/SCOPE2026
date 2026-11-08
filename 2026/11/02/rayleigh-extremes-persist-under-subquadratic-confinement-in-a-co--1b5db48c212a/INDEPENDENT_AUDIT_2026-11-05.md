# Independent mathematical audit

## correctness

PASS

For each fixed reset age t>0 the inward pathwise drift and last-zero excursion give sup|X| <= range(B) and sup|X-B| <= kappa alpha t range(B)^(alpha-1) for any continuous driver. Brownian range has Gaussian concentration, so with 0<beta=alpha-1<1 the error is bounded by exp(-c x^(2/beta)), superexponential relative to the gaussian exp(-x^2/(4Dt)). Gaussian tail sandwich yields fixed-age log P(X_t>x)/x^2 -> -1/(4Dt). Conditional iid maxima then satisfy m_N(t)/sqrt(4Dt log N)->1 in probability. A common stationary Poisson reset age T~Exp(r), independent of conditional noises, integrates the limiting CDF by bounded convergence to 1-exp(-z^2) under sqrt((4D/r)log N) normalization. Since 1/2-1/alpha<0, the alternative proposed (log N)^(1/alpha) normalization gives zero. The proof never requires uniformity for t growing with N. Independent script checks analytic scaling algebra and finite deterministic inequalities; numerical checks alone are not the infinite proof.

## originality

PASS

The common-reset-age renewal mixture for arbitrary potentials is known in de Mauro–Majumdar–Schehr (2026), and the Rayleigh extreme for free simultaneous-resetting Brownian particles is known in Biroli–Larralde–Majumdar–Schehr (2022). De Mauro Section VII equations 222–228 and Table 1 propose a different (log N)^(1/alpha) scaling for all alpha>1 on simulation/scaling evidence, rather than a proved result. The submitted strictly confining 1<alpha<2 theorem uses a fixed-time superGaussian pathwise drift perturbation and shows the free-gas Rayleigh law persists and the other normalization collapses. A general known sublinear-drift Gaussian large-deviation theorem could potentially imply the fixed-age step, but no covering complete conclusion for the common-reset mixture was identified.

## value

PASS

The theorem settles a proposed but explicitly heuristic universality-class boundary in the contemporary common-resetting model. It demonstrates a mathematically important interchange-of-limits effect: far tails at fixed reset ages can dominate the particle maximum despite a genuine equilibrium confining potential. The exact Rayleigh law and collapse of the competing normalization give a usable sharp asymptotic benchmark across every strictly subquadratic confining exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
