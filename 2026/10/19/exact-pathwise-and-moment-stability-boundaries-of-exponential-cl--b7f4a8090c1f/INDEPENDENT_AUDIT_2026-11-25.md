# Independent mathematical audit

## correctness

PASS

Split integration by parts about c=1/xi gives the log-integral identity: the two logarithmic boundary terms at c cancel in the limit, and the principal-value primitive for exp(-x)/(x-c) is exp(-c) Ei(c-x). The log multiplier has finite positive variance (the logarithmic singularity is square-integrable), and Ei is strictly increasing from negative to positive on (0,infinity). The strong law gives the knot exponent, and the centered law of the iterated logarithm gives both critical knot extremes. The absolute value of the linear interpolant is bounded by the larger adjacent knot magnitude, while the clock strong law gives the same asymptotic time per step at both ends; evaluating at the knots gives equality for the physical-time limsup. Independent overshoot events have constant positive probability, giving infinitely many zero crossings, not a full logarithmic limit. The knot log-moment function is strictly convex, has right derivative equal to the log exponent at zero, and is unbounded above (the multiplier exceeds some fixed number greater than one with positive probability). Below critical xi it has one positive zero (constant moment there); at and above critical xi all positive absolute moments grow. Direct integration verifies the first absolute and squared moments; growth of the signed mean above xi=2 refers to its magnitude, with alternating sign. No moment result for the interpolant is inferred. Independent 60-digit split quadrature and root finding reproduced xi_c=2.68451035082070765250…, p_*(1.2)=1.45320882793830844306…, and the exponent signs at xi=1.2 and 2.7. These are numerical corroborations, not probability limit proofs.

## originality

PASS

The model, signed mean and second moment are already known. The supported distinct contribution is the evaluated almost-sure boundary, including critical and physical-time behavior, and the all-real-order absolute knot moment frontiers. This is a judgment from scoped statement comparisons, not proof of priority.

## value

PASS

For the existing exponential-step integrator, the exact comparison of second-moment, first-absolute-moment, signed-mean and pathwise boundaries distinguishes incompatible numerical guarantees. In particular there is a nonempty range where typical trajectories decay while all positive integer absolute moments grow. The critical and interpolated-path classifications resolve what the exact boundary means. This is a useful scalar benchmark, not a guarantee for nonlinear or vector integrators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
