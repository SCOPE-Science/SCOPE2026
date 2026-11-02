# Mathematical review

## Correctness — PASS

The exact conditional variance identity in `RESULT.md` follows by conditioning only on refresh/copy decisions and using orthogonality of centered degree-two products of distinct independent fair signs. On a double-refresh event, the unique ordered time pair labels one character whose nonnegative multiplicity has square at least one. Summing these witnesses and applying total variance gives the finite-time constant \(\varepsilon^2/4\) without stationarity, mixing, or graph-size conditions. The source's explicit variance dichotomy and Theorem 2.7 apply to the same model and time-indexed statistic; the derived variance floor eliminates their logarithmic case and verifies their CLT's stated hypothesis. Independently checked 2,084 exact rational/Walsh instances using the supplied standalone verifier. Finite checks are not a proof of the general theorem.

## Originality — PASS, with historical-priority qualification

The closest primary paper [1] defines precisely this statistic and explicitly asks whether its variance can be sublinear; its Lemma 2.3 leaves an \(O(\log L)\) alternative and Theorem 2.7 assumes sufficient variance for the original statistic. The present quantified lower bound and nondegenerate-variance consequence cannot follow from those claims alone. Broader comparison with [2] and [3] concerns different observables or update frameworks, and no statement implying this lower bound was found in those accessible descriptions. Alternative harmonic-analysis or noisy Boolean dynamics terminology could conceal a precedent; priority is not certified.

## Value — PASS

This resolves a named uncertainty about the unmodified, local temporal statistic in a published research model. The lower bound is uniform over graph geometry, observation vertex, lag, finite observation length, and infinite locally finite graphs, and it strengthens an existing conditional central limit theorem into an unconditional, nondegenerate one. This is not merely a new estimate for a specially chosen graph or a renaming of the prior thinned-statistic result.

## Scientific boundaries

The explicit coefficient need not be best for interior noise parameters; its equality is proved at complete refresh. The normal-limit inference relies on the cited published theorem. No conclusions are established for biased refresh or asynchronous dynamics. Independent mathematical validation and complete historical priority remain open.

Self-review: passed. Independent audit: not yet performed.
