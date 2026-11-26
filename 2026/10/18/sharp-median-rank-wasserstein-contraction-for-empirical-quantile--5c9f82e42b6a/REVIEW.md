# Independent mathematical audit

## correctness

PASS

At data locations and pair midpoints the order of absolute residuals may change; between them each component of the clipped direction has slope +1 or −1. At least k have slope +1, including those tied at the active threshold, and continuity across all breakpoints gives the global Lipschitz and mean secant bounds. In the common-index squared difference, the linear-in-step term is bounded using that mean secant and the quadratic term using component Lipschitz continuity. One-step finite-second-moment preservation follows by linear growth; lifting the coupling to arbitrary input laws and applying completeness proves the asserted uniqueness in P2 and geometric convergence (including the zero-factor one-step case). On the witness interval (0,L/2) the two possible updates are (1−η)x, (1+η)x with masses k/m, (m−k)/m; their order is the same for all positive x, even when η>1, so the cost is exactly the squared-W2 optimum, not just a synchronous upper bound. At k=m the ordinary quadratic update is a translate of a fixed atomic law and all pairs attain the deterministic factor, also for genuinely two-location data. When k≤m/2 both support locations of the witness have k or more repeats and are absorbing. The fair binary affine example preserves uniform measure and its finite-time point-start laws have TV distance exactly one from it. Outside the uniform step window the result excludes strict one-step contraction, not necessarily long-term convergence. The finite exact tests in verify_empirical_qc.py were inspected, not rerun; its sharpness tests check a synchronous cost, whose optimality is separate and follows from the ordered witness.

## originality

PASS

The distinct core is the exact data-uniform majority-rank and step criterion for strict one-step W2 contraction with its sharp coefficient and witness; neither Wasserstein analyses of constant-step SGD, nor quantile clipping, nor the elementary Bernoulli affine example are credited as new mechanisms.

## value

PASS

An exact attainable stability boundary for a canonical finite-data quantile update is useful for interpreting rank rounding and selecting steps. At or below the threshold the worst-case obstruction is genuine nonuniqueness, while the loss of a strict uniform one-step rate at large steps is a separate statement. The examples make these distinctions and the difference between Wasserstein and TV mixing concrete. Scope is deliberately the equal-curvature scalar model, not a performance claim for private or approximate-quantile methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
