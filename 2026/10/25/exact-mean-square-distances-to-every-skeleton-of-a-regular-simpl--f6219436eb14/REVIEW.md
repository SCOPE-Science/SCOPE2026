# Scientific review

## Correctness — PASS
For each face, the proposed orthogonal projection lies inside the face and has explicitly computed squared residual. An exchange argument proves that the closest face uses the largest barycentric weights. A bijective ordered-gap transformation supplies a uniform Dirichlet vector; its exact second moments evaluate a finite quadratic form, yielding the stated harmonic expression. The joint law and all three asymptotic regimes follow from those identities. Independent exact-rational checks across 66 dimension/skeleton pairs and direct geometric enumeration of sampled configurations passed; sampled numerical checks supplement, rather than replace, the analytic proof.

## Originality — PASS (qualified)
The inspected 2012 sparse simplex projection paper already covers the deterministic support-selection step: this step is not claimed as new. The inspected Conway–Sloane 1982 paper gives fixed-centroid moments and lattice Voronoi averages, not expected distance to the union of simplex faces of a selected dimension. Published indexed research about convexification thresholds for simplex skeleta concerns Minkowski sums, not stochastic Euclidean quantization. The new claim is one exact simultaneous geometric distribution and its all-dimension evaluated mean-square profile. Searches found no statement that directly supplies this profile or its three scaling limits. An earlier equivalent evaluation is a residual bibliographic possibility, not ruled out by keyword search.

## Mathematical value — PASS
The finite-skeleton squared-distance error is a canonical metric approximation invariant: it quantifies the loss when a uniformly sampled simplex point is approximated by a face of prescribed dimension. Complete exact values for every dimension and every skeleton, plus the shared law enabling mixed-moment calculations, give a reusable analytic benchmark for sparse-simplex projection. The fixed-face-size, proportional-face-size, and fixed-codimension regimes differ in scale, so the exact calculation resolves a meaningful geometric transition rather than an arbitrary isolated number.

## Limits
The work does not establish the optimal choice of approximation complex among all complexes, nor any analogous formula for irregular simplices. The literature search and self-review are not substitutes for independent validation; the closest public full-text comparisons and residual risks are recorded in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
