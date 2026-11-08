# Scientific review: nearest-vertex covering of demihypercubes

## Correctness — PASS

The proof first obtains the complete cube-and-odd-sign halfspace description by comparing support functions in every direction. It then uses the nearest even-sign vertex and the pair-flip optimality inequalities to verify every coordinate and every odd-sign facet of the proposed witness. The only parameter inequality is \((n-2)(d-2)\ge2\), which holds for \(n\ge4\) and odd \(d\ge3\). Simplex-facet centroids give sharpness for every \(n\ge4\); dimension three is separated. An exact-rational finite checker passed 7,927 assertions; it is a corroboration rather than a replacement for the proof. Residual mathematical risk is unrecognized notation/normalization rather than an unverified numerical certificate.

## Originality — PASS for the stronger constructive statement, with priority risk

The numeric Schneider threshold \(n-1\) alone can be inferred from Artstein-Avidan–Falah–Slomka (arXiv:2407.20604v1) using their boundary-to-body lemma, the canonical facets, and the inclusion \(-P_n\subseteq(n-1)P_n\). It is explicitly *not* claimed as an independent novel index. Meyer (arXiv:2610.26744v1, 2026) provides general finite Minkowski-convexification criteria, likewise existential rather than a specified witness. The substantive new result is that **every nearest Euclidean vertex** gives a valid optimal decomposition, and that such a vertex is computable by a linear-time parity-corrected sign rule; the proof verifies all parity facets using pair-flip optimality. The earlier papers contain no such nearest-vertex conclusion, and their existential results do not logically force it. Comparisons with hypersimplex vertices, simplex skeletons, halfcube ellipsoids, and general convexification records found no encompassing nearest-vertex theorem. Historical coverage of older parity-polytope covering terminology remains a real risk.

## Mathematical value — PASS

Demihypercubes are canonical high-dimensional uniform/parity polytopes with simplex facets. Exact finite convexification of their discrete vertices is a natural unsolved-for-this-family invariant motivated by recent general criteria; the formula distinguishes \(n=3\) from \(n\ge4\), identifies the sharp index in every dimension, and provides a simple pointwise witness. A simplex-facet obstruction alone supplies only a lower bound; the new pair-flip construction establishes the matching global upper bound. The parity-corrected nearest-vertex construction is linear time although there are exponentially many vertices. This is more informative than the previously available existential boundary criterion and is not merely recomputing a known number.

## Boundaries

This is a mathematical self-review only. Independent validation and complete historical-priority confirmation have not occurred. The all-dimensional proof uses exact inequalities, not extrapolation from finite checks.

Self-review: passed. Independent audit: not yet performed.
