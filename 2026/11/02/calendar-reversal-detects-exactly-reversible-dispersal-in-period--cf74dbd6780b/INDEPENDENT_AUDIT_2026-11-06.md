# Independent mathematical audit

## correctness

PASS

Assume irreducible column-stochastic P, n>=2, and arbitrary strictly positive diagonal season matrices. Detailed balance symmetrizes P by a positive diagonal similarity, and transposition plus cyclic determinant identity makes all reversal products isospectral, including singular factors. Conversely concentrate seasons at each vertex of any directed simple cycle length 3..n; at epsilon=0 the period product has rank<=1 and spectral radius equal to the oriented product of P entries. Equality for each k and all positive seasons forces equality of forward/reverse cycle weights, symmetric support by irreducibility, and Kolmogorov path-ratio detailed balance; length-1/2 cycles are automatic. n=2 is automatically reversible and the reversal test is vacuous. Independently checked given 3x3 strictly positive witness exact rational traces, eigenvalue coefficients, and min R3^2 1 minus max F3^2 1=10651/10000, yielding strict growth reversal; scaling D by 17/27 yields opposite growth/decay. Inspected packaged verify.py implementing positive-vector Perron row bounds. These tests are for the witness, not a substitute for all-n cycle proof.

## originality

PASS

Mertens et al. (2006) analyze transient population responses and cyclic permutations, and Schreiber and Li (2011) study period-two migration dynamics with symmetrization; the classical Kolmogorov condition characterizes reversible Markov chains. The current combined necessary-and-sufficient condition quantifies spectral-radius equality for *every* diagonal calendar, detects nonreversibility with at most n seasons, and gives explicit sharp n=3,k=3 witness. No inspected primary theorem supplies this exact universal reversal characterization; classical cycle-balance is an acknowledged proof ingredient.

## value

PASS

A sharp finite-horizon, all-calendar test connecting observable asymptotic growth under time reversal with microscopic detailed balance is mathematically and conceptually natural. The explicit 3-patch example quantifies reversal-sensitive persistence within the model. Unlike a numerical hydrology claim, it is an exact structural statement and finite witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
