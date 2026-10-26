# Scientific review

## Correctness — PASS
The i.i.d. scalar-curvature assumptions are explicit. Expanding conditional squares yields the exact three-dimensional covariance recurrence and its characteristic polynomial. For positive momentum, a positive real root lies strictly above the best SGD factor, by the exact negative-polynomial and square-completion argument; for zero momentum, a single strictly convex quadratic gives its unique optimizer. The discrete Lyapunov equation and positive rank-one resolvent establish both directions of the stability criterion, including the boundary. The minibatch formulas follow by exact variance calculation. `verify.py` supplies 1,152 independent exact path-sum moment checks and 168 exact characteristic-polynomial/stability checks; it is supplementary rather than an infinite proof.

## Originality — PASS (priority uncertainty remains)
The 2026 Garg–Dereziński paper addresses acceleration upper bounds over interpolation quadratics, not a sharp all-distributions scalar no-momentum-gain theorem. Kidambi et al. (2018) treat a distinct two-dimensional adverse regression instance. Paquette–Paquette (2021) use high-dimensional asymptotic models. Kamo–Iiduka (2025) study nonconvex gradient-norm bounds and growing batches. Loizou–Richtárik (2017), Remark 4, already find their *sufficient upper convergence bound* deteriorates with momentum, but do not prove the exact actual-rate optimizer or sharp scalar all-batch frontier. Searches for scalar second-moment minimax, alternative stochastic-heavy-ball terminology, exact minibatch stability, and related published mathematical records did not identify equivalent implication or stronger coverage. Classical random-linear-recursion theory remains a specific priority risk; absence of a search result is not proof of novelty.

## Value — PASS
The question is motivated by recent general momentum parallelization theory: which part of acceleration requires spectral heterogeneity rather than merely variance reduction? The theorem resolves the exact obstruction for every nondegenerate scalar iid curvature law, proves a unique optimizer in both algorithmic parameters, and exposes a sharp finite-batch stability cost as the momentum coefficient approaches one. It is a natural structural boundary for interpreting theory and tuning momentum, not an arbitrary numerical instance or a reparameterization of an existing table.

## Limitations
Uniform mean-square, iid nonnegative curvature, fixed nonnegative momentum, fixed step, and a shared interpolation minimizer only. Neither general multidimensional Hessians nor Nesterov updates are covered. Earlier literature may express the same result in different stochastic-recurrence language; independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
