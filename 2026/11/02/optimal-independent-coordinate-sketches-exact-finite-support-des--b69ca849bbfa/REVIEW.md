# Review of the exact optimized one-coordinate sketch theorem

## Correctness

PASS. Independent coupon noncoverage gives the exact squared Hilbert--Schmidt error; strict convexity and a common threshold multiplier prove global optimality on the closed probability simplex; full-support mixtures approximate its optimal value. Monotone integral comparisons establish the sharp limit \(\rho^\rho\) for \(\rho>1\). The proof covers finite-\(L\) support thresholds, nonattainment under strict isotropy, and the \(L=2\) boundary. The 90-family standalone checker verifies exact finite-space combinatorics and numerical consistency, not infinite claims.

## Originality

PASS with historical-priority limitations. Lynch-Davies and Webb (arXiv:2610.31333v1) introduce an almost-surely finite one-coordinate isotropic sketch and establish general infinite-dimensional sketching theory; their inspected manuscript does not solve the exact spectral allocation. Saibaba--Międlar (arXiv:2308.05814v1) discuss non-Gaussian low-rank approximations and coordinate-sampling coupon loss but do not derive the finite-\(L\) power-law optimum or its sharp asymptotic factor. The earlier Halko--Martinsson--Tropp survey documents coupon-collector issues. The most similar indexed mathematical record concerns optimal coordinate descent on inverse-positive SPD quadratics, not independent coordinate coverage of a compact rangefinder. A generic weighted-coupon-coverage theorem could subsume the first-order formula; equivalence has not been ruled out by independent comprehensive literature review.

## Mathematical value

PASS. The result quantifies an implementationally relevant gap between isotropic one-coordinate sampling and best-rank spectral truncation, precisely \(\rho^\rho\) in expected squared Hilbert--Schmidt error. The closed-simplex nonattainment explains why strict full-support isotropy forces arbitrarily small but nonzero tail probabilities even in the optimal limit. This is not a result about general randomized or adaptive sketches.

## Boundaries and evidence

Only diagonal power-law compact operators, iid one-hot sketches, and squared Hilbert--Schmidt loss are claimed. The exact analytical derivation is the proof; finite computations support it. The full-text motivating manuscript was inspected; broader or peripheral related sources were only partially inspected as described in the audit. Published-priority uncertainty remains.

Self-review: passed. Independent audit: not yet performed.
