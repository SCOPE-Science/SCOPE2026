# Independent mathematical audit

## correctness

PASS

For dX=Vdt, dV=-gamma Vdt+sqrt(2D)dW with velocity-only Poisson resets, conditional Brownian increments over each reset interval give a Gaussian X_t with random variance A_t=sum q(T_j)+q(age), q(s)=2D/gamma^2[s-2(1-e^-gamma s)/gamma+(1-e^-2gamma s)/(2gamma)]. Hence kappa_4(X_t)=3 Var(A_t)>0 for t>0: no-reset and exactly-one-reset histories have positive probability and distinct A_t by strict convexity/superadditivity of q. For exponential inter-arrival T, centered reward q(T)-cT with c=r E q(T), the stopped-martingale/renewal argument yields Var(A_t)/t -> r E(q(T)-cT)^2; straddling-interval L2 remains bounded, so its variance contribution is o(t). Exact exponential integrals yield the stated K4 rate, c=4D/[(r+gamma)(r+2gamma)], and H(r/gamma). Differentiation gives H’=-6P/prod(beta+j)^2, P=7 beta^6+56 beta^5+116 beta^4-160 beta^3-959 beta^2-1344 beta-648. Descartes one sign change, P(0)<0 and P(infty)>0 prove exactly one positive maximizer; rational bracket (2.556536,2.556537), endpoint limits 0. Separately computed exact exponential reward integrals at gamma=D=1 and reset ratios 1/2,1,3, the normalized ratio, derivative and bracket; checks agree. No finite calculation was used to extrapolate the universal theorem.

## originality

PASS

The reset OU area is the same stochastic process as the observable integrated Ornstein-Uhlenbeck state in Meylahn–Sabhapandit–Touchette (2015); their general SCGF/renewal pole formulation already implies access to asymptotic cumulants by formal differentiation. Olsen–Löwen (2024) give the velocity-only reset propagator, recursive moments and diffusivity. Accordingly neither the model, renewal identity, nor implicit moment-generating information is new. The assessed final claim is the explicitly evaluated dimensionless fourth-cumulant coefficient, finite-time strict positivity, and especially the unique all-rate non-Gaussian correction optimum characterized by the degree-six polynomial. The inspected earlier source sections did not state an optimal-kurtosis reset ratio. This is a qualified O pass for a sharp optimized consequence, not priority for the underlying SCGF.

## value

PASS

The normalized fourth cumulant quantifies how velocity resetting changes finite-observation non-Gaussianity while diffusivity remains asymptotically linear. Its exact dependence on r/gamma and a single global optimal rate furnish a natural transport tradeoff across all D,gamma>0. The positive finite-time cumulant and both vanishing extreme-rate limits make the sharp optimizer mathematically informative; the result is not a numerical optimum of an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
