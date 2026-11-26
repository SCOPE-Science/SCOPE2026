# Independent mathematical audit

## correctness

PASS

Exact Taylor expansion on the quadratic gives error (h/2) B diag(Q^T C Q), with B=B0 Q. Orthonormality gives the squared-diagonal loss, even in a proper subspace. The diagonal sum is the trace; equality in the lower Cauchy–Schwarz bound requires equal diagonals, attainable by successively choosing a unit Rayleigh quotient at the mean and compressing to its complement. The Frobenius bound is attained by an eigenbasis. Normal fourth moments, divided by E||g||^4=k(k+2) for a standard Gaussian g whose direction is independent of its radius, give the claimed Haar risk. For every fixed designer law, Haar averaging of the adversary's orientation makes U^T Q Haar for each Q and yields the same lower bound; a Haar designer attains it for every U. Column sign symmetry cancels the mean vector, not its squared norm. Averaging signed differences gives centered differences in expectation at the same realized evaluation cost, and the third-derivative remainder has norm at most Mh^2 sqrt(k)/6. The trace-zero criterion and rank-one ratios follow directly, including k=1. A new exact check used a non-coordinate two-plane in R^3 and all four sign choices plus exact integration on the circle for k=2.

## originality

PASS

The estimator, balanced diagonal, Haar moments and invariant averaging are not new. The supported distinct contribution is the sharp basis-selection analysis for this estimator, in particular the exact minimax risk over orientation-independent frame laws for the fixed-spectrum quadratic problem. No inspected comparator states it or entails it by a parameter substitution alone.

## value

PASS

The projected one-sided estimator is a pre-existing evaluation primitive. This analysis answers a natural design question with fixed evaluation budget: span alone does not fix the error, a trace-zero compressed Hessian permits an exact choice, and Haar sampling attains the explicit price of not knowing eigendirections. The rank-one factors give a concrete attainable separation rather than just a smoothness estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
