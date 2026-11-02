# Independent mathematical audit

## correctness

PASS

The orthogonal Laplacian decomposition has eigenvalues 0 on constants, N on part-constant global mean-zero modes, and N-n_i on within-part fluctuations. This yields exact between-part entries (1-e^{-s})/N and within-part off-diagonal H_i/n_i. Jensen convexity forces H_i>0 for α<=1. For α>1, a_i=q_i^α<q_i, e^{a_i s}H_i=u_i e^{a_i s}+q_i e^{-(1-a_i)s}-1 is strictly convex, starts at zero with negative derivative and tends to +∞, so exactly one crossing. Row sums equal one and only within-part off-diagonals can be negative; sum of their absolute values gives the exact operator row/column norm. Differentiating -H_i yields its unique peak; Taylor expansion in ε=α-1 gives delay coefficient (2/N) max (-log q_i)/u_i and norm excess max (1-1/n_i)q_i(log q_i)²/u_i. Independently assembled raw graph Laplacians and spectral fractional heat for 80 graph/α/time combinations; checked block entries, signs and sharp row norms.

## originality

PASS

All four comparisons are grounded in actual primary or published-record searches; best-of-knowledge only. The exact α-dependent graph heat entries follow from a 3-level combinatorial Laplacian. Qualitative eventual positivity and low-eigenlevel abstractions do not themselves state the singular near-1 coefficient or complete sharp norm profile.

## value

PASS

The graph family has a natural three-level spectral decomposition, and passing α=1 changes genuine positivity of a Markov heat flow. Exact last sign-change time, attainable norms, and the distinct first/second-order critical scales are useful sharp structural invariants beyond qualitative eventual positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
