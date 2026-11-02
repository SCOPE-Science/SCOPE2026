# Scientific review

## Correctness — PASS

The claim is a fully quantified theorem for positive harmonic coefficients, symmetric \(1<\alpha<2\) stable noise, and masses up to critical damping. The stationary impulse kernels follow from the two negative characteristic roots and the double-root limit. Their \(L^\alpha\) norms are derived by a beta substitution, with the gamma quotient and critical endpoint checked algebraically. The decisive nonstandard step is strict positivity of the mass derivative: the digamma difference has a Laplace integrand involving \(\sinh((\alpha-1)t/2)/\sinh(t/2)\), strictly below \(\alpha-1\) for every positive argument. This proves strict monotonicity on the complete interval, not merely at sampled parameter values. Matching coupling and \(|x|\)-test bounds produce exact \(W_1\); the analytic Taylor expansion yields its sharp nonzero linear coefficient. The included standard-library checker passes 197 finite assertions, but the universal claim is established by the written argument.

## Originality — PASS, qualified

The prior 2017 harmonic stable oscillator paper already establishes the impulse-response and stationary scale-integral representation. This is openly reused, not relabeled as new. Jin–Tao (arXiv:2610.32217v1) prove a general \(m^{1/\alpha}\) bound, and Baldovin–Guéry-Odelin–Trizac (arXiv:2207.09357v1) analyze harmonic characteristic functions and control. Their inspected texts do not state the complete strict mass-inflation theorem or its sharp \(W_1\) derivative. General gamma-quotient inequalities, as surveyed by Qi–Agarwal (2019), may cover the auxiliary special-function inequality, but do not by themselves identify the oscillator's stationary position response. The distinction depends on a new normalization and implication comparison, not a title search. Historical-priority review is still needed.

## Mathematical value — PASS

This is a motivated exactly solvable test case for the 2026 general invariant-measure approximation problem. It proves a systematic, strictly signed inertia effect throughout the entire nonoscillatory range; establishes the exact Wasserstein distance; identifies a sharp order-one improvement in the small-mass exponent; and explicitly distinguishes the non-Gaussian regime from mass-invariant Gaussian equilibrium. The result says nothing about nonlinear drift, oscillatory masses, or finite \(W_1\) for stable indices at most one.

## Residual risks

The underlying stable integral and harmonic Green functions were known. A more general special-function monotonicity theorem could imply the gamma quotient inequality, and unlocated stochastic-oscillator work might already state the same mass effect. The finite checker is corroboration rather than a certificate for real-parameter quantifiers. Nothing has undergone independent validation.

Self-review: passed. Independent audit: not yet performed.
