# Independent mathematical audit

## correctness

PASS

Both laws give the same individual marginals and the reference A is SPD; the sweep is the stated sequential substitution with independent draws between sweeps. At omega=1 the update eliminates the first input component and the exact second-moment multiplier for the surviving recursion is E[(bc)^2], respectively 64/625 and 136/625; the sharp vector rate follows by conditioning on each fresh draw. At omega=1.87, every trace discriminant is negative and det M=(0.87)^2. I constructed the covariance operator directly on (x²,xy,y²) and independently verified the displayed Lyapunov residual, including both strictly positive leading minors, and the exact positive-definite covariance eigenmatrix with eigenvalue 1.00028424. Conditional quadratic contraction gives exponential stability for shared coupling. The anti eigenmatrix decomposes as a sum of deterministic-start rank-one matrices; its exponentially growing trace forces at least one such start to grow exponentially along a subsequence. The all-start stability criterion is equivalent to covariance spectral radius below one because deterministic rank-one matrices span symmetric matrices. Strict separation, strict spectral stability of the sample matrices and the omega=1 rate ordering persist by continuity. Replay: python3 /workspace/reproductions/finite_checks.py 2; shared omega=1.87 covariance radius is about 0.917477872302 (supplementary numerical value only).

## originality

PASS

The supported distinction is the concrete two-coordinate SOR dependence reversal with fixed coefficient marginals and exact strict certificates. Random-product instability despite individually stable factors and covariance lifting are not new general principles. The strongest accessible conceptual analogue has a different shear-flow law, and the directly relevant mixed-precision SOR passages treat different perturbations and bounds.

## value

PASS

This is a motivated counterexample to transferring the Gauss–Seidel benefit of antithetic coupling to overrelaxed sweeps, even when the individual factor laws are unchanged and every realized sweep is Schur-stable. Exact strict witnesses make the distinction reproducible and robust rather than a barely discernible simulation artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
