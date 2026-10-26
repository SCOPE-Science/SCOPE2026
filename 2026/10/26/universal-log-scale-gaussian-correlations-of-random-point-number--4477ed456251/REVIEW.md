# Review

## Correctness

PASS. The claim contains two linked assertions: an exact covariance for any pair of circle-window lengths and a finite-dimensional Gaussian law for jointly shrinking lengths. The proof reconstructs the degenerate order-two U-statistic, checks the only surviving covariance pairings, and integrates the overlap kernel exactly. Shared Brownian white-noise Fourier coefficients, rather than independently coupled scalar Fourier series, establish the joint law. A triangular-array Lyapunov bound and a common empirical-process strong approximation complete the limit. A standard-library verifier passed 134 exact-rational/numerical test cases; these support, but do not replace, the proof.

## Originality

PASS, with historical-priority risk. The October 2026 primary source proves one-scale distributional and variance statements. Its lemmas enable parts of the new proof but do not identify the cross-length law. Historical literature on planar Ripley statistics supplies multiscale Gaussian tests and covariance matrices under different geometry and asymptotic normalization. A broader derivation of the same circle-window limit might exist under integrated pair-correlation terminology; no proof of global priority is claimed.

## Mathematical value

PASS. At fixed marginal length, point number variance is a standard diagnostic. Multiple length windows on the same sample are not independent, and calibrating their joint behavior requires a joint covariance. The exact finite-sample identity and the universal stationary log-scale covariance answer this motivated question for independent uniform points, including the decay of correlation between increasingly separated scales. The proof does not claim functional weak convergence or optimize its growth condition.

## Limitations and comparison

The one-length fluctuation formula and KMT inequality are taken from Aistleitner–Hörmann–Manskova (2026). Aistleitner–Yesha (2025) treats arithmetic dilation sequences. Heinrich (2017) and Lang–Marcon (2013) treat general point-process multiscale K-statistics in distinct observation regimes. These comparisons were made on theorem statements and material full text, rather than titles alone. An independent specialist literature audit would still be useful.

Self-review: passed. Independent audit: not yet performed.
