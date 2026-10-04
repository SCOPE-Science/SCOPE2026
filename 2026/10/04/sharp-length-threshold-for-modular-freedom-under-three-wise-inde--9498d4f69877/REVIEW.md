# Review

## Correctness

PASS. Three-wise independence is reduced exactly to the first three factorial
moments of the Hamming weight. For a fixed residue class, scaling by the modulus
reduces the construction to an integer-valued variable with prescribed mean,
variance, and zero third centered moment. The lower lattice variance is proved
by a nonnegative cubic polynomial on the integer support and is attained by an
explicit three-point law. A separate four-point law has the same mean and zero
third centered moment with variance at least \(2/3\); convex interpolation
therefore hits the required variance at \(n=q^2+2\). The lower-bound argument
uses a nearest-lattice variance obstruction below \(q^2-1\) and explicit
cubic obstructions at the three remaining lengths.

The decoded standalone checker replayed the package with:
`VERIFY_OK construction_cases=20094 support_points=100075 pairwise_obstruction_checks=173558 third_moment_boundary_checks=591`.

## Originality

PASS, with a stated residual coding-literature risk. The inspected 2012
limited-independence paper establishes the general Boolean-function/moment
framework and treats functions such as majority, but does not state modular
Hamming-weight freedom or a quadratic-plus-two coordinate threshold. The
inspected 2012 discrete three-moment paper gives exact bounds for tail events,
not support on arithmetic progressions. The inspected orthogonal-array work
studies minimum row counts and simplicity, a different extremal parameter.

Targeted semantic and web searches over three-wise independence, binary
orthogonal arrays, Hamming-weight congruences, fixed residue support, and
modular Bernoulli sums did not locate the statement or an implication that
dominates it.

## Value

PASS. The result gives a natural exact cutoff for when third-order independence
ceases to constrain an entire nonmonotone statistic: above the sharp first
feasible length, the full probability simplex on Hamming-weight residues is
available. The proof also identifies the precise role of the third centered
moment in delaying the modular-freedom threshold beyond the second-moment
lattice barrier.

Same-model review: passed. Independent audit: not yet performed.
