# Independent mathematical audit

## correctness

PASS

Independently checked the projection factorization, the rank-one PSD residual, and its trace ab/(b+(a−b)T), with T the squared share of the leading eigencoordinate. A common scale cancels; the real share is arcsine and the circular complex share is uniform. The respective CDFs satisfy F_R(t)>t below 1/2 and F_R(t)<t above. For a symmetric share T, condition on the radius |T−1/2|: the real radius strictly stochastically dominates the complex radius. For convex g, [g(1/2+r)+g(1/2−r)]/2 is nondecreasing in r, strictly for strictly convex g. Apply this to g=phi composed with the residual map, which is convex and is strictly convex when phi is strictly increasing and a>b. This proves the entire risk comparison (both shares have no endpoint mass). Quantile inversion verifies the single interior crossing and common median, so neither error law first-order dominates. For the real first moment the angular integral becomes an integral of 1/(a+b u²) under u=tan(theta); differentiating the corresponding normalization after shifting both eigenvalues derives the real second moment. Direct uniform integration gives the complex moments. With R=a/b the mean ratio is (R−1)/(sqrt(R) log R), and a=b gives a point mass. No verifier execution was needed: the frozen numerical tests are finite diagnostics, not proof of the universal inequality.

## originality

PASS

The real-side law and mean are covered and are not credited. The supported distinct finding is the one-column field comparison: the complex error law, common-median crossover, and increasing-convex risk ordering together. The closest sources have either only the real side, more sketch columns and error bounds, or a different competing sketch and error.

## value

PASS

Dimension two with one column is the first nonconstant rank-one PSD residual where the field choice matters. A common median and crossing rule out ordinary stochastic dominance even though all increasing convex penalties prefer the complex law, and the unbounded mean separation shows why the distinction matters. This provides an exact benchmark for field-dependent risk analyses, not a recommendation about equal-cost algorithms or a general higher-rank result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
