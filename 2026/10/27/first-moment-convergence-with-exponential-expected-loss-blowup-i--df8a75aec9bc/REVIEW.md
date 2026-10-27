# Self-review

## Correctness

PASS. The exact scalar SPAM gradient update and proximal map produce the displayed two-client transition matrices. Their individual characteristic polynomials have roots strictly inside the unit disk. Directly expanding the averaged characteristic polynomial and applying the strict quadratic Jury inequalities establishes first-moment convergence throughout the given open interval. On an independent alternating-client event of probability \(4^{-n}\), exact two-step eigen-decomposition gives a nonzero coefficient on a mode of modulus \((b-2)/4>2\), hence a rigorous exponentially increasing positive contribution to expected squared error. The rational witness \(b=14\) is checked independently. No simulation is used as a substitute for universal algebra.

## Originality

PASS on accessible evidence. The SPAM source introduces the updates and gives general sufficient guarantees and empirical refresh effects, but the inspected algorithm, stated results, and appendix do not identify this expected-loss divergence in a first-moment-stable parameter family. The closest archived exact SPAM result addresses the first moment only, explicitly excluding claims about second moments. The new statement is not implied by that result: it constructs and analyzes a rare alternating-client product and its growing mean-square contribution. Published Loopless SVRG and PAGE stability classifications concern different algorithms. A residual risk is an equivalent stochastic-switching-matrix analysis elsewhere in the literature.

## Value

PASS. The same strongly convex two-client instance simultaneously exhibits individually stable component dynamics, exponential decay of the entire expected optimizer state, and exponentially increasing expected physical loss. The open interval and explicit integer example distinguish a structural mean-versus-mean-square failure from a finely tuned isolated numerical anomaly. This supplies a sharp qualitative warning about applying first-moment or frozen-client stability to the numerical reliability of momentum variance reduction.

## Scientific limitations

No conclusion about almost-sure instability or a complete mean-square frontier is established. The example lies outside a global bounded-gradient-variance assumption and beyond the conservative source guarantees. Independent validation and priority review have not been performed.

Self-review: passed. Independent audit: not yet performed.
