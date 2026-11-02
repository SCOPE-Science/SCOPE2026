# Mathematical assessment

## Correctness

**PASS (self-review).** The proof reduces the spectral norm of the QR-projected matrix to its first-coordinate projection. A deterministic one-axis scaling identity maps a Haar-uniform Gaussian sketch subspace into the power-filtered subspace, and the ordinary Haar beta law gives the exact finite-dimensional CDF. The chi-square ratio representation proves the fixed-width critical exponent and growing-width boundary. The actual standalone checker passed 1,133 seeded and deterministic numerical checks, including direct QR comparisons and independent tail-probability simulations. Computation is supplementary, not a substitute for the proof.

## Originality

**PASS (self-review, subject to priority risk).** Smith, Do and Chen's Algorithm 5 introduces the spectral look-ahead stopping statistic and Theorem 4.3 bounds its approximation guarantee by a non-unit factor, not an exact false-stop CDF. Halko, Martinsson and Tropp and Saibaba provide general range/canonical-angle bounds; Liu and Yu analyze related heavy-tail rank-deflation phenomena. A published one-spike ellipsoid section-radius law has the same underlying Haar beta ingredient, but not the two-stage filtered QB spectral observable or its false-decision and sample-power classification. Earlier mathematical formulations of this exact special case remain possible; independent scholarly priority checking has not occurred.

## Mathematical value

**PASS (self-review).** The formula exposes an operationally significant blind spot in a natural spectral-rank stopping proxy: at dimension 10,001 with 16 Gaussian test columns, the false-stop probability exceeds 98.9% despite a clear one-dimensional spectral rank. Exact calibration and a sharp power-filter threshold identify when more sketches or power iterations resolve this ambiguity. The result concerns one-spike flat tails, not arbitrary matrices or whole-algorithm behavior.

## Closest literature and limitations

Closest: arXiv:2607.06758v1, Algorithm 5 and Theorem 4.3; arXiv:0909.4061v2, Sections 9–10; arXiv:1804.02614, Sections 3–4; arXiv:2508.07553v1, Sections 2–3; published one-spike ellipsoid random-radius law. The one-spike Gaussian projection law is standard; the claimed contribution is the exact numerical stopping-risk translation and thresholds. Residual risks are unknown synonymous prior results, numerical-precision effects, nonflat tails, and the distinction between a single indicator and a complete adaptive algorithm.

Self-review: passed. Independent audit: not yet performed.
