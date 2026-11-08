# Review of the certified quartic three-method obstruction

## Correctness — PASS

All three maps are specified exactly; the quartic has four simple roots by rational Euclidean polynomial division. The derivative identities were independently checked from the coefficients. Rational interval arithmetic, applied to all points of the indicated intervals and 64 exact subintervals for each derivative bound, proves denominator nonvanishing, root exclusion, five strict cyclic containments and return Lipschitz products strictly below one. The Banach fixed-point theorem and holomorphic stability give the asserted nonroot attracting cycles. Running the exact verifier yielded `VERIFY_OK`. The finite computation certifies full intervals, not just a collection of floating-point trajectories.

## Originality — PASS, with residual risk

Basti–Cremaschi's arXiv:2610.03246v1 provides the same polynomial and approximate periods and multipliers, but explicitly leaves the Halley and Schröder rigorous interval certificates absent. It proves a different Newton–Halley quartic. The new contribution is certification of a single simple-root quartic with extraneous attracting cycles for all three root finders. Collins–Hunter's 2025 published simultaneous three-map theorem is described by the primary source as covering degrees at least five, and Collins's 2017 abstract treats cycles of the higher-order maps, not the triple conjunction. The predecessor full texts were not obtained; independent exact certificates may exist outside the searched literature.

## Mathematical value — PASS

The degree-four simultaneous three-method case was highlighted by the primary source as numerical evidence lacking proof. A rigorous primitive attracting three-cycle for the Chebyshev/Schröder map, together with a separately certified Halley two-cycle and Newton's exact cycle, settles the status of the specific natural open candidate. Exact local complex attraction matters for genuine positive-area failure basins; approximate periodic motion alone would not suffice. No common basin or cubic impossibility is claimed.

## Source and scope limitations

The original quartic and the candidate points are credited to the 2026 authors. The 2025 Collins–Hunter full text and 2017 Collins full text were not accessible from the reviewed sources; their relevant scope was checked through available abstracts and the 2026 primary discussion. The result is exact-arithmetic, unsafeguarded root-finding dynamics only. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
