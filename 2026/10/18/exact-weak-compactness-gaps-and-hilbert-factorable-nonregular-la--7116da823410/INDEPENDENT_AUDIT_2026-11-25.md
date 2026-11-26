# Independent mathematical audit

## correctness

PASS

The repaired Hilbert factorization holds in the full real spaces for every injection, including a possible f(a)=0 and the empty word. Prefixes 0^a have disjoint nonempty derivative supports D_a: a common suffix fixes its count of zeros r and then forces a=a' by injectivity. If a prefix already contains a one, a nonzero derivative is supported at precisely one all-ones suffix; the other prefixes have zero columns. Grouping coefficients by these two disjoint types has l1 norm at most the input norm, so the Hilbert input map is contractive. At a suffix at most one coordinate from each family is evaluated, giving output norm at most sqrt(2) times the Hilbert norm. Factorization through a reflexive space implies weak compactness; infinitely many norm-separated Boolean derivatives imply noncompactness and nonregularity. For L_le, fixed j gives eventual zero while fixed i gives eventual one along j. If R were weakly compact at distance delta<1/2, a weakly convergent subsequence of its zero-prefix columns would have limit r with |r(1^j)|<=delta for each j. A free-ultrafilter limit along 1^j is a bounded functional with values at least 1-delta on every such column and thus on r, a contradiction. The midpoint gives the matching upper bound. The prior approximation numbers apply to both nonregular languages. The original general gap is also correct: weak convergence in C(beta J) allows pointwise continuous thresholding and dominated convergence against each regular measure on a common norm bound; Eberlein–Šmulian then gives relative weak compactness of the thresholded column set and Krein's theorem gives that of its closed absolutely convex hull. No finite truncation, numerical assertion or computation is used to prove these infinite statements.

## originality

PASS

The frozen general-gap novelty claim does not pass: the midpoint together with classical weak compactness under continuous thresholding and the column hull criterion already yields the exact Boolean half-gap. This is stronger than a mere suspicion of folklore; there need not be a prior paper stating the operator distance verbatim. The repair removes the general gap from the main result and retains the concrete quantitative Hilbert factorization for arbitrary injective graphs. The same-tail comparison provides the motivation; neither the approximation numbers nor the order-language obstruction are claimed as new principles. Within the inspected literature no earlier coverage of the explicit arbitrary-injection factorization and norm bound was identified.

## value

PASS

The repaired result resolves a concrete question after the compact approximation-number theorem: a flat tail for nonregular languages does not decide weak compactness, even when one side is Hilbert-factorable. The positive witness is a uniform factorization for the whole natural injective-graph family, without monotonicity or computability restrictions, not merely an isolated example or a restatement of the shared tail. The familiar order pattern is a comparison witness, not a new general obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
