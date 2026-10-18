# Independent mathematical audit

## correctness

PASS

The source Algorithm 5 with f(w)=w^2/2, h>0, fixed eta>0, q i.i.d. Rademacher rank-one candidates, and first-sampled minimizer tie rule has candidate score w*xi+h/2. From each positive lattice site n=w/eta, the inward probability is 1-2^{-q}, outward probability p=2^{-q}; reflect at negatives, with unbiased departure from zero. For q=1 this is simple random walk and E f(w_t)=eta^2*t/2. For q>=2 detailed balance gives pi_0=(1-2p)/[2(1-p)] and pi_{+/-n}=(1-2p)[p/(1-p)]^{n-1}/[4(1-p)^2]; summing the second moment yields E_pi[N^2]=1/[2(1-2p)^2], hence a.s. objective Cesaro mean eta^2/[4(1-2p)^2]. Finite q yields irreducible positive recurrence; period 2 precludes claiming pointwise law convergence from zero. Constant nonzero increment precludes sample-path iterate convergence. Independent exact-rational detailed-balance, normalization and second-moment checks q=2..10 corroborated the algebra; the infinity-time statements rest on Markov recurrence and ergodic theory, not finite replay.

## originality

PASS

The source explicitly observes that fixed-step always-move direct structured search need not decrease its objective and proposes acceptance control. This theorem is a distinct exact specialization: invariant birth-death distribution and sharp nonvanishing ergodic objective level on a strongly convex scalar quadratic. The Roberts–Royer probabilistic descent algorithm uses rejection and step shrinkage, hence does not entail the same chain. Closely related Markov counterexamples under other terms remain a residual priority risk.

## value

PASS

A naturally motivated defect of an actually printed always-move search rule is quantified completely, beyond the immediate fact that nonzero constant increments prevent convergence: the exact ergodic floor, dependence on q, q=1 random-walk regime, and limit eta^2/4 distinguish directional-sampling improvements from step-size stabilization. Source specificity is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
