# Independent mathematical audit

## correctness

PASS

For the stated fixed real trial line, the Gaussian projections on u and (Au-mu*u)/beta are independent. After normalization by ||Su||, the dot product with the second projection has conditional law N(0,1) independent of V=||Su||^2, giving rate mu+beta*Z/sqrt(V) and the shifted Student law. The sign event is Z<0 and V/(V+Z^2)<beta^2/(mu^2+beta^2), which gives the half-beta expression, independently of sign, and V/ell tending to one gives convergence in probability. For p,t>0, conditioning on V and doing the normal integral gives E exp(-pt*Lambda)=exp(-pt*mu) E exp((pt*beta)^2/(2V)); this is infinite at V=0 under any finite chi-square degrees of freedom. A reused Euler multiplier raised to power 2k is comparable to |Z/sqrt(V)|^(2k) in the tails, so the inverse-chi-square integral converges exactly for ell>2k, with logarithmic divergence at equality. The same infinite second moment holds for the error relative to any deterministic finite comparator, by a triangle bound. In the independent case Tonelli factors the nonnegative product; no factor has zero expectation for beta>0 and h>0. For ell>2 the one-step expectation is (1-h*mu)^2+h^2*beta^2/(ell-2), strictly below one exactly on the stated interval and equal to one at the positive endpoint. The diagonal example and deterministic beta=0 exception agree. The uploaded script was read, not executed; finite samples can check scales/quantiles but not moment divergence.

## originality

PASS

Pass for the explicit dynamical comparison of frozen and independent-refresh Euler, particularly the independent mean-square frontier, not for the Gaussian sign law, the shifted-Student rate, or the sketched projected equation. An earlier same-rate reciprocal calculation is mathematically very close and makes the frozen-law consequences short deductions. A later Resultary exponential record substantively overlaps the exact-time portion, independently of its date, but neither it nor the earlier records give the two Euler reuse conventions and their different boundaries. No inspected source covers the combined Euler stability result.

## value

PASS

The same unconditional Gaussian sketch at the same finite row count and step size can have a decaying second moment under independent refresh and an infinite one after finitely many steps under reuse. The sharp refreshed stepsize ceiling and the precise reuse cutoff determine where this happens, which neither a high-probability embedding statement nor a negative-rate probability decides. The distinction concerns a fixed rank-one model, not a prescription for higher-rank algorithms or computational cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
