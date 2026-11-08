# Independent mathematical audit

## correctness

PASS

For three circular gaps a,b,c summing to 2pi, direct inversion of the exact degree-one trigonometric moments yields W=(2pi/S)(sin b,sin c,sin a), S=4 sin(a/2)sin(b/2)sin(c/2)>0 on distinct-node configurations. Every weight is positive iff every gap is below pi. Each bad gap is an event that a difference of two iid Uniform[-alpha,alpha] jitters exceeds 1/2, with triangular-tail mass (1/2)(1-1/(4alpha))^2; these three events are disjoint. The exact success probability is 1 for alpha<=1/4, and 1-(3/2)(1-1/(4alpha))^2 for alpha in (1/4,1/2], including 5/8 at alpha=1/2. At endpoint pair-collision cube corners the two singular weights scale as +-3*tan(pi*z/3)/(u+v); two-dimensional (u+v)^(-p) integration gives exactly p<2. The three-corner integral yields the log coefficient 54(2sqrt(3)/pi-1) with uniformly integrable error. Independently checked the moment inversion, triangular tails, tangent-square integral and coefficient; these support the analytic proof rather than replacing it.

## originality

PASS

Austin–Trefethen prove convergence over long perturbed trigonometric grids; Yu–Townsend give deterministic quadrature stability estimates and sufficiently-large-node negative weights. Neither in the inspected full primary text states the iid three-node gap-event probability, endpoint moment threshold, or logarithmic coefficient. Related published SCOPE three-knot cubic interpolation findings use polynomial, not circular trigonometric, weights. This is a best-of-knowledge addition with possible less-searchable old quadrature probability literature.

## value

PASS

The exact distribution of negative trigonometric quadrature weights and the separate endpoint noise-variance breakdown are natural stability questions for perturbed sampling, revealing two distinct critical jitter values 1/4 and 1/2. The model has three points only but this is the smallest nondegenerate periodic trigonometric interpolation rule, with an explicit sharp random probability and heavy-tail exponent useful as a diagnostic for larger-grid claims. It is neither a trivial substitution of polynomial nodes nor just a finite simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
