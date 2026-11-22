# Independent mathematical audit

## correctness

PASS

Correct for known Omega>0, gamma>0, N>=1, a single stationary synchronized ensemble snapshot: global Poisson age is Exp(gamma), its observable qubit density is periodic with pi/Omega, so the folded phase phi has h_x(phi)=x exp(-x phi)/(1-exp(-pi x)). Its score is S_x=1/x-phi-pi/(e^(pi x)-1). For any POVM the outcome score is the conditional mean of S_x; Fisher data processing yields F_Q^N<=Var_x(phi)/Omega^2=Omega^-2[x^-2-pi^2/(4sinh^2(pi x/2))]. Alternating local sigma_z/sigma_y means recover (cos2phi,-sin2phi) almost surely as N→infinity, and bounded score L2 martingale convergence proves exact asymptotic attainment without entangled measurements. A z-only count identifies theta=arcsin sqrt(p) and folds phi↔pi-phi with g_x(theta)=x cosh(x(a-theta))/sinh(ax), strictly reducing score variance. Its score is strictly monotone in theta; one additional Bernoulli observation strictly changes the posterior conditional score, proving N-strict monotonicity. Uniform small-x expansions give QFI pi^2/(12Omega^2)+O(x^2/Omega^2) and z-FI pi^4 x^2/(180Omega^2)+O(x^4/Omega^2). Independent clocks give p=2/(x^2+4), FI linear in N with stated coefficient. Replayed 12 finite density-matrix SLD calculations and 25 z-count quadratures; these corroborate but do not prove universal limits. Boundary cautions: fixed positive parameters before N→infinity; one observation of whole array, not repeated time snapshots or gamma→0 jointly with N.

## originality

PASS

Best-of-knowledge distinct sharp model-specific result: generic mixture QFI convexity and the common reset spin stationary law are prior, but the exact attainable stationary single-snapshot gamma-FI ceiling, local y/z saturation, strict z-only loss and pi^4/180 weak-rate coefficient were not established by the materially compared published sources. Direct Resultary searches do find the target itself, excluded as independent prior, and neighboring same-model entries which address different invariants and scalings. The 2026 blind-reset no-go presumes a theta-independent clock and does not cover estimating that clock rate. Residual v1 and unindexed-literature priority risks remain.

## value

PASS

It answers a naturally motivated inference/resource question in an exactly specified globally reset Rabi ensemble: arbitrarily many spatially correlated probes cannot overcome common unobserved clock-age uncertainty. It identifies a sharp saturable ceiling, a feasible two-fixed-axis readout, and a surprising change of small-rate order for the natural z-count readout; independent clocks recover extensive information. The exact constants matter for comparing experimental measurement resources, not merely relabeling classical Jensen. It is a meaningful sharp model classification with honest idealized limitations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
