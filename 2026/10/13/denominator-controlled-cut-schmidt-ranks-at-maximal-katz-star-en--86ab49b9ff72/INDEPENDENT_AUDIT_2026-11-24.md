# Independent mathematical audit

## correctness

PASS

For this Ising normalization the site coherence magnitude is the product over incident interactions of |cos(t K_uv)|. In particular the center has |cos(t/D)|^m and every leaf has a common factor |cos(t/D)|, so t*=pi D/2 is the first time at which the total one-body distance reaches its maximum. Expanding (1-2x)(1-2y) and dropping local phases gives the coefficient (-1)^(cj) exp(i pi beta i j) with the Dicke binomial multiplicities. Tracing out the center side cancels opposite-parity weights; the sum over its leaves gives the stated binomially weighted cosine power. Depending on coefficient convention the density matrix uses the transpose of the column Gram matrix, which is isospectral. The nonzero spectrum is that of the compression with zeros discarded; the complementary reduced space is padded with its own zeros. Taking absolute squares and convolving the two binomial coefficients by Vandermonde gives the stated purity. For rank, divide out the strictly positive multiplicities and use the first s Vandermonde columns (or first b+1 distinct nodes if fewer columns) for nodes z=(-1)^c exp(i pi beta i). Each distinct z^2 supplies both square roots; the squared nodes exp(2 pi i beta i) are distinct for irrational beta and have exact period q for beta=p/q reduced. This gives the asserted ranks for both parities of p, with no floating-point assumption. For a=0 use an empty product; for b=1 there are two eigenvalues 1/2 and rank two, including m=1. The bundled checker was inspected, not run; the independent algebra covers the infinite parameter domain.

## originality

PASS

Credit the all-cut Katz-star classification, in particular the sharp rank at every real coupling and its exact dependence on the lowest denominator. The weighted-graph partial trace and rational finite-component mechanisms themselves are known, and the Katz-specific Gram entries are a specialization and symmetric-basis compression of the known partial trace. The inspected prior implications do not fix the rank when the cut dimension competes with the rational period; the additional Vandermonde lower bound is essential. This is a best-of-knowledge distinction, not priority certification.

## value

PASS

The time is selected by the source model, not an ad hoc numerical slice. The result resolves whether the state uses all available symmetric-subspace dimensions across each cut, and gives the exact finite-cut saturation and denominator drop. Both distinguish states having the same maximal one-body distance. This also supplies an algebraic rank test when tiny eigenvalues make numerical rank unreliable; for m=80, a=30 the admissible 1/10 has rank 20 versus 51 at any admissible irrational coupling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
